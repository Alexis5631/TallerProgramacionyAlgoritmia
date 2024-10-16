import datetime

def datos():#Solicita los datos del empleado.
    nombre = input("Ingrese el nombre del empleado: ")
    apellidos = input("Ingrese los apellidos del empleado: ")
    telefono = input("Ingrese el teléfono del empleado: ")
    año_ingreso = int(input("Ingrese el año de ingreso a la empresa: "))
    edad = int(input("Ingrese la edad del empleado: "))
    
    return {
        "nombre": nombre,
        "apellidos": apellidos,
        "telefono": telefono,
        "año_ingreso": año_ingreso,
        "edad": edad
    }

def calcular_antiguedad(año_ingreso):#Calcula la antigüedad del empleado en años.
    año_actual = datetime.datetime.now().year
    return año_actual - año_ingreso

def imprimir_informacion(empleado):#Imprime la información requerida del empleado.
    antiguedad = calcular_antiguedad(empleado["año_ingreso"])
    print("\nInformación del empleado:")
    print(f"Nombre: {empleado['nombre']}")
    print(f"Apellidos: {empleado['apellidos']}")
    print(f"Antigüedad: {antiguedad} años")

def main():
    empleado = datos()
    imprimir_informacion(empleado)

if __name__ == "__main__":
    main()