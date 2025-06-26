import numpy as np

# Generate two fake images
img1 = np.random.rand(100, 100, 1)
img2 = np.random.rand(100, 100, 1)

# Expand dims to match batch input shape
img1 = np.expand_dims(img1, axis=0)
img2 = np.expand_dims(img2, axis=0)

# Get embeddings
embedding1 = base_network.predict(img1)
embedding2 = base_network.predict(img2)

# Compute Euclidean distance
distance = np.linalg.norm(embedding1 - embedding2)
print("Distance between images:", distance)
