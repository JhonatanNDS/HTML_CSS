from tkinter import *
from tkinter.ttk import *

janela = Tk()
janela.title('primeiro checkbutton')
janela.geometry('400x300')

def test():
    print('valor do checkbutton:', estado.get())

estado = StringVar()

check = Checkbutton(janela, text='escolha', var=estado, onvalue="ativado", offvalue='desativado',command=test)
check.place(x=100,y=100)
estado.set('desativado')

janela.mainloop()