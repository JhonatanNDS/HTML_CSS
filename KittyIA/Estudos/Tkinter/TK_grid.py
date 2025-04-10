from tkinter import *

janela = Tk()
janela.geometry('300x300')

vermelho = Button(janela, text='vermelho', fg='red')
vermelho.grid(column=1,row=0)

verde = Button(janela, text='verde', fg='green')
verde.grid(column=2,row=0)

azul = Button(janela, text='azul', fg='blue')
azul.grid(column=2,row=2)

janela.mainloop()