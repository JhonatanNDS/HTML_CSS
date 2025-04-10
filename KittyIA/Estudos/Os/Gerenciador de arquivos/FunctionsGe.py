import os
def exibir_diretorios():
    conteudo = os.listdir('.')
    print("="*30)
    print('Este é o conteudo do diretorio')
    for c in conteudo:
        print(c)
    print("="*30)

def criar_pasta():
    while True:
        nome = str(input("nome da pasta:"))
        if not os.path.exists(nome):
            os.mkdir(nome)
            print(f"A pasta {nome} foi criada!")
            cont1 = str(input('voce quer continuar criando uma pasta?(S)Sim (N)Nao:'))
            if cont1 in 'Nn':
                break

        else:
            print("Esta pasta ja existe, escolha outro nome!")
            cont2 = str(input('voce quer continuar criando a pasta?(S)Sim (N)Nao:'))
            if cont2 in 'Nn':
                break

def excluir_pasta():
    while True:
        pasta_exclusao = str(input('Qual pasta deseja excluir?:'))
        if os.path.exists(pasta_exclusao):
            try:
                os.rmdir(pasta_exclusao)
                print(f"Diretório '{pasta_exclusao}' excluído com sucesso!")
                cont3 = str(input('voce quer continuar excluindo uma pasta?(S)Sim (N)Nao:'))
                if cont3 in 'Nn':
                    break
            except:
                print(f"Erro: O diretório '{pasta_exclusao}' não está vazio.")
                cont4 = str(input('voce quer continuar excluindo uma pasta?(S)Sim (N)Nao:'))
                if cont4 in 'Nn':
                    break
        else:
            print(f"Diretório '{pasta_exclusao}' não encontrado.")
            cont5 = str(input('voce quer continuar excluindo uma pasta?(S)Sim (N)Nao:'))
            if cont5 in 'Nn':
                break

