var_Grados=float(input("Introduce los grados: "))
"""F=Cx5/9+32"""
calculo=var_Grados * 9/5 + 32
print("temperatura:", calculo, "°F")

#otra manera de presentar la forma con print:

print(f"2ª manera de presentar Temperatura: ")
#PRIMER METODO DE REDONDEO
print(round(calculo, 2))
print(f"metodo roura {calculo:.2f}")   