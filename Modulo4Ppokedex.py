#from curses.ascii import isalpha
import requests #Librerias para el manejo de los verbos http de la API
import matplotlib.pyplot as plt #Liberia para el manejo de gráficos
from PIL import Image #Libreria para el manejo de la imagen descargada
from urllib.request import urlopen #Libreria para descargar la imagen en url
import os #Libreria para recursos del sistema que maneja la funcion mkdir para crear directorios
import errno #Libreria para el manejo de errores 
import json #Libreria para la manipulacion de archivos json

while True:
    while True:
        pokemon = input(f"\nEscribe el nombre de un pokemon: ")
        if not pokemon.isalpha():#validamos que el nombre sea una cadena de texto
            print("Nombre inválido")
        else:
            break

    url = "https://pokeapi.co/api/v2/pokemon/" + pokemon #concatenamos url y nombre del pokemon

    respuesta = requests.get(url) #mediante llamada de API obtenemos la info del pokemon

    if respuesta.status_code != 200:#Si tenemos cualquier respuesta que no sea un exito en la llamada
        print("Pokemon no encontrado")
    else:
        datos = respuesta.json() #obtenemos el json o diccionario del pokemon

        try:
            url_imagen = datos["sprites"]["front_default"] #obtenemos imagen del poke
            imagen = Image.open(urlopen(url_imagen)) #Cargamos la imagen en variable mediante la 
        except:                                      #descarga via la libreria urlopen
            print("El pokemon no tiene imagen") #En caso de que no exista la imangen interceptamos 
            exit()                              #el error y salimos.  
        #Extraemos del json los datos del pokemon para imprimirlos
        nombre = datos["name"]
        peso = datos["weight"]
        altura = datos["height"]
        tipo = datos["types"][0]["type"]["name"]
        
        nunMov=len(datos["moves"])#Sacamos el numero de movs del pokemon
        #Imprimimos los datos del pokemon
        print(f"Nombre: {nombre}\nPeso: {peso} lbs\nAltura: {altura} ft\nTipo: {tipo}")
        print(f"Movimientos totales: {nunMov}") 
        #Con el numero de movimientos los imprimimos mediante un ciclo for
        for i in range(nunMov):
            movimiento = datos["moves"][i]["move"]["name"]
            print(f"Movimiento {i+1}: {movimiento}.")

        #Colocamos el nombre como titulo de la imagen    
        plt.title(datos["name"].capitalize())
        imgplot = plt.imshow(imagen) #cargamos la imagen en una variable
        plt.show()#Mostramos la imagen mediate pyplot
        #Creamos el directorio donde guardar el json
        try:
            os.mkdir('c:\\pokedex')
        except OSError as e: #Si ya existe usamos la instruccion raise
            if e.errno != errno.EEXIST:
                raise

        
        ruta= f"c:\\pokedex\\{pokemon}.json" #Creamos la ruta del archivo
        with open(ruta,"w") as f_pokedex: #Abrimos en modo escritura completa
            
            json.dump(datos, f_pokedex) #mediante el objeto json guardamos en ese formato

    while True:#Ciclo para determinar si realizamos otra consulta o salimos
        respuesta = input("¿Desea ingresar otro pokémon? (S) o (N) ").capitalize()
        if respuesta == "S":
            break
        elif respuesta == "N":
            print("Fin del programa.")
            exit()
        else:
            print("Opción inválida.")


    
