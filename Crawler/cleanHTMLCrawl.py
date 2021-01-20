def stripHTMLTags (html):
  """
    Strip HTML tags from any string and transfrom special entities
  """
  import re
  text = html.decode('UTF-8')

  # apply rules in given order!
  rules = [
    { r'>\s+' : u'>'},                  # remove spaces after a tag opens or closes
    { r'\s+' : u' '},                   # replace consecutive spaces
    { r'\s*<br\s*/?>\s*' : u'\n'},      # newline after a <br>
    { r'</(div)\s*>\s*' : u'\n'},       # newline after </p> and </div> and <h1/>...
    { r'</(p|h\d)\s*>\s*' : u'\n\n'},   # newline after </p> and </div> and <h1/>...
    { r'<head>.*<\s*(/head|body)[^>]*>' : u'' },     # remove <head> to </head>
    { r'<a\s+href="([^"]+)"[^>]*>.*</a>' : r'\1' },  # show links instead of texts
    { r'[ \t]*<[^<]*?/?>' : u'' },            # remove remaining tags
    { r'^\s+' : u'' }                   # remove spaces at the beginning
  ]

  for rule in rules:
    for (k,v) in rule.items():
      regex = re.compile (k)
      text  = regex.sub (v, text)

  # replace special strings
  special = {
    '&nbsp;' : ' ', '&amp;' : '&', '&quot;' : '"',
    '&lt;'   : '<', '&gt;'  : '>'
  }

  for (k,v) in special.items():
    text = text.replace (k, v)
    return text
	
import MySQLdb
import os
import traceback
import sys
import imghunter
import html2text
from bs4 import BeautifulSoup
import urlparse
from urllib import urlretrieve
import urllib2
import urllib
import requests
from requests.exceptions import HTTPError


def main(arg1,arg2):
	print "hello clean "
	print( 'Number of arguments: {} arguments.'.format(arg1))
	opener = urllib2.build_opener()
	opener.addheaders = [('User-agent', 'Mozilla/5.0')]
	i=0
	k=0
	j="1"
	file3=open("test.txt","w")
	file4=open("seed.txt","a")
	db = MySQLdb.connect(host="localhost", user="root", passwd="root",db="tutorial_clients")
	file = open("selected.txt", "w")
	cursor = db.cursor()
	with open("myunique.txt") as f:
		links=[]
		for line in f:
			print(line)
			image= urllib.URLopener()
			try:
				ourUrl = opener.open(line).read()
			except:
				print 'page not available'
			else:
				try:
					file_name=str(arg2)+str(i)+".txt"
					j="11"
					dir_path1=str(format(arg1))+"/";
					j="12"
					dir_path = os.path.join(dir_path1)
					try:
						os.makedirs(dir_path)                             # create directory [current_path]/feed/address
					except:
						print "path already exists"
					try:
						#print  str(dir_path)+str(arg2)+str(i)+"/"
						os.makedirs(str(dir_path)+str(arg2)+str(i)+"/")                             # create directory [current_path]/feed/address
					except:
						print "path already exists for images"
					#cleaned = stripHTMLTags(ourUrl)
					j="20"
					k=0
					j="30"
					soup = BeautifulSoup(ourUrl)
					j="31"
					tag_image=soup.findAll("img")
					j="32"
					for image in tag_image:
						#print "Image: %(src)s" % image  
						#print  str(dir_path)+str(arg2)+str(i)+"/"+str(k)+".png"
						urlretrieve('http:'+image["src"], str(dir_path)+str(arg2)+str(i)+"/"+str(k)+".png") 
						#print str('http:'+image["src"])
						image.replace_with("CrawlSysImage"+str(k))
						#print k
						k=k+1
					j="33"
					
					j="34"
					#betterHTML =  ourUrl.decode(errors='ignore')
					betterHTML=soup.prettify(formatter="html")
					j="21"
					cleaned= html2text.html2text(betterHTML)
					j="22"
					cleaned=cleaned.encode(sys.stdout.encoding, errors='replace')
					j="2"
					#cleaned = cleaned.encode("UTF-8")
					j="3"
					score = str(cleaned).count("DFA")
					j="4"
					score = score + str(cleaned).count("NFA")
					j="5"
					score = score + str(cleaned).count("state")
					j="6"
					#print str(dir_path1)
					#print str(os.path)  # will return 'feed/address'
					#print str(dir_path)
					j="13"
					j="10"
					file1 = open(os.path.join(dir_path, file_name), 'w')
					print str(os.path.join(dir_path, file_name))
					j="7"
					file1.write(line)
					file1.write(str(cleaned));
					j="8"
					print(score)
					j="9"
					i=i+1
				except:
					print ("Document is not HTML"+j)
					traceback.print_exc()
					break
				else:
					if score>=100:
						k=k+1						
						print "Link included "+str(k)
						file.write(line)
						#imghunter.main(arg1,os.path.join(dir_path, str(arg2)+str(i-1)))
						file1.close()
						if(k>5):
							break
					else:
						file1.close()
						print "Link not included"
						#print str(os.path.join(str(arg1)+"/"+str(arg2)+str(i-1)+".txt"))
						os.remove(os.path.join(str(arg1)+"/"+str(arg2)+str(i-1)+".txt"));

					print "Success!"
	file.close()
	file3.close()
	f.close()