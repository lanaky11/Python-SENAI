nomes= []
while True:
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
          
    elif menu_opções == 2:
        print(len(nomes))
        
    elif menu_opções == 3:
        for nome in nomes:
            print(nome)
        
    elif menu_opções == 4:
        nome= input("digite um nome")
        if nome in nomes:
            resposta= input("Nome encontrado, deseja remove-ló? (s/n)")
            if resposta == "s":
                nomes.remove(nome)
                print("removido com sucesso.")
        else:
            resposta= input("nome não encontrado, deseja adiciona-ló? (s/n).")
            if resposta == "n":
                print("nome não será adicionado.")
            else:
                nomes.append(nome)
                print("nome cadastrado com sucesso.")