
#for j>i and j<20
#if j%i==0
#continue
#else
#j--
print "start"
mul=1
for i in range(2,1,-1):
	j=5
	mul = mul*i
	print "processing"
	while j>i and j<=5:
		if j%i==0:
			print "heyy"
			continue
			print "not displayed"
		else:
			j-=1
			mul = mul/i
print mul	
print "re"











# # import pdb
# # import logging
# mul = 1
# # for i in xrange(20):
# # 	if i 
# # 	mul = mul*(i+1)
# # 	print mul,i
# i=5
# for i in range(5,1,-1):
# 	j=5
# 	k=i
# 	# logging.info(k)
# 	while j<=5 and j>=k :
# 		# pdb.set_trace()
# 		if(k%j!=0):
# 			j-=1
# 		else:
# 			# j-=1
# 			mul=mul*i
# 			continue
			
	
# print mul


# print mul
# for i in range(1,mul):
# 	j=1;
# 	while(i%j==0):
# 		j+=1;
# 		if(j==20):
# 			print i
# 			pdb.set_trace()
# 			mul = i+1;

	
	
	
print(10*"*")