"""
Escribe un programa que solicite al usuario
ingresar un número y luego muestre la tabla
de multiplicar de ese número del 1 al 10
"""

def numeroUsuario():
    while True:
        numero = int(input("Ingrese un numero: "))
        if numero > 0:
            return numero
        else:
            print("Recuerda ingresar numeros postivos.")
    
def tablasMultiplicar(numero):
    print(f"\nTabla de multiplicar del {numero}:")
    for i in range(1,11):
        print(f'{numero} x {i} = {numero*i}')

def solucion():
    numero = numeroUsuario()
    tablasMultiplicar(numero)

if __name__ == "__main__":
    solucion()