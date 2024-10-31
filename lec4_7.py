def my_func(a, b):
    x = 3 * a - b
    return x

tmp = my_func(a, b)

def my_func(a = 1, b = 0):
    x = 3 * a - b 
    return x 

print(my_func(a, b))
print(my_func(3, 4))
print(my_func(3))
print(my_func(b = 3))
print(my_func(b = 3, a = 9))
