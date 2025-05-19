#criar uma verificação de qual área o usuário ira escolher.
#o pi vale 3,14 (Área do circulo= π r²). Area do retângulo= b · h.
def calcula_triângulo_equilátero(área_perímetro_triângulo_equilátero):
    medidas_lados= int(input("digite a medida dos lados."))
    multi_número= medidas_lados * medidas_lados
    raiz= round(3**0.5, 3)
    multiplicação= multi_número * raiz
    divi_área= multiplicação / 4
    print("a área do triângulo equilátero é ", divi_área)
    
calcula_triângulo_equilátero(3)

área_perímetro_triângulo_equilátero= input(perímetro_triângulo_equilátero)
perímetro_triângulo_equilátero= int(input("digite um número."))
soma= perímetro_triângulo_equilátero + perímetro_triângulo_equilátero + perímetro_triângulo_equilátero
print("o resultado do perímetro é" , soma)

def calcula_quadrado(área_quadrado):
    medidas_lados= int(input("digite a medida dos lados."))
    multi_área= medidas_lados * medidas_lados
    print("a área do quadrado é " , multi_área)
    
calcula_quadrado(4)

def calcula_circulo(área_circulo):
    valor_pi= int(input("digite o valor de pi."))
    valor_raio= int(input("digite o valor do raio."))
    elevado= valor_raio * valor_raio
    multi_área= valor_pi * elevado
    print(multi_área)
    
calcula_circulo(10)

def calcula_retângulo(área_retângulo):
    base= int(input("digite os cm da base."))
    altura= int(input("digite os metros da altura."))
    multi_área= base * altura
    print("a área do retângulo é " , multi_área)
    
calcula_retângulo(20)

def calcula_hexágono(área_hexágono):
    quantidade= int(input("digite o número de lados do hexágono."))
    multi_quantidade= quantidade * quantidade
    multi_área= multi_quantidade * 2
    print("a área do hexágono é " , multi_área)

calcula_hexágono(6)
