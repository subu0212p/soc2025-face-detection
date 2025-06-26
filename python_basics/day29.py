# docstrings in python
# docstrings aree not ignored like comments..and unko tripple appostrope mai enclose kiya jaata 
# docstring ko right above fn bodyh or right below the function name dalana hota hai otherwise irt doesnt work 
# import this karne se zen ofpython print hota hai 
# import this
def square(n):
  '''Takes in a number n, returns the square of n'''
  print(n**2)
square(5)
print(square.__doc__)