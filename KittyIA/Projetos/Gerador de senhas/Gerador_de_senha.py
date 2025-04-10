import random
import string
import customtkinter as ctk
from tkinter import messagebox
from PIL.ImageOps import expand

def gerar_senha():
    try:
        comprimento = int(entry_comprimento.get())
        if comprimento <= 0:
            raise  ValueError('O comprimento deve ser maior que 0')
    except ValueError:
        messagebox.showerror('Erro','Digite um numero valido para o comprimento da senha!')
        return
    caracteres = ''
    if checkbox_letras.get():
        caracteres += string.ascii_letters
    if checkbox_numeros.get():
        caracteres += string.digits
    if checkbox_simbolos.get():
        caracteres += "!@#$%&*+=-_"
    if not caracteres:
        messagebox.showwarning("Aviso",'Selecione ao menos um tipo de caracter!')
        return
    senha = ''.join(random.choice(caracteres) for _ in range(comprimento))
    entry_senha.delete(0,ctk.END)
    entry_senha.insert(0,senha)

def guardar_senha():
   nome_serviço = entry_servico.get()
   senha = entry_senha.get()

   if not nome_serviço:
       messagebox.showerror("ERRO",'Digite um serviço!')
       return
   if not senha:
       messagebox.showerror("ERRO",'Nenhuma senha para ser gerada!')

   nome_arquivo ='senhas.txt'
   with open(nome_arquivo,'a') as arquivo:
       arquivo.write(f'{nome_serviço}: {senha}\n')
   messagebox.showinfo('Sucesso',f'Senha salva para o serviço: {nome_serviço}.')

def copiar_senha():
    senha = entry_senha.get()
    if senha:
        root.clipboard_clear()
        root.clipboard_append(senha)
        root.update()
        messagebox.showinfo('Sucesso', 'Senha copiada para area de transferencia!')
    else:
        messagebox.showwarning("Aviso",'Nenhuma senha gerada para ser copiada!')

def limpar():
    entry_comprimento.delete(0,ctk.END)
    entry_servico.delete(0,ctk.END)
    entry_senha.delete(0,ctk.END)
    checkbox_letras.select()
    checkbox_numeros.select()
    checkbox_simbolos.select()


#primeira janela
root = ctk.CTk()
root.title('Gerador de senhas!')
root.geometry('580x600')
root.resizable(width=False,height=False)


#titulo
ctk.CTkLabel(root,text='Gerador de senhas',font=('bold',17)).pack(pady=20,padx=20)
#frame
frame = ctk.CTkFrame(root)
frame.pack(padx=20,fill='both',expand=True)
#rodape
ctk.CTkLabel(root,text='Desenvolvido por Jhonatannds -2025').pack(pady=20)

#widgets dentro do frame
#cumprimento de senha
label_comprimento = ctk.CTkLabel(frame,text='Cumprimento da senha:')
label_comprimento.grid(row=0,column=0,pady=(10,0),padx=(20,5),sticky='w')
entry_comprimento = ctk.CTkEntry(frame,width=200)
entry_comprimento.grid(row=1,column=0,pady=(0,10),padx=(20,5),sticky='w')

#mome do serviço
label_servico = ctk.CTkLabel(frame,text='Nome do serviço:')
label_servico.grid(row=0,column=1,pady=(10,0),padx=(5,20),sticky='w')
entry_servico = ctk.CTkEntry(frame,width=200)
entry_servico.grid(row=1,column=1,columnspan=2,pady=(0,10),padx=(5,20),sticky='ew')

#tipos de caracteres
checkbox_letras = ctk.CTkCheckBox(frame,text='Incluir letras')
checkbox_letras.grid(row=2,column=0,pady=(10),padx=(5,5),sticky='w')
checkbox_letras.select()

checkbox_numeros = ctk.CTkCheckBox(frame,text='Incluir numeros')
checkbox_numeros.grid(row=2,column=1,pady=(10),padx=(5,5),sticky='w')
checkbox_numeros.select()

checkbox_simbolos = ctk.CTkCheckBox(frame,text='Incluir simbolos')
checkbox_simbolos.grid(row=2,column=2,pady=(10),padx=(5,5),sticky='w')
checkbox_simbolos.select()

#senha gerada
label_senha = ctk.CTkLabel(frame,text='Senha gerada:')
label_senha.grid(row=3,column=0,pady=(30,0),padx=(5,20),sticky='w')
entry_senha = ctk.CTkEntry(frame,width=200,font=('bold',15))
entry_senha.grid(row=4,column=0,columnspan=3,pady=(0,30),padx=20,sticky='ew')

#botoes
button_gerar = ctk.CTkButton(frame,text='Gerar senha',command=gerar_senha)
button_gerar.grid(row=5,column=0,pady=10,padx=(20,5),sticky='ew')

button_salvar = ctk.CTkButton(frame,text='Guardar senha',command=guardar_senha)
button_salvar.grid(row=5,column=1,pady=10,padx=(5,5),sticky='ew')

button_copiar = ctk.CTkButton(frame,text='Copiar senha',command=copiar_senha)
button_copiar.grid(row=5,column=2,pady=10,padx=(5,20),sticky='ew')

button_limpar = ctk.CTkButton(frame,text='Limpar campos',command=limpar)
button_limpar.grid(row=6,column=0,columnspan=3,pady=10,padx=(5,5),sticky='ew')

root.mainloop()