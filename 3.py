import numpy as np

# a = np.empty(10)
# print(a)
#
#
# a = np.empty(10, dtype='int16')
# print(a)
#
#
# a = np.empty((3,6,6), dtype='int16')
# print(a)
#
# a = np.eye(10, dtype='int16')
# print(a)
#
# a = np.eye(5,3)
# print(a)
#
# a = np.identity(5)
# print(a)
#
# a = np.zeros((3,5))
# print(a)
# ====================================================================

# a = np.mat([1,2,3,4])
# print(a)
#
# a = np.mat('1 2; 3 4')
# print(a)
# # [[1 2]
# #  [3 4]]
#
# a = np.diag([1,2,3,4,5])    # эл-ты диаганали
# print(a)
#
# a = np.diag([
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ])
# print(a)
# # [1 5 9]
#
# a = np.tri(5)
# print(a)
# # [[1. 0. 0. 0. 0.]
# #  [1. 1. 0. 0. 0.]
# #  [1. 1. 1. 0. 0.]
# #  [1. 1. 1. 1. 0.]
# #  [1. 1. 1. 1. 1.]]

a = np.arange(5)
print(a)

a = np.arange(3,8)
print(a)

a = np.arange(3,8, 0.5)
print(a)

a = np.logspace(1,4,6)
print(a)

a = np.geomspace(1,4,6)
print(a)

