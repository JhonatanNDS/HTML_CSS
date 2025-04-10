from tkinter import *
from datetime import datetime

# Criacao da janela
janela = Tk()
janela.geometry('800x500')
janela.title('Dia da Semana')

# Titulo
titulo = Label(janela, text='ME DE UMA DATA E RETORNAREI O DIA DA SEMANA DELA!', fg='green')
titulo.pack(side=TOP)

# Função para adicionar placeholder no campo de entrada
def on_focus_in(event):
    if data_entrada.get() == "AAAA/MM/DD":
        data_entrada.delete(0, "end")
        data_entrada.config(fg="black")

def on_focus_out(event):
    if data_entrada.get() == "":
        data_entrada.insert(0, "AAAA/MM/DD")
        data_entrada.config(fg="gray")

# Caixa de entrada com placeholder
data_entrada = Entry(janela, width=15, fg="gray")
data_entrada.place(x=360, y=28)
data_entrada.insert(0, "AAAA/MM/DD")  # Placeholder inicial
data_entrada.bind("<FocusIn>", on_focus_in)
data_entrada.bind("<FocusOut>", on_focus_out)

data_text = Label(janela, text='DATA:')
data_text.place(x=315, y=27)

# Label para exibir resultado
resultado_label = Label(janela, text='')
resultado_label.place(x=280, y=70)

def proc_data():
    try:
        conteudo = datetime.strptime(data_entrada.get(), "%Y/%m/%d").date()
        dias_semana = ['Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sábado', 'Domingo']
        resultado = dias_semana[conteudo.weekday()]
        resultado_label.config(text=f'A data {conteudo} corresponde a: {resultado}', fg='blue')
    except ValueError:
        resultado_label.config(text='Formato inválido! Use AAAA/MM/DD', fg='red')

# Botao
botao = Button(janela, text='Informar', fg='white', bg='green', command=proc_data)
botao.place(x=470, y=23)

janela.mainloop()
