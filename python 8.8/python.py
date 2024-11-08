print("Arzaba Diaz April")
print("1173")
print("3W")
#esta linea definirs el numero para la tabla de multiplicar
numero = 5  #esta linea puede cambiar este valor para imprimir la tabla de otro numero

#esta linea imprimira la tabla de multiplicar utilizando un bucle for y rango
for i in range(1, 11):  #el rango va de 1 a 10 (inclusive)
    resultado = numero * i  #multiplicamos el numero por el valor de i
    print(f"{numero} x {i} = {resultado}")  #esta linea mostramra el resultado
