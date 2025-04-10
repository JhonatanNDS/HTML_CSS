import customtkinter as ct

janela = ct.CTk()
janela.geometry('700x400')
janela.title('Aula CustomTkinter')
janela.resizable(width=False,height=False)

textbox = ct.CTkTextbox(janela,width=300,height=350,scrollbar_button_color='green',scrollbar_button_hover_color='green')
textbox.pack()

textbox.insert('0.0','titilo do seu texto\n\n' + 'ola estou aprendendo customtkinter no youtube,'
                                                 ' estou indo bem, os arcontes nao me atrapalhao'*20)
janela.mainloop()