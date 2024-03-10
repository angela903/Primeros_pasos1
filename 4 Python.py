# Validar el digito verificador único

# Imprime el texto para ingresar un rut sin digito verificador
rut= input("Ingrese el rut sin el digito verificador: ")
rut = rut.replace(".", "").replace("-","")

# Declaración de variables de total y multiplicador
total = 0
multiplicador = 2

# Se utiliza el ciclo for para inicializar una variable de tipo entero y de nombre i
for i in reversed(rut):
    total += int(i) * multiplicador
    multiplicador += 1

# Se utiliza la condicional if para hacer una comparativa entre multiplicadores
    if multiplicador == 8:
        multiplicador = 2
resto = total % 11
digito_verificador_calculado = 11 - resto

# Se utiliza la condicional if para validar que no existan dos números como dígito verificador
if digito_verificador_calculado ==11:
    digito_verificador_calculado = "0"
elif digito_verificador_calculado == 10:
    digito_verificador_calculado="k"

# Imprime el digito verificador
print("el digito verificador es: ", digito_verificador_calculado)