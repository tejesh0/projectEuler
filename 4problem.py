#check for palindrome
def isPalindrome(num):

	num_str = str(num)

	if(str(num) == num_str[::-1]):
		return True
	return False

print isPalindrome(99009)
max = 0
for i in list(range(999,99,-1)):
	for j in list(range(990,99,-11)):
		if(isPalindrome(i*j)):
			print i*j
			if(max < i*j):
				max = i*j
				print max


print max