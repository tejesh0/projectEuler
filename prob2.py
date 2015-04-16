new =0
one =1 
two =2 
sum =0
while(new<4000000):    
    new = one + two
    one = two
    two = new
    print new
    if(new%2==0):
    	sum = sum + new

print sum