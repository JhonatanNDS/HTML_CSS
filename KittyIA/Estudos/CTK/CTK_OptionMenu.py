import customtkinter as ct

janela = ct.CTk()
janela.geometry('700x500')
janela.title('Aula CustomTkinter')
janela.resizable(width=False,height=False)

ct.CTkLabel(janela, text='Menu de opçoes',font=('arial bold',20)).pack(pady=20,padx=5)
ct.CTkLabel(janela, text='Escolha o seu mes de nascimento:',font=('arial bold', 14)).pack()

def msec(escolha):
    print(escolha)

mes = ct.CTkOptionMenu(janela,
                 values=['Janeiro','Fevereiro',"Março",'Abril','maio','junho','julho'
                         ,'agosto','setembro','outubro','novembro','dezembro'],command=msec)

mes.pack(pady=10)
mes.set('Mes de nascimento')



janela.mainloop()