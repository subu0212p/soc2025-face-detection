# local vs global variable in python 
# manlo mere pass koi variable h jise maine fn ke andar banaya h to ham use fn ke bahar use nahi kar sakte to use local variable kehte h 
# jo fn ke bahar variablr hota h use global bolte h and wwe can use it inside fn as long as there is no other variable with the samne name inside the fn 
# and if fn ke andar aur bahar dono jagah same variable name h to fn ke andar vo local wale ko hi usse karega 
# local variable destroys once fn returns but not global 
# ek tarika aisa hota h jisse ham global variable ki value fn ke andar bhi change kar sakte hai..global naam ka fn use kar.for eg global x
# manlo ki maine koi variable fn ke andar define kiya h and usee bina fn call kiye use karunga to vo error batayega 
x = 10  # global variable


def my_function():
  global x
  x = 5  # this will change the value of the global variable x
  y = 5  # local variable


my_function()
print(x)  # prints 5
# print(y) # this will cause an error because y is a local variable and is not accessible outside of the function