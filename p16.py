def power(num):
   power = 2 ** 1000
   return power
def sum_of_digits(power):
   sum = 0
   rem = 0
   num = power
   k = power(num)
   while k > 0:
      rem = k % 10
      sum = sum + rem 
      k //= 10
   return sum
print(sum_of_digits(power))
