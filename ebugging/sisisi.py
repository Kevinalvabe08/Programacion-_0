#Código del ejercicio de debugging
#Primero comentamos todo lo que no sea codigo
def calcular_promedio(numeros):
    return sum(numeros) / len(numeros)

def comparar_con_promedio(numeros, promedio):
    for num in numeros:
        if num > promedio:#colocamos los 2 puntos
            print(f"{numeros} es mayor que el promedio.")
        elif num < promedio:
            print(f"{numeros} es menor que el promedio.")
        else:
            print(f"{num} es igual al promedio.")

# Pedir al usuario tres números
numeros = []
for i in range(3):
    num = input("Introduce un número: ")
    numeros.append(numeros)

# Calcular el promedio
promedio = calcular_promedio(numeros)

# Comparar cada número con el promedio
comparar_con_promedio(numeros,promedio)
#convertimos el num a numero
#eliminamos el espacio que estaba antes del promedio
#colocar los 2 puntos en los lugares donde hacia falta