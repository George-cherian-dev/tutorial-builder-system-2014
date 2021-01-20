from Queue import Queue
from threading import Thread


def main():
	visited = open("visited.txt", "w")


	with open("seed.txt") as seed:
		for link in seed:
			visited.write(link)
			links = open("link.txt", "w")
			links.write(link)
			links.close()
			execfile("links.py")
			execfile("cleanHtml.py")
			with open("selected.txt") as selected:
				for s in selected:
					visited.write(s)

				selected.close()


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


def Links(link,depth):
	i=0
	print( 'Number of arguments: {} arguments.')
	rmdup=open('myunique.txt', 'w')
	used=open('used.txt', 'a')
#myUrl="http://en.wikipedia.org/wiki/Deterministic_finite_automaton"
	try:
		i=3
		myUrl = link
		i=4
		usock = urllib.urlopen(myUrl)
		i=6
		parser = URLLister()
		parser.feed(usock.read())
		i=7
		parser.close()
		usock.close()
		i=5
		mySeed = Queue(maxsize=0)
		mySeed.put(myUrl)
		#print(myUrl)
		i=1
		for url in parser.urls:
			try:
				if url.startswith("http"):
					#print url
					if url not in mySeed:
						mySeed.put(url)
					else:
						pass
				else:
					if url.startswith("/"):
						tempUrl = myUrl[:myUrl.index('org')+3]+url
						#print tempUrl
						if url not in mySeed:
							mySeed.put(url)
						else:
							pass
					else:
						pass
			except:
				traceback.print_exc()
		i=2
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

def do_stuff(q):
  while True:
	print q.get()
	q.task_done()

visited = open("visited.txt", "w")

v = Queue(maxsize=0)
s = Queue(maxsize=0)
def VisitedQ():
	with open("seed.txt") as seed:
		for link in seed:
			visited.write(link)
			v.put(link)
			s.put(link)

def ExtractLinks():
	pass

num_threads = 10

for i in range(num_threads):
  worker = Thread(target=main, args=())
  worker.setDaemon(True)
  worker.start()

for x in range(100):
  v.put(x)

v.join()