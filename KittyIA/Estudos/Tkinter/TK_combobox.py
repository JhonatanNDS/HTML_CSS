from tkinter import *
from tkinter.ttk import *

#cria a janela
janela = Tk()
janela.title("Criando Combobox")
janela.geometry('400x400')

#cria a combobox
combo = Combobox(janela)
combo['values']= ('pedro','marcos','joao','maria')
combo.current(0)
combo.grid(row=0, column=0)

#obtem o item selecionado
def obter(eventObject):
    label = Label(janela, text=combo.get())
    label.grid(row=1, column=0)

combo.bind('<<ComboboxSelected>>',obter)
janela.mainloop()