# constructor ek object banane mai madat karta h
# agar ham class ke andar koi method define karenge to self dena hi dena h
# kuch exceptions honge vo dekh lena
# normally class ke andar hame koi variable banane hote h like name occ jaise to unko kuch assign karna padta h...but aisa kyu kare
# manlo ki maine kardiya a.name() = "Subodh"..to jo class ke andart pahlr se name ki value to waste hogayi to 
# iske liye constructor use kiya jata hai
# manlo mera class name h person and mai koi 0bject 'a" bana raha hu a= Person()..to isse constructor sidhe call hojata h
# constructor banane ka tarika hota hai def __init__(self):
# jitne bar bhi ek object banaya jayega like some x = person().har baaar constructor invoke hoga
# constructor mai ek argument automatically pass hota h and vo h self 
#class Person:
class Person():
  def __init__(self, name, occ):
    print("Hey I am a person")
    self.name = name
    self.occ = occ

  def info(self):
    print(f"{self.name} is a {self.occ}")


a = Person("Harry", "Developer")
b = Person("Divya", "HR") 
a.info()
b.info()
# print(a.name)
# a.name = "Divya"
# a.occ = "HR"
# a.info()