import customtkinter as ct

janela = ct.CTk()
janela.geometry('700x400')
janela.title('Aula CustomTkinter')
janela.resizable(width=False,height=False)

tabview = ct.CTkTabview(janela,width=400, corner_radius=20,border_width=2,border_color='blue',fg_color='teal',
                        segmented_button_fg_color='red',segmented_button_selected_color='green',segmented_button_unselected_color='yellow')
tabview.pack()
tabview.add('Nomes')
tabview.add('idades')
tabview.add('genero')
tabview.tab('Nomes').grid_columnconfigure(0, weight=1)
tabview.tab('idades').grid_columnconfigure(0, weight=1)
tabview.tab('genero').grid_columnconfigure(0, weight=1)

#add  elementos na tab
text = ct.CTkLabel(tabview.tab('Nomes'), text='Jhonatan Nunes\nKitty packge\nfausto gsantos\nguts santos')
text.pack()

ida = ct.CTkLabel(tabview.tab('idades'), text='18\n34\n55\n27')
ida.pack()

gen = ct.CTkLabel(tabview.tab('genero'), text='masculino\nfeminino')
gen.pack()
janela.mainloop()