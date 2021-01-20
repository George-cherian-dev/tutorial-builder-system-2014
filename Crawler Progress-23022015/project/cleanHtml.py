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

from collections import Counter
def scoreHTML(myStr):
    with open("terms.txt") as t:
        myScore=0
        for terms in t:
            a=terms.split()
            myTerm=a[0]
            myScr=a[1]
            myScore = myScore +myStr.count(str(myTerm))*float(myScr)
        wordCount = myStr.split().__len__()
        print(myScore)
        print(wordCount)
        finalScore=myScore/wordCount*100
        print(finalScore)
        #I'm not sure about scoring, so I'm just returning original score without dividing with wordCount
        return myScore
import sqlite3
def storeDB(url, data):
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    #c.execute("DROP TABLE Extracted")
    c.execute('''CREATE TABLE if not exists Extracted
    (link text PRIMARY KEY, data text)''')

    try:
        c.execute("INSERT INTO Extracted VALUES(? , ?)",(url.decode("UTF-8"), data.decode("UTF-8")))
    except:
        print("Not stored in DB")

    conn.commit()
import urllib2
import requests
from requests.exceptions import HTTPError

opener = urllib2.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
i=0
file = open("selected.txt", "w")
with open("myunique.txt") as f:
    links=[]
    for line in f:
        print(line)

        try:
            ourUrl = opener.open(line).read()
        except:
            print 'page not available'
        else:
            try:
                cleaned = stripHTMLTags(ourUrl)
                cleaned = cleaned.encode("UTF-8")
                score = scoreHTML(str(cleaned))

            except:
                print "Document is not HTML"
            else:
                if score>=10:
                    print "Link included"
                    print(ourUrl)
                    print(cleaned)
                    storeDB(ourUrl, cleaned)
                    file.write(line)
                else:
                    print "Link not included"

                print "Success!"

file.close()
f.close()