#18. Cines Paradiso celebran su décimo aniversario y por ser un día especial realizan importantes descuentos. A los adultos se les aplicará un 10% de descuento y a los menores de 18 años un 50%. Si la entrada cuesta 12 euros, calcula el total a pagar introduciendo por teclado el número de menores y el número de adultos que asisten al cine. 

num_menores = int(input("Introduce el número de menores: "))
num_adultos = int(input("Introduce el número de adultos: "))

precio_entrada = 12
descuento_adultos = 0.10
descuento_menores = 0.50

total_pagar_menores = num_menores * precio_entrada * (1 - descuento_menores)
total_pagar_adultos = num_adultos * precio_entrada * (1 - descuento_adultos)

print(f"El total a pagar de los menores es: {total_pagar_menores} euros")
print(f"El total a pagar de los adultos es: {total_pagar_adultos} euros")
