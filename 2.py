import numpy as np

# a = np.array([1,2,3,4], 'float64')  # задали вещественный тип 64
#
# print(a)
# print(a.dtype)
#
#
# # какие типы поддерживает numpy?
# print(np.sctypeDict)    # uint8 - беззнаковое целое 8 бит
# # for x in np.sctypeDict:
# #     print(x)
#
#
# a = np.array([1,2,3,4], 'uintc')
# print(a)
# print(a.dtype)
#
#
# # преобразование типов
# b = np.complex64(10)
# print(b)
# print(b.dtype)
#
#
# d = np.array([1, 2, 5000, 1000], dtype='int8')
# print(d)
# print(d.dtype)
#
# d = np.array([1, 2, 5000, 1000])
# print(d)
# print(d.dtype)
#
#
# d=np.complex64(d)
# print(d)
# print(d.dtype)

a=np.array([
    [[1,2],[3,4]],
    [[5,6],[7,8]],
    [[9,10],[11,12]]
])
print(a)
print(a.dtype)

print(a[2,1,1])
print('==================')
for x in range(3):
    print('x=', x, a[x, 0, 0])

print('==================')
for x in range(3):
    print('x=', x, a[x, 1, 0])

print('==================')
for x in range(3):
    print('x=', x, a[x, 1, 1])

print('==================')
print(a[0]) # срез
print(a[1]) # срез
print(a[2]) # срез