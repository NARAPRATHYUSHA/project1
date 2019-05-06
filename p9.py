def pythagorean(a,b,c):
   for a in range(1,11):
      for b in range(1,11):
          for c in range(1,11):
              if a + b + c ==12 and (a ** 2) + (b ** 2) +(c ** 2): 
               return a , b , c
def product(a,b,c):
   if a < b < c:
       product = a * b * c
       return product
print(product(a,b,c))
