# why decorators
# basically isko ham use karte ki koi ek fn normally kuch return kar raha h to uske alawa bhi koi chiz return kare
# like tumne koi avg ka fn banaya h and u want ki har baar avg dene se pahle vo user ko greet kare like good morning so
# aisi jagah ham decorators use karte h

def greet(fx):
  def mfx(*args, **kwargs):
    print("Good Morning")
    fx(*args, **kwargs)
    print("Thanks for using this function")
  return mfx

@greet
def hello():
  print("Hello world")

@greet
def add(a, b):
  print(a+b)
  
# greet(hello)()
hello()
# greet(add)(1, 2)
add(1, 2)