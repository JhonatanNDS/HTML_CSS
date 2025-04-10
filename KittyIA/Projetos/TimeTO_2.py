from tkinter import *
from tkinter.ttk import *
from datetime import datetime, timedelta

# Listas para os valores dos combobox
lista_ano = list(range(2025, 1900, -1))
lista_mes = list(range(12, 0, -1))
lista_dia = list(range(31, 0, -1))
lista_hora = list(range(23, -1, -1))
lista_minuto = list(range(59, -1, -1))
lista_segundo = list(range(59, -1, -1))

# Data inicial
lista_data = [2025, 12, 31, 0, 0, 0]

# Criar janela
janela = Tk()
janela.geometry("800x600")
janela.title("TIMETO")

# Labels
descricao = Label(janela, text='QUANTO TEMPO ATÉ:')
descricao.place(x=330, y=16)
data_texto = Label(janela, text='DATA:')
data_texto.place(x=210, y=82)

# Labels dos campos
Label(janela, text='ano').place(x=260, y=60)
Label(janela, text='mes').place(x=308, y=60)
Label(janela, text='dia').place(x=355, y=60)
Label(janela, text='hora').place(x=397, y=60)
Label(janela, text='min').place(x=442, y=60)
Label(janela, text='seg').place(x=487, y=60)

#labels da semana
lista_cond = ['nao informar','informar']
Label(janela, text='Informar dia da semana').place(x=650, y=60)
dia_semana_cond = Combobox(janela, width=12, values=lista_cond)
dia_semana_cond.current(0)
dia_semana_cond.place(x=650,y=80)


# Label para exibir a diferença
dif_exibicao = Label(janela, text='')
dif_exibicao.place(x=150, y=140)

# Combobox para seleção dos valores
ano = Combobox(janela, width=4, values=lista_ano)
ano.current(0)
ano.place(x=250, y=80)

mes = Combobox(janela, width=3, values=lista_mes)
mes.current(0)
mes.place(x=300, y=80)

dia = Combobox(janela, width=3, values=lista_dia)
dia.current(0)
dia.place(x=345, y=80)

hora = Combobox(janela, width=3, values=lista_hora)
hora.current(23)
hora.place(x=390, y=80)

minuto = Combobox(janela, width=3, values=lista_minuto)
minuto.current(59)
minuto.place(x=435, y=80)

segundo = Combobox(janela, width=3, values=lista_segundo)
segundo.current(59)
segundo.place(x=480, y=80)

# Funções para atualizar a lista_data com os valores selecionados
def obter_ano(eventObject): lista_data[0] = int(ano.get())
def obter_mes(eventObject): lista_data[1] = int(mes.get())
def obter_dia(eventObject): lista_data[2] = int(dia.get())
def obter_hora(eventObject): lista_data[3] = int(hora.get())
def obter_minuto(eventObject): lista_data[4] = int(minuto.get())
def obter_segundo(eventObject): lista_data[5] = int(segundo.get())

# Bind para capturar mudanças nos combobox
ano.bind('<<ComboboxSelected>>', obter_ano)
mes.bind('<<ComboboxSelected>>', obter_mes)
dia.bind('<<ComboboxSelected>>', obter_dia)
hora.bind('<<ComboboxSelected>>', obter_hora)
minuto.bind('<<ComboboxSelected>>', obter_minuto)
segundo.bind('<<ComboboxSelected>>', obter_segundo)

# Função para formatar a diferença no formato desejado
def formatar_diferenca(diferenca):
    total_segundos = int(abs(diferenca.total_seconds()))

    anos = total_segundos // (365 * 24 * 3600)
    total_segundos %= (365 * 24 * 3600)

    meses = total_segundos // (30 * 24 * 3600)  # Aproximação de meses
    total_segundos %= (30 * 24 * 3600)

    dias = total_segundos // (24 * 3600)
    total_segundos %= (24 * 3600)

    horas = total_segundos // 3600
    total_segundos %= 3600

    minutos = total_segundos // 60
    segundos = total_segundos % 60

    return f"{anos} anos, {meses} meses, {dias} dias, {horas} horas, {minutos} minutos e {segundos} segundos"

# Função para calcular a diferença de tempo
def diferenca_tempo():
    # Converter a lista para inteiros e criar um objeto datetime
    ano, mes, dia, hora, minuto, segundo = map(int, lista_data)
    data_fornecida = datetime(ano, mes, dia, hora, minuto, segundo)

    # Data e hora atuais
    agora = datetime.now()

    # Diferença entre as datas
    diferenca = data_fornecida - agora

    # Formatar a diferença no formato desejado
    diferenca_formatada = formatar_diferenca(diferenca)

    # Exibir a mensagem correta no Label
    if diferenca.total_seconds() > 0:
        mensagem = f"Falta {diferenca_formatada} para a data informada!"
    else:
        mensagem = f"Se passou {diferenca_formatada} da data informada!"

    dif_exibicao.configure(text=mensagem)

# Botão para calcular a diferença
bot_cal = Button(janela, text='Calcular', command=diferenca_tempo)
bot_cal.place(x=560, y=79)

# Rodar a interface gráfica
janela.mainloop()
