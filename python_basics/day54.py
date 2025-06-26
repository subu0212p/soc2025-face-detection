# 'is' vs '==' in python..so 'is' exact location ko comparekarta h and '==' value ko compare karta hai
# do alag variables ko agar ham koi immutable ciz asign karenge to vo memory location waaste nahi karega and dono ko same memory location assign karega
# to "is" and "==" dono true ayenge 
# list ke case a "is" b false ayega coz vo mutable hoti hai 
# tuple mai bhi true ayega coz vo immutable hota h 
a = None
b = None

print(a is b) # exact location of object in memory
print(a is None) # exact location of object in memory
print(a == b) # value