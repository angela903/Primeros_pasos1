def mapear_palabras(palabra1, palabra2):
    #verificación del mismo largo de las palabras

    if len(palabra1) != len(palabra2):
        print("Las palabras no contienen el mismo largo")
        return None
    

    # Creación de un diccionario de mapeo
    mapeo = {}

    # Iterar sobre las letras de las palabras

    for letra1, letra2 in zip(palabra1, palabra2):
        if letra1 in mapeo and mapeo[letra1] != letra2:
            print(f"La letra '{letra1}' ya ha sido mapeada a '{mapeo[letra1]}' y no puede ser mapeada a {letra2}")
            return None
        
    # Mapear la letra de la primera palabra a la letra de la segunda palabra

        mapeo[letra1] = letra2

    return mapeo
    
def transformar_frase(frase, mapeo):
    nueva_frase = ""
    # Iterar sobre cada letra del contenido de la frase

    for letra in frase:
        nueva_frase +=mapeo.get(letra, letra)
        return nueva_frase
    
def main():

    # Debe solicitar al usuario final que ingrese las dos palabras
    palabra1= input ("Ingresa la primera palabra: ")
    palabra2= input ("Ingrese la segunda palabra: ")

    # Obtener el mapeo entre las dos palabras

    mapeo = mapear_palabras(palabra1, palabra2)
    if mapeo is None:
        return
    
   
    # Solicitar la frase al usuario final

    frase= input("Ingrese la frase para para transformar: ")
    nueva_frase = transformar_frase(frase, mapeo)
    print("Frase transformada: ", nueva_frase)

if __name__ == "__main__":
    main()