respuesta=input("introduce una letra: ")
if respuesta.isnumeric()==False:
    if respuesta.isupper():
        print("Es mayúscula")
    else:
        print("Es minúscula")
else: 
    print("el valor itroducido no es una letra")
