# try except ki tarah ek finally bhi hota h uska use dekhenge abhi
# finally ke andar dala hua code always run hota hai irrespective of code run hua ya nahi 
# finally ka main use function ke andar hota hai..like manlo ek baar fn se koi chiz return hogayi to vo uske baad
#ka code execute nahi hota to ham finally ka use karte hai taki return ke baad bhi code execute ho
def func1():
  try:
    l = [1, 5, 6, 7]
    i = int(input("Enter the index: "))
    print(l[i])
    return 1
  except:
    print("Some error occurred")
    return 0

  finally:
    print("I am always executed")
  # print("I am always executed")


x = func1()
print(x)