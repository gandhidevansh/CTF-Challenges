
function setvalues() {
var c = 0;
var txt = '< d3vil CTF />';
typeeffect();
}

function typeeffect() {
  if (c < txt.length) {
    document.getElementById("title").innerHTML += txt.charAt(i) ;
    c++;
    setTimeout(typeeffect, 200);
  }
}

