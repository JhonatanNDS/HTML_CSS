from tkinter import *

janela = Tk()
janela.title('ListBox')
janela.geometry('600x400')

listbox = Listbox(janela, height=8)
listbox.place(x=70,y=20)

listbox.insert(0,'php')
listbox.insert(1,'python')
listbox.insert(2,'java')
listbox.insert(END,'c#')

janela.mainloop()