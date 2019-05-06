list = []
for a in range(2,6):
   for b in range(2,6):
      power = a ** b
      list.append(power)
set = list(power)
print(len(set))
