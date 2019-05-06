n = 0
rem = 0
sum = 0
n = 2 ** 1000
while n> 0:
  rem = n % 10
  sum += rem
  n //= 10
print(sum)
