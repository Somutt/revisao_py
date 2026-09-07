import math

def area_retangulo(base, altura):
    return base * altura

def area_circulo(raio):
    return math.pi * raio**2

def area_triangulo(base, altura):
    return (base * altura) / 2

def volume_esfera(raio):
    return 4/3 * math.pi * raio**3