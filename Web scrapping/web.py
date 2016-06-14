import urllib2
from bs4 import BeautifulSoup

for i in range(150002,150003):
	url="http://home.iitk.ac.in/~romit/studentsearch/profile.php?view="+str(i)
	page=urllib2.urlopen(url).read()
	soup=BeautifulSoup(page)
	div1=soup.find_all("div",{"id":"values"})
	for element in div1:
		div2=div1.text
		with open('data.csv','w') as csvfile:
			writer=csv.writer(csvfile)
			[writer.writerow(r) for r in div2]
