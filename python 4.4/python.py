print("Arzaba Diaz April")
print("1173")
print("3W")
#esta linea dara una funcion que recibe una lista de notas y muestra la mas baja y la mas alta
def mostrar_notas_extremos(lista_de_notas):
    #esta linea verificara si la lista no esta vacia
    if len(lista_de_notas) > 0:
        #en esta linea encontraremos la nota mas baja
        nota_baja = min(lista_de_notas)
        #en esta lista encontraremos la nota mas alta
        nota_alta = max(lista_de_notas)
        
        #esta linea imprimiera los resultados
        print("la nota mas baja es:", nota_baja)
        print("la nota mas alta es:", nota_alta)
    else:
        print("la lista esta vacia")

#esta linea dara un ejemplo de uso
notas = [7, 9, 5, 8, 3, 6]
mostrar_notas_extremos(notas)
