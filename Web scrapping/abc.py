import urllib2
from bs4 import BeautifulSoup
import sqlite3
conn=sqlite3.connect('students.db')
c=conn.cursor()
#c.execute('''CREATE TABLE students
	#(name text,roll_no text,imgsrc text)''')

for i in range(150100,150846):
	url="http://home.iitk.ac.in/~romit/studentsearch/profile.php?view="+str(i)
	page=urllib2.urlopen(url).read()
	soup=BeautifulSoup(page,'html.parser')
	div1=soup.find_all("div",{"id":"values"})
	img=soup.find_all("img")
	for element in img:
		imgsrc=element.get("src")

	for elements in div1:
		div2=elements.text
		
	x=div2.split('\n')
	c.execute("INSERT INTO students VALUES (?,?,?)",(str(x[1]),str(x[2]),str(imgsrc)))
	conn.commit()
