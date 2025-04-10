import customtkinter as ctk

janela = ctk.CTk()
janela.geometry('700x400')
janela.title('Aula CustomTkinter')
janela.resizable(width=True,height=True)

#label estatica(definido por codigo)
ctk.CTkLabel(janela,text='Texto estatico!',font=('arial bond',15)).pack()

janela.mainloop()