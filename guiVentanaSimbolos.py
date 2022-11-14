import tkinter as tk

root = tk.Tk()
root.geometry('400x600')
root.geometry("+400+100")
root.title("Ventana Simbolos")
root.resizable(True, True)
Simbolos=tk.Text(root, font=("Italic", 15))
Simbolos.place(relx=0.01, rely=0.05,relwidth=0.98, relheight=0.9)

root.mainloop()