def div(num):
	for n in range(1,40000):
		for i in range(1,11):
			if n % i == 0:
				count += 1
			return count
def smallest_number(num):
	if div(num):
		if count == 10: 
 			return num
