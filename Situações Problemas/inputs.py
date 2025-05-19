def input_int():
    while True:
        try:
            num_int= int(input("digite um número."))
            return num_int
        except ValueError:
            print("digite apenas números.")
            
def input_float():
    while True:
        try:
            num_float= float(input("digite um número."))
            return num_float
        except ValueError:
            print("digite apenas números.")
            
def input_str():
    while True:
        try:
            num_str= str(input("digite um número."))
            return num_str
        except ValueError:
            print("digite apenas números.")