#!/usr/bin/python

import sys
import urllib2

for i in xrange(12, 13) :
	string_number = str(i) if i > 9 else '0' + str(i)
	url = "http://npteldownloads.iitm.ac.in/downloads_mp4/106102064/lec{0}.mp4".format(string_number)
	file_name = url.split('/')[-1]
	u = urllib2.urlopen(url)
	f = open(file_name, 'wb')
	meta = u.info()
	file_size = int(meta.getheaders("Content-Length")[0])
	print("Downloading: {0} Bytes: {1}".format(url, file_size))

	file_size_dl = 0
	block_sz = 8192
	while True:
	    buffer = u.read(block_sz)
	    if not buffer:
	        break
	    file_size_dl += len(buffer)
	    f.write(buffer)
	    p = float(file_size_dl) / file_size
	    status = r"{0}  [{1:.2%}]".format(file_size_dl, p)
	    status = status + chr(8)*(len(status)+1)
	    sys.stdout.write(status)

	f.close()
