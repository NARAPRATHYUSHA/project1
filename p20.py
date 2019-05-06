def fact(n):
   fact = 1
   for i in range(2,n + 1):
       fact *= i
   return fact
def digit_sum(n):
   sum = 0
   k = fact(n)
   while k > 0:
      rem = k % 10
      sum += rem
      k //= 10
   return sum
print(digit_sum(100))


