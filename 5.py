import numpy as np

# a = np.array([1,2,3,4,5,6,7,8,9,10])
#
# a.shape = -1,2
#
# print(a)
#
# a.shape = -1
# print(a)
#
# a.resize(2,5)
# print(a)
#
# a.resize(3,3)   # хм не ругается влаг не установлен refcheck=True
# print(a)
# # [[1 2 3]
# #  [4 5 6]
# #  [7 8 9]]
#
# # help(a.resize)
#
# a.resize(4,5)   # хм не ругается влаг не установлен refcheck=True
# print(a)
# # [[1 2 3 4 5]
# #  [6 7 8 9 0]
# #  [0 0 0 0 0]
# #  [0 0 0 0 0]]
#
# b = a.T
# print(b)
#
# x = np.arange(1,10)
# print(x)
# x.T
# print(x)
# x.shape = 1,-1
# print(x)
# x.T
# print(x)
# # array([[1],
# #        [2],
# #        [3],
# #        [4],
# #        [5],
# #        [6],
# #        [7],
# #        [8],
# #        [9]])


x = np.arange(32).reshape(8,2,2)
# print(x)
x.shape
# пусть захотели добавить новую ось
y = np.expand_dims(x, axis=0)
print(y)
print(y.shape)
#
# x[0] = 100
#
# print(y)

a = np.append(y,y,axis=0)
print(a.shape)
print(a)

b = np.delete(a, 0, axis=0)
print(b.shape)


