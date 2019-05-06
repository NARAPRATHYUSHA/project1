n = 600851475143
large = 2
for i in range(2,n + 1):
   if n % i == 0:
      if i % 1 == 0 and i % i ==  0:
        if large <  i:
           large = i
print(large)
