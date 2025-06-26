# if else in python
a= int(input("Enter your age: ")) #coz python takes input as string so thats why we used int
print("Your age is:", a)
if(a>18):
    print("You can drive")#this space is called as indentation..like if u will use modern ides then after u press enter it gives space automatically,so if we tryt to remove the space then it will show the error 
    # indentation basically means that we are starting a block..in c++ we use curly brackets so the space here is just the replcement of that ..
    # so we can say that whatever is return after if or else with space is executed inside if and else respectively
else:
    print("You cannot drive") 
print("Yaaay!!")# this print is not the part of else as it is not written with space ..so it will be ex\ecuted irrespeective of the outcome of else
    # Conditional operators
    # >,<,>=,<=,==,!=
print(a>18)
print(a<18)
print(a==18)
print(a!=18)
# is is basically a conditional operator fn it searches for a condition and checks if that is true or not and gives output accordingly 
# now elif...it is similar to else if in c++..like if we start with if then elif and so on then it checks each condition stepwise like first it will check if and if it is true then loop exits and if false then checks another condition and so on
# now nested if its basically if ke andar if