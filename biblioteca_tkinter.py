#bibliotecas unidas
import tkinter as tk 
from tkinter import messagebox, Toplevel


#sistema de usuarios

usuario_contraseña = {}
sesion_activa = []


lista_libros = []
libros_prestamo = {}

#ventana princial
ventana = tk.Tk()
ventana.title("BIBLIOTECA")
ventana.geometry("600x350")
ventana.config(background="blue2")

#PAGINA DE INICIO DE SESION 
def iniciar_sesion():    
    #ventana de inicio de sesion 
    pagina_inicio = Toplevel(ventana)
    pagina_inicio.title("INICIO DE SESION")
    pagina_inicio.geometry("300x300")
    pagina_inicio.config(background="blue2")
    
    #mensaje1
    mensaje1 = tk.Label(master= pagina_inicio,text= " USUARIO ", background= "blue",font= "ARIAL 10")
    mensaje1.place(x = 50 , y = 30 )

    #entrada de informaci ( usuario )
    usuario = tk.Entry(pagina_inicio,font=("ARIAL 14"), width = 20)
    usuario.place(x = 50, y = 50 )
    usuario.configure(background= "silver")

    #mensaje2
    mensaje2 = tk.Label(master = pagina_inicio, text= "CONTRASEÑA", background="blue", font="arial 10")
    mensaje2.place(x = 50, y = 90 )

    #entrada de  informacion ( contraseña )
    contraseña = tk.Entry(pagina_inicio, font = ("Arial 14"), width = 20)
    contraseña.place(x = 50, y = 110 )
    contraseña.configure(background= "silver")

    #boton de inicio de sesion 
    usuario_entrada = tk.Button(pagina_inicio, text= "INICIAR SESION", bg = "steel blue", border = 5, command= lambda : verificar_usuario())  
    usuario_entrada.place(x = 100, y = 150 )

    def verificar_usuario():
        valor_usuario = str(usuario.get())
        valor_contraseña = str(contraseña.get())
        if valor_usuario in usuario_contraseña and  valor_contraseña ==  usuario_contraseña[valor_usuario]:
            messagebox.showinfo("SESION INICIADA", "**HAS INICIADO SESION CORRECTAMENTE**")
            pagina_inicio.withdraw()
            sesion_activa.append(valor_usuario)
            messagebox.showinfo("ESTADO SESION", "SESION ACTIVA")
        else:
            messagebox.showinfo("ERROR", "CONTRASEÑA O USUARIO INCORRECTOS")
        usuario.delete(0, 100)
        contraseña.delete(0, 100)

#PAGINA DE REGISTRO DE USUARIOS
def iniciar_registro():
    #VENTANAS 
    register = Toplevel(ventana)
    register.title("REGISTARSE")
    register.geometry("400x400")
    register.config(background= "blue2")

    #REGISTRO

    mensaje1 = tk.Label(master = register,text= "USUARIO", background= "blue", font="ARIAL 10")
    mensaje1.place(x = 50, y = 50)

    usuario = tk.Entry(master= register, font ="ARIAL 10 ", width= 20)
    usuario.place(x = 50, y = 70)

    mensaje2 = tk.Label(master = register, text = "CONTRASEÑA", background= "blue", font= "ARIAL 10" )
    mensaje2.place(x = 50, y = 90)

    contraseña = tk.Entry(master= register, font = "ARIAL 10", width= 20)
    contraseña.place(x = 50, y = 110)

    mensaje3 = tk.Label(master=register, text ="CONFIRMAR CONTRASEÑA", background= "blue", font = "ARIAL 10")
    mensaje3.place(x = 50, y = 130)

    confir_contraseña = tk.Entry(master = register, font = "ARIAL 10 ", width= 20)
    confir_contraseña.place(x = 50, y = 150)

    #BOTON REGISTRO 
    boton_registro = tk.Button(master= register, text = "REGISTRAR USUARIO ", bg = "steel blue", border = 5, command= lambda: registrar_user())
    boton_registro.place(x = 250, y = 100)
    def registrar_user():
        usuario_a_registrar = usuario.get()
        contraseña_a_registrar = contraseña.get()
        confi_contraseña = confir_contraseña.get()
        if usuario_a_registrar in usuario_contraseña:
            messagebox.showinfo("**ALERTA**", "**USUARIO YA REGISTRADO**")
        else:
            if contraseña_a_registrar != confi_contraseña:
                messagebox.showinfo("**ERROR**" , "**LAS CONSTRASEÑAS NO COINCIDEN**")
            else:
                messagebox.showinfo("**EXITO!!**"," USUARIO Y CONTRASEÑA REGISTRADA")
                usuario_contraseña[usuario_a_registrar] = contraseña_a_registrar
                register.withdraw()
                print(usuario_contraseña)
        usuario.delete(0,100)
        confir_contraseña.delete(0,100)
        contraseña.delete(0,100)

    register.mainloop()

def cerrar():
    for widget in ventana.winfo_children():
        if isinstance(widget, Toplevel):
            widget.destroy()
    ventana.destroy()


def pagina_busqueda_libro():
    pagina_busqueda = Toplevel(ventana)
    pagina_busqueda.title("PAGINA DE BUSQUEDA")
    pagina_busqueda.geometry("300x200")
    pagina_busqueda.config(background= "blue2")

    libro_a_buscar = tk.Label(master = pagina_busqueda, text= "TITULO DEL LIBRO", background="blue2", font="ARIAL 15")
    libro_a_buscar.place(x = 50, y = 25)

    libro = tk.Entry(master = pagina_busqueda, font=("ARIAL 15"), width= 20)
    libro.place(x = 40 , y = 50 )

    buscar = tk.Button(master = pagina_busqueda, text="BUSCAR LIBRO", bg= "steel blue", border=5, command= lambda:busqueda())
    buscar.place(x = 100, y = 80)
    
    salida = tk.Button(master=pagina_busqueda, text= "SALIR", bg= "red", border=5, command= pagina_busqueda.withdraw)
    salida.place(x = 120, y = 150)
    
    def busqueda():
        libro1 = libro.get()
        if libro1 in lista_libros:
            messagebox.showinfo("LIBRO ENCONTRADO!!", "HEMOS ENCONTRADO EL LIBRO ,  ESTA DISPONIBLE EN LA LIBRERIA!!")
        elif libro1 in libros_prestamo:
            mss = "EL LIBRO ",libro1, " SE ENCUENTRA EN PRESTAMO POR EL USUARIO", libros_prestamo[libro1]
            messagebox.showinfo("LO LAMENTAMOS MUCHO!!",mss)
        else:
            mss2 = "EL LIBRO ",libro1," NO SE ENCUENTRA EN LA BASE DE DATOS DE LA BILBIOTECA"
            messagebox.showinfo("ALERTA", mss2)



# BOTONES EN PANTALLA 

registrar_user = tk.Button(text="REGISTARSE", bg = "steel blue", border = 5,command = lambda: iniciar_registro())
inicio_sesion = tk.Button(text= "INICIAR SESION", bg = "steel blue", border = 5, command= lambda: iniciar_sesion())
buscar_libro = tk.Button(text= "BUSCAR UN LIBRO", bg = "steel blue", border = 5, command =lambda: pagina_busqueda_libro())
agregar_libro = tk.Button(text= "AGREGAR UN LIBRO", bg = "steel blue", border= 5, command= ventana.destroy)
salir = tk.Button(text = "SALIR", bg = "red", border= 5 , command= lambda: cerrar())

#posicion
registrar_user.place(x =5, y = 5 )
inicio_sesion.place(x = 5, y = 35)
buscar_libro.place(x = 5 , y = 65)
agregar_libro.place(x =5 , y = 95)
salir.place(x = 5, y = 125)

#tamaño
registrar_user.config(width= 25)
inicio_sesion.config(width= 25)
buscar_libro.config(width=25)
agregar_libro.config(width=25)
salir.config(width=25)




ventana.mainloop()



