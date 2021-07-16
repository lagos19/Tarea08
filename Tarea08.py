from tkinter import *

def menu():
    print("App de Formulas matematicas")
    print("En el siguiente diccionario usted, puede visualizar diferentes formulas matematicas como ser:")
    print("1. Teorema de pitagoras")
    print("2. Trapecio Isoceles")
    print("3. Ecuacion cuadratica ")
    print("4. Limite de una susecion")
    print("5. Integral de una funcion real")
    print("6. Salir")
    op = input ("Escriba la opcion:")
    op = int(op)
    if op==1: Teorema()
    elif op==2: Trapecio()
    elif op==3: cuadratica()
    elif op==4: limite_susecion()
    elif op==5: integral()
    else: exit()

def Teorema():
    ventana = Tk("Teorema de pitagoras")
    ventana.title("Teorema de pitagoras")
    img = PhotoImage(file="Teorema.png")
    widget = Label(ventana, image=img).pack()
    ventana.mainloop()
    menu()

def Trapecio():
    ventana = Tk("Trapecio Isoceles")
    ventana.title("Trapecio Isoceles")
    img = PhotoImage(file="Trapecio.png")
    widget = Label(ventana, image=img).pack()
    ventana.mainloop()
    menu()

def cuadratica():
    ventana = Tk("Ecuacion Cuadratica")
    ventana.title("Ecuacion Cuadratica")
    img = PhotoImage(file="Cuadratica.png")
    widget = Label(ventana, image=img).pack()
    ventana.mainloop()
    menu()

def limite_susecion():
    ventana = Tk("Limite de una susecion")
    ventana.title("Limite de sucesion")
    img = PhotoImage(file="LimiteSucesion.png")
    widget = Label(ventana, image=img).pack()
    ventana.mainloop()
    menu()

def integral():
    ventana = Tk("Integral de una funcion real")
    ventana.title("Integral de una funcion real")
    img = PhotoImage(file="IntegralReal.png")
    widget = Label(ventana, image=img).pack()
    ventana.mainloop()
    menu()
menu()