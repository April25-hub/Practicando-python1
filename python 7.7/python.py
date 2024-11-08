print("Arzaba Diaz April")
print("1173")
print("3W")

#esta linea iniciara una variable para almacenar la suma
suma_pares = 0

#esta linea usara la funcion range() para iterar desde 2 hasta 100 con paso de 2 (solo numeros pares)
for numero in range(2, 101, 2):
    suma_pares += numero  #estsa linea sumara el numero par a la variable suma_pares

#esta linea imprimira el resultado de la suma
print("la suma de los numeros pares desde el 2 hasta el 100 es:", suma_pares)
