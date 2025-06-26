# seek basically skip karne ke liye use hota hai like manlo ki mujhe 123456789tet ye diya hai and
# maine seek(10) kiya to 1 se t tk skip ho jayega and then read use kiya to vo bas et ko read karega 
# also read ke andar bhi ham specify kar sakte h ki kha tk vo read kare like kitne bytes tk
# f.tell() fn seek kaha tk kiya h vo batata hai 
# truncate file ka size reduce karne ke liye use hoti hai 
with open('sample.txt', 'w') as f:
  f.write('Hello World3!')
  f.truncate(3)

with open('sample.txt', 'r') as f:
  print(f.read())