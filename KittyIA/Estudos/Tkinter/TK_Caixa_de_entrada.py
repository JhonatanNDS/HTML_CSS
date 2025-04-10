from tkinter import *

janela = Tk()
janela.geometry("400x400")
janela.title('Criando uma Entry')

label_nome = Label(janela, text='Nome:')
label_nome.grid(row=0, column=0)
nome = Entry(janela, width=15)
nome.grid(row=0, column=1)

label_idade = Label(janela, text='Idade:')
label_idade.grid(row=1, column=0)
idade = Entry(janela, width=15)
idade.grid(row=1, column=1)

label_pais = Label(janela, text='País:')
label_pais.grid(row=2, column=0)
pais = Entry(janela, width=15)
pais.grid(row=2, column=1)

def teste():
    n = nome.get()
    i = idade.get()
    p = pais.get()
    label = Label(janela, text=n + ' ' + i + ' ' + p)
    label.grid(row=5,column=0)

b = Button(janela, text='Obter dados digitados!',bg='green', command=teste)
b.grid(row=4, column=0)


janela.mainloop()
