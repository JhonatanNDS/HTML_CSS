import widgethud as wg
import FunctionsGe as fg

wg.cabecalho()

while True:
    wg.opcoes_de_gerenciamento()
    while True:
        try:
            escolha = int(input('Qual sua escolha: '))
            break
        except:
            print("escolha invalida, escolha uma opçao valida")

    if escolha == 1:
        fg.exibir_diretorios()

    if escolha == 2:
        fg.criar_pasta()
    if escolha == 3:
        fg.excluir_pasta()
    if escolha == 4:
        print('Gerenciador encerrado!!!')
        break
    else:
        print("Digite uma opcao valida")