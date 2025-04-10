from  tkinter import *
from tkinter.ttk import *

janela = Tk()
janela.title('Primeiro radiobutton')
janela.geometry('400x300')

def obter():
    print('O valor do botao selecionado é:',selecionado.get())

selecionado = IntVar()

rad_1 = Radiobutton(janela,text='primeiro', value=1,var=selecionado,command=obter)
rad_1.grid(row=0, column=0)

rad_2 = Radiobutton(janela,text='segundo', value=2,var=selecionado,command=obter)
rad_2.grid(row=1, column=0)

rad_3 = Radiobutton(janela,text='terceiro ', value=3,var=selecionado,command=obter)
rad_3.grid(row=2, column=0)

janela.mainloop()