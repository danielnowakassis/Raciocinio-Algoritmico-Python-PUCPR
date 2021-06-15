
"""
1) Elabore uma App em Python para ler do teclado uma matriz 3x3 de valores reais. A
App devera´ chamar uma função que receba essa matriz como parâmetro de entrada
e retorne o valor da soma de todos os elementos. A App deverá imprimir a matriz de
entrada e o valor da soma.

lista matriz


lista soma_matriz(matriz):
    soma = 0
    Para i no Escopo(9):
        Se i < 3
            Leia(n)
            matriz[0].append(n)
        Senão se i < 6
            Leia(o)
            matriz[1].append(o)
        Senão:
            Leia(p)
            matriz[2].append(p)
    Para j no Escopo(3):
        Se j = 0
            soma = soma + matriz[0][0] + matriz[0][1] + matriz[0][2]
        Senão se j = 1
            soma = soma + matriz[1][0] + matriz[1][1] + matriz[1][2]
        Senão se j = 2
            soma = soma + matriz[2][0] + matriz[2][1] + matriz[2][2]
    Imprima("A soma dos elementos da matriz é: ", soma)
    Imprima(matriz)
matriz = [[], [], []]
soma_matriz(matriz)
"""
def soma_matriz(matriz):
    soma = 0
    for i in range(9):
        if i < 3:
            n = float(input("Digite os valores da primeira linha: "))
            matriz[0].append(n)
        elif i < 6:
            o = float(input("Digite os valores da segunda linha: "))
            matriz[1].append(o)
        else:
            p = float(input("Digite os valores da terceira linha: "))
            matriz[2].append(p)
    for j in range(3):
        if j == 0:
            soma = soma + matriz[0][0] + matriz[0][1] + matriz[0][2]
        elif j == 1:
            soma = soma + matriz[1][0] + matriz[1][1] + matriz[1][2]
        elif j == 2:
            soma = soma + matriz[2][0] + matriz[2][1] + matriz[2][2]
    print("A soma dos elementos da matriz é: ", soma)
    print(matriz)
matriz = [[], [], []]
soma_matriz(matriz)
"""2) Elabore uma App em Python para ler do teclado uma matriz 5x5 de valores
inteiros. A App devera´ chamar uma função que receba essa matriz como parâmetro
de entrada e retorne o valor da soma de todos os elementos da diagonal principal. A
App deverá imprimir a matriz de entrada e o valor da soma.


lista soma_matriz(matriz):
    soma = 0
    Para i in range(9):
        if i < 3:
            Leia(n) 
            matriz[0].append(n)
        elif i < 6:
            Leia(o)
            matriz[1].append(o)
        else:
            Leia(p)
            matriz[2].append(p)
    for j in range(3):
        if j = 0:
            soma = soma + matriz[0][0] + matriz[0][1] + matriz[0][2]
        elif j = 1:
            soma = soma + matriz[1][0] + matriz[1][1] + matriz[1][2]
        elif j = 2:
            soma = soma + matriz[2][0] + matriz[2][1] + matriz[2][2]
    Imprima("A soma dos elementos da matriz é: ", soma)
    Imprima(matriz)
matriz = [[], [], []]
soma_matriz(matriz)"""

def soma_matriz(matriz):
    soma_diagonal = 0
    for i in range(25):
        if i < 5:
            n = float(input("Digite os valores da primeira linha: "))
            matriz[0].append(n)
        elif i < 10:
            o = float(input("Digite os valores da segunda linha: "))
            matriz[1].append(o)
        elif i < 15:
            p = float(input("Digite os valores da terceira linha: "))
            matriz[2].append(p)
        elif i < 20:
            q = float(input("Digite os valores da quarta linha: "))
            matriz[3].append(q)
        elif i < 25:
            r = float(input("Digite os valores da quinta linha: "))
            matriz[4].append(r)
    soma_diagonal = matriz[0][0] + matriz[1][1] + matriz[2][2] + matriz[3][3] + matriz[4][4]
    print("A soma da diagonal da matriz é: ", soma_diagonal)
    print(matriz)
matriz = [[], [], [], [], []]
soma_matriz(matriz)

"""3) Elabore uma App que leia uma matriz de 3x4 de caracteres, imprima se existe
entre os elementos um caractere ʻBʼe em que linha e coluna ele foi encontrado. A App
devera chamar uma função que receba a matriz lida e retorne a linha e coluna onde o
caractere foi encontrado. Caso ele não esteja presente a função deverá retornar ( -1,
- 1). 
def verificador_b(matriz):
    Para x no Escopo(12):
        Se x < 4
            Leia(n)
            matriz[0].append(n)
        elif x < 8:
            Leia(o)
            matriz[1].append(o)
        elif x < 12:
            Leia(p)
            matriz[2].append(p)
    contadorB = 0
    Para i no Escopo(3):
        Para j no Escopo(4):
            Se "B" está em matriz[i][j]:
                contadorB += 1
                Imprima("Existe o caracter B na linha", i + 1, "e na coluna", j + 1)
    Se contadorB = 0:
        Imprima("-1, -1")
matriz = [[], [], []]
verificador_b(matriz)
"""
def verificador_b(matriz):
    for x in range(12):
        if x < 4:
            n = str(input("Digite os valores da primeira linha: "))
            matriz[0].append(n)
        elif x < 8:
            o = str(input("Digite os valores da segunda linha: "))
            matriz[1].append(o)
        elif x < 12:
            p = str(input("Digite os valores da terceira linha: "))
            matriz[2].append(p)
    contadorB = 0
    for i in range(3):
        for j in range(4):
            if "B" in matriz[i][j]:
                contadorB += 1
                print("Existe o caracter B na linha", i + 1, "e na coluna", j + 1)
    if contadorB == 0:
        print("-1, -1")
matriz = [[], [], []]
verificador_b(matriz)