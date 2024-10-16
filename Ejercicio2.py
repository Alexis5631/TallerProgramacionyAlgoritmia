"""Crea un programa que solicite al
usuario un número entero positivo y
luego imprima los números desde ese
número hasta 1 utilizando un
buclewhile."""


def solicitarNumero():#solicitamos al usuario ingresar un numero positivo
    while True:
        numero = int(input("Ingrese un numero positivo: "))#ponemos una condicion si el numero es negativo
        if numero > 0:
            return numero
        else:
            print("El numero es negativo, recuerda ingresar un numero positivo")

def numeroDescendente(numero):#hacemos un bucle para que el numero ingresado vaya descendiendo hasta llegar a 1
    while numero >= 1:
        print(numero)
        numero -= 1

if __name__ == "__main__":#imprimimos el resultado
    numero = solicitarNumero()
    numeroDescendente(numero)


