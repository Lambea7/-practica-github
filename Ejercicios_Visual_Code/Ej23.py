#23. Modifica el programa anterior para establecer si la nota es un excelente (8.5 a 10), un notable (>=6.5 -<8.5), satisfactorio (<6.5 -5) o insuficiente (<5). Controla que la nota introducida esté entre 0 y 10. Utilizar elif sin operadores lógicos.
nota = float(input("Introduce tu nota (0-10): "))
if 0 <= nota <= 10:
    if nota >= 8.5:
        print("Excelente")
    elif nota >= 6.5:
        print("Notable")
    elif nota >= 5:
        print("Satisfactorio")
    else:
        print("Insuficiente")   