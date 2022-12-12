import numpy as np

a = np.array([1,2,3,10,20,30])
b = np.array([2])

print(a*b)
print(a+b)

print('====================================')
a = np.arange(1,10).reshape(3,3)
b = np.array([4,5,6])
print(a)
print(b)

print(a*b)
print(a+b)