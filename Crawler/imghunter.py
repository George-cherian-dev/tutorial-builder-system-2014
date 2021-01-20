import os
import urllib
import urllib2
import sys
from bs4 import BeautifulSoup
import urllib2
import urlparse
from urllib import urlretrieve

def main(arg1,arg2):
	print "start of img for "+str(arg2)
	file2=open(arg2+".txt",'r')
	file3=open("test.txt",'a')
	opener = urllib2.build_opener()
	opener.addheaders = [('User-agent', 'Mozilla/5.0')]
	i=0
	try:
			os.makedirs(arg2)                             # create directory [current_path]/feed/address
	except:
			print "path already exists"
	for line in file2:
		page = opener.open(line).read()
		soup = BeautifulSoup(page)
		tag_image=soup.findAll("img")
		for image in tag_image:
			#print "Image: %(src)s" % image  
			#print str('http'+image["src"])
			urlretrieve('http:'+image["src"], arg2+"/"+str(i)+".png") 
			image.replace_with("CrawlSysImage"+str(i))
			i=i+1
		file3.write(str(soup))
		break
	