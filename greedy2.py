s = [1,3,0,5,3,5,6,8,8,2,12]
f = [4,5,6,7,8,9,10,11,12,13,14]

def compatible(j,i):
	if j ==i:
		return True
	return (s[j] >= f[i] or f[j] <= s[i])
	
ll = [0]

def maxsub(i):
	if i == len(s)-1:
		return
	global ll
	y = i
	
	for x in xrange(i+1, ll):
		if compatible(x, i) and compatible(x,10):
			ll.extend([x])
			y = x
			break
	maxsub(y)
maxsub(0)
print 'A' + reduce(lamda x,y:str(x) + ',A' + str(y), ll)
