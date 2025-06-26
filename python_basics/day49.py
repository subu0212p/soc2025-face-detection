# file handling in python 
# read mode mai agar aisi file kholdi jo exist nahi karti to vo err0r dega 
# write mode mai agar aisi file kholi jo exist nahi karti to vo khud ek nayi file bana dega 
# write mode content overwrite karta hai and append existing content mai new content add karte h 
# file open karenge to end mai use close karna complusory hota hai
# but agar close nahi karna hai to 'with' statement ka use karo
# READING A FILE

# f = open('myfile.txt', 'r')
# # print(f)
# text = f.read()
# print(text)
# f.close()

# WRITING A FILE

f = open('myfile.txt', 'a')
f.write('Hello, world!')
f.close()

with open('myfile.txt', 'a') as f:
  f.write("Hey I am inside with")