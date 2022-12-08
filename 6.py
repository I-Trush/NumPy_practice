import numpy as np

a = np.array([
    [1,2],
    [3,4]
])
b = np.array([
    [5,6],
    [7,8]
])

x = np.hstack([a,b])
print(x)

x = np.vstack([a,b])
print(x)

