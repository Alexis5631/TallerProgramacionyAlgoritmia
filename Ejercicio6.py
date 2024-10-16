"""
Escribe un programa que solicite al usuario ingresar el día, el mes y el año de
una fecha. Luego, verifica si la fecha es válida o no. Considera los diferentes
casos, como los días de cada mes y si el año es bisiesto. Muestra un mensaje
indicando si la fecha es válida o no.
"""

def bisiesto(año):
    return año % 4 == 0 and (año % 100 != 0 or año % 400 == 0)

def dias_en_mes(mes, año):
    dias_por_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if mes == 2 and bisiesto(año):
        return 29
    return dias_por_mes[mes - 1]

def fecha_valida(dia, mes, año):
    if mes < 1 or mes > 12:
        return False
    if dia < 1 or dia > dias_en_mes(mes, año):
        return False
    return True

def main():
    dia = int(input("Ingrese el día: "))
    mes = int(input("Ingrese el mes: "))
    año = int(input("Ingrese el año: "))

    if fecha_valida(dia, mes, año):
        print(f"La fecha {dia}/{mes}/{año} es válida.")
    else:
        print(f"La fecha {dia}/{mes}/{año} no es válida.")

if __name__ == "__main__":
    main()