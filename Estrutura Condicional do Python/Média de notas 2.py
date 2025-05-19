nota1= int(input("solicite um número."))
nota2= int(input("solicite outro número."))
resultado_soma = nota1 + nota2
média = resultado_soma / 2
print(média)
if média > 70:
    print("o aluno está aprovado.")
else:
    print("o aluno está reprovado.")