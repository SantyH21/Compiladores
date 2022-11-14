import tkinter as tk
#from guiVentanaSimbolos import VentanaSimbolos

def getTexto():
    mensaje = Texto_EntradaTX.get("1.0",'end-1c')
    print(mensaje)

root = tk.Tk()
root.geometry('700x600')
root.geometry("+400+100")
root.title("Analizador Lexico")
root.resizable(True, True)

Cargar_archivos=tk.Button(root, text="Cargar archivo", font=("Italic", 15), bg="LightSkyBlue1", command=getTexto)
Cargar_archivos.place(relx=0.01, rely=0.88, relwidth=0.25, relheight=0.1)


Tabla_de_Simbolos=tk.Button(root, text="Tabla de simbolos", font=("Italic", 15), bg="LightSkyBlue1")
Tabla_de_Simbolos.place(relx=0.375, rely=0.88, relwidth=0.25, relheight=0.1)

Analizar = tk.Button(root, text="Analizar", font=("Italic", 15), bg="LightSkyBlue1")
Analizar.place(relx=0.73, rely=0.88, relwidth=0.25, relheight=0.1)

Texto_EntradaLB=tk.Label(root, text="Texto Entrada", font=("Italic", 12))
Texto_EntradaLB.place(relx=0.01, rely=0.01)

Texto_SalidaLB=tk.Label(root, text="Texto Salida", font=("Italic", 12))
Texto_SalidaLB.place(relx=0.5, rely=0.01)

Texto_EntradaTX=tk.Text(root, font=("Italic", 15))
Texto_EntradaTX.place(relx=0.01, rely=0.05,relwidth=0.45, relheight=0.8)

Texto_SalidaTX=tk.Text(root, font=("Italic", 15))
Texto_SalidaTX.config(state='disabled')
Texto_SalidaTX.place(relx=0.5, rely=0.05,relwidth=0.48, relheight=0.8)



root.mainloop()
