from tkinter import *
from tkinter import ttk

class InterfazDeVentana:

  def __init__(self,ventana):
    self.ventana = ventana
    self.productos = ("Dulces-$1","Jugos-$5","agua-$6","papel-$3","chocolates-$7","chorizo-$18","cocacola-$10","aceite-$12","azucar-$7")
    self.cantidad = IntVar()
    self.cajatotal = IntVar()
    self.total = 0
    self.dibujarComponentes()

  def dibujarComponentes(self):
    self.ventana.title("caja registradora")
    self.ventana.geometry("650x450")
    Label(self.ventana,text="selecciona tu producto").place(x=10,y=10)
    Label(self.ventana,text="selecciona la cantidad").place(x=10,y=60)
    Label(self.ventana,text="el total es:").place(x=400,y=400)
    self.combo = ttk.Combobox(self.ventana,state="readonly")
    self.combo.place(x=10,y=35)
    self.combo["values"]=self.productos
    self.combo.current(0)
    Entry(self.ventana,textvariable=self.cantidad).place(x=10,y=85)
    Entry(self.ventana,textvariable=self.cajatotal).place(x=470,y=400)
    Button(self.ventana,text="Agregar",command=self.agregarProducto).place(x=10,y=110)
    
    self.tabla = ttk.Treeview(self.ventana,columns=("Cantidad","Subtotal"))
    self.tabla.heading("#0",text="Producto")
    self.tabla.heading("Cantidad",text="Cantidad")
    self.tabla.heading("Subtotal",text="Subtotal")
    self.tabla.place(x=10,y=150)

  def agregarProducto(self):
    texto = self.combo.get()
    datos = texto.split("-$")
    producto = datos[0]
    precio = datos [1]
    cantidad = self.cantidad.get ()
    subtotal = int(precio)*int(cantidad)
    self.tabla.insert("",END,text=producto,values=(cantidad, "$"+str(subtotal)))
    self.total = self.total + subtotal
    self.cajatotal.set("$"+str(self.total))

obj = InterfazDeVentana(Tk())
obj.ventana.mainloop()