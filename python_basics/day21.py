# default arguement basically vo hote hai jinko ham function mai already koi value dedete hai to agar koi user koi bhi input na de to vo by default set values ko use karta hai otherwise user ki value ko leta hai
# keyword argument basically vo hota hai like..agar fn mai a,b bas rakha hai and ham pahle b and then a de to vo lega...bc samjh lena khud\
# return matlab wapas chale jaao uss value ko leke...ek return ke baad aur kitne bhi retur add kardo usse farak nahi padega 
# You are probably thinking why use return when you have print, or something like that.

# print just prints the result and forgets about it, like the c button on calculator. you saw it and that's that.

# but return keeps the result just in case if you want to use the result on somewhere else.

# also finishes the function.
# def average(a, b, c=1):
#   print("The average is ", (a + b + c) / 2)


def average(*numbers):
  # print(type(numbers))
  sum = 0
  for i in numbers:
    sum = sum + i
  # print("Average is: ", sum / len(numbers))
  # return 7
  return sum / len(numbers)


# average(4, 6)
# average(b=9)

c = average(5, 6, 7, 1)
print(c)


# def name(**name):
#   # print(type(name))
#   print("Hello,", name["fname"], name["mname"], name["lname"])


# name(mname="Buchanan", lname="Barnes", fname="James")