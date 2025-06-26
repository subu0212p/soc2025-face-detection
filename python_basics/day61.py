# inheritance basically hota h existing class ko extend karna 
# manlo ki ek employee class ..to mai ek naya class bna saktaa hu programmer naam ka
# like class programmer(employee): jisme employee ke sare chize hongi and iske andar ham extra chixe bhi call kar sakte h
class Employee:
  def __init__(self, name, id):
    self.name = name
    self.id = id 

  def showDetails(self):
    print(f"The name of Employee: {self.id} is {self.name}")

class Programmer(Employee):
  def showLanguage(self):
    print("The default langauge is Python")


e1 = Employee("Rohan Das", 400)
e1.showDetails()
e2 = Programmer("Harry", 4100) #agar idhar programmer ki jagah employee likhta
e2.showDetails()
e2.showLanguage()#code error deta coz showlanguAGE programmer ke andar h naki employee m