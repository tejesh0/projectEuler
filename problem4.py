def is_palindrome(num):
	
	arr =  map(int,str(num))
	n  = len(arr)
	i=0
	while(n):
		if(arr[n-1]== arr[i]):
			
			n-=1
			i+=1
			print(10*"*")
			continue	
		if(arr[n-1]!=arr[i]):	
			print("oops")
			return false
	return "is_palindrome"
t = is_palindrome(9009)
print t
assert(is_palindrome(9009)=="is_palindrome"), "error"
assert(is_palindrome(909)=="is_palindrome"), "error"
assert(is_palindrome(90009)=="is_palindrome"), "error"

