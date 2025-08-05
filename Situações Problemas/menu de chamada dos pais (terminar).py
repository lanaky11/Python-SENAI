# pedir para escolher a opção
# fazer a verificação opção (if elif else)
nomes_pais= []
print("[1]- Cadastrar nome dos pais.")
print("[2]- Exibir total de pais na chamada.")
print("[3]- Exibir nomes dos pais por ordem alfabética.")
print("[4]- Consulta da chamda de pais presentes.")
print("[5]- Exibir relatório de presenças.")

menu_opções= int(input("escolha um número."))
if menu_opções == 1:
    nome= input("digite um nome")
    if nome in nomes_pais:
        print("esse nome não está na lista.")
    else:
        nomes_pais.append(nome)
        print("nome cadastrado com sucesso.")
        if menu_opções == 2:
            quantidade= int(input("for nome in nomes_pais:"))
            print(nome)