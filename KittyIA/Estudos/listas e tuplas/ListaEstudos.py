#inserir um  elemnto na lista
lista = ['hoje','ola','leao','fim','amanha','pc']
lista.insert(0,'voce')

#deletarum elemento por index
del lista[2]

#deletar pelo elemento
lista.remove('leao')

#deletaro ultimo elemento
lista.pop()

#criar uma lista com range
valores = list(range(4,11))
print(valores)

#organizar elemntos de uma lista
numeros = [4,6,3,8,2,1]
numeros.sort()  #numeros.sort(reverse=True) ordena ao contrario
print(numeros)

