import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
 
# Определяем переменную величину
x = np.arange(-5, 5, 0.01)
 
 
# Определяем функцию для системы диф. уравнений
def diff_func(i, x): # z - изменяемая величина для системы
    y, z = i # Указание изменяемых функций, через z
	
    # Первое уравнение системы
    dy_dx = (y ** 2) * z
    # Второе уравнение системы
    dz_dx = z / x - y * (z ** 2)
    
    return dy_dx, dz_dx
 
 
# Определяем начальные значения и параметры,
# входящие в систему диф. уравнений
z0 = -3
y0 = 1
 
# Начальное значение изменяемой величины системы# 
i0 = y0, z0
 
 
# Решаем систему диф. уравнений
sol = odeint(diff_func, i0, x)
 
# Строим решение в виде графика
plt.plot(x, sol[:, 0], 'b', label='theta(x)')
 
plt.legend()
plt.savefig('fig_1.png')