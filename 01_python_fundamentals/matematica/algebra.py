import math

def calcular_delta(a, b, c):
    return b**2 - 4 * a * c

def calcular_raizes(a, b, c):
    delta = calcular_delta(a, b, c)
    if delta < 0:
        return None # não existem raízes reais
    elif delta == 0:
        x = -b / (2 * a)
        return (x, x)
    else:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        return (x1, x2)