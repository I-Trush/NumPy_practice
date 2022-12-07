import numpy as np

a = np.array([1,2,3,4,5,6])

print(a)
print(a.dtype)

print(a[2])
print(a[(2)])
print(a[(2,)])

b = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])

print(b)
print(b.dtype)
print(b[(2,2)])
b[(2,1)] = 10
print(b)
print(b.dtype)

# выдаст только те эл-ты напротив которых стоит True
print(a[[True,True,False,False,True,False]])    # кро-во Бул. значение должно совпадать с длинной массива (если их меньше или больше, то будет ругаться) [1 2 5]

print(a[[2,2,2,3,3,3]]) # выдаст массив заполненный эл-тами массива а по номерам [3 3 3 4 4 4]



x = np.array([1,2,3,4,5,6,7,8,9])
d = x.reshape(3,3)      # преобразует одноменрый массив в двумерный
print(d)
