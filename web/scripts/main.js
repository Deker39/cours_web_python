var myImage = document.querySelector('img');

myImage.onclick = function() {
    var mySrc = myImage.getAttribute('src');
    if(mySrc === 'image/london.jpg') {
      myImage.setAttribute ('src','image/londonn.jpg');
    } else {
      myImage.setAttribute ('src','image/london.jpg');
    }
}

function viewDiv(){
  document.getElementById("div1").style.display = "block";
};
