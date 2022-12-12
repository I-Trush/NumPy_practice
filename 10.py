import numpy as np

a = np.array([1,2,3,10,20,30])

print(a.sum())
print(a.mean())
print(a.max())
print(a.min())
print('====================================')

print(np.argmax(a))

a = np.array([1.1,2.2,-3.499,10,20,30])
print(np.around(a))

print(np.abs(a))

print(np.argmin(a))

a.resize(2,3)
print(a)

print(np.argmax(a, axis=0))     # max по столбцам
print(np.argmax(a, axis=1))     # max по строкам

print('==================================')
a = np.linspace(0, np.pi, 10)
print(a)

print(np.sin(a))

print('==================================')

print(np.random.rand(5,5))
print('==================================')
print(np.random.randint(10))
print(np.random.randint(3,10,size=(5,5)))


print(np.random.pareto(2.0, size=(5,5)))
print('==================================')
print(np.random.beta(0.1,0.3,size=(5,4)))

print('==================================')
np.random.seed(15)
print(np.random.randint(3,10,size=(5,5)))
np.random.seed(15)
print(np.random.randint(3,10,size=(5,5)))
# случ числа совпали


