#jai shri rama

import random
import math
p1=2**127-1
a1=2
x1=random.randint(2,p1-2)
d1=pow(a1,x1,p1)
print('Public key is',p1,a1,d1)
#private key is x1


def decrypt(y1,z1):
	r1=pow(y1,p1-1-x1,p1)
	m=((r1%p1)*(z1%p1))%p1
	return m


def revvalass(m3):
	if(m3==39):
		return('.')
	elif(m3==38):
		return(',')
	elif(m3==37):
		return(' ')
	elif(m3==36):
		return('z')
	elif(m3==35):
		return('y')
	elif(m3==34):
		return('x')
	elif(m3==33):
		return('w')
	elif(m3==32):
		return('v')
	elif(m3==31):
		return('u')
	elif(m3==30):
		return('t')
	elif(m3==29):
		return('s')
	elif(m3==28):
		return('r')
	elif(m3==27):
		return('q')
	elif(m3==26):
		return('p')
	elif(m3==25):
		return('o')
	elif(m3==24):
		return('n')
	elif(m3==23):
		return('m')
	elif(m3==22):
		return('l')
	elif(m3==21):
		return('k')
	elif(m3==20):
		return('j')
	elif(m3==19):
		return('i')
	elif(m3==18):
		return('h')
	elif(m3==17):
		return('g')
	elif(m3==16):
		return('f')
	elif(m3==15):
		return('e')
	elif(m3==14):
		return('d')
	elif(m3==13):
		return('c')
	elif(m3==12):
		return('b')
	elif(m3==11):
		return('a')
	elif(m3==40):
		return('A')
	elif(m3==41):
		return('B')
	elif(m3==42):
		return('C')
	elif(m3==43):
		return('D')
	elif(m3==44):
		return('E')
	elif(m3==45):
		return('F')
	elif(m3==46):
		return('G')
	elif(m3==47):
		return('H')
	elif(m3==48):
		return('I')
	elif(m3==49):
		return('J')
	elif(m3==50):
		return('K')
	elif(m3==51):
		return('L')
	elif(m3==52):
		return('M')
	elif(m3==53):
		return('N')
	elif(m3==54):
		return('O')
	elif(m3==55):
		return('P')
	elif(m3==56):
		return('Q')
	elif(m3==57):
		return('R')
	elif(m3==58):
		return('S')
	elif(m3==59):
		return('T')
	elif(m3==60):
		return('U')
	elif(m3==61):
		return('V')
	elif(m3==62):
		return('W')
	elif(m3==63):
		return('x')
	elif(m3==64):
		return('Y')
	elif(m3==65):
		return('Z')


def revun(m):
	x0=revvalass(m%67)
	m=int(m/67)
	x1=revvalass(m%67)
	m=int(m/67)
	x2=revvalass(m%67)
	m=int(m/67)
	x3=revvalass(m%67)
	m=int(m/67)
	x4=revvalass(m%67)
	return x0+x1+x2+x3+x4

z=int(input('No. of cipher texts'))
message=' '

while(z):
	y1=int(input('First term of cipher text '))
	z1=int(input('Second term of cipher text '))
	z=z-1
	message=message+revun(decrypt(y1,z1))

print('Your message is')
print(message)
