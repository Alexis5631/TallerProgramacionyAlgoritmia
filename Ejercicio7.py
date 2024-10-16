"""
Crea un programa que solicite al usuario ingresar tres
longitudes y determine si esas longitudes pueden formar
un triángulo válido. Utiliza la desigualdad triangular
para realizar la comprobación y muestra un mensaje
indicando si se puede formar un triángulo o no.
La desigualdad triangular es un concepto matemático
que establece una condición necesaria para que tres
segmentos puedan formar un triángulo válido. La
desigualdad triangular establece que la suma de las
longitudes de dos lados de un triángulo siempre debe ser
mayor que la longitud del tercer lado.
En términos más precisos, si tienes tres segmentos con
longitudes a, b y c, donde a, b y c son números
positivos, entonces estos segmentos pueden formar un
triángulo válido si y solo si se cumple la siguiente
condición:
a + b > c
a + c > b
b + c > a
"""

def verificarTriangulo(a, b, c):#Verifica si las longitudes a, b y c pueden formar un triángulo válido.
    return a + b > c and a + c > b and b + c > a

def solicitarLongitudes():#Solicitamos al usuario ingresar tres longitudes.
    a = float(input("Ingresa la longitud del primer lado: "))
    b = float(input("Ingresa la longitud del segundo lado: "))
    c = float(input("Ingresa la longitud del tercer lado: "))
    return a, b, c

def resultado():
    a, b, c = solicitarLongitudes()
    if verificarTriangulo(a, b, c):
        print("Las longitudes pueden formar un triángulo válido.")
    else:
        print("Las longitudes no pueden formar un triángulo válido.")

#Resultado 
if __name__ == "__main__":
    resultado()