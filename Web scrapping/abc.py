import urllib2
from bs4 import BeautifulSoup
import subprocess

f= open('a.txt','w')
for i in range(150002,150003):
	url="http://home.iitk.ac.in/~romit/studentsearch/profile.php?view="+str(i)
	page=str(subprocess.call(['curl',url]))
	soup=BeautifulSoup(page,'html.parser')
	div1=soup.find_all("div",{"id":"values"})
	img=soup.find_all("img")
	for element in img:
		imgsrc=element.get("src")

	for elements in div1:
		div2=elements.text
		
	x=div2.split('\n')
	f.write(x[1]+'\t'+x[2]+'\t'+imgsrc)
