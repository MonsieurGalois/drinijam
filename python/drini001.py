def lonelyones(n):
	N=set(n)
	for j in N:
		if n.count(j)<2:
			n.remove(j)
	return n
'''
Ejemplo:
A=[1,1,1,2,3,4,4,5,6,6,7,8,9,9,10,10,11,1,1,11,2,3,4]

print lonelyones(A)
'''
