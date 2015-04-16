
denominations = [1,2,5,10,20,50,100,200]


def combinations(amount):
	# print num
	
	possibilities = 0
	sum =0 
	i = len(denominations)
	for i in range(0,len(denominations)):
		sum =0
		remaining = amount - sum
		while(remaining):
			#calculate remaning/denomination[i]
			#if result is < 1 reduce i
			#if result is > 1 
			if(remaining/denominations[i] > 1):
				sum = sum + denominations[i]
				if(sum==amount):
					possibilities+=1

			else:
				i-=1




	return possibilities

amount = 10

answer = combinations(amount)

# assert(0)
print answer