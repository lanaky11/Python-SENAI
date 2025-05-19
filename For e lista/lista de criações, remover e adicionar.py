#1 etapa lista.
elementos= ["Cama","travesseiro","mesa","cadeira", "lápis"]
#2 etapa adiciona.
elementos.append("tesoura")
#3 etapa exiba elemento da 2 posição.
print(elementos[1])
#4 etapa remova e exiba um elemento.
print(elementos.remove("lápis"))
#5 etapa tamanho da lista.
print(len(elementos))
#6 etapa exiba todos os elementos.
for cama in elementos:
    print(cama)
#7 etapa verificação de adicionar/remover.
if "cadeira" in elementos:
    elementos.remove("cadeira")
else:
    elementos.append("cadeira")
#8 etapa ordene e exiba antes e depois.
print(elementos)
elementos.sort()
print(elementos)
#9 etapa mostre o primeiro e último objeto.
print(elementos[0])
print(elementos[3])
#10 etapa limpe a lista.
elementos.clear()