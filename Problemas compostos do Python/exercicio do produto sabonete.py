produto= str(input("nome do produto"))
preço= float(input("preço do produto"))
porcentagem = preço / 20
valor_final = preço - porcentagem
print("o desconto é de", porcentagem, "reais")
print("o novo valor é", valor_final, "reais")