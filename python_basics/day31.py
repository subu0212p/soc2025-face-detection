# set doesnt take repeated values and is represented by curly brackets ..set is an unordered collection of items 
# sets are unchangeable
# set ko agar empty chhod diya to vo ek dict batayega coz dono ka syntax mai curly bracket hote hai..empty set banane ka correct 
# way hai subodh= set() not subodh ={}..
s = {2, 4, 2, 6}
print(s)

info = {"Carla", 19, False, 5.9, 19}
print(info)

harry = set()
print(type(harry))

for value in info:
  print(value)