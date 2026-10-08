#16. Utiliza el método sqrt de la librería math para calcular la raíz cuadrada de un número. El resultado de la raíz cuadrada divídelo entre 2 de manera que se obtenga siempre un resultado entero. Haz que se muestre por pantalla los dos  resultados de todo el proceso (raíz y división). 
import math
numero = float(input("Introduce un número para calcular su raíz cuadrada: "))
raiz_cuadrada = math.sqrt(numero)
division = raiz_cuadrada // 27
print("La raíz cuadrada de", numero, "es:", raiz_cuadrada)
print("El resultado de dividir la raíz cuadrada entre 27 es:", division)