def opções_númerais(Opção0, Opção1, Opção2, Opção3, Opção4):

    Opção0= print("(0) Sair.")
    Opção1= print("(1) Fatorial.")
    Opção2= print("(2) Quadrado.")
    Opção3= print("(3) Cubo.")
    Opção4= print("(4) Tabuada.")

    if Opções_númerais == 0:
        print("exiba Opção0.")
        return "Saida"

    if Opções_númerais >= 1:
        print("exiba Opção1.")
        return "Fatorial"

    if Opções_númerais >= 2:
        print("exiba Opção2.")
        return "Quadrado"

    if opções_númerais >= 3:
        print("exiba Opção3")
        return "Cubo"

    if opções_númerais <= 4:
        print("exiba Opção4")
        return "Tabuada"