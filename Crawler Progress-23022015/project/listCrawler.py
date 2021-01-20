from bs4 import BeautifulSoup
import urllib2

url = "http://www.pythonforbeginners.com/python-on-the-web/beautifulsoup-4-python/" #write your url here
opener = urllib2.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
usock = opener.open(url)
soup = BeautifulSoup(usock)
redditAll = soup.find_all("a")
for links in soup.find_all('a'):
    print (links.get('href'))