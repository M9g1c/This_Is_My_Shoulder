import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from math import e
import math as mt
 
# Определяем переменную величину
t = np.arange(-1, 1, 0.01)
 
 
# Определяем функцию для системы диф. уравнений
def diff_func(z, t): # z - изменяемая величина для системы
    x, y = z # Указание изменяемых функций, через z
	
    # Первое уравнение системы
    dx_dt = 3 * x - 2 * y + ((mt.e ** (3 * t)) / (mt.e ** t + 1))
    # Второе уравнение системы
    dy_dt = x - ((mt.e ** (3 * t)) / (mt.e ** t + 1))
    
    return dx_dt, dy_dt
 
 
# Определяем начальные значения и параметры,
# входящие в систему диф. уравнений
x0 = 5
y0 = -7
 
# Начальное значение изменяемой величины системы# 
z0 = x0, y0
 
 
# Решаем систему диф. уравнений
sol = odeint(diff_func, z0, t)
 
# Строим решение в виде графика
plt.plot(t, sol[:, 0], 'b', label='theta(t)')
 
plt.legend()
plt.savefig('fig_2.png')