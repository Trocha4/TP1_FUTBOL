import tkinter as tk
from tkinter import messagebox
import random

#-----------Archivos-----------Fidel Vanasco----------

def leer_usarios_csv():
    #Funcion que lee el archivo usuarios y crea un diccionario en base a eso.
    usuarios=open("usuarios.csv","r+")
    diccionario_usuarios={}
    linea=usuarios.readline()
    while linea != "":
        usuario,clave=linea.rstrip("\n").rsplit(",")
        diccionario_usuarios[usuario]=clave
        linea=usuarios.readline()
    return diccionario_usuarios

def registrar_usuario(user,clave,clave_repetida):
    #Funcion que revisa que todo lo ingresado sea correcto y lo escribe en el archivo de usuarios. 
    if validar_registro(user,clave,clave_repetida):
        try:
            usuarios=open("usuarios.csv","r+")
        except FileNotFoundError:
            usuarios=open("usuarios.csv","w")
            usuarios.close()
            usuarios=open("usuarios.csv","r+")
        linea=usuarios.readline()
        while linea!="":
            linea=usuarios.readline()
        usuarios.write(user + "," + clave + "\n")
        usuarios.close()
        messagebox.showinfo("Usuario registrado exitosamente", message="El usuario fue registrado exitosamente")
    else:
        messagebox.showerror("Error en el registro", message="EL usuario no pudo ser registrado, revise los datos ingresados")
    return

def leer_config():
    #Funcion que lee el archivo de configuracion y retorna una lista con los parametros a usar para el juego.
    base=[4,10,5,10,3]
    i=0
    archivo=open("configuracion.csv")
    lista=[]
    for linea in archivo:
        variable,valor=linea.rstrip("\n").split(",")
        lista.append(int(valor))
    archivo.close()
    for config in lista:
        if config < 1:
            lista[i]=base[i]
        i+=1
    if lista[1] > 27:
        lista[1]=base[1]
    return(lista)

def leer_archivos(longitud_palabra_minima):
    #Funcion que lee los dos archivos y crea el diccionario.
    palabras=open("palabras.txt", encoding="utf-8")
    definiciones=open("definiciones.txt",encoding="utf-8")
    palabra=palabras.readline().rstrip("\n")
    definicion=definiciones.readline().rstrip("\n")
    diccionario={}
    while palabra !="":
        if len(palabra) >= longitud_palabra_minima:
            diccionario[palabra]=definicion
        palabra=palabras.readline().rstrip("\n")
        definicion=definiciones.readline().rstrip("\n")
    palabras.close()
    definiciones.close()
    return diccionario

def crear_archivo_dicc(palabras,dicc_definicion):
    #Funcion que crea un archivo que contiene las palabras y sus respectivas definiciones.
    palabras=sorted(palabras)
    archivo=open("diccionario.csv","w",encoding="utf-8")
    for palabra in palabras:
        definicion=dicc_definicion[palabra]
        archivo.write(palabra + "," + definicion + "\n")
    archivo.close()
#--------------------------------------------------------------------------------------------


def validar_registro(user,clave,clave_repetida):
    #Funcion que valida que los datos ingresados en el registro sean correctos.
    valido=False
    if validar_user_registro(user):
        if validar_clave_registro(clave):
            if clave==clave_repetida:
                valido=True
    return valido

def validar_user_registro(usuario):
    #Funcion que valida si el usuario a crear es valido.
    valido=False
    if len(usuario) >= 4 and len(usuario) <=20:
        valido=True
        i=0
        while valido and i<len(usuario):
            caracter=usuario[i]
            if not caracter.isalnum():
                if caracter!= "-":
                    valido=False
            i+=1
    return valido

def validar_clave_registro(clave):
    #Funcion que valida si la clave ingresada en el registro es valida.
    LONGITUD_MINIMA=6
    LONGITUD_MAXIMA=12
    acentuadas=["Á","É","Í","Ó","Ú","á","é","í","ó","ú"]
    caracteres_acentuados=0
    simbolos_invalidos=0
    caracteres_en_mayuscula=0
    caracteres_en_minuscula=0
    numeros=0
    numerales=0
    acentos=0

    if (LONGITUD_MINIMA<=len(clave)<=LONGITUD_MAXIMA):
        for caracter in clave:
            if caracter in acentuadas:
                caracteres_acentuados+=1
            elif not caracter.isalnum() and caracter!="#" and caracter!="!":
                simbolos_invalidos+=1
            elif caracter.isupper():
                caracteres_en_mayuscula+=1
            elif caracter.islower():
                caracteres_en_minuscula+=1
            elif caracter.isnumeric():
                numeros+=1
            elif caracter=="#":
                numerales+=1
            elif caracter=="!":
                acentos+=1
    else:
        devolver=False

    if caracteres_acentuados>0:
        devolver=False
    elif simbolos_invalidos>0:
        devolver=False
    elif caracteres_en_mayuscula==0:
        devolver=False
    elif caracteres_en_minuscula==0:
        devolver=False
    elif numeros==0:
        devolver=False
    elif numerales==0 and acentos==0:
        devolver=False
    else:
        devolver=True

    return devolver
#-------------------Interfaz--------------Ignacio Buzzone------------------    
def iniciar_sesion():
    #Funcion que crea la primer ventana de interfaz grafica.
    lista_usuarios=[]
    raiz= tk.Tk()
    miFrame=tk.Frame(raiz,width=100,height=100)
    miFrame.pack()

    raiz.title("INGRESO DE JUGADOR")
    raiz.resizable(False,False)
    raiz.iconbitmap("pasapalabra.ico")
    raiz.geometry("350x150")

    
    cuadro_usuario=tk.Entry(miFrame) 
    cuadro_usuario.grid(row=0,column=1)
    
    
    cuadro_clave=tk.Entry(miFrame) 
    cuadro_clave.grid(row=1,column=1) 
    cuadro_clave.config(show="*")
    

    label_usuario=tk.Label(miFrame, text="Ingrese el usuario: ")
    label_usuario.grid(row=0,column=0,pady=5)

    label_clave=tk.Label(miFrame, text="Ingrese la clave: ")
    label_clave.grid(row=1,column=0)

    boton_iniciarsesion=tk.Button(miFrame, text="Iniciar sesion",command=lambda: iniciar_user(lista_usuarios,cuadro_usuario.get(),cuadro_clave.get()))
    boton_iniciarsesion.grid(row=2,column=1,padx=5,pady=10)


    boton_empezarjuego=tk.Button(miFrame, text="Empezar juego",command=lambda: main(lista_usuarios))
    boton_empezarjuego.grid(row=2,column=2,padx=5,pady=10)

    boton_registrarse=tk.Button(miFrame, text="Registrarse",command=nueva_ventana)
    boton_registrarse.grid(row=2,column=0,padx=5,pady=10)

    raiz.mainloop()

def nueva_ventana():
    #funcion que crea la segunda ventana de interfaz grafica.
    nueva_ventana=tk.Toplevel()
    nueva_ventana.title("REGISTRO")
    nueva_ventana.iconbitmap("pasapalabra.ico")
    nueva_ventana.geometry("350x150")

    label_usuario_registro=tk.Label(nueva_ventana, text="Ingrese el usuario: ")
    label_usuario_registro.grid(row=0,column=0,pady=5)

    label_clave_registro=tk.Label(nueva_ventana, text="Ingrese la clave: ")
    label_clave_registro.grid(row=1,column=0,pady=5)

    label_confimar_clave_registro=tk.Label(nueva_ventana, text="Confirme clave: ")
    label_confimar_clave_registro.grid(row=2,column=0,pady=5)

    cuadro_usuario_registro=tk.Entry(nueva_ventana) 
    cuadro_usuario_registro.grid(row=0,column=1)
    
    cuadro_clave_registro=tk.Entry(nueva_ventana)
    cuadro_clave_registro.grid(row=1,column=1) 
    cuadro_clave_registro.config(show="*")

    cuadro_confirmar_clave_registro=tk.Entry(nueva_ventana)
    cuadro_confirmar_clave_registro.grid(row=2,column=1) 
    cuadro_confirmar_clave_registro.config(show="*")

    boton_enviar_registro=tk.Button(nueva_ventana,text="Enviar registro ", command=lambda: registrar_usuario(cuadro_usuario_registro.get(),cuadro_clave_registro.get(),cuadro_confirmar_clave_registro.get()))
    boton_enviar_registro.grid(row=3)

def iniciar_user(lista_usuarios,user,clave):
    #funcion que valida el inicio de sesion.
    diccionario_usuarios=leer_usarios_csv()
    if user in diccionario_usuarios.keys():
        if diccionario_usuarios[user] == clave:                    
            aux= [user,0,0,0]
            lista_usuarios.append(aux)
            messagebox.showinfo("Inicio correcto", message="El usuario ha iniciado sesion correctamente")
            if len(lista_usuarios) == MAXIMO_DE_JUGADORES:
                main(lista_usuarios)
        else:
            messagebox.showerror("Clave Incorrecta",message="La clave ingresada es incorrecta")
    else:
        messagebox.showerror("El usuario no existe",message="El usuario ingresado no coincide con un usuario registrado, por favor registrese")
    return lista_usuarios
#--------------------------------------------------------------------------------------------

#---------------Adaptacion--------------Tomas Rocha------------------------------------------

LONGITUD_PALABRA_MINIMA=4
INICIAL=0
NOMBRE=0
ACIERTOS=1
ERRORES=2
PUNTAJE=3
PUNTAJE_ACIERTO=10
PUNTAJE_DESACIERTO=3
MAXIMO_PARTIDAS=5
MAXIMO_DE_JUGADORES=4
partidas_jugadas=1


def lista_palabras(diccionario):
    #Funcion que recibe el diccionario palabras definición e imprime el total de palabras que hay.
    palabras=diccionario.keys()
    print("Hay un total de", len(palabras), "palabras")
    return palabras

def diccionario_por_letras(palabras):
    #Funcion que clasifica las palabras en un diccionario según su inicial.
    diccionario_por_letras={}
    for palabra in palabras:
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
        if inicial in diccionario_por_letras:
            diccionario_por_letras[inicial].append(palabra)
        else:
            diccionario_por_letras[inicial]=[palabra]
    return diccionario_por_letras

def palabras_por_letra(diccionario):
    #Funcion que imprime la cantidad de palabras por cada letra.
    letras=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z']
    for letra in letras:
        lista_aux=diccionario[letra]
        print("Hay", len(lista_aux), "palabras con la letra", letra)
    print(separador())
    
def seleccionar_letras(cantidad_letras_rosco):
    #Funcion que selecciona la cantidad de letras al azar que diga el archivo config.
    letras=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z']
    random.shuffle(letras)
    slice=letras[0:cantidad_letras_rosco]
    slice.sort()
    return slice

def seleccionar_palabras(letras,diccionario):
    #Funcion que selecciona una palabra por cada letra.
    palabras_seleccionadas=[]
    for letra in letras:
        lista_auxiliar=diccionario[letra]
        palabra_elegida= random.choice(lista_auxiliar)
        palabras_seleccionadas.append(palabra_elegida)
    return palabras_seleccionadas

def pasapalabra(cadena,palabras_seleccionadas,dicc_definiciones,lista_jugadores):
    nro_turno=0
    asignacion_turnos(lista_jugadores)
    lista_roscos_turnos=[]
    lista_roscos_rtas=[]
    lista_turno=[]
    respuestas=[]
    for jugador in lista_jugadores:
        jugador[ACIERTOS]=0
        jugador[ERRORES]=0
    for palabra in palabras_seleccionadas:
        print(cadena)
        print(roscos(lista_roscos_turnos))
        print(roscos(lista_roscos_rtas))
        parciales(lista_jugadores)
        print("Turno jugador numero ", nro_turno+1 , "- Letra ", palabra[INICIAL].upper(), "- palabra de: ",len(palabra),"letras")
        print("Definicion: ", dicc_definiciones[palabra])
        teclado=input("Ingrese palabra: ")
        while not validar_entrada(teclado,palabra):
            print("Palabra inválida")
            teclado=input("Ingrese palabra: ")
        if teclado==palabra:
            lista_jugadores[nro_turno][ACIERTOS]+=1
            lista_roscos_rtas.append("a")
            lista_roscos_turnos.append(str(nro_turno+1))
            lista_turno.append(nro_turno+1)
        else:
            lista_jugadores[nro_turno][ERRORES]+=1
            lista_roscos_rtas.append("e")
            lista_roscos_turnos.append(str(nro_turno+1))
            lista_turno.append(nro_turno+1)
            nro_turno+=1
            if nro_turno == len(lista_jugadores):
                nro_turno=0
        separador()
        respuestas.append(teclado)
    return lista_jugadores,respuestas,lista_turno

def resumen(palabras_seleccionadas,lista_jugadores,respuestas,lista_nro_turno,puntaje_acierto,puntaje_desacierto):
    for turno in range(0,len(respuestas)):
        if respuestas[turno]==palabras_seleccionadas[turno]:
            print("Turno letra: ",palabras_seleccionadas[turno][INICIAL], "- Jugador ", lista_nro_turno[turno], lista_jugadores[lista_nro_turno[turno]-1][NOMBRE], "- Palabra de ", len(palabras_seleccionadas[turno]), "letras - ", respuestas[turno], "- acierto")
        else:
            print("Turno letra: ",palabras_seleccionadas[turno][INICIAL], "- Jugador ", lista_nro_turno[turno], lista_jugadores[lista_nro_turno[turno]-1][NOMBRE], "- Palabra de ", len(palabras_seleccionadas[turno]), "letras - ", respuestas[turno], "- error", "- Palabra correcta: ", palabras_seleccionadas[turno])
    print("Puntajes de la partida" )
    i=1
    for jugador in lista_jugadores:
        aux= jugador[ACIERTOS]*puntaje_acierto - jugador[ERRORES]*puntaje_desacierto
        jugador[PUNTAJE]+=aux
        print(i,".", jugador[NOMBRE], "-" , aux, " Puntos")
        i+=1
    separador()
    print("Puntajes Parciales")
    i=1
    for jugador in lista_jugadores:
        print(i,".", jugador[NOMBRE], "-" , jugador[PUNTAJE], " Puntos")
        i+=1
    return lista_jugadores
    
def volver_a_jugar(dicc_por_letras,dicc_definiciones,lista_jugadores,partidas_jugadas,maximo_partidas,config):
    if partidas_jugadas < maximo_partidas:
        reiniciar= input("Desea jugar otra partida (si/no): ")
        while reiniciar != "si" and reiniciar != "no" :
            reiniciar = input("Respuesta invalida, desea jugar otra partida (si/no): ")   
        if reiniciar == "si":
            juego(dicc_por_letras,dicc_definiciones,partidas_jugadas,config,lista_jugadores)
            partidas_jugadas+=1    
        else:
            print("Reporte Final:")
            print("Partidas jugadas: ",partidas_jugadas)
            print("")
            print("")
            print("")
            print("Puntajes Totales")
            print("")
            i=1
            for jugador in lista_jugadores:
                print(i,".", jugador[NOMBRE], " - ", jugador[PUNTAJE], " puntos")
                i+=1
    else:
        print("Reporte Final:")
        print("Partidas jugadas: ",partidas_jugadas)
        print("")
        print("")
        print("")
        print("Puntajes Totales")
        print("")
        i=1
        for jugador in lista_jugadores:
            print(i,".", jugador[NOMBRE], " - ", jugador[PUNTAJE], " puntos")
            i+=1
    return partidas_jugadas    
        
def parciales(jugadores):
    #Funcion que muestra los aciertos y errores de cada jugador en el transcurso del juego.
    print("Jugadores:")
    i=1
    for jugador in jugadores:
        print(i,".",jugador[NOMBRE],"- Aciertos:", jugador[ACIERTOS], "- Errores:", jugador[ERRORES])
        i+=1

def asignacion_turnos(jugadores):
    #Funcion que asigna los turnos al inicio de la partida.
    random.shuffle(jugadores)
    i=1
    for jugador in jugadores:
        print("El jugador numero:", i ,"es:", jugador[NOMBRE])
        i+=1

def validar_entrada(teclado,palabra):
    #Funcion que valida que la palabra ingresada tenga la longitud correcta y este formada por letras.
    valor=False
    i=0
    if len(palabra)==len(teclado):
        valor=True
        while len(teclado)>i and valor:
            if not teclado[i].isalpha():
                valor=False
            i+=1
    return valor

def roscos(caracteres):
    #Funcion que recibe una lista e imprime una cadaena con el formato del rosco.
    cadena=""
    for caracter in caracteres:
        cadena += "[" + caracter + "]"
    return cadena

def separador():
    #separador
    separador="="
    print(separador*50)
    for i in range(0,5):
        print("")

#--------------------------------------------------------------------------------------------

def juego(dicc_por_letras,dicc_definiciones,partidas_jugadas,config,lista_jugadores):
    letras_elegidas=seleccionar_letras(config[1])
    palabras_seleccionadas=seleccionar_palabras(letras_elegidas,dicc_por_letras)
    letras=roscos(letras_elegidas)
    rosco=pasapalabra(letras,palabras_seleccionadas,dicc_definiciones,lista_jugadores)
    lista_resumen=resumen(palabras_seleccionadas,rosco[0],rosco[1],rosco[2],config[3],config[4])
    partidas_jugadas=volver_a_jugar(dicc_por_letras,dicc_definiciones,lista_resumen,partidas_jugadas,config[2],config)

def main(lista_jugadores):
    config=leer_config()
    dicc_definiciones=leer_archivos(config[0])
    palabras_dicc=lista_palabras(dicc_definiciones)
    crear_archivo_dicc(palabras_dicc,dicc_definiciones)
    dicc_por_letras=diccionario_por_letras(palabras_dicc)
    palabras_por_letra(dicc_por_letras)
    juego(dicc_por_letras,dicc_definiciones,partidas_jugadas,config,lista_jugadores)

iniciar_sesion()