# Exercise 2 ...good morning sir 
# import time
# h=int(time.strftime('%H'))
# if h<12:
#     print("Good Morning Sir")

# elif h<17:
#     print("Good Afternoon Sir")

# else:
#     print("Good Evening Sir")
import time
x= input("enter the time (24:00): ")
y= x[0:2]
z= int(y)

if (z<12):
    print("Good Morning !")
elif (z==12):
    print("Good Noon !")
elif (z<17):
    print("Good Afternoon !")
else:
    print("Good Evening !") 