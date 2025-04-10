from tkinter import *

janela = Tk()
janela.title('Frame')
janela.geometry('600x600')

frane_1 = Frame(janela, width=300, height=300,bg='blue')
frane_1.grid(row=0,column=0)

frane_2 = Frame(janela, width=300, height=300,bg='red')
frane_2.grid(row=0,column=1)

frane_3 = Frame(janela, width=600, height=300,bg='green')
frane_3.grid(row=1,column=0,columnspan=2)

label = Label(frane_1, text='ola mundo',bg='blue',fg='white')
label.place(x=100,y=100)

janela.mainloop()