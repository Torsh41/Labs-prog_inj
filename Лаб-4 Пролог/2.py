import math

def z(x, y):
    return (math.sin(x) ** 2 + math.cos(y) ** 2) * 2

x = 5
y = 5
z = z(x, y)
print(z)