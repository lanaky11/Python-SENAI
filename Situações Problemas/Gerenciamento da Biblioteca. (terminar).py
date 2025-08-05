import inputs
biblioteca= []
while True:   
    print("[1]- Cadastrar um livro por vez.")
    print("[2]- Exibir todos os livros cadastrados.")
    print("[3]- Exibir apenas títulos dos livros.")
    print("[4]- Permitir editar dados de um livro.")
    print("[5]- Buscar livros de autor específico.")
    print("[6]- Buscar livros de determinada categoria.")
    print("[7]- Exibir quantidade total de livros registrados.")
    opcao= int(input("escolha um número desejado."))
    
    if opcao == 1:
        livros= {
    "título":input("digite o nome do livro"),
    "autor":input("digite o nome do autor"),
    "categoria":input("digite a categoria do livro"),
    "ano de publicação": input("digite o ano da publicação")
    }
    biblioteca.append(livros)
    print(biblioteca)
    if livro in livros:
        print("este nome já está na lista")
    else:
        lista_livros.append(livro)
        print("nome do livro adicionado ")

    if opcao == 2:
        for livro in lista_livros:
            print("")
            print("TITULO - {livro['titulo']}")
            print("ISBN - {livro['isbn']}")
            print("AUTOR - {livro['autor']}")
            print("CATEGORIA - {livro['categoria']}")
            print("ANO DE PUBLICAÇÃO - {livro['ano de publicacao']}")
            print("")
   
    elif opcao == 3:
        print("a quantidade de livros adicionados é ", len(livros))
    elif opcao == 4:
        for titulo in livros:
            print("TITULO - {titulo['titulo']}")
    elif opcao == 5:
        autor_escolhido= inputs.input("digite o nome do autor")
        for livro in livros:
            if autor_escolhido == livro['autor']:
                print("")
                print("TITULO -",f" {livro['titulo']}")
                print("ISBN -",f" {livro['isbn']}")
                print("AUTOR -",f" {livro['autor']}")
                print("CATEGORIA -",f" {livro['categoria']}")
                print("ANO DE PUBLICAÇÃO -",f" {livro['ano de publicacao']}")
                print("")
   
    elif opcao == 6:
        categoria_escolhida = inputs.input_str("digite a categoria")
        for livro in livros:
            if categoria_escolhida == livro['categoria']:
                print("")
                print("TITULO -",f" {livro['titulo']}")
                print("ISBN -",f" {livro['isbn']}")
                print("AUTOR -",f" {livro['autor']}")
                print("CATEGORIA -",f" {livro['categoria']}")
                print("ANO DE PUBLICAÇÃO -",f" {livro['ano de publicacao']}")
                print("")
               
    elif opcao == 7:
        isbn_editar = inputs.input_int("digite o ISBN do livro que deseja editar:")
        for livro in biblioteca:
            if livro['isbn'] == isbn_editar:
                print("livro encontrado. Faça as alterações:")
                livro['titulo'] = inputs.input_str("digite um novo titulo:")
                livro['isbn'] = inputs.input_int("digite um novo ISBN:")
                livro['categoria'] = inputs.input_str("digite uma nova categoria:")
                livro['ano de publicacao'] = inputs.input_int("digite um novo ano d epublicação:")
                livro['autor'] = inputs.input_str("digite um novo autor:")
                print("dados do livro atualizados com sucesso")
            else:
                print("livro não encontrado")