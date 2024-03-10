# Realiza un programa que reciba tres numeros por teclado y calcule su promedio.

# Declaracion de varibles de tipo float
n1 = float(input("Ingrese la nota numero uno: "))
n2 = float(input("Ingrese la nota numero dos: "))
n3 = float(input("Ingrese la nota numero tres: "))

# Operatoria para el calculo del promedio
prom  = (n1+n2+n3)/3

# Se utilizo la condicional if que prom sea mayor o igual a 4 con esta nota el alumno esta aprobado
if(prom>=4):
    print("Su promedio es:",prom,"¡Felicitaciones su promedio ha sido aprobado!")

# Aquí se utiliza la condicional else, si el if no cumple la condición
else:

# Imprime
    print("Su promedio es:", prom," Lo siento su promedio es inferior al solicitado para aprobar")
