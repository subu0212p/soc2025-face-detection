# sometimes we would need to run the code multiple times..suppose i want to print 1-15 15 tim4es in a code and code for that is 10 lines each then 
# i wont want to add that code 15 times ..it would increase the program size and would also consume too much time 
# what if i seperate that code from my main program and make it another entity so that whenever it is required we would callthat function so we can just make a another new function 
# if we dont add body to a function then it will show error so use pass for the function which u wish to define later
# built in fn vo hote hai jinko def se define nahi karna padta..user defined basically def wale hote hai
def calculateGmean(a, b):
  mean = (a*b)/(a+b)
  print(mean)

def isGreater(a, b):
  if(a>b):
    print("First number is greater")
  else:
    print("Second number is greater or equal")

def isLesser(a, b):
  pass
  

a = 9
b = 8
isGreater(a, b)
calculateGmean(a, b)
# gmean1 = (a*b)/(a+b)
# print(gmean1)
c = 8
d = 74
isGreater(c, d)
calculateGmean(c, d)
# gmean2 = (c*d)/(c+d)
# print(gmean2)