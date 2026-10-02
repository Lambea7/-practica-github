#10. Introduce por teclado dos números y muestre por pantalla la siguiente información: cociente, resto y si el dividendo es par o impar. 
num1 = int(input("Introduce el primer número (dividendo): "))
num2 = int(input("Introduce el segundo número (divisor): "))
print("El cociente es:", num1 // num2)
print("El resto es:", num1 % num2)
if num1 % 2 == 0:
    print("El dividendo es par.")
else:
    print("El dividendo es impar.")


