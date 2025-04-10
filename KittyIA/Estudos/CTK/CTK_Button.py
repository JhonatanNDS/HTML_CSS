import customtkinter as ct

janela = ct.CTk()
janela.geometry('700x500')
janela.title('Button')
janela.resizable(width=True,height=True)

def evento():
    print('O botao foi clicado')

btn = ct.CTkButton(janela,text='clique em mim!',command=evento,width=333,height=33,).pack(pady=7)

janela.mainloop()