# static methods in python
# static method class ke andar hotaa h fir bhi usme self argument pass karne ki jrurat nhi hoti
# interview question - kya class ke andar method ko self dena compulsory hota h ? - Ans no
class Math:
  def __init__(self, num):
    self.num = num

  def addtonum(self, n):
    self.num = self.num +n
    
  @staticmethod
  def add(a, b):
      return a + b

# result = Math.add(1, 2)
# print(result) # Output: 3
a = Math(5)
print(a.num)
a.addtonum(6)
print(a.num)

print(Math.add(7, 2)) 