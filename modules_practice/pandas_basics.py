import pandas as pd

# From a list
s = pd.Series([10, 20, 30, 40]) # Default Index- integers from zero

# From a list with custom index labels
s = pd.Series([10, 20, 30], index=['a', 'b', 'c'])

# From a dictionary
s = pd.Series({'x': 100, 'y': 200, 'z': 300})
# From a dictionary of lists
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Paris', 'London']
}
df = pd.DataFrame(data)

# From a list of dictionaries
data2 = [
    {'Name': 'Alice', 'Age': 25},
    {'Name': 'Bob', 'Age': 30}
]
df2 = pd.DataFrame(data2)
