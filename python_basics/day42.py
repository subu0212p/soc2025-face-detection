# enumerate function in python \
# pahle index likhna h then marks likhna h:)
marks = [12, 56, 32, 98, 12,  45, 1, 4]

# index = 0
# for mark in marks:
#   print(mark)
#   if(index == 3):
#     print("Harry, awesome!")
#   index +=1

for index, mark in enumerate(marks, start=1):#yaha start nahi likha to index 0 se hi st hoga..
  print(mark)
  if(index == 3):
    print("Harry, awesome!")