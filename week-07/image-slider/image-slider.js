'use strict';
const photos = [
  { 
    file : 'white.jpg',
    title : 'White',
    story : 'Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. '
  },
  { 
    file : 'sample.jpg',
    title : 'Sample',
    story : 'Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. '
  },  
  {
    file : 'tropical_beach.jpg',
    title : 'Tropical Beach',
    story : 'Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. '
  },
  { 
    file : 'canyon.jpg',
    title : 'Canyon',
    story : 'Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. '
  },
  { 
    file : 'horse.jpg',
    title : 'Horses',
    story : 'Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. '
  },
  { 
    file : 'welsh_corgi.jpg',
    title : 'Welsh corgi',
    story : 'Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. '
  },
  { 
    file : 'moonlight.jpg',
    title : 'Moonlight',
    story : 'Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. '
  },
  { 
    file : 'dragonfly.jpg',
    title : 'Dragonfly',
    story : 'Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. '
  }
];

const thumbnails = document.querySelectorAll('.thumbnail');
const thumbBg = document.querySelectorAll('li');
const chosenPhoto = document.querySelector('.chosen-photo');
const thumbsCont = document.querySelector('.thumbs-cont');
const rightBtn = document.querySelector('.right');
const leftBtn = document.querySelector('.left');
const photoTitle = document.querySelector('.title');
const photoDesc = document.querySelector('.story');
let activeThumb = 0;

rightBtn.addEventListener('click', (event) => {
  rightEvent();
});

leftBtn.addEventListener('click', (event) => {
  leftEvent();
});

window.addEventListener('keyup', keyPressed);

function keyPressed(event){
  if(event.code === 'ArrowRight'){
    rightEvent();
  }
  if(event.code === 'ArrowLeft'){
    leftEvent();
  }
}

function rightEvent(){
  if (activeThumb < thumbnails.length - 1){
    setNormalThumbnail();
    activeThumb++;
    setChosenThumbnail(activeThumb);
  } else {
    oneStepLeft();
  }
}

function leftEvent(){
  if (activeThumb > 0){
    setNormalThumbnail();
    activeThumb--;
    setChosenThumbnail(activeThumb);
  } else {
    oneStepRight();
  }
}


function oneStepLeft(){
  for(let i = 1; i < thumbnails.length; i++){
    thumbnails[i-1].style.backgroundImage = getFileFromThumb(i);
    thumbnails[i-1].setAttribute('data-photosindex', thumbnails[i].dataset.photosindex);
  }
  let lastPhotosIndex = thumbnails[thumbnails.length - 1].dataset.photosindex;
  if( lastPhotosIndex < photos.length - 1){
    lastPhotosIndex++;

  } else {
    lastPhotosIndex = 0;
  }
  thumbnails[thumbnails.length - 1].style.backgroundImage = 'url("images/' + photos[lastPhotosIndex].file + '")'; 
  thumbnails[thumbnails.length - 1].setAttribute('data-photosindex', lastPhotosIndex);
  setChosenPhoto(thumbnails[activeThumb].dataset.photosindex);    
}
 
function oneStepRight(){
  for(let i = thumbnails.length - 2; i >= 0 ; i--){
    thumbnails[i+1].style.backgroundImage = getFileFromThumb(i);
    thumbnails[i+1].setAttribute('data-photosindex', thumbnails[i].dataset.photosindex);
  }
  let firstPhotosIndex = thumbnails[0].dataset.photosindex;
  if( firstPhotosIndex > 0){
    firstPhotosIndex--;
  } else {
    firstPhotosIndex = photos.length - 1;
  }
  thumbnails[0].style.backgroundImage = 'url("images/' + photos[firstPhotosIndex].file + '")'; 
  thumbnails[0].setAttribute('data-photosindex', firstPhotosIndex);
  setChosenPhoto(thumbnails[activeThumb].dataset.photosindex);  
}

function setNormalThumbnail() {
  thumbBg[activeThumb].style.background='linear-gradient(to top, grey, white)' ; //setAttribute('background-color', 'red')); // .getAttribute('width'));
  thumbBg[activeThumb].style.boxShadow = '0 0 0 grey';
}


thumbsCont.addEventListener('click', function(event){
  setNormalThumbnail();
  activeThumb = event.target.dataset.index;
  setChosenThumbnail(activeThumb);

});

function setChosenPhoto(photoIndex){
  chosenPhoto.style.backgroundImage = 'url("images/' + photos[photoIndex].file + '")';
  photoTitle.textContent = photos[photoIndex].title;
  photoDesc.textContent = photos[photoIndex].story;

}

function styleChosenThumbnail(index){
  thumbBg[index].style.background='linear-gradient(to bottom, grey, white)' ; //setAttribute('background-color', 'red')); // .getAttribute('width'));
  thumbBg[index].style.boxShadow = '0 -10px 5px grey';
}

function getFileFromThumb(index){
  let file = thumbnails[index].getAttribute('style');
  file = file.substring(18, file.length-1);
  return file;  
}

function setChosenThumbnail(index){
  setChosenPhoto(thumbnails[index].dataset.photosindex);
  styleChosenThumbnail(index);
}

function initPhotoViewer(){
  thumbnails.forEach((thumbnail, index, array) => {
    thumbnail.style.backgroundImage = 'url("images/' + photos[index].file + '")';
    thumbnail.setAttribute('data-index', index);
    thumbnail.setAttribute('data-photosindex', index);
  });
  setChosenThumbnail(activeThumb);
}

initPhotoViewer();