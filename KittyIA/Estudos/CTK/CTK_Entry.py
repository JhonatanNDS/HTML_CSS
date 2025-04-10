import customtkinter as ctk
from tkinter import *

janela = ctk.CTk()
janela.geometry('700x500')
janela.title('Entry')
janela.resizable(width=True,height=True)

#criacao da entry
entry = ctk.CTkEntry(janela,width=200,placeholder_text='digite um texto')
entry.pack(pady=15)

#pegar o conteudo da entry
def texto_digitado():
    print(entry.get())
    #limpar a entry(tem que usar o tkinter)
    entry.delete(0, END)

btn = ctk.CTkButton(janela,text='Enviar',width=75, command=texto_digitado).pack(pady=20)


janela.mainloop()