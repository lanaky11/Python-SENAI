from datetime import datetime
def exibir_nome(nome):
    print("Olá", nome)
    horario_atual= datetime.now().hour
    if horario_atual > 0 and horario_atual < 5:
        print("Boa madrugada.")
    elif horario_atual > 5 and horario_atual < 12:
        print("Bom dia.")
    elif horario_atual > 12 and horario_atual < 19:
        print("Boa tarde.")
    elif horario_atual > 19 and horario_atual < 23:
        print("Boa noite.")
exibir_nome("Ana Lyvia")