'use strict';

const server = 'http://localhost:3000';
const allTracks = document.querySelector('.alltracks');
const tracks = document.querySelectorAll('.track');
const trackList = document.querySelector('.track-list');
const audio = document.querySelector('.audio');
const playpause = document.querySelector('.playpause');
const volume = document.querySelector('.volume');
const time = document.querySelector('.time');
const elapsed = document.querySelector('.elapsed');
const duration = document.querySelector('.duration');
const myevent = new Event('playplay', {"bubbles":true, "cancelable":false});

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
  
  // let trackList = document.querySelector('.track-list');
  
  data.forEach((item) => {

    const track = document.createElement('div');
    track.classList.add('track');
    track.setAttribute('data-track-id', item.id);
    track.setAttribute('data-track-artist', item.artist);
    track.setAttribute('data-track-path', item.path);

    const trackId = document.createElement('div');
    trackId.classList.add('tr-id');
    trackId.textContent = item.id;

    track.appendChild(trackId);

    const trackTitle = document.createElement('div');
    trackTitle.classList.add('tr-title');
    trackTitle.textContent = item.title;

    track.appendChild(trackTitle);

    const trackDuration = document.createElement('div');
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

allTracks.addEventListener('click', (event) => {
  if (event.target.parentElement.classList.contains('alltracks')) {
    getTracks();
    allTracks.classList.add('now-playing');
  }
});

trackList.addEventListener('click', (event) => {
  let src = event.target.dataset.trackPath;
  src = `http://127.0.0.1:8887/${src.slice(35)}`;
  console.log(src);
  audio.setAttribute('src', src);
  audio.addEventListener('loadedmetadata', function (e) {
    loadAudioData(event.target);
  });

});





function convertSeconds(seconds) {
  let minutes = Math.floor(seconds / 60);
  seconds = Math.floor(seconds % 60);
  return `${minutes}:${seconds < 10 ? '0'+ seconds : seconds}`;
}

function loadAudioData(track) {
  track.classList.add('now-playing');
  const trackTitle = document.querySelector('.title');
  trackTitle.textContent = track.querySelector('.tr-title').textContent;
  const trackNote = document.querySelector('.note');
  trackNote.textContent = track.dataset.trackArtist;
  console.log(audio);
  console.log(audio.duration);
  volume.value = audio.volume * 100;
  time.value = audio.currentTime * 100 / audio.duration;
  elapsed.textContent = convertSeconds(audio.currentTime);
  duration.textContent = convertSeconds(audio.duration);
  playpause.style.backgroundImage = 'url(img/play.svg)';
  
}

// window.addEventListener('load', e => {
//   loadAudioData();
// });

time.addEventListener('input', (e) => {
    audio.currentTime = audio.duration * parseInt(time.value) / 100;
    elapsed.textContent = convertSeconds(audio.currentTime);
} );

volume.addEventListener('input', (e) => {
    audio.volume = parseInt(volume.value) / 100;
} );

playpause.addEventListener('click', (e) => {
  if (audio.paused) {
    // window.setInterval(window.dispatchEvent('playplay'), 1000);
    audio.play();
    playpause.style.backgroundImage = 'url(img/pause.svg)';
    console.log(audio.volume);
  } else {
    // window.clearInterval();
    audio.pause();
    playpause.style.backgroundImage = 'url(img/play.svg)';
  }

}, false);

// Add the following events: loadstart, play, ended, progress
// console.log the event name + "hap pened" to the console
// window.addEventListener('playplay', (e) => {
//   time.value = audio.currentTime * 100 / audio.duration;
//   elapsed.textContent = convertSeconds(audio.currentTime);
// });

audio.addEventListener('loadstart', function(e) {
    console.log(`event ---> : ${e.type}`);
});

audio.addEventListener('loadedmetadata', function(e) {
  duration.textContent = convertSeconds(audio.duration);
  // console.log(`event ---> : ${e.type}`);
});

audio.addEventListener('playing', function(e) {

    console.log(`event ---> : ${e.type}`);
});

audio.addEventListener('ended', function(e) {
    console.log(`event ---> : ${e.type}`);
});

audio.addEventListener('progress', function(e) {
  time.value = audio.currentTime * 100 / audio.duration;
  elapsed.textContent = convertSeconds(audio.currentTime);
  // duration.textContent = convertSeconds(audio.duration);
    // console.log(`event ---> : ${e.type}`);
});