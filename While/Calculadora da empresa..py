despesas_totais= 0
despesas_empresas = 1 
valor_total = 2

while True:
    opções_empresáriais= int(input("escolha um número."))
    print("escolha uma opção.")
    
    print("(1) valor da despesa.")
    despesas_empresas= int(input("digite o valor das despesas."))
    
    print("(2) quantidade e valor total das despesas.")
    valor_total= int(input("digite uma quantidade para o valor total de despesas."))
    
    resultado_totais = despesas_empresas + valor_total
    print(resultado_totais)
    
    print("(0) Sair.")
    despesas_totais= input("byeeee.")
    
    if opções_empresáriais == 0:
        print("exibir saída" , "0.")
        break
    elif opções_empresáriais >= 1:
        print("exibir valor da despesa" , "1.")
    elif opções_empresáriais >= 2:
        print("exibir quantidade e valor total das despesas","2.")
