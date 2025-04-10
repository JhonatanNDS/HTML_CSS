from tkinter import *

janela = Tk()
janela.geometry('800x500')

a = Button(janela, text='Usando place')
a.place(x=100,y=100)

b = Button(janela, text='Usando place')
b.place(x=200,y=200)

janela.mainloop()