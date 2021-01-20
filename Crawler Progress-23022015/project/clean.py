__author__ = 'Omkar'
import urllib
from bs4 import BeautifulSoup
import re
html = urllib.urlopen("http://host.madison.com/daily-cardinal/science/machine-learning-program-used--d-tissue-chip-to-distinguish/article_065b78fc-648e-11e4-927d-0391ab7d1420.html").read()
soup = BeautifulSoup(html)
texts = soup.findAll(text=True)

def visible_text(element):
    if element.parent.name in ['style', 'script', '[document]', 'head', 'title']:
        return ''
    result = re.sub('<!--.*-->|\r|\n', '', str(element), flags=re.DOTALL)
    result = re.sub('\s{2,}|&nbsp;', ' ', result)
    return result

visible_elements = [visible_text(elem) for elem in texts]
visible_text = ''.join(visible_elements)
print(visible_text)