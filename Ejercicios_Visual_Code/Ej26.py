#26. Realiza un programa que, al introducir una letra por teclado, aparezca por pantalla si está o no en mayúscula. Utiliza dos IF’s que establezcan True o False a la condición.

respuesta=input("introduce una letra: ")
if respuesta.isnumeric()==True:
    if respuesta.isupper()==False:
        print("Es mayúscula")
    else:
        print("Es minúscula")
