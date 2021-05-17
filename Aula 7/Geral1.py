def funcao(a, b, c):
    soma = 0
    if b > c:
        contador_bc = c
        while contador_bc < b:
            if contador_bc % a == 0:
                soma = soma + contador_bc
            else:
                continue
            contador_bc += 1
    elif b < c:
        contador_cb = b
        while contador_cb < c:
            if contador_cb % a == 0:
                soma = soma + contador_cb
            else:
                continue
            contador_bc += 1
    return soma



num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

if num1 < 1:
    print("Digite um número maior que 1")
    exit(1)
else:
    print(funcao(num1, num2, num3))

""" Escreva um Algoritmo e um App em Python que converta horas, minutos e
segundos em segundos. A função recebe os valores das horas, minutos e
segundos lidos do teclado no programa principal, envia os três valores para a
função e retorna o total de segundos, que será impresso pelo programa
principal.
"""

def funcao(a, b, c):
    soma = 0
    soma = soma + (3600 * a)
    soma = soma + (60 * b)
    soma = soma + c
    print(soma)

hora = int(input("Digite as horas: "))
minutos = int(input("Digite as minutos: "))
segundos = int(input("Digite os segundos: "))

funcao(hora, minutos, segundos)

    

"""3) Escreva um Algoritmo e um App em Python que converta segundos em horas,
minutos e segundos. A função recebe o valor total de segundos, lidos do teclado
no programa principal, envia o valor para a função e retorna as horas, minutos e
segundos equivalentes, que será impresso pelo programa principal. """



def conversao(segundos):
  conversao_hora = segundos // 3600
  conversao_minutos = segundos // 60 - (60 * conversao_hora)
  conversao_segundos = segundos % 10
  print(conversao_hora)
  print(conversao_minutos)
  print(conversao_segundos)

segundos = int(input("Digite os segundos: "))
conversao(segundos)

