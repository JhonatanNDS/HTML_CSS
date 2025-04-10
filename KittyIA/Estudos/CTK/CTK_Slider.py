import customtkinter as ct
from PIL import Image

janela = ct.CTk()
janela.geometry('1000x700')
janela.title('Slider')
janela.resizable(width=False,height=False)

def slider_value(value):
    print(value)

slider = ct.CTkSlider(janela,from_=0,to=100,command=slider_value,
                      width=500,button_color='red').pack(pady=30)

janela.mainloop()