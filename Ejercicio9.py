"""
Crea un programa que solicite al usuario
ingresar una serie de números positivos y
luego calcule e imprima el promedio de los
números ingresados utilizando un bucle while.
El programa debe terminar cuando el usuario
ingrese un número negativo.
"""

def solicitar_numero():#Solicita un número al usuario
    return float(input("Ingrese un número (negativo para terminar): "))

def calcular_promedio(suma, cantidad):#Calcula el promedio dados la suma y la cantidad de números
    return suma / cantidad if cantidad > 0 else 0

def imprimir_resultado(promedio):#Imprime el resultado del cálculo del promedio
    print(f"El promedio de los números ingresados es: {promedio:.2f}")

def main():
    suma = 0
    cantidad = 0
    
    while True:
        numero = solicitar_numero()
        
        if numero < 0:
            break
        
        suma += numero
        cantidad += 1
    
    promedio = calcular_promedio(suma, cantidad)
    imprimir_resultado(promedio)

if __name__ == "__main__":
    main()