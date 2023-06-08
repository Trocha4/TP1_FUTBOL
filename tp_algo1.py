from datos import obtener_lista_definiciones
import random

#CONSTANTES
PALABRA=0
DEFINICION=1
LONG_MINIMA_PALABRA=5
INICIAL=0
VALOR_ACIERTOS=10
VALOR_ERRORES=-3
RESPUESTAS=2
ACIERTOS=0
ERRORES=1

#VARIABLES GLOBALES
puntos=0
espacio="="
total=0

def armar_dicc(lista):
 #Recibe una lista con sublistas formadas por una palabra y su definicion
 #Retorna un diccionario en el que las claves son las palabras y el valor es su definicion
 #Condicion extra, las palabras deben tener un minimo de 5 letras para ser ingresadas en el diccionario
 #Hecho por todos en conjunto
    dicc_definiciones={}
    for palabra in lista:
        if len(palabra[PALABRA]) >= LONG_MINIMA_PALABRA:
            dicc_definiciones[palabra[PALABRA]]=palabra[DEFINICION]
    return dicc_definiciones

def lista_palabras(dicc_definiciones):
#Recibe un diccionario y retorna una lista formada por las claves
#Hecho por todos en conjunto
    palabras=dicc_definiciones.keys()
    print("Hay un total de ",len(palabras), "palabras")
    return palabras

def armar_dicc_letras(lista_palabras):
#Recibe la lista de palabras que pertenecen al diccionario
#Clasifica las palabras segun su inicial
#Retorna un diccionario en el que las claves son las letras y el valor es una lista con todas las palabras que comienzan con esa letra
#Hecho por todos
    dicc_letras={}
    for palabra in lista_palabras:
        if palabra[INICIAL] =="á":
            inicial="a"
        elif palabra[INICIAL] == "é":
            inicial="e"
        elif palabra[INICIAL] == "í":
            inicial="i"
        elif palabra[INICIAL] == "ó":
            inicial= "o"
        elif palabra[INICIAL] == "ú":
            inicial = "u"
        else:
            inicial=palabra[INICIAL]
        if inicial in dicc_letras:
            dicc_letras[inicial].append(palabra)
        else:
            dicc_letras[inicial]=[palabra]
    return dicc_letras

def palabras_por_letra (diccionario):
#Imprime la cantidad de palabras por letra
    letras=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z']
    for letra in letras:
        lista_aux= diccionario[letra]
        print("Hay", len(lista_aux), "palabras con la letra", letra)
    print(espacio*50)
    

def seleccionar_letras ():
#Recibe una lista con letras y selecciona 10 al azar, luego las ordena por orden alfabetico
#Tomas Rocha
    letras=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z']
    random.shuffle(letras)
    slice=letras[0:10]
    slice.sort()
    return slice

def seleccionar_palabras(letras, diccionario ):
#Recibe una lista de letras y un diccionario (claves=letras, valores=palabras que comienzan con esa letra)
#Selecciona al azar una palabra por cada letra de la lista dada
#Retorna una lista con las palabras seleccionadas
#Tomas Rocha
    palabras_seleccionadas=[]
    for letra in letras:
        lista_auxiliar= diccionario[letra]
        palabra_elegida=random.choice(lista_auxiliar)
        palabras_seleccionadas.append(palabra_elegida)
    return palabras_seleccionadas

def validar_entrada(teclado,palabra):
#Revisa que la palabra ingresada sea válida
#Nicolas Nayar
    valor=False
    i=0
    if len(palabra) == len(teclado): 
        valor=True
        while len(teclado)>i and valor:
            if not teclado[i].isalpha():
                valor=False
            i+=1

    return valor

def pasapalabra(cadena,palabras_seleccionadas,dicc_definiciones):
#Imprime el tablero turno por turno y revisa si hay acierto o error en la respuesta
#Buzzone, Rocha, Vanasco
    aciertos=0
    errores=0
    indice_tablero_dos=0
    respuestas =[]
    cadena_dos=""
    tablero_dos=["  ","   ","   ","  ","  ","  ","  ","  ","  ","  "]
    for palabra in palabras_seleccionadas:
        print(cadena)
        for respuesta in tablero_dos:
            cadena_dos += "[" + respuesta + "]"
        print(cadena_dos)
        cadena_dos=""
        print("Aciertos :",aciertos)
        print("Errores :",errores)
        print("Turno letra ",palabra[0].upper(), "- Palabra de",len(palabra) ,"letras" )
        print("Definicion :",dicc_definiciones[palabra])        
        teclado=input("Ingrese palabra: ")
        while not validar_entrada(teclado,palabra):
            print("Palabra inválida")
            teclado=input("Ingrese palabra: ")
        if teclado == palabra:
            aciertos+=1       
            tablero_dos[indice_tablero_dos]= "a"
        else:
            errores+=1
            tablero_dos[indice_tablero_dos]= "e"
        print(espacio*50)
        indice_tablero_dos+=1
        respuestas.append(teclado)
    return aciertos,errores,respuestas
                
def rosco_inicial(letras_elegidas):
#Funcion que muestra las letras con las que se va a jugar
#Buzzone, Vanasco
    cadena=""
    for letra in letras_elegidas:
        cadena+= "[" + letra.upper() + "]"
    return cadena

def resumen(palabras_seleccionadas,respuestas,puntos,aciertos,errores):
#Hace un resumen de la partida y retorna el puntaje
#Rocha,Buzzone
    puntos = (aciertos*VALOR_ACIERTOS)+(errores*VALOR_ERRORES)
    for palabra in range(0,10):
        if respuestas[palabra] == palabras_seleccionadas[palabra]:
            print("Turno letra ",palabras_seleccionadas[palabra][INICIAL].upper(), "- Palabra de",len(palabras_seleccionadas[palabra]) ,"letras","-",respuestas[palabra],"- acierto")
        else:
            print("Turno letra ",palabras_seleccionadas[palabra][INICIAL].upper(), "- Palabra de",len(palabras_seleccionadas[palabra]) ,"letras -",respuestas[palabra],"- error - Palabra correcta: ",palabras_seleccionadas[palabra])
    print("Puntaje final: ",puntos)
    return puntos

def juego(dicc_por_letras,dicc_definiciones,total):
#Funcion que corre el juego
    letras_elegidas=seleccionar_letras()
    palabras_seleccionadas= seleccionar_palabras(letras_elegidas,dicc_por_letras)
    letras=rosco_inicial(letras_elegidas)
    rosco=pasapalabra(letras,palabras_seleccionadas,dicc_definiciones)
    puntito= resumen(palabras_seleccionadas,rosco[RESPUESTAS],puntos,rosco[ACIERTOS],rosco[ERRORES])
    volver_a_jugar(dicc_por_letras,dicc_definiciones,puntito,total)     
    
def volver_a_jugar(dicc_por_letras,dicc_definiciones,puntos,total):
#Da la opcion de volver a jugar 
#Nayar,Buzzone,Rocha
    puntos+=total
    total=puntos
    print(total)
    reiniciar= input("Desea jugar otra partida (si/no): ")
    while reiniciar != "si" and reiniciar != "no" :
        reiniciar = input("Respuesta invalida, desea jugar otra partida (si/no): ")   
        
    if reiniciar == "si":
        juego(dicc_por_letras,dicc_definiciones,total)
        
    else:
        print("Juego finalizado")
    

def main():
    definiciones=obtener_lista_definiciones()
    dicc_definiciones=armar_dicc(definiciones)
    palabras_dicc=lista_palabras(dicc_definiciones)
    dicc_por_letras=armar_dicc_letras(palabras_dicc)
    palabras_por_letra(dicc_por_letras)
    juego(dicc_por_letras,dicc_definiciones,total)
    
main()    





