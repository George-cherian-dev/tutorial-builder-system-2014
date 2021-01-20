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
                score = str(cleaned).count("DFA")
                score = score + str(cleaned).count("NFA")
                score = score + str(cleaned).count("state")
                print(score)
            except:
                print "Document is not HTML"
            else:
                if score>=10:
                    print "Link included"
                    file.write(line)
                else:
                    print "Link not included"

                print "Success!"

file.close()
f.close()