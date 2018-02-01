'use strict';

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
      // console.log(metadata);
      const values = [
        metadata.title,
        metadata.artist,
        metadata.duration,
        track,
      ];
      console.log(values);
      connection.query('INSERT INTO tracks (title, artist, duration, path) VALUES (?, ?, ?, ?)', values, (err) => {
        if (err) {
          console.log(`sql insert error: ${err}`);
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
// app.use('C:\\Users\\tothbandi\\Documents\\music\\', express.static('music'));

// let playlists = [
//   { "id": 1, "title": "Favorites", "system": 1},
//   { "id": 2, "title": "Music for programming", "system": 0},
//   { "id": 3, "title": "Driving", "system": 0},
//   { "id": 5, "title": "Fox house", "system": 0},
// ];

// let playlistTracks = [
//   { "id": 21, "title": "Halahula", "artist": "Untitled artist", "duration": 545, "path": "c:/music/halahula.mp3" },
//   { "id": 412, "title": "No sleep till Brooklyn", "artist": "Beastie Boys", "duration": 312.12, "path": "c:/music/beastie boys/No sleep till Brooklyn.mp3" }
// ];

app.get('/playlists', (req, res) => {
  let playlists = [];
  connection.query('SELECT * FROM playlists;', (err, rows) => {
    if (err) {
      console.log(`sql select error: ${err}`);
    }
    playlists = rows.map((row) => {
      console.log(row);
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

app.get('/playlist-tracks', (req, res) => {
  let playlistTracks = [];
  connection.query('SELECT * FROM tracks;', (err, rows) => {
    if (err) {
      console.log(`sql select error: ${err}`);
    }
    playlistTracks = rows.map((row) => {
      return {
        id: row.id,
        title: row.title,
        artist: row.artist,
        duration: row.duration,
        path: row.path,
      };
    });
    res.status(200);
    res.json(playlistTracks);
  });
});

app.listen(3000, (e) => {
  if (e) {
    console.log('listen error');
    throw e;
  }
  console.log('listen 3000');
});
