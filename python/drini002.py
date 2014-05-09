def multipar(L):
	X=0
	for i in xrange(1,len(L),2):
		X+=L[i]
	return 	X*L[-1]

A=[1,2,3,1,12,3,4,5,6,1]
print A
print multipar(A)
