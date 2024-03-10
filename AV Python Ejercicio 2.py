# Crea programa en Python que solicite al usuario:
# 1. Ingresar un número entero cualquiera del 1 al 9.
# 2. Luego solicitar que ingrese números secuenciales partiendo por 1, 
# 3. pero saltándose aquellos que sean múltiplos del valor ingresado al comienzo. 
# 4. En caso de ingresar un valor erróneo, 
# 5. enviar un mensaje indicando el error y 
# 6. El número que correspondía ingresar.
# Por ejemplo, si el usuario ingresa el valor 3, el juego debería mostrar lo siguiente
# Con que número desea jugar: 3
# 1
# ingrese un numero secuencial que no sea múltiplo de 3
9
def main():
    print("juego de secuencias numericas")
    
    try:
        #solicitar al usuario ingrese un numero del 1 al 

        numero= int(input("ingresa un numero del 1 al 9: "))

        #validación
        if numero < 1 or numero > 9:
            print("por favor ingresa un numero del 1 al 9")
            return
        
        #contador

        i = 1

        while True:
            #solicitar que ingrese los numeros secuenciales
            entrada = int(input("Ingrese el numero {i}: "))

            #Salte los numeros que son multiplos del numero que yo ingreso

            if i % numero == 0:
                i += 1

            # en caso de ingrese un valor erroneo
            if entrada != i:
                #enviar un mensaje indicando el error
                # el numero que debia ingresar
                print(f"ERROR. Debias ingresar el numero {i}.")
                break
            i += 1
    except ValueError:
        print("Por favor, ingrese un número válido.")
    finally:
        print("\n====FIN DEL JUEGO====\nGracias por jugar")

if __name__== "__main__":
    main()