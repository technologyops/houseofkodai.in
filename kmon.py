#!/usr/bin/python
'''
  28 DEC 2012: karthik@houseofkodai.in
'''
import os, time, socket

def daemonize(run, *runparams):
  try:
    #first fork
    pid = os.fork()
    if pid > 0: sys.exit(0) #exit first parent
    #decouple from parent
    os.chdir('/')
    os.setsid()
    os.umask(0)
    #second fork
    pid = os.fork()
    if pid > 0: sys.exit(0) #exit second parent
    sys.stdout.flush()
    sys.stderr.flush()
    #close all file-descriptors - use resource.getrlimit() for more precise value
    for fd in range(0, 3):
      try: os.close(fd)
      except: pass
    #open stdio handles
    if hasattr(os, "devnull"):
      os.open(os.devnull, os.O_RDWR) #stdin
    else:
      os.open('/dev/null', os.O_RDWR) #stdin
    os.dup2(0, 1) #stdout
    os.dup2(0, 2) #stderr
    import signal
    signal.signal(signal.SIGTERM, onsignal)
    run(runparams)
  except:
    pass

def http_parse_response(response):
  rcode = 0
  rhdr = []
  rbody = ''
  rlines = response.split('\r\n')
  a = rlines[0].split(' ', 2)
  try:
    rcode = int(a[1])
  except:
    rbody = 'ERR invalid response'
    return (rcode, rhdr, rbody)
  for i, ln in enumerate(rlines[1:]):
    if not ln:
      rbody = '\r\n'.join(rlines[i+2:])
      break
    rhdr.append(ln)
  return (rcode, rhdr, rbody)

def httpreq(host, port, request, timeout=2, maxrecv=1024):
  #simple quick-n-dirty http request
  try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  except:
    return '-ERR unable to create socket'
  s.settimeout(timeout)
  try:
    s.connect((host, port))
  except:
    s.close()
    return '-ERR unable to connect with %s:%s'%(host, port)
  s.sendall(request)
  response = []
  try:
    while 1:
      _ = s.recv(65536)
      if not _: break
      response.append(_)
  except:
    s.close()
    return '-ERR unable to recv from %s:%s'%(host, port)
  s.close()
  if not response:
    return '-ERR no response from %s:%s'%(host, port)
  return ''.join(response)

def run(svrlist=(), logfile='/tmp/kmon.log', pollinterval=5):
  request = 'GET %s HTTP/1.0\r\n\r\n'
  while True:
    try:
      svrlog = []
      for svr in SVRLIST:
        response = httpreq(svr[0], svr[1], request%(svr[2]))
        if ('-' == response[0]):
          rbody = response
        else:
          rcode, rhdr, rbody = http_parse_response(response)
        #log only the first line of response
        svrlog.append('%s %s %s' % (time.strftime('%d %b %Y %H:%M:%S'), svr[0], rbody.split('\n')[0]))
      #save log file
      file(LOGFILE, 'w').write('\n'.join(svrlog))
      time.sleep(POLLINTERVAL)
    except KeyboardInterrupt:
      break

if '__main__' == __name__:
  SVRLIST = (('trefoil.as.arizona.edu', 80, '/kweb/proc/status?kweb'),)
  LOGFILE = 'kmon.log'
  POLLINTERVAL = 5 #in seconds
  if hasattr(os, 'fork'):
    daemonize(run, SVRLIST, LOGFILE, POLLINTERVAL)
  else:
    run(SVRLIST, LOGFILE, POLLINTERVAL)
