nascimento = int(input("solicite uma data de nascimento."))
data = int(input("solicite um ano atual."))
resultado_subtração = data - nascimento
if resultado_subtração > 18:
   print("maior de idade.")
else:
    print("menor de idade.")