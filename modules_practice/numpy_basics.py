import numpy as np

# Create a 3x3 array of random integers
arr = np.random.randint(1, 100, size=(3, 3))
print("Array:\n", arr)

# Shape and dtype
print("Shape:", arr.shape)
print("Data Type:", arr.dtype)

# Basic operations
print("Mean:", arr.mean())
print("Sum:", arr.sum())
print("Transpose:\n", arr.T)

# Broadcasting example
a = np.array([1, 2, 3])
b = np.array([[10], [20], [30]])
print("Broadcasted Sum:\n", a + b)
