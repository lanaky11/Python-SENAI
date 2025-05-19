# def cria uma função, depois tenho que chamar
#para chamar uma função precisamos colocar o nome da funçao com os () na frente
def exibir_números(num1 , num2):
    print("resultado_soma", somar(num1 , num2))
    print("resultado_subtração", subtrair(num1 , num2))
    print("resultado_vezes", multiplicar(num1 , num2))
    print("resultado_divisão", dividir(num1 , num2))

def somar(num1 , num2):
    return num1 + num2

def subtrair(num1 , num2):
    return num1 - num2

def multiplicar(num1 , num2):
    return num1 * num2

def dividir(num1 , num2):
    return num1 / num2

def menu_calculadora(num1 , num2):
    soma= input("1- Adição.")
    subtração= input("2- menos.")
    multiplicação= input("3- Vezes.")
    divisão= input("4- Divisão.")
