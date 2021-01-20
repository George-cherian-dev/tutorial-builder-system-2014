
import sys
import re
import urllib
import urlparse
import socket
import urllib2
import os
from urllib import FancyURLopener
from time import strftime
import time
timeout = 15
socket.setdefaulttimeout(timeout)
tocrawl = []
crawled = []
result=[]
visited={}
t1=0
t2=0
t3=0
code_200=0
code_403=0
code_404=0
error=0
number=0
totalsize=0
link_exp = re.compile('adurl=(.*?)[\'"].*?>')
link_exp1 = re.compile('<a\s*href=[\'|"](.*?)[\'"]')
link_exp2 = re.compile('<a.*?q=(.*?)[\'"]')
frame_exp=re.compile('<frame\s*src=[\'|"](.*?)[\'"].*?>')  # added R
numberoflink = raw_input("How many links you want to crawl")
numberoflinks=int(numberoflink)
var = raw_input("Enter key phrase: ")
crawling="http://www.google.com/search?q="+var
f=open(var+".txt","w")
size=open("filesize.txt","w")  # added R
#f.write("*******Level-1*********\n")
#f.write("http://www.google.com/search?q="+var)
#f.write("        \n")
class MyOpener(FancyURLopener):
	version = 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)'

try:
    myopener = MyOpener()
    page = myopener.open(crawling)
    msg=page.read()
    #print msg
except IOError, error_code:
    error=1
    if error_code[0]=="http error":
        if error_code[1]==401:
            print "Password required"
        elif error_code[1]==404:
            print "file not found"
        elif error_code[1]==500:
            print "server is down"
        else:
            print (error_code)
if error==0:
    links=[]
    #links = link_exp.findall(msg)
    links1 = link_exp1.findall(msg)
    morelinks = link_exp2.findall(msg)
    mainlink1=[]
    newlinks1 = frame_exp.findall(msg) # added R
    print msg
    size.write(msg)                    # added R
    crawled.append(crawling)
    mainlink = links + newlinks1 +links1 + morelinks       # added R
    f.write("*******Level-2*********\n")
    f.write("        \n")
    #print mainlink
    for linkin in (mainlink.pop(0) for _ in xrange(len(mainlink))):
        if 'http' in linkin and linkin.startswith('h'):
            print linkin
            ind = linkin.find(':http://')
            print(ind)
            linkin = linkin[ind+1:]
            print(linkin)
            ind = linkin.find('&amp')
            print(ind)
            if ind > -1:
                linkin = linkin[:ind]
            print(linkin)
            ind = linkin.find('%')
            print(ind)
            if ind > -1:
                linkin = linkin[:ind]
            print(linkin)
            mainlink1.append(linkin)

    for link in (mainlink1.pop(0) for _ in xrange(len(mainlink1))):  # added R

        if number+1 <= numberoflinks:
            if (link not in crawled) and (link not in tocrawl) and (not link.startswith('/') and not link.startswith('#') and  "google.com" not in link and  "youtube" not in link and  "q=cache" not in link):
                size=open("filesize.txt","w")
                myopener = MyOpener()
                page1=myopener.open(link)
                code=urllib.urlopen(link).getcode()
                if code==200:
                   code_200+=1
                elif code==403:
                   code_403+=1
                elif code==404:
                   code_404+=1
                msg1=page1.read()
                size.write(msg1)
                t=time.time()
                print number+1,"|",link,"|",os.path.getsize("filesize.txt"),"bytes","|", strftime("%H:%M:%S"),"|", code
                totalsize+=os.path.getsize("filesize.txt")
                tocrawl.append(link)
                result.append(link)
                f.write(link)
                size.close()
                f.write("\n")
                if number==1:
                        t1=t
                elif number==numberoflinks-1:
                        t2=t
                number+=1
	else:
            t3=t2-t1
            print "total time=",t3
            print "total number of 200(ok) pages=",code_200
            print "total number of 403(forbidden) pages=",code_403
            print "total number of 404(page not found) pages=",code_404
            print "totalsize = ",totalsize
            sys.exit()
#################################################################
#####################Got 10 results from Google##################
#################################################################
for URL in (tocrawl.pop(0) for _ in xrange(len(tocrawl))):
    try:
        myopener = MyOpener()
        page = myopener.open(URL)
        f.write("        \n")
        f.write("********"+URL+"*********")
        f.write("        \n")
        msg=page.read()
    except IOError, error_code:
        error=1
        if error_code[0]=="http error":
            if error_code[1]==401:
                print "Password required"
            elif error_code[1]==404:
                print "file not found"
            elif error_code[1]==500:
                print "server is down"
            else:
                print (error_code)
    if error==0:
       newlinks = link_exp1.findall(msg)
       newlinks1 = frame_exp.findall(msg)   # added R
       size=open("filesize.txt","w")
       size.write(msg)
       crawled.append(URL)
       mainlink = newlinks1 + newlinks          # added R
       Domain = urlparse.urlparse(URL)
       for link in (mainlink.pop(0) for _ in xrange(len(mainlink))): # added R

           if number+1 <= numberoflinks:
                if link.startswith('/'):
		    link = 'http://' + Domain[1] + link
                elif link.startswith('#'):
		    link = 'http://' + Domain[1] + Domain[2] + link
                elif not link.startswith('http'):
		    link = 'http://' + Domain[1] + '/' + link

                if (link not in crawled) and (link not in tocrawl) and (link not in result):
                    size=open("filesize.txt","w")
                    myopener = MyOpener()
                    page1=myopener.open(link)
                    code=urllib.urlopen(link).getcode()
                    if code==200:
                         code_200+=1
                    elif code==403:
                         code_403+=1
                    elif code==404:
                         code_404+=1
                    msg1=page1.read()
                    size.write(msg1)
                    t=time.time()
                    print number+1,"|",link,"|",os.path.getsize("filesize.txt"),"bytes","|", strftime("%H:%M:%S"),"|", code
                    totalsize+=os.path.getsize("filesize.txt")
                    tocrawl.append(link)
                    result.append(link)
                    f.write(link)
                    size.close()
                    f.write("\n")
                    if number==1:
                        t1=t
                    elif number==numberoflinks-1:
                        t2=t
                    number+=1
           else:
               print "End of program"
               t3=t2-t1
               print "total time=",t3
               print "total number of 200(ok) pages=",code_200
               print "total number of 403(forbidden) pages=",code_403
               print "total number of 404(page not found) pages=",code_404
               print "totalsize = ",totalsize
               sys.exit()

print "End of program"
t3=t2-t1
print "total time=",t3
print "total number of 200(ok) pages=",code_200
print "total number of 403(forbidden) pages=",code_403
print "total number of 404(page not found) pages=",code_404
print "totalsize = ",totalsize
sys.exit()
f.close()

