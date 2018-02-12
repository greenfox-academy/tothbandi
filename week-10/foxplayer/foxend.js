'use strict'; // eslint-disable-line

/* eslint linebreak-style: ["error", "windows"] */

// https://freemusicarchive.org/

const express = require('express');
const fs = require('fs');
const mm = require('musicmetadata');
const path = require('path');
const mysql = require('mysql');

const connection = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: '12345',
  database: 'foxplayer',
});

function getFullPath(dir, file) {
  const pathOb = path.parse(path.join(dir, file));
  return `${pathOb.dir}\\${pathOb.base}`;
}

function walkSync(dir, filelist = []) {
  const files = fs.readdirSync(dir);
  files.forEach((file) => {
    if (fs.statSync(`${dir}/${file}`).isDirectory()) {
      const list = walkSync(`${dir}/${file}`, []);
      filelist = filelist.concat(list);
    } else {
      filelist.push(getFullPath(dir, file));
    }
  });
  return filelist;
}

function fillDbTracks() {
  const fp = 'C:\\Users\\tothbandi\\Documents\\music\\';
  const filelist = walkSync(fp);
  filelist.forEach((track) => {
    const readableStream = fs.createReadStream(track);
    mm(readableStream, { duration: true }, (err2, metadata) => {
      if (err2) throw err2;
      const values = [
        metadata.title,
        metadata.artist,
        metadata.duration,
        track,
      ];
      connection.query('INSERT INTO tracks (title, artist, duration, path) VALUES (?, ?, ?, ?)', values, (err) => {
        if (err) {
        }
      });
      readableStream.close();
    });
  });
}

//fillDbTracks();

const app = express();
app.use(express.json());
app.use(express.static('.'));
app.get('/', (req, res) => {
  res.status(200);
  res.sendFile(path.join(__dirname, 'index.html'));
});

app.get('/playlists', (req, res) => {
  let playlists = [];
  connection.query('SELECT * FROM playlists;', (err, rows) => {
    playlists = rows.map((row) => {
      return {
        id: row.id,
        title: row.playlist,
        system: row.system,
      };
    });
    res.status(200);
    res.json(playlists);
  });
});

app.post('/playlists/:newList', (req, res) => {
  connection.query(`INSERT INTO playlists (playlist, system) VALUES ('${req.params.newList}', 0);`, (err, rows) => {
    res.status(200);
    res.json({ inserted: true });
  });
});

app.get('/playlist-tracks', (req, res) => {
  connection.query('SELECT * FROM tracks;', (err, rows) => {
    if (err) {
      console.log(`sql select error: ${err}`);
    }
    res.status(200);
    res.json(rows);
  });
});

app.get('/playlist-tracks/:listId', (req, res) => {
  console.log(req.params.listId);
  connection.query(`SELECT * FROM tracks T RIGHT JOIN playlist P ON T.id = P.track_id WHERE P.playlist_id =${req.params.listId};`, (err, rows) => {
    if (err) {
      console.log(`sql select error: ${err}`);
    }
    res.status(200);
    res.json(rows);
  });
});

app.post('/playlist-tracks/:listId/:trackId', (req, res) => {
  const data = [req.params.listId, req.params.trackId];
  connection.query('SELECT * FROM playlist WHERE playlist_id = ? AND track_id = ?;', data, (err, rows) => {
    if (rows.length === 0) {
      connection.query('INSERT INTO playlist (playlist_id, track_id) VALUES (?, ?);', data, () => {});
    }
  });
  res.status(200);
  res.json({ result: 'success' });
});

app.post('/favorite-track/:trackId', (req, res) => {
  connection.query(`SELECT * FROM playlist WHERE playlist_id = 1 AND track_id = ${req.params.trackId}`, (err, rows) => {
    if (rows.length === 0) {
      res.status(200);
      res.json({ result: false });
    } else {
      res.status(200);
      res.json({ result: true });
    }
  });
});

app.delete('/playlists/:listId', (req, res) => {
  let id = [req.params.listId];
  connection.query('DELETE FROM playlist WHERE playlist_id=?;', id, (err, rows) => {
    connection.query('DELETE FROM playlists WHERE id=?;', id, (err, rows) => {
      res.json({ result: 'deleted' });
    });
  });
});

app.listen(3000, (e) => {
  if (e) {
    console.log('listen error');
    throw e;
  }
  console.log('listen 3000');
});
