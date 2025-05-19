# pedir para escolher a opção
# fazer a verificação opção (if elif else)
nomes= []

print("[1]- Cadastrar nome dos alunos.")
print("[2]- Exibir total de pessoas na chamada.")
print("[3]- Exibir nomes dos alunos por ordem alfabética.")
print("[4]- Consulta da chamada de nomes dos alunos.")

menu_opções= int(input("escolha um número."))
if menu_opções == 1:
    nome= input("digite um nome")
    if nome in nomes:
        print("esse nome não está na lista.")
    else:
        nomes.append(nome)
        print("nome cadastrado com sucesso.")