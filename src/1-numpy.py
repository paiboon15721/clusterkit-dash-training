import numpy as np

print('--- Overview ---')

x = np.random.uniform(0, 1, size=1000000)
print(x)
print(x.mean())

print('--------------------\n')

print('--- Basic ---')

my_list = [0, 1, 2, 3, 4]
print(my_list)

arr = np.array(my_list)
print(arr)
print(type(arr))

print('--------------------\n')

print('--- Arange integers, takes in start, stop, and step size ---')

a = np.arange(0, 10)
print(a)

a = np.arange(0, 10, 2)
print(a)

print('--------------------\n')

print('--- Create an array of zeros ---')

a = np.zeros((5, 5))
print(a)

print('--------------------\n')

print('--- Create an array of ones ---')

a = np.ones((2, 4))
print(a)

print('--------------------\n')

print('--- Create an array of random integers ---')

a = np.random.randint(0, 10)
print(a)

print('--------------------\n')

print('--- Create 2d matrix of random integers ---')

a = np.random.randint(0, 10, (3, 3))
print(a)

print('--------------------\n')

print('--- Create linearly spaced array ---')

a = np.linspace(0, 10, 6)
print(a)

print('--------------------\n')

print('--- Operations On Arrays ---')

arr = np.random.randint(0, 100, 10)
print(arr)
print(arr.max())
print(arr.min())
print(arr.mean())
print(arr.argmin())
print(arr.argmax())
print(arr.reshape(2, 5))

print('--------------------\n')

print('--- Additional Functionality ---')

mat = np.arange(0, 100).reshape(10, 10)
print(mat)
print()

row = 0
col = 1

print('--- Select an individual number ---')

print(mat[row, col])
print()

print('--- Select an entire column ---')

print(mat[:, col])
print()

print('--- Select an entire row ---')

print(mat[row, :])
print()

print('--- Masking ---')

print(mat > 50)
print(mat[mat > 50])

print('--------------------\n')
