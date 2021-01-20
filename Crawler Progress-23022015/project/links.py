from sgmllib import SGMLParser

class URLLister(SGMLParser):
  def reset(self):
    SGMLParser.reset(self)
    self.urls = []

  def start_a(self, attrs):
    href = [v for k, v in attrs if k=='href']
    if href:
      self.urls.extend(href)

import urllib

#myUrl="https://www.cs.rochester.edu/~nelson/courses/csc_173/fa/fa.html"
myUrl = open("link.txt", "r").readline()
try:
    print(myUrl)
    usock = urllib.urlopen(myUrl)
    parser = URLLister()
    parser.feed(usock.read())
    parser.close()
    usock.close()
    f = open("myseed.txt","w")
    for url in parser.urls:
        if url.startswith("http"):
            print url
            f.write(url+ "\n")
        else:
            if url.startswith("/"):
                tempUrl = myUrl[:myUrl.index('org')+3]+url
                print tempUrl
                f.write(tempUrl+ "\n")
            else:
                pass

    with open('myseed.txt') as result:
            uniqlines = set(result.readlines())
            with open('myunique.txt', 'w') as rmdup:
                rmdup.writelines(set(uniqlines))

    f.close()
    result.close()
    rmdup.close()
except :
    print "error"