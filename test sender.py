#jai shri rama

import random
import math
p1=2**127-1
a1=2
d1=int(input('Third term of public key of receiver'))

def valass(m1):
	if(m1=='a'):
		return 11
	elif(m1=='b'):
		return 12
	elif(m1=='c'):
		return 13
	elif(m1=='d'):
		return 14
	elif(m1=='e'):
		return 15
	elif(m1=='f'):
		return 16
	elif(m1=='g'):
		return 17
	elif(m1=='h'):
		return 18
	elif(m1=='i'):
		return 19
	elif(m1=='j'):
		return 20
	elif(m1=='k'):
		return 21
	elif(m1=='l'):
		return 22
	elif(m1=='m'):
		return 23
	elif(m1=='n'):
		return 24
	elif(m1=='o'):
		return 25
	elif(m1=='p'):
		return 26
	elif(m1=='q'):
		return 27
	elif(m1=='r'):
		return 28
	elif(m1=='s'):
		return 29
	elif(m1=='t'):
		return 30
	elif(m1=='u'):
		return 31
	elif(m1=='v'):
		return 32
	elif(m1=='w'):
		return 33
	elif(m1=='x'):
		return 34
	elif(m1=='y'):
		return 35
	elif(m1=='z'):
		return 36
	elif(m1==' '):
		return 37
	elif(m1==','):
		return 38
	elif(m1=='.'):
		return 39
	elif(m1=='A'):
		return 40
	elif(m1=='B'):
		return 41
	elif(m1=='C'):
		return 42
	elif(m1=='D'):
		return 43
	elif(m1=='E'):
		return 44
	elif(m1=='F'):
		return 45
	elif(m1=='G'):
		return 46
	elif(m1=='H'):
		return 47
	elif(m1=='I'):
		return 48
	elif(m1=='J'):
		return 49
	elif(m1=='K'):
		return 50
	elif(m1=='L'):
		return 51
	elif(m1=='M'):
		return 52
	elif(m1=='N'):
		return 53
	elif(m1=='O'):
		return 54
	elif(m1=='P'):
		return 55
	elif(m1=='Q'):
		return 56
	elif(m1=='R'):
		return 57
	elif(m1=='S'):
		return 58
	elif(m1=='T'):
		return 59
	elif(m1=='U'):
		return 60
	elif(m1=='V'):
		return 61
	elif(m1=='W'):
		return 62
	elif(m1=='X'):
		return 63
	elif(m1=='Y'):
		return 64
	elif(m1=='Z'):
		return 65


m1=input('Your message ')

def un(i):
	return (67**4)*valass(m1[5*i+4])+(67**3)*valass(m1[5*i+3])+(67**2)*valass(m1[5*i+2])+67*valass(m1[5*i+1])+valass(m1[5*i])

n1=len(m1)
if(n1/5 != int(n1/5)):
	for i in range(5*(int(n1/5)+1)-n1):
		m1=m1+' '

def encrypt(m2):
	k1=random.randint(2,p1-2)
	y1=pow(a1,k1,p1)
	z1=(pow(d1,k1,p1)*(m2%p1))%p1
	return y1,z1

if(n1/5 == int(n1/5)):
	for j in range(int(n1/5)):
		print('Your cipher text',j,'is')
		print(encrypt(un(j)))
else:
	for j in range(int(n1/5)+1):
		print('Your cipher text',j,'is')
		print(encrypt(un(j)))

