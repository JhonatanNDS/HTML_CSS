import customtkinter as ct

janela = ct.CTk()
janela.geometry('700x500')
janela.title('Aula CustomTkinter')
janela.resizable(width=True,height=True)

def nova_tela():
    janela2 = ct.CTkToplevel(janela, fg_color='green')
    janela2.geometry('500x250')

btn_nova_tela = ct.CTkButton(master=janela, text='Abrir nova janela',command=nova_tela).place(x=300,y=100)

janela.mainloop()