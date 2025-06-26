# for loop ke sath else statement ko use karna sikhenge aaj.same chiz while ke sath bhi hoti hai 
# else ke execute hone ka matlab hi ye h ki loop break nahi hua end hua hai to agar ham for mai break lagate hai to else bi execute nahi hoga
i = 0
while i<7:
  print(i)
  i = i + 1
  # if i == 4:
  #   break

else:
  print("Sorry no i")

for x in range(5):
    print ("iteration no {} in for loop".format(x+1))
else:
    print ("else block in loop")
print ("Out of loop")