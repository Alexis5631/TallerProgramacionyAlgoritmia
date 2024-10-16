"""Escribe un programa que solicite al
usuario ingresar su edad y luego
determine si es mayor de edad o no
utilizando una declaraciónif. Si la edad
es mayor o igual a 18, muestra el
mensaje "Eres mayor de edad", de lo
contrario, muestra el mensaje "Eres
menor de edad".
"""

def solicitarEdad ():#solicitamos al usuario ingresar la edad
    edad = int(input("Ingrese su edad: "))
    return edad

def verificarEdad(edad):#verificamos si cumple las condiciones
    if edad >= 18:
        print("Eres mayor de edad.")
    else:
        print("Eres menor de edad.")

if __name__ == "__main__":#imprimimos el resultado
    edad = solicitarEdad()
    verificarEdad(edad)

