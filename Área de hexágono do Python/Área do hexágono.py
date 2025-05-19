#calcular a área do hexágono.
# mult é elevado (ao quadrado).
#calcular a área do triângulo equilátero.
# fazer lado x lado x a raiz de 3.
num1 = int(input("digite o número de lados do hexágono"))
mult = num1 * num1
raiz = round(3**0.5, 3)
mult1 = mult * raiz
resultado_área_triângulo = mult1 / 4
Área_Hexágono = round(6 * resultado_área_triângulo, 3)

print("A área do hexágono é " + str(Área_Hexágono))