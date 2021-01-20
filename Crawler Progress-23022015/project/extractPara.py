import urllib2
from bs4 import BeautifulSoup

opener = urllib2.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]

url = ('http://en.wikipedia.org/wiki/Deterministic_finite_automaton')

ourUrl = opener.open(url).read()

soup = BeautifulSoup(ourUrl)

title = soup.title.text

body = soup.findAll('p')
outfile = open("wikipedia.txt", "w")
for i in body:
    print(i.text + "\n\n")
    outfile.write(i.text + '\n\n')

outfile.close()