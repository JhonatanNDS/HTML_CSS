import customtkinter as ct

janela = ct.CTk()
janela.geometry('700x500')
janela.title('Aula CustomTkinter')
janela.resizable(width=False,height=False)

def abrir():
    dialog = ct.CTkInputDialog(title='Caixa de dialogo',text='Digite o seu numero de celular:')
    print(dialog.get_input())

btn = ct.CTkButton(janela,text='abri caixa de dialogo!',command=abrir).pack()

janela.mainloop()