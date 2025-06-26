# strings are immutable 
a ="subodh"
b ="SUBODH"
print(a.upper())
print(b.lower())
# rstrip removes any trailing characters not leading ones
c="!!!suboddh!!!!!!"
print(c.rstrip("!"))
# replace function replaces the particular word of the string with another word 
d= "subodh and darpan are friends"
print(d.replace("subodh", "vedant"))
# split function converts the string into list itmes by splitting them at whitespaces not necessary..we can specify
print(d.split(" "))
# capitalize function is used to capitalise the first letter of the sentence 
# one more thing the capitalize can do is that except the first letter of the sentence it will lowercase rest all the letters
print(d.capitalize())
e="lEts tEsT the Capitalize Fn"
print(e.capitalize())
# center function shifts the string to the right by the amount given by us..like if i do center(50)..then first subtract the characters used in the sentence and then the remaining amount will be the shift
print(d.center(50))
print(len(d.center(50)))
print(len(d))
# count function counts the number of times a particular word is repeated in the sentence
f= "baba baba black ship where do you go"
print(f.count("baba"))
# endswith function is used to find whether a string ends by a particular word..we can even specifty the lenght of the string for the inspection
print(f.endswith("go"))
print(f.endswith("do"))
print(f.endswith("do", 16, 32))
# find function is used to find the first occurrence of the particular word and returns its index and if that word is not present then it returns -1
# index also does the same but it doesnt return -1 instead it shows error.so we will index only when we are sure
print(f.find("baba"))
print(f.find("babas"))
print(f.index("baba"))
# isalnum function is used to verify that only A-Z a-z or 0-9 are used in the string 
# isalpha function is used to verify that only A-Z a-z  are used in the string 
g= "I am the father of @"
h= "RCB has 0 trophies\n"
print(g.isalnum())
print(g.isalpha())
# islower function checks if all letters of the string are lowercase or not and then returns true or false
print(h.islower())
# isprintable function is used to check whether all  the characters of the string are printable or not
print(g.isprintable())
print(h.isprintable())
# isspace returns true if and only if there are whitespaces in the string 
i="      "
print(h.isspace())
print(i.isspace())
# istitle returns true if and only if all words in the string start with a uppercase letter
print(h.istitle())
# isupper function checks if all letters of the string are uppercase or not and then returns true or false
# startswith function is used to find whether a string starts by a particular word..we can even specifty the lenght of the string for the inspection
# swapcase converts lower to upper and vice versa in a string
print(h.swapcase())
# title conerts the string in the title that is all words start with a uppercase
print(h.title())
# Here are few more string methods which may be useful to someone:

# 1. casefold(): similar to lower() but more aggressive and strong.
# 2. encode(): return a encoded version of a string.
# 3. format(): format specific values inside the string.


