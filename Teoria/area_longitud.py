import math 

var_radio=float(input("introduce el valor de radio: "))

var_area=math.pi * (var_radio ** 2)

var_longitud= 2 * math.pi * var_radio

print(var_area)
print(var_longitud)

#metodos de redondeo y print
print("el resultado es: ", round(var_area,2))
print(f"El resultado es: {var_area:.f2}")
print("El resultado es: ", math.ceil(var_area))
print("El resultado es: ", math.floor(var_area))
