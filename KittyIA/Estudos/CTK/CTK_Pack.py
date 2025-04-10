import customtkinter as ctk
janela = ctk.CTk()
janela.geometry('400x647')
janela.title('Login')

ctk.CTkLabel(janela,text='Login',font=('arial bold',15)).pack(pady=6)
#ctk.CTkLabel(janela,text='Usuario',font=('arial bold',15)).pack(pady=20,padx=15)
#ctk.CTkLabel(janela,text='Senha',font=('arial bold',15)).pack(pady=40)

ctk.CTkEntry(janela,placeholder_text='Username...',width=200,height=35).pack()
ctk.CTkEntry(janela,placeholder_text='Password...',width=200,height=35,show='*').pack(pady=15)
ctk.CTkButton(janela,text='LOGIN',width=200,height=35).pack()

janela.mainloop()