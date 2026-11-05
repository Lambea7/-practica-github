#25. Repite el programa número 23 pero en esta ocasión utilizando operadores lógicos. 
nota = float(input("Introduce tu nota (0-10): "))
if 0 <= nota <= 10:
    if nota >= 8.5:
        print("Excelente")
    elif 6.5 <= nota < 8.5:
        print("Notable")
    elif 5 <= nota < 6.5:
        print("Satisfactorio")
    else:
        print("Insuficiente")