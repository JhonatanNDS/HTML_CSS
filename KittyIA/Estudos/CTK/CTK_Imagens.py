import customtkinter as ct
from PIL import Image

janela = ct.CTk()
janela.geometry('1000x700')
janela.title('Imagens')
janela.resizable(width=False,height=False)

img1 = ct.CTkImage(light_image=Image.open('./1.png'),size=(400,400))
ct.CTkLabel(janela,text=None, image=img1).pack()

janela.mainloop()