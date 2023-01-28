from tkinter import *

root = Tk()
root.title('Моё первое приложение')
root.geometry('600x500')
canvas = Canvas(root, width=400, height=400, bg='navy')
canvas.pack()


def color1():
    canvas.itemconfig(oval, fill='white')


def color2():
    canvas.itemconfig(polygon, fill='orange')


def color3():
    canvas.itemconfig(rectangle, fill='sienna')


rectangle = canvas.create_rectangle(100, 200, 300, 400, width=5, outline='black', fill='saddle brown')
polygon = canvas.create_polygon(100, 200, 200, 100, 300, 200, width=5, outline='black', fill='brown')
oval = canvas.create_oval(350, 10, 300, 50, width=5, outline='black', fill='yellow')
b1 = Button(root, height=3, width=10, text='Солнце', bg='cyan', activebackground='red', command=color1)
b2 = Button(root, height=3, width=10, text='Крыша', bg='cyan', activebackground='red', command=color2)
b3 = Button(root, height=3, width=10, text='Основание', bg='cyan', activebackground='red', command=color3)
b1.pack()
b2.pack()
b3.pack()
root.mainloop()
