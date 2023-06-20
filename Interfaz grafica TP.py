from tkinter import *

raiz= Tk()
miFrame=Frame(raiz,width=100,height=100)
miFrame.pack()


raiz.title("INGRESO DE JUGADOR")
raiz.resizable(False,False)
raiz.iconbitmap("pasapalabra.ico")
raiz.geometry("350x150")

cuadro_usuario=Entry(miFrame) 
cuadro_usuario.grid(row=0,column=1)

cuadro_clave=Entry(miFrame) 
cuadro_clave.grid(row=1,column=1) 
cuadro_clave.config(show="*")

label_usuario=Label(miFrame, text="Ingrese el usuario: ")
label_usuario.grid(row=0,column=0,pady=5)

label_clave=Label(miFrame, text="Ingrese la clave: ")
label_clave.grid(row=1,column=0)

boton_iniciarsesion=Button(miFrame, text="Iniciar sesion")
boton_iniciarsesion.grid(row=2,column=1,padx=5,pady=10)

boton_empezarjuego=Button(miFrame, text="Empezar juego")
boton_empezarjuego.grid(row=2,column=2,padx=5,pady=10)
#--------------------------------------
def nueva_ventana():
    nueva_ventana=Toplevel()
    nueva_ventana.title("REGISTRO")
    nueva_ventana.iconbitmap("pasapalabra.ico")
    nueva_ventana.geometry("350x150")

    label_usuario_registro=Label(nueva_ventana, text="Ingrese el usuario: ")
    label_usuario_registro.grid(row=0,column=0,pady=5)

    label_clave_registro=Label(nueva_ventana, text="Ingrese la clave: ")
    label_clave_registro.grid(row=1,column=0,pady=5)

    label_confimar_clave_registro=Label(nueva_ventana, text="Confirme clave: ")
    label_confimar_clave_registro.grid(row=2,column=0,pady=5)

    cuadro_usuario_registro=Entry(nueva_ventana) 
    cuadro_usuario_registro.grid(row=0,column=1)
    
    cuadro_clave_registro=Entry(nueva_ventana)
    cuadro_clave_registro.grid(row=1,column=1) 
    cuadro_clave_registro.config(show="*")

    cuadro_confirmar_clave_registro=Entry(nueva_ventana)
    cuadro_confirmar_clave_registro.grid(row=2,column=1) 
    cuadro_confirmar_clave_registro.config(show="*")

    boton_enviar_registro=Button(nueva_ventana,text="Enviar registro ")
    boton_enviar_registro.grid(row=3)

boton_registrarse=Button(miFrame, text="Registrarse",command=nueva_ventana)
boton_registrarse.grid(row=2,column=0,padx=5,pady=10)
#---------------------------------------------


raiz.mainloop()


