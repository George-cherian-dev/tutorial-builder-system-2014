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
import traceback


def main(arg1,arg2):
	i=0
	print( 'Number of arguments: {} arguments.'.format(arg1))	
	rmdup=open('myunique.txt', 'w')
	used=open('used.txt', 'a')
#myUrl="http://en.wikipedia.org/wiki/Deterministic_finite_automaton"
	try:
		i=3
		myUrl = open("link.txt", "r").readline()
		i=4
		usock = urllib.urlopen(myUrl)
		i=6
		parser = URLLister()
		parser.feed(usock.read())
		i=7
		parser.close()
		usock.close()
		i=5
		f = open("myseed.txt","w")
		f.write(myUrl)
		#print(myUrl)
		i=1
		for url in parser.urls:
			try:
				if url.startswith("http"):
					#print url
					f.write(url+ "\n")
				else:
					if url.startswith("/"):
						tempUrl = myUrl[:myUrl.index('org')+3]+url
						#print tempUrl
						f.write(tempUrl+ "\n")
					else:
						pass
			except:
				traceback.print_exc()
		i=2
		f.close()
		with open('myseed.txt') as result:
				uniqlines = set(result.readlines())
				with open("used.txt") as used1:
					#print "A"
					unlines=set(used1.readlines())
					for line in uniqlines:
						#print "B"
						flag=0
						for line1 in unlines:
							if str(line)==str(line1):
								flag=1
								break
						#print flag
						
						#print "D"
						if flag==0:
							#print "C"
							rmdup.write(line)
							used.write(line)
				#rmdup.writelines(set(uniqlines))
				#print(uniqlines)
		
		#print(myUrl)
		#rmdup.write(myUrl)
		result.close()
		rmdup.close()
	except:
		print "error"+str(i)
		traceback.print_exc()