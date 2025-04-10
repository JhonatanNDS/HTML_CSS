from tkinter import *

janela = Tk()
janela.geometry('200x200')


vermelho = Button(janela, text='vermelho', fg='red')
vermelho.pack(side=LEFT)

azul = Button(janela, text='azul', fg='blue')
azul.pack(side=TOP)

verde = Button(janela, text='verde', fg='green')
verde.pack(side=RIGHT)

amarelo = Button(janela, text='amarelo', fg='yellow')
amarelo.pack(side=BOTTOM)

janela.mainloop()