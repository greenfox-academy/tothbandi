'use strict';
const photos = [
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
// console.log(document.querySelectorAll('li'));
// consol.log(thumbBg);
// let a = document.querySelector('.chosen-photo');
// a.style.backgroundImage = 'url("images/sample.jpg")';

// let lis = document.querySelectorAll('.thumbnail');
// lis[0].style.backgroundImage

rightBtn.addEventListener('click', (event) => {
  if (activeThumb < thumbnails.length - 1){
    setNormalThumbnail();
    activeThumb++;
    setChosenThumbnail(activeThumb);
  } else {
    oneStepLeft();
  }
});

leftBtn.addEventListener('click', (event) => {
  if (activeThumb > 0){
    setNormalThumbnail();
    activeThumb--;
    setChosenThumbnail(activeThumb);
  } else {
    oneStepRight();
  }
});

function oneStepLeft(){
  for(let i = 1; i < thumbnails.length; i++){
    thumbnails[i-1].style.backgroundImage = getFileFromThumb(i);
    // thumbnails[i-1].setAttribute('data-index', thumbnails[i].dataset.index);
    thumbnails[i-1].setAttribute('data-photosindex', thumbnails[i].dataset.photosindex);
  }
  let lastPhotosIndex = thumbnails[thumbnails.length - 1].dataset.photosindex;
  if( lastPhotosIndex < photos.length - 1){
    lastPhotosIndex++;

  } else {
    lastPhotosIndex = 0;
  }
  console.log(lastPhotosIndex);
  console.log(photos[lastPhotosIndex].file);
  thumbnails[thumbnails.length - 1].style.backgroundImage = 'url("images/' + photos[lastPhotosIndex].file + '")'; 
  thumbnails[thumbnails.length - 1].setAttribute('data-photosindex', lastPhotosIndex);
  setChosenPhoto(thumbnails[activeThumb].dataset.photosindex);    
}
 
function oneStepRight(){
  for(let i = thumbnails.length - 2; i >= 0 ; i--){
    thumbnails[i+1].style.backgroundImage = getFileFromThumb(i);
    // thumbnails[i-1].setAttribute('data-index', thumbnails[i].dataset.index);
    thumbnails[i+1].setAttribute('data-photosindex', thumbnails[i].dataset.photosindex);
  }
  let firstPhotosIndex = thumbnails[0].dataset.photosindex;
  if( firstPhotosIndex > 0){
    firstPhotosIndex--;
  } else {
    firstPhotosIndex = photos.length - 1;
  }
  console.log(firstPhotosIndex);
  console.log(photos[firstPhotosIndex].file);
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

  // console.log(event.target.dataset.index);  //getAttribute('style'));
  activeThumb = event.target.dataset.index;
  setChosenThumbnail(activeThumb);

});

function setChosenPhoto(photoIndex){
  // let str = 'url("images/' + photo.file + '")';

  // console.log(str);
  chosenPhoto.style.backgroundImage = 'url("images/' + photos[photoIndex].file + '")';
  photoTitle.textContent = photos[photoIndex].title;
  photoDesc.textContent = photos[photoIndex].story;

}

// setChosenPhoto(photos[1]);

// thumbnails.forEach((thumbnail, index, array) => {
//   thumbnail.style.backgroundImage = 'url("images/' + photos[index].file + '")';
// });

function styleChosenThumbnail(index){
  thumbBg[index].style.background='linear-gradient(to bottom, grey, white)' ; //setAttribute('background-color', 'red')); // .getAttribute('width'));
  //   box-shadow: 0 10px 5px gray;
  thumbBg[index].style.boxShadow = '0 -10px 5px grey';
}

function getFileFromThumb(index){
  let file = thumbnails[index].getAttribute('style');
  file = file.substring(18, file.length-1);
  return file;  
}

function setChosenThumbnail(index){
  // let file = thumbnails[index].getAttribute('style');
  // file = file.substring(18, file.length-1);
  // console.log(file);
// getFileFromThumb(index)
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