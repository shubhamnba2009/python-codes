a=[x for x in raw_input().split()]
for i in xrange(len(a)-1):
	for j in xrange(i+1,len(a)):
		if(a[i]+a[j]<a[j]+a[i]):
			a[i],a[j]=a[j],a[i]
print ''.join(a

