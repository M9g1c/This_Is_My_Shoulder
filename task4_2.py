import numpy as np
b = [1, 2, 3, 4, 5]
c = np.array(b)
def z(a):
    ar = 1
    for i in a:
        ar *= i
    return ar
print(z(c))
    
    