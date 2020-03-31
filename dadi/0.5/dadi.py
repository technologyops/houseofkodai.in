#! /usr/bin/env python
'''
  23 APR 2011: karthik@houseofkodai.in
    * for use with DaDi
'''

xlate={0xc0:'A', 0xc1:'A', 0xc2:'A', 0xc3:'A', 0xc4:'A', 0xc5:'A',
  0xc6:'Ae', 0xc7:'C',
  0xc8:'E', 0xc9:'E', 0xca:'E', 0xcb:'E',
  0xcc:'I', 0xcd:'I', 0xce:'I', 0xcf:'I',
  0xd0:'Th', 0xd1:'N',
  0xd2:'O', 0xd3:'O', 0xd4:'O', 0xd5:'O', 0xd6:'O', 0xd8:'O',
  0xd9:'U', 0xda:'U', 0xdb:'U', 0xdc:'U',
  0xdd:'Y', 0xde:'th', 0xdf:'ss',
  0xe0:'a', 0xe1:'a', 0xe2:'a', 0xe3:'a', 0xe4:'a', 0xe5:'a',
  0xe6:'ae', 0xe7:'c',
  0xe8:'e', 0xe9:'e', 0xea:'e', 0xeb:'e',
  0xec:'i', 0xed:'i', 0xee:'i', 0xef:'i',
  0xf0:'th', 0xf1:'n',
  0xf2:'o', 0xf3:'o', 0xf4:'o', 0xf5:'o', 0xf6:'o', 0xf8:'o',
  0xf9:'u', 0xfa:'u', 0xfb:'u', 0xfc:'u',
  0xfd:'y', 0xfe:'th', 0xff:'y',
  0xa1:'!', 0xa2:'{cent}', 0xa3:'{pound}', 0xa4:'{currency}',
  0xa5:'{yen}', 0xa6:'|', 0xa7:'{section}', 0xa8:'{umlaut}',
  0xa9:'{C}', 0xaa:'{^a}', 0xab:'<<', 0xac:'{not}',
  0xad:'-', 0xae:'{R}', 0xaf:'_', 0xb0:'{degrees}',
  0xb1:'{+/-}', 0xb2:'{^2}', 0xb3:'{^3}', 0xb4:"'",
  0xb5:'{micro}', 0xb6:'{paragraph}', 0xb7:'*', 0xb8:'{cedilla}',
  0xb9:'{^1}', 0xba:'{^o}', 0xbb:'>>',
  0xbc:'{1/4}', 0xbd:'{1/2}', 0xbe:'{3/4}', 0xbf:'?',
  0xd7:'*', 0xf7:'/'
}

fortunelines = '''
Do not argue with an idiot. He will drag you down to his level and beat you with experience.
I want to die peacefully in my sleep, like my grandfather.. Not screaming and yelling like the passengers in his car.
I asked God for a bike, but I know God doesn't work that way. So I stole a bike and asked for forgiveness.
Going to church doesn't make you a Christian any more than standing in a garage makes you a car.
We live in a society where pizza gets to your house before the police.
Women might be able to fake orgasms. But men can fake a whole relationship.
The last thing I want to do is hurt you. But it's still on the list.
Light travels faster than sound. This is why some people appear bright until you hear them speak.
If I agreed with you we'd both be wrong.
We never really grow up, we only learn how to act in public.
War does not determine who is right - only who is left.
Knowledge is knowing a tomato is a fruit; Wisdom is not putting it in a fruit salad.
Children: You spend the first 2 years of their life teaching them to walk and talk. Then you spend the next 16 years telling them to sit down and shut-up.
Politicians and diapers have one thing in common. They should both be changed regularly, and for the same reason.
My mother never saw the irony in calling me a son-of-a-bitch.
The early bird might get the worm, but the second mouse gets the cheese.
Evening news is where they begin with 'Good evening', and then proceed to tell you why it isn't.
To steal ideas from one person is plagiarism. To steal from many is research.
If God is watching us, the least we can do is be entertaining.
If 4 out of 5 people SUFFER from diarrhea... does that mean that one enjoys it?
If you think nobody cares if you're alive, try missing a couple of payments.
Better to remain silent and be thought a fool, than to speak and remove all doubt.
How is it one careless match can start a forest fire, but it takes a whole box to start a campfire?
A bus station is where a bus stops. A train station is where a train stops. On my desk, I have a work station..
Some people are like Slinkies ... not really good for anything, but you can't help smiling when you see one tumble down the stairs.
Did you know that dolphins are so smart that within a few weeks of captivity, they can train people to stand on the very edge of the pool and throw them fish?
A bank is a place that will lend you money, if you can prove that you don't need it.
I thought I wanted a career, turns out I just wanted paychecks.
Never, under any circumstances, take a sleeping pill and a laxative on the same night.
Whenever I fill out an application, in the part that says "If an emergency, notify:" I put "DOCTOR". What's my mother going to do?
I didn't fight my way to the top of the food chain to be a vegetarian
A computer once beat me at chess, but it was no match for me at kick boxing.
I didn't say it was your fault, I said I was blaming you.
I saw a woman wearing a sweat shirt with "Guess" on it...so I said "Implants?"
The shinbone is a device for finding furniture in a dark room.
Why does someone believe you when you say there are four billion stars, but check when you say the paint is wet?
The sole purpose of a child's middle name, is so he can tell when he's really in trouble.
God must love stupid people. He made SO many.
Women will never be equal to men until they can walk down the street with a bald head and a beer gut, and still think they are sexy.
Good girls are bad girls that never get caught.
Behind every successful man is his woman. Behind the fall of a successful man is usually another woman.
Some people say "If you can't beat them, join them". I say "If you can't beat them, beat them", because they will be expecting you to join them, so you will have the element of surprise.
Why do Americans choose from just two people to run for president and 50 for Miss America?
Crowded elevators smell different to midgets.
You do not need a parachute to skydive. You only need a parachute to skydive twice.
The voices in my head may not be real, but they have some good ideas!
A clear conscience is usually the sign of a bad memory.
The main reason Santa is so jolly is because he knows where all the bad girls live.
Laugh at your problems, everybody else does.
Never get into fights with ugly people, they have nothing to lose.
It's not the fall that kills you; it's the sudden stop at the end.
Artificial intelligence is no match for natural stupidity.
Always borrow money from a pessimist. He won't expect it back.
He who smiles in a crisis has found someone to blame.
A diplomat is someone who can tell you to go to hell in such a way that you will look forward to the trip.
We have enough gun control. What we need is idiot control.
Hospitality: making your guests feel like they're at home, even if you wish they were.
My opinions may have changed, but not the fact that I am right.
Money can't buy happiness, but it sure makes misery easier to live with.
When in doubt, mumble.
I discovered I scream the same way whether I'm about to be devoured by a great white shark or if a piece of seaweed touches my foot.
I intend to live forever. So far, so good.
Women may not hit harder, but they hit lower.
A little boy asked his father, "Daddy, how much does it cost to get married?" Father replied, "I don't know son, I'm still paying."
Worrying works! 90% of the things I worry about never happen.
Just remember...if the world didn't suck, we'd all fall off.
My psychiatrist told me I was crazy and I said I want a second opinion. He said okay, you're ugly too.
Some cause happiness wherever they go. Others whenever they go.
Jesus loves you, but everyone else thinks you're an asshole.
I don't trust anything that bleeds for five days and doesn't die.
I like work. It fascinates me. I sit and look at it for hours.
I should've known it wasn't going to work out between my ex-wife and me. After all, I'm a Libra and she's a bitch.
I always take life with a grain of salt, ...plus a slice of lemon, ...and a shot of tequila.
Never hit a man with glasses. Hit him with a baseball bat.
I used to be indecisive. Now I'm not sure.
You're never too old to learn something stupid.
When tempted to fight fire with fire, remember that the Fire Department usually uses water.
You are such a good friend that if we were on a sinking ship together and there was only one life jacket... I'd miss you heaps and think of you often.
I got in a fight one time with a really big guy, and he said, "I'm going to mop the floor with your face." I said, "You'll be sorry." He said, "Oh, yeah? Why?" I said, "Well, you won't be able to get into the corners very well."
Knowledge is power, and power corrupts. So study hard and be evil.
Does this rag smell like chloroform to you?
With sufficient thrust, pigs fly just fine.
To be sure of hitting the target, shoot first and call whatever you hit the target.
A bargain is something you don't need at a price you can't resist.
Some people hear voices.. Some see invisible people.. Others have no imagination whatsoever.
A TV can insult your intelligence, but nothing rubs it in like a computer.
If winning isn't everything why do they keep score?
Virginity is like a soapbubble, one prick and it is gone.
If at first you don't succeed, skydiving is not for you!
A bus is a vehicle that runs twice as fast when you are after it as when you are in it.
Hallmark Card: "I'm so miserable without you, it's almost like you're still here."
Whoever coined the phrase "Quiet as a mouse" has never stepped on one.
If you are supposed to learn from your mistakes, why do some people have more than one child.
Nostalgia isn't what it used to be.'''.split('\n')

nfortune = len(fortunelines)
import random
fortune = lambda: fortunelines[random.randint(0,nfortune)]

import re
nonasciire = re.compile(u'([\x00-\x7f]+)|([^\x00-\x7f])', re.UNICODE).sub

def latin1_to_ascii(unicrap):
  return str(nonasciire(lambda x: x.group(1) or xlate.setdefault(ord(x.group(2)), ''), unicrap))

import urllib2
def urlget(url):
  try:
    uh = urllib2.urlopen(url)
    udata = uh.read()
    uh.close()
  except:
    udata = ''
  return udata.strip()

SEPERATOR = '\n\g  *\n\y *\n\\r * \n'

import urlparse # if we're pre-2.6, this will not include parse_qs
try:
  from urlparse import parse_qs
except ImportError: # old version, grab it from cgi
  from cgi import parse_qs
  urlparse.parse_qs = parse_qs

gnewsurl = lambda s: parse_qs(str(s)).get('url',('',))[0]
surl = lambda s: s

channels = {
 'ins': ('http://news.google.com/news?ned=in&topic=n&output=rss', gnewsurl, 19800, '\g  I\n\y n\n\\r d\n\w i\n\\b a \n\g N\n\\r e\n\y w\n\g s ', 'India News'),
 'wns': ('http://news.google.com/news?ned=us&topic=w&output=rss', gnewsurl, 19800, '\g  W\n\y o\n\\r r\n\w l\n\\b d \n\g N\n\\r e\n\y w\n\g s ', 'World News'),
 'mnt': ('http://www.livemint.com/SectionRssfeed.aspx?LN=Latestnews', surl, 19800, '\g  M\n\y i\n\\r n\n\\b t ', 'Mint'),
 'nyt': ('http://www.nytimes.com/services/xml/rss/nyt/GlobalHome.xml', surl, 19800, '\g  New \n\y York \n\\r Times ', 'New York Times'),
 'bbc': ('http://feeds.bbci.co.uk/news/rss.xml', surl, 19800, '\g  B \n\y B \n\\r C ', 'BBC'),
 'hdu': ('http://www.thehindu.com/?service=rss', surl, 0, '\g  H \n\y i \n\\r n \n\\b d \n\w u ', 'The Hindu'),
 'hns': ('http://news.ycombinator.com/rss', surl, 19800, '\g  H\n\y a\n\\r c\n\w k\n\\b e\n\w r \n\g N\n\\r e\n\y w\n\g s ', 'Hacker News'),
}

import time
from xml.dom import minidom
def rss(feed):
  if not channels.has_key(feed): return ''
  (url, urlfn, toffset, title, mtitle) = channels[feed]
  s = urlget(url)
  try: xmldom = minidom.parseString(s)
  except: return ''

  a = []
  for item in xmldom.getElementsByTagName('item'):
    d = l = t = ''
    for child in item.childNodes:
      if 'pubDate' == child.nodeName:
        d = time.strftime('%H:%M', time.localtime(time.mktime(time.strptime(child.childNodes[0].data[:25].strip(),'%a, %d %b %Y %H:%M:%S')) + toffset))
      elif 'link' == child.nodeName: 
        l = urlfn(child.childNodes[0].data)
      elif 'title' == child.nodeName: 
        t = latin1_to_ascii(child.childNodes[0].data)
    a.append('%s %s %s\n%s %s'%(l, d, t, d, t))
  if len(a) > 25: a = a[:25]
  return ' %s IST\n%s\n%s\n'%(time.strftime('%H:%M', time.localtime()), title, SEPERATOR.join(a))

def dorss():
  for k in channels.keys():
    s = rss(k)
    if s:
      try: file(k, 'wb').write('\\b (-; %s ;-)\n%s'%(fortune(), s))
      except: continue

#protocol:timeout:host:port:params


import smtplib
def dosmtp(svr, port, helostr, timeout):
  (svr, port, helostr, timeout) = ('mx.enmail.com', 25, 'stmpmon', 2)
  now = time.time()
  try:
    svr = smtplib.SMTP(svr, port, helostr, timeout)
    r = svr.docmd('NOOP')
    t = int((time.time()-now)*100)
    svr.quit()
    if 250 == r[0]: return t
    else: return 0
  except:
    return 0

import os
if '__main__' == __name__:
  os.chdir('/home/enmail/domains/houseofkodai.in/dadi/0.5/')
  dorss()
  #print dosmtp()
