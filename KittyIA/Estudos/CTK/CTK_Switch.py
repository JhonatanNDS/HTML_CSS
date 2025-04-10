import customtkinter as ct
from PIL import Image

janela = ct.CTk()
janela.geometry('1000x700')
janela.title('Switch')
janela.resizable(width=False,height=False)

switch_var = ct.StringVar(value='on')

def funcao():
    if switch_var.get() == 'ativado':
        ct.set_appearance_mode('Light')
    elif switch_var.get() == 'desativado':
        ct.set_appearance_mode('Dark')
    else:
        ct.set_appearance_mode('System')

switch = ct.CTkSwitch(janela,text='Switch',command=funcao,variable=switch_var,onvalue='ativado',offvalue='deativado')
switch.pack(pady=30)

janela.mainloop()