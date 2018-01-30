'use strict';

let express = require('express');

let app = express();
app.use(express.json());
app.use(express.static('.'));

let playlists = [
  { "id": 1, "title": "Favorites", "system": 1},
  { "id": 2, "title": "Music for programming", "system": 0},
  { "id": 3, "title": "Driving", "system": 0},
  { "id": 5, "title": "Fox house", "system": 0},
]

let playlistTracks = [
  { "id": 21, "title": "Halahula", "artist": "Untitled artist", "duration": 545, "path": "c:/music/halahula.mp3" },
  { "id": 412, "title": "No sleep till Brooklyn", "artist": "Beastie Boys", "duration": 312.12, "path": "c:/music/beastie boys/No sleep till Brooklyn.mp3" }
]

app.get('/playlists', (req, res) => {
  res.status(200);
  res.json(playlists);
});

app.get('/playlist-tracks', (req, res) => {
    res.status(200);
    res.json(playlistTracks);
  });


app.listen(3000, e => {
  if(e){
    console.log('listen error');
    throw e;
  }
  console.log('listen 3000')
});
