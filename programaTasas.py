def __inicio__():
    print("-------Bienvenido a la calculadora de tasas-------")
    tasa = float(input("Por favor, digite el porcentaje de interés, en formato porcentual. Ej: 18"))
    while (True):
        print("Escoja el formato en el que se encuentra su tasa")
        print("1. NA/SV")
        print("2. NA/TV")
        print("3. MV")
        print("4. AV")
        print("5. NB/MV")
        print("6. NA/TA")
        print("7. Anual Continua")
        print("8. Salir")
        opcion = int(input())
        if(opcion == 1):
            efectivo_anual = nom_anual_semestre_vencido(tasa)
            calcular_todo(efectivo_anual)
        elif(opcion == 2):
            efectivo_anual = nom_anual_trimestre_vencido(tasa)
            calcular_todo(efectivo_anual)
        elif(opcion == 3):
            efectivo_anual = efectivo_mensual(tasa)
            calcular_todo(efectivo_anual)
        elif(opcion == 4):
            calcular_todo(tasa)
        elif(opcion == 5):
            efectivo_anual = nom_bimestral_mensual_vencido(tasa)
            calcular_todo(efectivo_anual)
        elif(opcion == 6):
            efectivo_anual = nom_anual_trimestre_anticipado(tasa)
            calcular_todo(efectivo_anual)
        elif(opcion == 8):
            break


def nom_anual_semestre_vencido(tasa: int):
    return ((tasa/2) + 1)**2 -1

def nom_anual_trimestre_vencido(tasa):
    return ((tasa/4) + 1)**(4) -1

def efectivo_mensual(tasa):
    return (tasa + 1)**(12) -1

def nom_bimestral_mensual_vencido(tasa):
    return ((tasa/2)+1)**(12) -1


def nom_anual_trimestre_anticipado(tasa):
    interes = (tasa/4)
    return nom_anual_trimestre_vencido((interes/(1-interes))*4)


def efectivo_anual_a_nominal_anual_trimestre_vencido(tasa):
    return ((1+tasa)**(1/4) -1)*4


def efectivo_anual_a_nominal_anual_semestre_vencido(tasa):
    return ((1+tasa)**(1/2)-1)*2


def efectivo_anual_a_efectivo_mensual(tasa):
    return (1+tasa)**(1/12) -1


def efectivo_anual_a_nominal_bimestral_mensual_vencido(tasa):
    return efectivo_anual_a_efectivo_mensual(tasa)*2


def efectivo_anual_a_nominal_anual_trimestre_anticipado(tasa):
    interes =((1+tasa)**(1/4) -1)/100
    return (interes/(interes+1))*4


def calcular_todo(efectivo_anual):
    print("Efectivo Anual: ", efectivo_anual)
    print("NA/SV: ", efectivo_anual_a_nominal_anual_semestre_vencido(efectivo_anual))
    print("NA/TV: ", efectivo_anual_a_nominal_anual_trimestre_vencido(efectivo_anual))
    print("Efectivo Mensual: ", efectivo_anual_a_efectivo_mensual(efectivo_anual))
    print("NB/MV: ", efectivo_anual_a_nominal_bimestral_mensual_vencido(efectivo_anual))
    print("NA/TA: ", efectivo_anual_a_nominal_anual_trimestre_anticipado(efectivo_anual))
__inicio__()
