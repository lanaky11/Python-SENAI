num1= int(input("solicite um número."))
n = 0
quantidade_númerica= 0
while n <= num1:
    if n % 2 == 0:
        print(n)
        quantidade_númerica = quantidade_númerica + 1
    n = n + 1
print("quantidade_númerica é ", quantidade_númerica)