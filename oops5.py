class Person:
      def __init__(self, name, age):
        self.name = name
        self.age = age

      def myfunc(self):
         print("Hello my name is " + self.name)
p1 = Person("chinna",19)
p1.myfunc()
                      
