sum1 = 0
sum2 = 0
sum3 = 0
for i in range(1,101):
   sum1 = sum1 + (i ** 2)
   sum2 = sum2 + i
   sum3 = sum2 ** 2
dif = sum3 - sum1
print(dif)
