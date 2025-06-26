# match case in python
# for example the question is do u want to vote ..so the ans would be yes or no and if it is yes then u will get four options more like which party do u want to vote
# python mai jo case match hoga uska hin code run hoga isme break vagere ki bakchhodi nahi karni hai
# case is basically called a pattern
#  case_ is basically else jab koi case match na ho to ye match ho jayega
# we can even use if within a case
x = int(input("Enter the value of x: "))
# x is the variable to match
match x:
    # if x is 0
    case 0:
        print("x is zero")
    # case with if-condition
    case 4:
        print("case is 4")

    case _ if x!=90:
        print(x, "is not 90")
    case _ if x!=80:
        print(x, "is not 80")
    case _:
        print(x)