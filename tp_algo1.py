from datos import obtener_lista_definiciones
import random



PALABRA=0
DEFINICION=1
LONG_MINIMA_PALABRA=5
INICIAL=0


def armar_dicc(lista):
 #Recibe una lista con sublistas formadas por una palabra y su definicion
 #Retorna un diccionario en el que las claves son las palabras y el valor es su definicion
 #Condicion extra, las palabras deben tener un minimo de 5 letras para ser ingresadas en el diccionario
    dicc_definiciones={}
    for palabra in lista:
        if len(palabra[PALABRA]) >= LONG_MINIMA_PALABRA:
            dicc_definiciones[palabra[PALABRA]]=palabra[DEFINICION]
    return dicc_definiciones

def lista_palabras(dicc_definiciones):
#Recibe un diccionario y retorna una lista formada por las claves
    palabras=dicc_definiciones.keys()
    return palabras

def armar_dicc_letras(lista_palabras):
#Recibe la lista de palabras que pertenecen al diccionario
#Clasifica las palabras segun su inicial
#Retorna un diccionario en el que las claves son las letras y el valor es una lista con todas las palabras que comienzan con esa letra
    dicc_letras={}
    for palabra in lista_palabras:
        if palabra[INICIAL] in dicc_letras:
            dicc_letras[palabra[INICIAL]].append(palabra)
        else:
            dicc_letras[palabra[INICIAL]]=[palabra]
    return dicc_letras

def seleccionar_letras ():
#Recibe una lista con letras y selecciona 10 al azar, luego las ordena por orden alfabetico
    letras=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z']
    random.shuffle(letras)
    slice=letras[0:10]
    slice.sort()
    return slice

def seleccionar_palabras(letras, diccionario ):
#Recibe una lista de letras y un diccionario (claves=letras, valores=palabras que comienzan con esa letra)
#Selecciona al azar una palabra por cada letra de la lista dada
#Retorna una lista con las palabras seleccionadas
    palabras_seleccionadas=[]
    for letra in letras:
        lista_auxiliar= diccionario[letra]
        palabra_elegida=random.choice(lista_auxiliar)
        palabras_seleccionadas.append(palabra_elegida)
    return palabras_seleccionadas


def main():
    definiciones=obtener_lista_definiciones()
    dicc_definiciones=armar_dicc(definiciones)
    palabras_dicc=lista_palabras(dicc_definiciones)
    dicc_por_letras=armar_dicc_letras(palabras_dicc)
    letras_elegidas=seleccionar_letras()
    palabras_seleccionadas= seleccionar_palabras(letras_elegidas,dicc_por_letras)
    return palabras_seleccionadas
print(main())