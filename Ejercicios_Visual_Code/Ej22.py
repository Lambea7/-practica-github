#22. Programa que al introducir una nota por teclado te diga si has aprobado o suspendido. Si la nota es menos de un 5 es suspenso y si la nota es 5 o mayor estás aprobado.  Y que haga repetir al usuario el valor introducido si no esta del 1 al 10.
nota = float(input("Introduce tu nota (1-10): "))
if 1 <= nota <= 10:
 if nota >= 5:
    print("Has aprobado.")
 else: 
    print("Has suspendido.")
else:  
    print("Nota no válida. Introduce un valor entre 1 y 10.")
