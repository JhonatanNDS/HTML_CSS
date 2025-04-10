a = (1,2,3)
b = (8,5,2,9)
c = a+b

#tamanho da tupla
print(len(c))

#quantas vezes aparece um elemento
print(c.count(2))

#em que posiçao esta um elemento
print(c.index(5))

#deleta uma tupla
del(b)

#maior valor
print(f'O maior valor é {max(c)}')
print(f'O menor valor é {min(c)}')

