def is_prime(n):
  count= 0
  for i in range(2,int(n ** 0.5)+1):
     if n % i == 0:
        count += 1
  if count == 0:
      return n
  else:
      return 0
def sum_of_primes(n):
   sum = 0
   for i in range(2,n):
      p = is_prime(i)
      sum = sum + p
   return sum
print(sum_of_primes(10))
