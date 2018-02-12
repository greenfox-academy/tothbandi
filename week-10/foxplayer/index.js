'use strict'; // eslint-disable-line

/* eslint linebreak-style: ["error", "windows"] */

let prevTrack;
let prevList;

function connect(method, query, callback) {
  const xhr = new XMLHttpRequest();
  const url = `http://localhost:3000${query}`;
  xhr.open(method, url);
  xhr.addEventListener('readystatechange', () => {
    if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
      const data = JSON.parse(xhr.responseText);
      callback(data);
    }
  });
  xhr.send();
}

function addNewList() {
  const newPlayList = window.prompt('Enter the new playlist name.', 'play list name');
  const doPlayList = window.confirm(`Create list named ${newPlayList} ?`);
  if (doPlayList) {
    connect('POST', `/playlists/${newPlayList}`, () => {
      connect('GET', '/playlists', generatePlayLists);
    });
  }
}

function deletePlayList(event) {
  if (window.confirm(`Realy delete ${event.target.parentNode.dataset.listTitle}?`)) {
    connect('DELETE', `/playlists/${event.target.parentNode.dataset.listId}`, () => {
      connect('GET', '/playlists', generatePlayLists);
    });
  }
}

function generatePlayLists(data) {
  
  let defaultLists = document.querySelector('.default-lists');
  let userLists = document.querySelector('.user-lists');
  defaultLists.innerHTML = '';
  let allList = document.createElement('div');
  allList.classList.add('playlist');
  allList.classList.add('alltracks');
  let allTracks = document.createElement('span');
  allTracks.textContent = 'All tracks';
  allList.appendChild(allTracks);
  defaultLists.appendChild(allList);

  allTracks.addEventListener('click', () => {
    if (prevList !== undefined) {
      prevList.classList.remove('now-playing');
    }
    prevList = allTracks.parentNode;
    allTracks.parentNode.classList.add('now-playing');
    connect('GET', '/playlist-tracks', generateTracks);
  });
  userLists.innerHTML = '';
  document.querySelector('.track-list').innerHTML = '';
  
  data.forEach((item) => {
    
    let playList = document.createElement('div');
    playList.classList.add('playlist');
    playList.setAttribute('data-list-id', item.id);
    playList.setAttribute('data-list-title', item.title);
    
    let span = document.createElement('span');
    span.textContent = item.title;
    span.addEventListener('click', () => {
      if (prevList !== undefined) {
        prevList.classList.remove('now-playing');
      }
      prevList = span.parentNode;
      span.parentNode.classList.add('now-playing');
      connect('GET', `/playlist-tracks/${span.parentNode.dataset.listId}`, generateTracks);
    });
    playList.appendChild(span);
    
    if (item.system === 1) {
      
      playList.classList.add('favorites');
      defaultLists.appendChild(playList);
      
    } else if (item.system === 0) {
      
      let delButton = document.createElement('div');
      delButton.classList.add('playlist-delete');
      delButton.textContent = 'X';
      delButton.addEventListener('click', deletePlayList);
      
      playList.appendChild(delButton);
      
      userLists.appendChild(playList);
    }
  });

  const addList = document.querySelector('.add-list');
  addList.addEventListener('click', addNewList);
}

function convertSeconds(seconds) {
  let minutes = Math.floor(seconds / 60);
  seconds = Math.floor(seconds % 60);
  return `${minutes}:${seconds < 10 ? '0'+ seconds : seconds}`;
}

function addToFavorite(track) {
  connect('POST', `/playlist-tracks/1/${track.dataset.trackId}`, console.log);
  const star = document.querySelector('.star');
  star.style.backgroundImage = 'url(img/starblue.svg)';
}

function colorStar(data) {
  const star = document.querySelector('.star');
  if (data.result) {
    star.style.backgroundImage = 'url(img/starblue.svg)';
  } else {
    star.style.backgroundImage = 'url(img/star.svg)';
  }
}

function starFavoriteTrack(track) {
  connect('POST', `/favorite-track/${track.dataset.trackId}`, colorStar);
}

function addPlaylistsToDialog(data) {
  const trackforinsert = document.querySelector('.track-for-insert');
  const currentTrack = document.querySelector('.currenttrack');
  trackforinsert.innerHTML = `Insert <b>${currentTrack.dataset.trackTitle}</b> into the chosen playlist`;
  const lists = document.getElementById('lists');
  lists.innerHTML = '';
  const emptyoption = document.createElement('option');
  lists.appendChild(emptyoption);
  data.forEach((list, index) => {
    if (index > 0) {
      const option = document.createElement('option');
      option.setAttribute('data-list-id', list.id);
      option.textContent = list.title;
      lists.appendChild(option);
    }
  });
  const cancelButton = document.getElementById('cancel');
  const listDialog = document.getElementById('list-dialog');
  const save = document.getElementById('save');
  listDialog.showModal();
    
  cancelButton.addEventListener('click', () => {
    listDialog.close();
    listDialog.removeAttribute('open');
  });

  save.addEventListener('click', () => {
    const listId = lists.options[lists.selectedIndex].dataset.listId;
    const trackId = currentTrack.dataset.trackId;
    listDialog.close();
    listDialog.removeAttribute('open');
    connect('POST', `/playlist-tracks/${listId}/${trackId}`, console.log);
  });
}

function addTrackToList() {
  connect('GET', '/playlists', addPlaylistsToDialog);
}

function displayCurrentTrack(track) {
  let src = track.dataset.trackPath;
  src = `music/${src.slice(35)}`;
  const audio = document.querySelector('.audio');
  audio.setAttribute('src', src);
  audio.addEventListener('loadedmetadata', () => {
    const currentTrack = document.querySelector('.currenttrack');
    currentTrack.setAttribute('data-track-id', track.dataset.trackId);
    currentTrack.setAttribute('data-track-title', track.dataset.trackTitle);
    const trackTitle = document.querySelector('.title');
    trackTitle.textContent = track.dataset.trackTitle;
    const trackNote = document.querySelector('.note');
    trackNote.textContent = track.dataset.trackArtist;
    const volume = document.querySelector('.volume');
    volume.value = audio.volume * 100;
    volume.addEventListener('input', (e) => {
      audio.volume = parseInt(volume.value, 10) / 100;
    });
    const elapsed = document.querySelector('.elapsed');
    elapsed.textContent = convertSeconds(audio.currentTime);
    const time = document.querySelector('.time');
    time.value = audio.currentTime * 100 / audio.duration;
    time.addEventListener('input', (e) => {
      audio.currentTime = audio.duration * parseInt(time.value, 10) / 100;
      elapsed.textContent = convertSeconds(audio.currentTime);
    });
    const duration = document.querySelector('.duration');
    duration.textContent = convertSeconds(audio.duration);
    const playpause = document.querySelector('.playpause');
    playpause.style.backgroundImage = 'url(img/play.svg)';
    playpause.addEventListener('click', (e) => {
      if (audio.paused) {
        audio.play();
        playpause.style.backgroundImage = 'url(img/pause.svg)';
      } else {
        audio.pause();
        playpause.style.backgroundImage = 'url(img/play.svg)';
      }
    });
    audio.addEventListener('timeupdate', (e) => {
      time.value = audio.currentTime * 100 / audio.duration;
      elapsed.textContent = convertSeconds(audio.currentTime);
    });
    const addTrack = document.querySelector('.trackadd');
    addTrack.addEventListener('click', () => {
      addTrackToList();
    });
    const star = document.querySelector('.star');
    star.addEventListener('click', () => {
      addToFavorite(track);
    });
    starFavoriteTrack(track);
  });
}

function emptyCurrentTrack() {
  const audio = document.querySelector('.audio');
  audio.setAttribute('src', '#');
  const trackTitle = document.querySelector('.title');
  trackTitle.textContent = 'Current track';
  const trackNote = document.querySelector('.note');
  trackNote.textContent = 'artist';
  const star = document.querySelector('.star');
  star.removeEventListener('click', () => {});
}

function loadTrack(event) {
  if (prevTrack !== undefined) {
    prevTrack.classList.remove('now-playing');
  }
  prevTrack = event.target;
  event.target.classList.add('now-playing');
  displayCurrentTrack(event.target);
}

function generateTracks(data) {
  emptyCurrentTrack();
  const trackList = document.querySelector('.track-list');
  trackList.innerHTML = '';
  data.forEach((item) => {
    const track = document.createElement('div');
    track.classList.add('track');
    track.setAttribute('data-track-id', item.id);
    track.setAttribute('data-track-artist', item.artist);
    track.setAttribute('data-track-path', item.path);
    track.setAttribute('data-track-title', item.title);
    track.addEventListener('click', loadTrack);     // !!!!!!!!!!!!!   EZ JON

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

connect('GET', '/playlists', generatePlayLists);
