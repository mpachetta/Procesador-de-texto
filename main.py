from tkinter import *
from tkinter import scrolledtext

from tkinter.filedialog import askopenfilename, asksaveasfilename
import sys
from tkinter import filedialog as fd
from tkinter import messagebox as mb
from tkinter import messagebox as mb

        
        
root=Tk()
root.title("Trazo")
#root.iconbitmap("icono.ico")
root.geometry("800x600")
root.config(bg="white")





#página
letter=25
fuente="Arial"

pagina=scrolledtext.ScrolledText(font=(fuente,letter))
pagina.config(bg="white")
pagina.config(width="800",height="600",bd="3",relief="groove")


#Barra de herramientas

barra_herramientas=Frame()
barra_herramientas.config(bg="gray")
barra_herramientas.config(width="800")


#imagenes para botones
img_aumentar=PhotoImage(file="aumenta-el-tamano-de-la-fuente.png")
img_achicar=PhotoImage(file="disminuir-el-tamano-de-la-fuente.png")
img_copiar=PhotoImage(file="copiar.png")
img_pegar=PhotoImage(file="pegar.png")
img_minusculas=PhotoImage(file="minusculas.png")
img_mayusculas=PhotoImage(file="mayusculas.png")
img_fondo_negro=PhotoImage(file="carta-a.png")
img_fondo_blanco=PhotoImage(file="carta-a2.png")

img_abrir_archivo=PhotoImage(file="open-folder.png")
img_nuevo_archivo=PhotoImage(file="new folder.png")
img_guardar_archivo=PhotoImage(file="guardar-el-archivo.png")



#funciones botones

def tipoFuente_roman():
    global fuente
    fuente="Times New Roman"
    pagina.config(font=(fuente,letter))
    
def tipoFuente_arial():
    global fuente
    fuente="Arial"
    pagina.config(font=(fuente,letter))
    
def tipoFuente_comic():
    global fuente
    fuente="Comic Sans MS"
    pagina.config(font=(fuente,letter))
    
def tipoFuente_impact():
    global fuente
    fuente="Impact"
    pagina.config(font=(fuente,letter))
    
        
def fondoNegro():
    pagina.config(bg="black",fg="white")
    
def fondoBlanco():
    pagina.config(bg="white",fg="black")
    
def aumentarLetra():
    global letter, fuente
    letter+=2
    pagina.config(font=(fuente,letter))

    

    
def disminuirLetra():
    global letter, fuente
    letter-=2
    pagina.config(font=(fuente,letter))
    
def copiar():
    pagina.event_generate("<<Copy>>")
def pegar():
    pagina.event_generate("<<Paste>>")
    

    
    
    
def NuevoArchivo():

       
    pagina.delete(1.0,END)
    print("New File!")
    
def AbrirArchivo():
  
    filename = askopenfilename(initialdir="C:/",filetypes=[("Archivos de texto","*.txt"),("Word",".doc")])
    text1 = open(filename)
    
    read_file = text1.read()
    pagina.insert(1.0,read_file)
    text1.close()
    
def About():
    
    mb.showinfo("Trazo","Trazo es un bloc de notas simple con fines educativos creado por Martín Pachetta ")
    
def GuardarArchivo():
        nombrearch=fd.asksaveasfilename(initialdir = "C:/",title = "Guardar como",defaultextension=".txt",filetypes = (("Archivos de texto","*.txt"),("Word",".doc"),("Todos los archivos","*.*")))
        if nombrearch!='':
            archi1=open(nombrearch, "w", encoding="utf-8")
            archi1.write(pagina.get("1.0", END))
            global guardado
            guardado=True
            global text
            text=""
            print(text)
            archi1.close()
            mb.showinfo("Información", "Los datos fueron guardados en el archivo.")


 
        


#botones barra de herramientas

frm_herram_archivo=Frame(barra_herramientas,padx=6,pady=2,relief="sunken",bg="gray")
frm_herram_fondo=Frame(barra_herramientas,padx=6,pady=2,relief="sunken",bg="gray")
frm_herram_edicion=Frame(barra_herramientas,padx=6,pady=2,relief="sunken",bg="gray")
frm_herram_tamano=Frame(barra_herramientas,padx=6,pady=2,relief="sunken",bg="gray")
frm_herram_tipo=Frame(barra_herramientas,padx=6,pady=2,relief="sunken",bg="gray")


label_herram_archivo=Label(frm_herram_archivo,text="Archivo",bg="gray",fg="white")
label_herram_fondo=Label(frm_herram_fondo,text="Fondo",bg="gray",fg="white")
label_herram_edicion=Label(frm_herram_edicion,text="Editar",bg="gray",fg="white")
label_herram_tamano=Label(frm_herram_tamano,text="Tamaño",bg="gray",fg="white")
label_herram_tipo=Label(frm_herram_tipo,text="Fuente",bg="gray",fg="white")


btn_aumentar_tamaño_letra=Button(frm_herram_tamano,image=img_aumentar,command=aumentarLetra)
btn_disminuir_tamaño_letra=Button(frm_herram_tamano,image=img_achicar,command=disminuirLetra)



btn_archivo_abrir=Button(frm_herram_archivo,image=img_abrir_archivo,command=AbrirArchivo)
btn_archivo_guardar=Button(frm_herram_archivo,image=img_guardar_archivo,command=GuardarArchivo)
btn_archivo_nuevo=Button(frm_herram_archivo,image=img_nuevo_archivo,command=NuevoArchivo)
btn_fondo_negro=Button(frm_herram_fondo,image=img_fondo_negro,command=fondoNegro)
btn_fondo_blanco=Button(frm_herram_fondo,image=img_fondo_blanco,command=fondoBlanco)

btn_copiar=Button(frm_herram_edicion,image=img_copiar,command=copiar)
btn_pegar=Button(frm_herram_edicion,image=img_pegar,command=pegar)

btn_fuente_serif=Button(frm_herram_tipo,text="Abc",font=("Times New Roman",11),command=tipoFuente_roman)
btn_fuente_sanserif=Button(frm_herram_tipo,text="Abc",font=("Arial",11),command=tipoFuente_arial)
btn_fuente_comic=Button(frm_herram_tipo,text="Abc",font=("Comic Sans MS",10),command=tipoFuente_comic)
btn_fuente_impact=Button(frm_herram_tipo,text="Abc",font=("Impact",11),command=tipoFuente_impact)


#empaquetado

barra_herramientas.pack(fill="x")
pagina.pack(fill="both",expand=True)
frm_herram_archivo.grid(row=0,column=0)
frm_herram_fondo.grid(row=0,column=1)
frm_herram_edicion.grid(row=0,column=2)
frm_herram_tamano.grid(row=0,column=3)
frm_herram_tipo.grid(row=0,column=4)


label_herram_archivo.grid(row=0,column=0,columnspan=3)
label_herram_fondo.grid(row=0,column=0,columnspan=2)
label_herram_edicion.grid(row=0,column=0,columnspan=2)
label_herram_tamano.grid(row=0,column=0,columnspan=2)
label_herram_tipo.grid(row=0,column=0,columnspan=4)

btn_archivo_nuevo.grid(row=1,column=0)
btn_archivo_abrir.grid(row=1,column=1)
btn_archivo_guardar.grid(row=1,column=2)

btn_aumentar_tamaño_letra.grid(row=1,column=0)
btn_disminuir_tamaño_letra.grid(row=1,column=1)


btn_fondo_negro.grid(row=1,column=0)
btn_fondo_blanco.grid(row=1,column=1)

btn_copiar.grid(row=1,column=0)
btn_pegar.grid(row=1,column=1)

btn_fuente_serif.grid(row=1,column=1)
btn_fuente_sanserif.grid(row=1,column=0)
btn_fuente_comic.grid(row=1,column=2)
btn_fuente_impact.grid(row=1,column=3)



#menu





menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label="Archivo", menu=filemenu)
filemenu.add_command(label="Nuevo", command=NuevoArchivo)
filemenu.add_command(label="Abrir", command=AbrirArchivo)
filemenu.add_command(label="Guardar", command=GuardarArchivo)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)

helpmenu = Menu (menu)
menu.add_cascade(label="Ayuda", menu=helpmenu)
helpmenu.add_command(label="Acerca de...", command=About)




root.mainloop()

#botones para subrayar y negritas y fondo negro
#crear frames dentro de la barra que agrupen a los botones
#botones para abrir y guardar

