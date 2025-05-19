#criar
aluno= {
    "nome": "Ana lyvia",
    "idade": 16,
    "altura": 1.67,
    "matriculado": True
    }
#print(aluno)
    #criar
carro1= {
    "nome": "Civic",
    "cor": "prata",
    "marca": "Honda"
    }
print(carro1)

carro2= {
    "nome": "corolla",
    "cor": "preto",
    "marca": "Sedan",
    }
print(carro2)

carro3= {
    "nome": "Chevrolet",
    "cor": "preto",
    "marca": "americana",
    }
print(carro3)

#adicionar campo
aluno["peso"]= 67
#print(aluno)

#alterar campo
aluno["idade"]= 17
#print(aluno)

#deletar campo
del aluno["matriculado"]
print(aluno)

#verificar
if "matriculado" in aluno:
    print("matricula existente")
else:
    print("matricula inexistente")
    
#exibir
for chave, valor in aluno.items():
    print(f"{chave}: {valor}")
    
#exibir uma lista de dicionários
    lista_carros= [carro1, carro2, carro3]
    
#escolhendo os campos
for carros in lista_carros:
    print(f"{carros['marca']}")
    
#exibindo todos
for carros in lista_carros:
        for chave, valor in carros.items():
            print(f"{chave} - {valor}")
        print()