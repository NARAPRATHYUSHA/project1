class Person:
      def __init__(self, name, age):
          self.name = name
          self.age = age

      def myfunc(self):
          print("Hello my name is " + self.name)
          
p1 = Person("John", 36)
p1.myfunc()
print(p1)
print("{} age is {}".format(p1.name,p1.age))
