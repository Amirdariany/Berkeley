#Include	a	section	with	your	name	
person = input('Enter your name: ')
print('Hello', person)
#Create	matrix	A	with	size	(3,5)	containing	random	numbers
import numpy as np
a=np.random.rand(3,5)
np.matrix(a)
print(a)
#Find	the	size	and	length	of	matrix	A
print(np.size(a))
print(a.shape)
#Resize (crop/slice) matrix A to size (3,4)
f=np.resize(a,(3,4))
print(f)
#Find	the	transpose	of	matrix	A	and	assign	it	to	B	
b=np.transpose(a)
print(b)
#Find	the	minimum	value	in	column	1	of	matrix	B	
print(b[:,0])
print(b[:,0].min())
#Find	the	minimum	and	maximum	values	for	the	en4re	matrix	A	
print(np.min(a),np.max(a))
#Create	vector	X	(an	array)	with	4	random	numbers
h=np.random.rand(4)
print(h)
#Create	a	func4on	and	pass	vector	X	and	matrix	A	in	it
def f_mu(f,h):
    f=np.array(f)
    h=np.array(h)
    D=h*f
    return D
#In	the	new	func4on	mul4ply	vector	X	with	matrix	A	and	assign	the	result	to	D	
D=f*h
print(D)
#. Create	a	complex	number	Z	with	absolute	and	real	parts	!=	0
z=complex(3,4)
print(z)
#Show	its	real	and	imaginary	parts	as	well	as	it’s	absolute	value	
print(z.real)
print(z.imag)
print(np.absolute(z))
#Mul4ply	result	D	with	the	absolute	value	of	Z	and	record	it	to	C	
C=D*(np.absolute(z))
print(C)
#Convert	matrix	B	from	a	matrix	to	a	string	and	overwrite	B
b=C.flatten()
print(b)
#Display	a	text	on	the	screen:	‘Your Name	is	done	with	HW2‘	
print('amir dariany is done with HW2')


    


