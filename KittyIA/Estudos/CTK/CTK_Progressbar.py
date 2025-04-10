import customtkinter as ct

janela = ct.CTk()
janela.geometry('1000x700')
janela.title('Progressbar')
janela.resizable(width=False,height=False)


progressbar = ct.CTkProgressBar(janela,width=250,height=10,corner_radius=30,progress_color='red')
progressbar.pack(pady=20)

progressbar.start()
#progressbar.step()
#progressbar.stop()
janela.mainloop()