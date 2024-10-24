import math as M
import task1 as cst
h = 100 
a = 45
b = 35 
v = M.sqrt((cst.g * h * (M.tan(M.pi*0.19) ** 2))/(2 * (M.cos(M.pi/45) ** 2) * (1 - (M.tan(M.pi*0.19)*M.tan(M.pi/4)))))
print(v)