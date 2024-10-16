"""
Escribe un programa que solicite al
usuario ingresar su calificación en un
examen y determine si ha aprobado o
no. Si la calificación es igual o mayor a
60, muestra el mensaje "Has aprobado".
De lo contrario, muestra el mensaje "Has
reprobado".
"""

def NotaCalificacion():#solictar al usuario ingresar la calificacion
    calificacion = float(input("Ingrese tu calificacion: "))
    return calificacion

def verificacionCalificacion(calificacion):#verificamos si cumple las condiciones 
    if calificacion >= 60:
        print("Has aprobado.")
        
    else:
        print("Has reprobado.")


if __name__ == "__main__":#imprimimos el resultado
    calificacion = NotaCalificacion()
    verificacionCalificacion(calificacion)
