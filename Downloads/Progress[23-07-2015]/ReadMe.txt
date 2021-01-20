Run main.py to execte.

It will start fetching links from seed.txt and will 
store all the selected links based on score in visited.txt file
at this moment only 1 iteration occurs, I will need to design 
tree structure or keep count of links to add more links from
visited pages.

Scoring system is as basic as it can be at the moment.

Rest of the files are intermediate ones, I am not passing
links as arguments but storing them in files and executing
modules independently as they were written independently.

It takes some time to visit all the links and select few based
on score so I didn't move forward with multiple iterations.
(All I mean to say is have some patience once you run it,lol)

Also, you might need to install few libraries namely 
BeautifulSoup, 
SGMLParser,
re, 
urllib2.