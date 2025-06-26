# sometimes we want that loop ends after a particular iteration at that time we need break or continue 
# break statement kahega iss loop ko chhodke nikal jaao
# continue ka maatlab hai iteration chhodkar nikal jaao
# for i in range(12):
#   if(i == 10):
#     print("Skip the iteration")
#     continue
#   print("5 X", i, "=", 5 * i)
# below is the code for emulated do while loop..as do while doesnt exist implicitly in python
i = 0
while True:
  print(i)
  i = i + 1
  if(i%100 == 0):
    break
