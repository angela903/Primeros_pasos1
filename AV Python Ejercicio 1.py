# Dibuje una matriz de 4 filas por 4 columnas

def dibuje_una_matriz(filas, columnas):

    # Utilice un ciclo for para ejecutar el código una cierta cantidad de veces, en este caso 4 filas por 4 columnas

    for i in range(filas * 2 + 1):
        for j in range(columnas * 2 + 1):
            if i % 2 == 0: 
                if j % 2 == 0:
                    print('+', end='')
                else:
                    print('--', end='')
            else: 
                if j % 2 == 0: 
                    print('|', end='')
                else:
                    print(' ', end='') 
        print() # cambio de la línea al final de cada fila

def main():
    try: # Es necesario utilizar try para prever excepciones en la ejecución del programa

        filas = int(input("ingresa el N° de filas requeridas: "))
        columnas = int(input("ingresa el N° de columnas requeridas: "))
        dibuje_una_matriz(filas, columnas)
    except ValueError:
        print("Ingrese un número válido.")

if __name__=="__main__":
    main()
                   