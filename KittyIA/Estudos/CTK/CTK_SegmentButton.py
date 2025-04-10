import customtkinter as ct
from PIL import Image

janela = ct.CTk()
janela.geometry('1000x700')
janela.title('SegmentButton')
janela.resizable(width=False,height=False)

def btn(value):
    print(value)

segment = ct.CTkSegmentedButton(janela, values=['tkinter','ola mundo','java','python'], command=btn).pack(pady=20)


janela.mainloop()