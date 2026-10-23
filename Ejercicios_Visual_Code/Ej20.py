#20. A partir del ejercicio anterior, forzar que el usuario solo pueda introducir por teclados números entre 0 y 10.
num1= int(input("Introduce el primer numero del 1 al 10: "))
num2= int(input("Introduce el segundo numero del 1 al 10: "))
if num1 and num2 in [1,2,3,4,5,6,7,8,9,10]: 
 if num1>num2:
    print("el primero es mas grande ")
 elif num1<num2:
    print("el segundo es mas grande ")
 else:
    print("ambos son iguales")
else: 
   print("Uno o los dos números están fuera de los límites establecidos ")

    