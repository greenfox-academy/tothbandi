'use strict';

let audio = document.querySelector('.audio');
let pp = document.querySelector('.playpause');
let v = document.querySelector('.volume');
let t = document.querySelector('.time');
let el = document.querySelector('.elapsed');
let du = document.querySelector('.duration');
console.log(audio);
v.value = audio.volume * 100;
t.value = audio.currentTime * 100 / audio.duration;

function convertSeconds(seconds) {
    let minutes = Math.floor(seconds / 60);
    seconds = Math.floor(seconds % 60);
    return `${minutes}:${seconds < 10 ? '0'+ seconds : seconds}`;
}

el.textContent = convertSeconds(audio.currentTime);
du.textContent = convertSeconds(audio.duration);
t.addEventListener('input', (e) => {
    console.log(`time value: ${typeof parseInt(t.value)}`);

    audio.currentTime = audio.duration * parseInt(t.value) / 100;
    el.textContent = convertSeconds(audio.currentTime);

} );

v.addEventListener('input', (e) => {
    console.log(`volume value: ${typeof parseInt(v.value)}`);

    audio.volume = parseInt(v.value) / 100;
} );

pp.addEventListener('click', function(e)
{
  if(audio.paused)
  {
    audio.play();
    pp.style.backgroundImage = 'url(img/pause.svg)';
    console.log(audio.volume);
  }
  else
  {
    audio.pause();
    pp.style.backgroundImage = 'url(img/play.svg)';
  }

}, false);

// Add the following events: loadstart, play, ended, progress
// console.log the event name + "happened" to the console

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