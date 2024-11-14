import random
flowers = ["Ромашка","Незабудка", "Василёк"]
colors = ["Белый", "Фиолетовый", "  Голубой", "Красный"]
b = list(colors[random.randint(0,3)]for x in range(0,len(flowers)))
a = dict(zip(flowers, b))
print(a)