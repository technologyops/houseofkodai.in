/*
 Author: karthik@houseofkodai.in
 Last upDate: 10 February 2010
 Notes:
    - learnt from emile http://github.com/madrobby/emile
    - seperates timer-loop from easings
    - check-out scripty2 for more easings
 */


/* 
  duration in milliseconds
  fn is invoked multiple times in the duration
  takes one parameter position 
  pos is 0 in start and 1 in end 
  pos returns true to continue and false to stop
*/
function tween(duration, fn) {
  if (!fn) return;
  var start = +new Date, duration = duration||1000, finish = start+duration
  var interval = setInterval(function(){
    var time = +new Date, pos = time>finish ? 1 : (time-start)/duration;
    if (fn(pos) || (time>finish)) { clearInterval(interval); };
  }, 20);
};

/*
 different easings grouped together
 */
easings = {
  /* acceleration at start and deceleration at end */
  speedupdown: function(pos){
    return (-Math.cos(pos*Math.PI)/2) + 0.5; 
  },

  /* refer to anime docs to understand this */
  color: function(source,target,pos){
    function s(str, p, c){ return str.substr(p,c||1); }
    var i = 2, j, c, tmp, v = [], r = [];
    while(j=3,c=arguments[i-1],i--)
      if(s(c,0)=='r') { c = c.match(/\d+/g); while(j--) v.push(~~c[j]); } else {
        if(c.length==4) c='#'+s(c,1)+s(c,1)+s(c,2)+s(c,2)+s(c,3)+s(c,3);
        while(j--) v.push(parseInt(s(c,1+j*2,2), 16)); }
    while(j--) { tmp = ~~(v[j+3]+(v[j]-v[j+3])*pos); r.push(tmp<0?0:tmp>255?255:tmp); }
    return 'rgb('+r.join(',')+')';
  },

  /* starts fast and bounces slowly to end */
  bounce: function(pos) {
    if (pos < (1/2.75)) {
      return (7.5625*pos*pos);
    } else if (pos < (2/2.75)) {
      return (7.5625*(pos =(1.5/2.75))*pos + .75);
    } else if (pos < (2.5/2.75)) {
      return (7.5625*(pos =(2.25/2.75))*pos + .9375);
    } else {
      return (7.5625*(pos =(2.625/2.75))*pos + .984375);
    }
  }
};

