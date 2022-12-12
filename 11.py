import numpy as np

a = np.arange(1,10).reshape(3,3)
print(a)

b = np.arange(10,19).reshape(3,3)
print(b)
print('================================')

print(a*b)
print(np.dot(a,b))
print(np.matmul(a,b))

print('================================')

a = np.matrix(a)
b = np.matrix(b)
print(a*b)

print('================================')

a = np.arange(1,10)
b = np.ones(9)
print(a)
print(b)
print(np.dot(a,b))  # Внутреннее умножение
print('================================')
# a = np.matrix(a)
# b = np.matrix(b.reshape(-1,1))
# print(a*b)

print(np.inner(a,b))    # Внутреннее умножение

print('================================')
# Внешнее умножение
print(np.outer(a,b))

# a = np.matrix(a.reshape(-1,1))
# b = np.matrix(b)
# print(a*b)


print('================================')
a = np.array([
    [1,2,3],
    [1,4,9],
    [1,8,27]
])

print(a)
print(np.linalg.matrix_rank(a))
