'use strict';
const server = 'http://localhost:3000';

getPlayLists();

function getPlayLists() {
  let httpRequest = new XMLHttpRequest();
  httpRequest.open('GET', `/playlists`);
  httpRequest.setRequestHeader('Accept', 'application/json');
  httpRequest.setRequestHeader("Content-Type", "application/json");
  httpRequest.send();
  httpRequest.addEventListener('load', function () {
    let data = JSON.parse(httpRequest.responseText);
    console.log('data = responsetext:\n', data);
    generatePlayLists(data);
  });
}

// let playlists = [
//     { "id": 1, "title": "Favorites", "system": 1},
//     { "id": 2, "title": "Music for programming", "system": 0},
//     { "id": 3, "title": "Driving", "system": 0},
//     { "id": 5, "title": "Fox house", "system": 0},
//   ]

function generatePlayLists(data) {

  let defaultLists = document.querySelector('.default-lists');
  let userLists = document.querySelector('.user-lists');

  data.forEach(item => {

    let playList = document.createElement('div');
    playList.classList.add('playlist');
    playList.setAttribute('data-list-id', item.id);

    let span = document.createElement('span');
    span.textContent = item.title;
    playList.appendChild(span);

    if (item.system === 1) {
      
      playList.classList.add('favorites');
      defaultLists.appendChild(playList);

    } else if (item.system === 0) {

      let delButton = document.createElement('div');
      delButton.classList.add('playlist-delete');
      delButton.textContent = 'x';

      playList.appendChild(delButton);

      userLists.appendChild(playList);
    }
  });
}

// let playlistTracks = [
//     { "id": 21, "title": "Halahula", "artist": "Untitled artist", "duration": 545, "path": "c:/music/halahula.mp3" },
//     { "id": 412, "title": "No sleep till Brooklyn", "artist": "Beastie Boys", "duration": 312.12, "path": "c:/music/beastie boys/No sleep till Brooklyn.mp3" }
//   ]

function generateTracks(data) {
  
  let trackList = document.querySelector('.track-list');
  
  data.forEach(item => {

    let track = document.createElement('div');
    track.classList.add('track');

    let trackId = document.createElement('div');
    trackId.classList.add('tr-id');
    trackId.setAttribute('data-track-id', item.id);
    trackId.textContent = item.id;

    track.appendChild(trackId);

    let trackTitle = document.createElement('div');
    trackTitle.classList.add('tr-title');
    trackTitle.textContent = item.title;

    track.appendChild(trackTitle);

    let trackDuration = document.createElement('div');
    trackDuration.classList.add('tr-time');
    trackDuration.textContent = convertSeconds(item.duration);

    track.appendChild(trackDuration);

    trackList.appendChild(track);
  });
}

function getTracks() {
    let httpRequest = new XMLHttpRequest();
    httpRequest.open('GET', `/playlist-tracks`);
    httpRequest.setRequestHeader('Accept', 'application/json');
    httpRequest.setRequestHeader("Content-Type", "application/json");
    httpRequest.send();
    httpRequest.addEventListener('load', function () {
      let data = JSON.parse(httpRequest.responseText);
      console.log('data = responsetext:\n', data);
      generateTracks(data);
    });
  }

window.addEventListener('click', event => {
  if (event.target.parentElement.classList.contains('alltracks')) {
    getTracks();
  }
});

let audio = document.querySelector('.audio');
let playpause = document.querySelector('.playpause');
let volume = document.querySelector('.volume');
let time = document.querySelector('.time');
let elapsed = document.querySelector('.elapsed');
let duration = document.querySelector('.duration');
console.log(audio);
console.log(audio.duration);
volume.value = audio.volume * 100;
time.value = audio.currentTime * 100 / audio.duration;

function convertSeconds(seconds) {
    let minutes = Math.floor(seconds / 60);
    seconds = Math.floor(seconds % 60);
    return `${minutes}:${seconds < 10 ? '0'+ seconds : seconds}`;
}

elapsed.textContent = convertSeconds(audio.currentTime);
duration.textContent = convertSeconds(audio.duration);

time.addEventListener('input', (e) => {
    audio.currentTime = audio.duration * parseInt(time.value) / 100;
    elapsed.textContent = convertSeconds(audio.currentTime);
} );

volume.addEventListener('input', (e) => {
    audio.volume = parseInt(volume.value) / 100;
} );

playpause.addEventListener('click', function(e)
{
  if(audio.paused)
  {
    audio.play();
    playpause.style.backgroundImage = 'url(img/pause.svg)';
    console.log(audio.volume);
  }
  else
  {
    audio.pause();
    playpause.style.backgroundImage = 'url(img/play.svg)';
  }

}, false);

// Add the following events: loadstart, play, ended, progress
// console.log the event name + "hap pened" to the console

audio.addEventListener('loadstart', function(e) {
    console.log(`event ---> : ${e.type}`);
});

audio.addEventListener('play', function(e) {
    console.log(`event ---> : ${e.type}`);
});

audio.addEventListener('ended', function(e) {
    console.log(`event ---> : ${e.type}`);
});

audio.addEventListener('progress', function(e) {
    console.log(`event ---> : ${e.type}`);
});