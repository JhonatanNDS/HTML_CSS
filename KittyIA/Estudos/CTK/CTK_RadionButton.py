import customtkinter as ct
from PIL import Image

janela = ct.CTk()
janela.geometry('1000x700')
janela.title('RadioButton')
janela.resizable(width=False,height=False)

radio_var = ct.IntVar(value=0)
def funcao():
    print(radio_var.get())

radio1 = ct.CTkRadioButton(janela, text='Masculino',command=funcao,variable=radio_var, value=1)
radio2 = ct.CTkRadioButton(janela, text='Feminino',command=funcao,variable=radio_var, value=2)

radio1.pack()
radio2.pack(pady=8)

janela.mainloop()