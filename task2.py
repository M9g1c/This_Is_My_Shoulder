a=int(input('Введите число: '))
b=int(input('Введите знаменатель: '))
c=int(input('Введите число членов прогрессии: '))
print(a)
for i in range(1,c):
    a=a*b
    print(a)
