names = ['Adolf', 'Leha', 'Vanya']
ages = [14, 26, 83]

def checker(user):
    name, age = user
    return age > 21

users = list(zip(names, ages))
cDA = list(filter(checker, users))
print(cDA)