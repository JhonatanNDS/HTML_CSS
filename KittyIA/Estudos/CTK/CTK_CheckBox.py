import customtkinter as ct
from PIL import Image

janela = ct.CTk()
janela.geometry('1000x700')
janela.title('CheckBox')
janela.resizable(width=False,height=False)

check_var = ct.StringVar(value='on')
def funcao():
    print(check_var.get())

checkbox = ct.CTkCheckBox(janela,text='CheckBox',variable=check_var,onvalue='ON',offvalue='OFF',command=funcao).pack(pady=20)

janela.mainloop()