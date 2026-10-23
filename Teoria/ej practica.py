''' quiero que el jugador introduzca un numero del 1-5 y el ordenador piensa otro numero al azar y si es correcto digan correct o false''' 
import random

var_random= random.randint(1,5)

var_usuario=int(input("introduce un numero del 1 al 5: "))
if var_usuario in [1,2,3,4,5]:
 if int(var_usuario)==var_random:
    print("acertaste")
 else: 
    print("fallaste")
else:
  print("no has introducido el rango correcto")
    