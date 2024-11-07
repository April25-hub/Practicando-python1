print("Arzaba Diaz April")
print("1173")
print("3W")
#esta linea dara una funcion que evalua la nota y devuelve el equivalente segun el rango
def evaluar_nota(nota):
    """
    esta funcion recibe una nota (numero) y devuelve una cadena que describe la calificacion
    correspondiente de acuerdo al rango en el que se encuentra la nota
    
    parametros:
    nota (float): la calificacion a evaluar
    
    retorna:
    str: el texto correspondiente a la calificacion segun el rango
    """
    #esta linea verificara si la nota esta en el rango de 0 a 10
    if nota >= 0 and nota < 5:
        return "SUSPENSO"
    elif nota >= 5 and nota < 6:
        return "SUFICIENTE"
    elif nota >= 6 and nota < 7:
        return "BIEN"
    elif nota >= 7 and nota < 9:
        return "NOTABLE"
    elif nota >= 9 and nota <= 10:
        return "SOBRESALIENTE"
    else:
        return "NOTA NO VALIDA"  #esta linea te dira que en caso de que la nota no este dentro del rango valido

#esta linea dara un breve ejemplo del uso de la funcion
nota = float(input("introduce la nota: "))  #esta linea le pedira la nota al usuario
print(evaluar_nota(nota))  #esta linea imprimira el resultado de la evaluacion de la nota
