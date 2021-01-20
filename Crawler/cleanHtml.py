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



def isNotNum(s):
    try:
        float(s)
        return False
    except ValueError:
        return True
def isNotExist(t,sub):
	try:
		cnx5 = MySQLdb.connect(host="localhost",user="root",passwd="root",db="tutorial_clients")
		db5 = cnx5.cursor()
		s5='SELECT * FROM terms WHERE term="{}" AND sub_id={}'.format(t,sub)
		db5.execute(s5)
		for row in db5:
			return False
		return True
	except ValueError:
		return True
		
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
	cnx2=MySQLdb.connect(host="localhost",user="root",passwd="root",db="tutorial_clients")
	db2 = cnx2.cursor() 
	i=0
	k1=0
	j="1"
	file3=open("test.txt","w")
	file4=open("seed.txt","a")
	cnx = MySQLdb.connect(host="localhost", user="root", passwd="root",db="tutorial_clients")
	db = cnx.cursor()
	s='SELECT * FROM subject WHERE sub_id = {}'.format(arg1)
	db.execute(s)
	file = open("selected.txt", "w")
	for row in db:
	    top='{}'.format(row[1])
	    subj=row[3]
	print top+" in "+subj
	with open("myunique.txt") as f:
		links=[]
		for line in f:
			flag=0
			flagc=0
			score=0
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
						
					file1 = open(os.path.join(dir_path, file_name), 'w')
					print str(os.path.join(dir_path, file_name))
					#cleaned = stripHTMLTags(ourUrl)
					j="20"
					k=0
					j="30"
					soup = BeautifulSoup(ourUrl)
					j="31"
					tag_image=soup.findAll("img")
					j="32"
					#print tag_image
					i1=0
					for image in tag_image:
						try:
							flag=1
							#print "Image: %(src)s" % image  
							#print  str(dir_path)+str(arg2)+str(i)+"/"+str(k)+".png"
							a1=str(image['src'])
							format1 =a1[-4:]
							#print format1
							#print "hello "+a1
							if(format1=='.gif'):
								continue
							if a1.startswith("http"):
								print str(' perm http:'+a1)
								urlretrieve('http:'+a1, str(dir_path)+str(arg2)+str(i)+"/"+str(k)+format1) 
								
							else:
								#print "temp"
								try:
									ind=line.index('org')
									tempUrl = line[ind+3]+a1
								except:
									try:
										ind=line.index('com')
										tempUrl = line[ind+3]+a1
									except:
										try:
											ind=line.index('edu')
											tempUrl = line[ind+3]+a1
										except:
											pass
								#print tempUrl
								tempUrl=line[:-1]+tempUrl
								#print 'temp '+tempUrl
								urlretrieve(tempUrl, str(dir_path)+str(arg2)+str(i)+"/"+str(k)+format1) 
							image.replace_with("CrawlSysImage"+str(k))
							#print k
							i1=i1+1
							k=k+1
						except:
							print "image error"
					
					if(i1==0):
						imgp="N"
					else:
						imgp="Y"
					if(flagc==0):
						commp="N"
					else:
						commp="Y"
					j="33"
					try:
						ddata= os.path.join(str(arg1)+"/"+str(arg2)+str(i)+".txt")
						s3="INSERT INTO crawlable(c_id,data,img_p,comment_p,sub_id) VALUES("+str(arg1)+str(arg2)+str(i)+",'"+ddata+"','"+imgp+"','"+commp+"',"+str(arg1) +" )"
						db2.execute(s3)
						cnx2.commit()
						if(i1!=0):
							s3="INSERT INTO images(c_id,imageloc,imagecount) VALUES("+str(arg1)+str(arg2)+str(i)+",'"+str(dir_path)+str(arg2)+str(i)+"/"+"',"+str(i1)+" )"
							db2.execute(s3)
							cnx2.commit()
					except:
						print "db error"
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
					score = str(cleaned).count(top)
					j="4"
					score = score + str(cleaned).count(subj)
					j="5"
					score = score + (str(cleaned).count(top+" in "+subj)*2)
					score = score + (str(cleaned).count(top+" for "+subj)*2)
					score = score + (str(cleaned).count(top+" from "+subj)*2)
					score = score + (str(cleaned).count(top+" of "+subj)*2)
					j="6"
					#print str(dir_path1)
					#print str(os.path)  # will return 'feed/address'
					#print str(dir_path)
					j="13"
					j="10"
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
						print "Link included "+str(k)
						file.write(line)
						#ddata=os.path.join(str(arg1)+"/"+str(arg2)+str(i-1)+".txt")
						#s3="INSERT INTO data(data_id,data,img,comment_p,sub_id) VALUES("+arg1+str(arg2)+str(i-1)+",'"+ddata+"','"+imgp+"','"+commp+"',"+str(arg1) +"  )"
						#db2.execute(s3)
						#cnx2.commit()
						#imghunter.main(arg1,os.path.join(dir_path, str(arg2)+str(i-1)))
						file1.close()
					else:
						file1.close()
						print "Link not included"
						try:
							ddata=os.path.join(str(arg1)+"/"+str(arg2)+str(i-1)+".txt")
							s3="DELETE FROM crawlable WHERE c_id="+arg1+str(arg2)+str(i-1)
							db2.execute(s3)
							s3="DELETE FROM images WHERE c_id="+arg1+str(arg2)+str(i-1)
							db2.execute(s3)
							cnx2.commit()
						except:
							print "error"
						#print str(os.path.join(str(arg1)+"/"+str(arg2)+str(i-1)+".txt"))
						os.remove(os.path.join(str(arg1)+"/"+str(arg2)+str(i-1)+".txt"));
					print "Success!"
					
			k1=k1+1		
			if(k1>24):
					break
	file.close()
	file3.close()
	f.close()
	cnx2.close()
	db2.close()