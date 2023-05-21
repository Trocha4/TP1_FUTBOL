from datos import obtener_lista_definiciones
import random



PALABRA=0
DEFINICION=1
LONG_MINIMA_PALABRA=5
INICIAL=0
aciertos=0
errores=0

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



indice_tablero_dos=0
espacio=""
cadena_dos=""
tablero_dos=["  ","   ","   ","  ","  ","  ","  ","  ","  ","  "]

def roscooo(tablero_dos,cadena_dos,cadena,palabras_seleccionadas,dicc_definiciones):
    aciertos=0
    errores=0
    indice_tablero_dos=0
    respuestas =[]
    for palabra in palabras_seleccionadas:
        print(cadena)
        for x in tablero_dos:
            cadena_dos += "[" + x + "]"
        print(cadena_dos)
        cadena_dos=""
        print("Aciertos :",aciertos)
        print("Errores :",errores)
        print("Turno letra ",palabra[0].upper(), "- Palabra de",len(palabra) ,"letras" )
        print("Definicion :",dicc_definiciones[palabra])        
        teclado=input("Ingrese palabra: ")
        print(espacio)
        if teclado == palabra:
            aciertos+=1       
            tablero_dos[indice_tablero_dos]= "a"
        else:
            errores+=1
            tablero_dos[indice_tablero_dos]= "e"
        
        indice_tablero_dos+=1
        
        respuestas.append(teclado)
    return aciertos,errores,respuestas
        
        
        
def rosco_inicial(letras_elegidas):
    cadena=""
    for letra in letras_elegidas:
        cadena+= "[" + letra.upper() + "]"
    return cadena

puntos=0 
VALOR_ACIERTOS=10
VALOR_ERRORES=-3
def resumen(palabras_seleccionadas,respuestas,puntos,aciertos,errores):
    puntos = (aciertos*VALOR_ACIERTOS)+(errores*VALOR_ERRORES)
    i=0
    for respuesta in respuestas:
        if respuesta == palabras_seleccionadas[i]:
            print("Turno letra ",palabras_seleccionadas[i][INICIAL].upper(), "- Palabra de",len(palabras_seleccionadas[i]) ,"letras","-",respuesta,"- acierto")
    
        else:
            print("Turno letra ",palabras_seleccionadas[i][INICIAL].upper(), "- Palabra de",len(palabras_seleccionadas[i]) ,"letras -",respuesta,"- error - Palabra correcta: ",palabras_seleccionadas[i])
    
        i+=1
    
    
    
    
    
    print("Puntaje final: ",puntos)
    
    return puntos

    


def main():
    definiciones=obtener_lista_definiciones()
    dicc_definiciones=armar_dicc(definiciones)
    palabras_dicc=lista_palabras(dicc_definiciones)
    dicc_por_letras=armar_dicc_letras(palabras_dicc)
    letras_elegidas=seleccionar_letras()
    palabras_seleccionadas= seleccionar_palabras(letras_elegidas,dicc_por_letras)
    letras=rosco_inicial(letras_elegidas)
    rosco=roscooo(tablero_dos,cadena_dos,letras,palabras_seleccionadas,dicc_definiciones)
    puntos_total= resumen(palabras_seleccionadas,rosco[2],puntos,rosco[0],rosco[1])
    
    
    return puntos_total
    
print(main())



    


