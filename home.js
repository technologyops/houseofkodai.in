var divstatus = false;
var bkimg = false;
var bkimg2 = false;
var bkimgidx = 0;
var wnd = {width:0, height:0};
var divcontent = false;
var diviframe = false;
var fontsz = "1.0em";
var req = mkreq();

/* image preloading */
var bkimglist = ['hok.jpg', 'guido-snoopy.jpg', 'laila-majnu.jpg', 'where-eagles-dare.jpg'];
_preload = {};

/* function _rndimgsort() { return Math.floor((Math.random()*bkimglist.length)-1);};
bkimglist = bkimglist.sort(_rndimgsort); */

function bkslide(direction){
  bkimg2.style.visibility='hidden';
  direction=direction?direction.charAt(0).toLowerCase():'u';
  if (('l' == direction) || ('d' == direction)) {
    bkimgidx--;
  } else {
    bkimgidx++;
  };
  if (bkimgidx < 0) bkimgidx = bkimglist.length - 1;
  else if (bkimgidx >= bkimglist.length) bkimgidx = 0;

  bkimg2.src = bkimglist[bkimgidx];
  slyde(bkimg2, direction, function(){bkimg.src=bkimglist[bkimgidx]; bkimg2.style.visibility='hidden';});
};

var divhide = "<div id='hide'; display:'block'; float:top;>\
  <p><a onclick='resizeText(1); return false;' href='javascript:void(0);'>+</a>\
  &nbsp;<a onclick='resizeText(-1); return false;' href='javascript:void(0);'>-</a>\
  &nbsp;<a href='javascript:void(0);' onclick='togglevisible(divcontent); return false;' id='toggle'>h for hide</a>\
  </p></div>";

function menu(idx) {
  if ((!idx) || (0 > idx) || (idx >= html_content.length)) idx = 0;
  divcontent.innerHTML = divhide + html_content[idx];
  diviframe.style.visibility = 'hidden';
  divcontent.style.visibility = 'visible';
  divcontent.focus();
};

function geturl(url, newin) {
  if (newin) {
    window.open(url);
  } else {
    diviframe.innerHTML = '<iframe src="'+url+'" width="100%" height="100%" marginwidth="0" marginheight="0" frameborder="no" scrolling="yes"></iframe>';
    diviframe.style.visibility = 'visible';
    diviframe.focus();
    divcontent.style.visibility = 'hidden';
  };
};

function _onkeyup(k) {
  var ev=window.event?event:k; //IE explicit window.event and Firefox implicit k
  var keyval=ev.keyCode?ev.keyCode:ev.charCode;
  //alert('_onkeyup: '+ev.type+" ("+keyval+")");
  if (37==keyval) {
    bkslide('left');
  } else if (39==keyval) {
    bkslide('right');
  /*} else if (72==keyval) {
    togglevisible(divcontent);
  } else if (107==keyval) {
    resizeText(1);
  } else if (109==keyval) {
    resizeText(-1); */
  } else {
    //sethtml(divstatus, '_onkeyup: '+keyval);
  };
};

function resizeText(multiplier) {
  fontsz = parseFloat(fontsz) + (multiplier * 0.2) + "em";
  document.body.style.fontSize = fontsz;
};

function _onorderboks() {
  if (4 == req.readyState) {
    sethtml(divstatus, '');
    if (200 == req.status) {
      divcontent.innerHTML = req.responseText;
    };
    diviframe.style.visibility = 'hidden';
    divcontent.style.visibility = 'visible';
  };
};

function postorderboks() {
  sethtml(divstatus, '&nbsp;ordering bok, please wait...&nbsp;');  
  req.open("POST", '/bok', true);
  req.onreadystatechange = _onorderboks;
  req.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
  var frmbok = document.forms[0];
  var s = '';
  if (frmbok.elements.length > 0) {
    if (frmbok.elements[0].name) {
      s = frmbok.elements[0].name + '=' + frmbok.elements[0].value;
    };
    for(i=0; i<frmbok.elements.length; i++) {
      if (frmbok.elements[i].name && frmbok.elements[i].value) {
        if (s) {
          s = s + '&' + frmbok.elements[i].name + '=' + frmbok.elements[i].value;
        } else {
          s = s + frmbok.elements[i].name + '=' + frmbok.elements[i].value;
        };
      };
    };
  };
  req.send(s);
};

function orderboks() {
  sethtml(divstatus, '&nbsp;bok wait...&nbsp;');
  req.open("GET", '/bok', true);
  req.onreadystatechange = _onorderboks;
  req.send(null);
};

window.onresize = onresize;
document.onkeyup = _onkeyup;
window.onload = function() {
  onresize(); // to initialize wnd
  divstatus = getelement('status');
  bkimg = getelement('bkimg');
  bkimg2 = getelement('bkimg2');
  divcontent = getelement('content');
  diviframe = getelement('iframe');
  divcontent.innerHTML = html_content[0];

  /* image preloading - cache images */
  var img = new Image();
  for (var i=0; i<bkimglist.length; i++) {
    _preload[bkimglist[i]] = false; /* undefined is false - this is not reqd. ?! */
    img.onload = function() { _preload[bkimglist[i]] = true; };
    img.src = bkimglist[i];
  };

  /* the following to slide, if user clicked and hok.jpg is not preloaded yet */
  bkimg.onload = function() {
    sethtml(divstatus, '');
    _preload[bkimglist[0]] = true;
    bkimg.style.visibility = 'visible';
    /*slyde(bkimg, 'up', function(){bkimg.onload=function(){}; getelement('topmenu').style.visibility='visible'; menu(0);}); */
    slyde(bkimg, 'up', function(){bkimg.onload=function(){}; getelement('topmenu').style.visibility='visible'; });
  };
  sethtml(divstatus, '&nbsp;loading...&nbsp;');
  bkimg.src = bkimglist[0];
};
