# access modifiers in python
# python mai actually private public protected jaisi chiz nahi hoti h
# but inki baat jarur karte h
# jab bhi ham class banate h to uske variables by default public hote h but ham use private bana sakate h
# private class ke bahr se access nahi kiye ja sakte
# protected class ke andar se kiye jaa sakte h aur subclass se kiye ja sakte h yani child class se
# manlo maine class ke andar ek constructor banaya h amd uske andar likha h...self.name = "harry"
# ab mai use agar bahar a.name se acces karunga to vo ho jayega..but usi konagar 
# mai self.__name = "harry" karta to double uderscore ke vajah se vo rpivate bana gaya and use bahae se access nahi kar sakte
# but isko compare karo ki manlo tumne gadi bina lock ke chhoddi and uspe poster laga dia ki ise koi ccchuna mat 
# to agar double underscore wale ko access karna h to a.__Employee__name se access karo jaha employee class name h
# ise hi name mangling bolte h
# protected ke liye single underscore use kiya jata h
class Student:
    def __init__(self):
        self._name = "Harry"

    def _funName(self):      # protected method
        return "CodeWithHarry"

class Subject(Student):       #inherited class
    pass

obj = Student()
obj1 = Subject()
print(dir(obj))

# calling by object of Student class
print(obj._name)      
print(obj._funName())     
# calling by object of Subject class
print(obj1._name)    
print(obj1._funName())