import html2text
import urllib2
import sys
#import ntlk
opener = urllib2.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
html = opener.open("http://en.wikipedia.org/wiki/UML_state_machine#Entry_and_exit_actions").read()
#data= ntlk.clean(html)
#print data
j=10
betterHTML = html.decode(errors='ignore')
data= html2text.html2text(betterHTML)
data=data.encode(sys.stdout.encoding, errors='replace')
file = open("newdoc.doc","w")
file.write(data)
print data
#data = unicode(data, "utf-8", errors="ignore")
#print(data.decode('utf-8').encode('cp850','replace').decode('cp850'))
print j
#print data
print j