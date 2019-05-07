class myclass:
  def __init__(self,*args):
      self.l = []
      for i in args:
          self.l.append(i)
  def __repr__(self):
      return str(self.l)
  def squares(self):
      return [i ** 2 for i in self.l]

k = myclass(1,2,3,4,5)
p = myclass.squares(k)
print(k,p)
