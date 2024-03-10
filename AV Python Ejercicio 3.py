# Para trabajar con fechas se debe utilizar la clase datetime

from datetime import datetime

# Ingrese el año de nacimiento
ano_nacimiento = int(input("Ingrese el año de nacimiento: "))

# Ingrese el año de fallecimiento (Ingrese un N°0 si la persona esta viva)
ano_fallecimiento = int(input("Ingrese el año de fallecimiento (ingrese el N° 0 si la persona esta viva): "))

# Si el año de fallecimiento es el N° 0, se debe interpretar como la persona vive utilizando el año actual
if ano_fallecimiento == 0:
    ano_fallecimiento = datetime.now().year

# Crear una opción que cuente los años bisiestos y crear un almacenamiento para la lista de años bisiestos
anos = 0
anos_bisiestos = []

# Utilizar un bucle for para iterar sobre todos los años desde que la persona nace hasta el año actual, considerando
# que la persona este fallecida también

for ano in range(ano_nacimiento, ano_fallecimiento + 1):

    # Verificación del año bisiesto
    if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):

        # Si el año es bisiesto, el contador debe incrementar e incluir el año a la lista de años bisiestos
        anos += 1
        anos_bisiestos.append(ano)

# Imprimir la cantidad de años que la persona ha vivido en años bisiestos y la lista de los
#  N° de años bisiestos vividos

print(f"La cantidad de años que la persona ha vivido son: {anos} años bisiestos.")
print(f"Los años bisiestos que la persona a vivido son: {anos_bisiestos}")