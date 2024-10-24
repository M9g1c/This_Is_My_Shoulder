import math as M
import task1 as cst
T = 200
er = 300
N = (2/(M.pi ** 0.5)) * (cst.h/((cst.k * T) ** (3/2)) * cst.E ** ((-er)/(cst.k * T)) * er ** (T/2))
print(N)