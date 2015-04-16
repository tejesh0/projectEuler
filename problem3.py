import math

ans=1
for i in range(2,775146):
	if(600851475143%i ==0 and ans!=600851475143):
		print i
		ans=ans*i

