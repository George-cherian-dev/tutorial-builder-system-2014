import urllib2
from bs4 import BeautifulSoup
import re

opener = urllib2.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]

url = ('http://en.wikipedia.org/wiki/Deterministic_finite_automaton ')

ourUrl = opener.open(url).read()

soup = BeautifulSoup(ourUrl)



body = soup.findAll('p')
out = open("wikipedia.txt", "w")
for i in body:
    i=i.text.encode('UTF-8')
    i=re.sub("\[\d+\]", "", str(i) )
    i=re.sub("\[\.*?\]", "", str(i) )
    out.write(i+"\n\n")

out.close()