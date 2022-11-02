# Modulo4Pkedex
Durante la creacion de este proyecto basicamente usamos los verbos http para comunicarnos on una APi en el intenet de la cual podiamos descargar 
informacion de cada uno de los pokemones disponibles en la base de datos. Para esto tuvimos que tener un comprension de los Status codes que podiamos 
resolver mediante nuestras llamadas GET y yo lo simplifique ne que solo estaba buscando las llamadas tipo 200 que me devolvieran informacion correcta y
todas las dmás las maneje como un error más, lo que simplifico el manejo de ellas, todo ello utilizando la librería Requests.
Una vez delimitada la descarga, mediante la funcion GET haciamos la llamada a la API y obtenemos el archivo json correspondiente, almacenandolo temporalmente
en una variable a la cual podemmos acceder a sus valores con keys, ya que al final el archivo json es un diccionario (o así me parcio que se maneja).
Para el manejo de la imagen que descargamos utilizarmos de la libreia PIL la funcioon Image que nos permitio almacenar la imagen en un variable, previamente 
descargada mediante la funcion UrlOpen (de hecho se hace en un solo paso ausando de parametro una en otra).
De nuestra variable mediante la variable de tipo diccionario sacamos la info para mostrarla en pantalla, aplicando la direccion correcta de cada llave para
mostrar las caracteristicas. Como cada pokemon tiene muchos movimientos saqué el numero de movimientos totales de la llave de movimientos e implemente un ciclo for 
que recorria toda la llave e imprime cada movimiento.
Como siguiente paso cargamos la imagen en un grafica de la librería pyplot enviando la imagen previamente obtenida con un imshow().
En este punto tenia que crear el directoria de la pokedex por lo cul importe una libreria llmada os que nos permite utilizar funciones del sistema operativo 
y meti un try except para validar el directorio: si no existe, lo crea. Si ya existe, lo obvia para no crearlo de nuevo, mediante la funcion EEXIST de una libreria 
de manejo de errores llamada errno.
Como ultimo paso creamos en un variable la direccion de donde queremos el archivo concatenando el nombre del pokemon al directorio pokedex (En mi caso yo lo puse en c:\ 
pero esto igual podria dar problemas en usuarios limitados de permisos de escritura). Al principio creo que podía escribir simplemente con un writelines mi
archivo final, pero ya después vi que no me guardaba todo po lo cual investigue y hay una libreria especial para escribir archivos json llamada asi mismo, por lo cual 
tuve que crear un archivo y usar la funcion dump de esa libreria , que me respetaba toda la estructura de archivo al escribirlo.

Tuve que investigar muchas cosas, pero fue divertido crear este programa, al final use tods estas librerías:
import requests #Librerias para el manejo de los verbos http de la API
import matplotlib.pyplot as plt #Liberia para el manejo de gráficos
from PIL import Image #Libreria para el manejo de la imagen descargada
from urllib.request import urlopen #Libreria para descargar la imagen en url
import os #Libreria para recursos del sistema que maneja la funcion mkdir para crear directorios
import errno #Libreria para el manejo de errores 
import json #Libreria para la manipulacion de archivos json



