name = "Artem Smirnov"
name_str = '_'.join(name)
nu = name_str.upper()
nl = name_str.lower()
print(nu)
print(nl)
name_symbolU = [ord(symbol) for symbol in nu]
name_symbolL = [ord(symbol) for symbol in nl]
print(name_symbolU)
print(name_symbolL)
print("minimum:", min(name_symbolU))
print("maximum:", max(name_symbolU))
print("minimum:", min(name_symbolL))
print("maximum:", max(name_symbolL))