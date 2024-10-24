import numpy as np
x0 = 8
y0 = 7
v0 = 5
a=np.zeros([6,3])

for t in range(0,6):
    for i in range(0,3):
        if i==0:
            x = x0 + v0 * t
            a[t,i]=x
        elif i==1:
            y = y0 + v0 * t
            a[t,i]=y
        elif i==2:
            a[t,i]=t
print(a)