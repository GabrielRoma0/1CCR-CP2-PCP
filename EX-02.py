'''

Faça um programa que leia 3 valores que representam os lados de um triângulo A,
B e C e ordene-os em ordem decrescente, de modo que o lado A representa o
maior dos 3 lados. A seguir, determine o tipo de triângulo que estes três lados
formam, com base nos seguintes casos:
Se A ≥ B+C, apresente a mensagem: NAO FORMA TRIANGULO;
Se A² = B² + C², apresente a mensagem: TRIANGULO RETANGULO;
Se A² > B² + C², apresente a mensagem: TRIANGULO OBTUSANGULO;
Se A² < B² + C², apresente a mensagem: TRIANGULO ACUTANGULO;
Se os três lados forem iguais, apresente a mensagem: TRIANGULO EQUILATERO;
Se apenas dois dos lados forem iguais, apresente a mensagem: TRIANGULO ISOSCELES

'''

a = float(input('Digite o valor de um lado do triângulo: '))
b = float(input('Digite o valor de outro lado do triângulo: '))
c = float(input('Digite o valor de mais um lado do triângulo: '))

#lista dos lados + colocando eles em ordem decrescente

if a >= b and a >= c and b >= c:
    a, b, c = a, b, c
elif a >= b and a >= c and c > b:
    a, b, c = a, c, b
elif b > a and b >= c and a >= c:
    a, b, c = b, a, c
elif b > a and b >= c and c > a:
    a, b, c = b, c, a
elif c > a and c > b and a >= b:
    a, b, c = c, a, b
else:
    a, b, c = c, b, a

# Vendo casos de formar triângulo, se é ret, acu ou obt.

if a >= b + c:
    print('Não forma triângulo ')
else:
    if a**2 == (b**2)+(c**2):
        print('Triângulo retângulo ')
    elif a**2 > (b**2)+(c**2):
        print('Triângulo obtusângulo ')
    elif a**2 < (b**2)+(c**2):
        print('Triângulo acutângulo ')

#Verificar lados iguais + classifcação pelos lados.

    if a == b and b == c:
        print('TRIANGULO EQUILATERO')
    elif a == b or b == c or a == c:
        print('TRIANGULO ISOSCELES')
    else:
        print('Triângulo escaleno ')




