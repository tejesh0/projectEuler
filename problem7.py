n=2
prime_list=[]
while(len(prime_list)!=10002):
	if(any(n%value==0 for value in prime_list)):

		n+=1
	else:
		prime_list.append(n)
		n+=1

print prime_list[3]
print prime_list[10000]
	
