from tkinter import *

janela = Tk()
janela.title('Botao e label')
janela.geometry('800x500')

label = Label(janela, text='Clique no botao')
label.grid(column=0,row=0)

def ola():
    label.configure(text='Ola jhonatan')

botao = Button(janela, text="Botao clicavel",fg='green',command=ola)
botao.grid(column=1,row=0)

janela.mainloop()
