# dictonaries in python 
# it is basically combination of key value pairs 
# pahle dictionaries unordered hoti thi but python 3.7 onwaards vo ordered ho chuki hai 
# ek basic example we can take is employee id wala ..like ek id ke aage name likhdo so agar ham id ko access karenge to vo particular employee ka name pata chal jayega 
# ab dict ke kisi item ko access karne ke do tarike hai ek bracket ka usw karke and dusra get info se aagr tumhe error nahi chahiye to get info se karo ad vice versa 
info = {'name':'Karan', 'age':19, 'eligible':True}
# print(info) 
# print(info.keys())
# print(info.values())

# for key in info.keys():
#   print(f"The value corresponding to the key {key} is {info[key]}")

print(info.items())
for key, value in info.items():
  print(f"The value corresponding to the key {key} is {value}") 
  