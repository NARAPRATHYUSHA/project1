count = 0
small = 0
for n in range(1,40000):
	for i in range(1,11):
		if n % i == 0:
	        	count =count + 1
if count == 10: 
	print (n)

