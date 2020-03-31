/*
 site: www.houseofkodai.in
 author: karthik ayyar
 last update date: 5 feb 2010
 */

/*
  function onreq(req){
    if (req.readyState == 4) {
      if (req.status==200) {
        homehtml = req.responseText;
      } else {
        sethtml(divstatus, 'fatal error: unable to load home page.');
      };
  };

  var req = mkreq();
  req.open('GET', 'home.html', true);
  req.onreadystatechange=function(){onreq(req);}
  req.send(null);

 */
function mkreq() {
  var request = false;
  try {
    request = new XMLHttpRequest();
  } catch (trymicrosoft) {
    try {
      request = new ActiveXObject("Msxml2.XMLHTTP");
    } catch (othermicrosoft) {
      try {
        request = new ActiveXObject("Microsoft.XMLHTTP");
      } catch (failed) {
        request = false;
      }
    }
  }
  if (!request) alert("Error initializing XMLHttpRequest!");
  return request;
};

function getelement(id) {
  if (document.getElementById) return document.getElementById(id);
  else if(document.all) return document.all[id]; //old IE
  else return false;
};

function sethtml(el, html) {
  el = typeof el == 'string' ? getelement(el) : el;
  if (!el) return;
  el.innerHTML = html;
  if (html) el.visibility = 'visible';
  else el.visibility = 'hidden';
};

function togglediv(div) {
  div = typeof div == 'string' ? getelement(div) : div;
  //toggle div style between block and none
  if (!div) return; //do nothing - no need to alert like getreq
  if (div.style.display == '' && div.offsetWidth != undefined && div.offsetHeight != undefined) {
    div.style.display = (div.offsetWidth!=0 && div.offsetHeight!=0)?'block':'none';
  };
  div.style.display = (div.style.display=='' || div.style.display=='block')?'none':'block';
};

function getwidth() {
  if (self.innerWidth) {
    return self.innerWidth;
  } else if (document.documentElement && document.documentElement.clientWidth) {
    return document.documentElement.clientWidth;
  } else if (document.body) {
    return document.body.clientWidth;
  };
  return false;
};

function getheight() {
  if (self.innerHeight) {
    return self.innerHeight;
  } else if (document.documentElement && document.documentElement.clientHeight) {
    return document.documentElement.clientHeight;
  } else if (document.body) {
    return document.body.clientHeight;
  };
  return false;
};

function getPosition(e) {
  e = window.event || e;
  var cursor = {x:0, y:0};
  if (e.pageX || e.pageY) {
    cursor.x = e.pageX;
    cursor.y = e.pageY;
  } else {
    var de = document.documentElement;
    var b = document.body;
    cursor.x = e.clientX + (de.scrollLeft || b.scrollLeft) - (de.clientLeft || 0);
    cursor.y = e.clientY + (de.scrollTop || b.scrollTop) - (de.clientTop || 0);
  };
  return cursor;
};

function togglevisible(el) {
  el = typeof el == 'string' ? getelement(el) : el;
  if (el && ('visible' == el.style.visibility)) {
    el.style.visibility = 'hidden';
  } else {
    el.style.visibility = 'visible';
  };
};

var wnd = {width:0, height:0};
function onresize() {
  wnd.width = getwidth();
  wnd.height = getheight();
};

function slyde(el, direction, ondone) {
  el = typeof el == 'string' ? getelement(el) : el;
  if (!el) return;
  direction=direction?direction.charAt(0).toLowerCase():'u';

  var startpos = wnd.height;
  var prop = 'top';
  el.style.left = 0;
  if ('l' == direction) {
    prop = 'left';
    startpos = wnd.width;
    el.style.top = 0;
  } else if ('r' == direction) {
    prop = 'left';
    startpos = -wnd.width;
    el.style.top = 0;
  } else if ('d' == direction) {
    startpos = -wnd.height;
  } else {
    direction = 'u';
  };

  //var now = +new Date;
  //sethtml('status', now+':'+direction+':'+prop+'('+startpos+','+el.style.left + ',' + el.style.top + ')');
  el.style[prop] = startpos+'px';
  el.style.visibility = 'visible';
  _slyde = function(pos) {
    var done = true;
    if (pos == 1) {
      done = true;
    } else {
      pos = Math.round(1000*pos);
      if (startpos > 0) {
        pos = startpos - pos;
        done = (pos <= 0);
      } else {
        pos = startpos + pos;
        done = (pos >= 0);
      };
    };
    if (done) {
      el.style[prop] = 0;
      if (ondone) ondone();
    } else {
      el.style[prop] = pos + 'px';
    };
    return done;
  };
  tween(5000, _slyde);
};

