from Queue import Queue
from threading import Thread
import os
import MySQLdb
import sys
import links
import cleanHtml

def mainPy():
	print( 'Number of arguments: {} arguments.'.format(len(sys.argv)))
	print ('Argument List: {}'.format(str(sys.argv)))
	print ('Argument List: {}'.format(sys.argv[1]))

	visited = open("visited.txt", "w")
	used=open('used.txt', 'w')
	with open("seed"+str(sys.argv[2])+".txt") as mainseed:
		with open("seed.txt","w") as seed:
			for line in mainseed:
				seed.write(line)

	mainseed.close()
	seed.close()
	used.close()			
	i=0
	j=0
	print "hello"
	for z in range(0,2) :
		print "***********level "+str(z)+"*********************"
		visited2=open("visitedNew.txt","w")
		with open("seed.txt") as seed:
				for link in seed:
					#visited.write(link)
					link1 = open("link.txt", "w")
					link1.write(link)
					link1.close()
					links.main(str(sys.argv[1]),j)
					cleanHtml.main(str(sys.argv[1]),j)
					j=j+1
					#execfile("links.py " )
					#print "hello 4"
					#execfile("cleanHtml.py " )
					with open("selected.txt") as selected:
						for s in selected:
							i=i+1
							print str(i)
							visited.write(s)
							visited2.write(s)
							if i>7:
								print "breaker"
								break
								print "breaker"

						selected.close()
					if(i>7):
						break

				seed.close()
		#seed=open("seed.txt","w")
		with open('visitedNew.txt') as result:
			print(result)
			uniqlines = set(result.readlines())
			with open('seed.txt', 'w') as rmdup:
				rmdup.writelines(set(uniqlines))
				
		result.close()
		visited2.close()
		rmdup.close()
	visited.close()	
 
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

def do_stuff(q):
  while True:
    print q.get()
    q.task_done()
 
q = Queue(maxsize=0)
num_threads = 10
	
for i in range(num_threads):
  worker = Thread(target=mainPy, args=())
  worker.setDaemon(True)
  worker.start()
 
for x in range(100):
  q.put(x)
 
q.join()