#21. Programa que calcula una ecuación de segundo grado. Controla que el valor de la raíz cuadrada no de un valor negativo.
import math
a = float(input("Introduce el coeficiente a: "))
b = float(input("Introduce el coeficiente b: "))
c = float(input("Introduce el coeficiente c: "))

ecuación = b**2 - 4*a*c

if ecuación < 0:
    print("El valor de la raíz cuadrada es negativo.")
else:
    x1 = (-b + math.sqrt(ecuación)) / (2*a)
    x2 = (-b - math.sqrt(ecuación)) / (2*a)
    print(f"Las soluciones son: x1 = {x1}, x2 = {x2}")