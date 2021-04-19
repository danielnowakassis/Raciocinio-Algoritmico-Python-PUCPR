""" Criar um Algoritmo que leia os limites inferior e superior de um intervalo e
imprima todos os números impares no intervalo aberto e seu somatório. Suponha
que os dados digitados são para um intervalo crescente, ou seja, o primeiro
valor é menor que o segundo.

# corpo do código
Leia(limite_inferior)
Leia(limite_superior)
contador <- limite_superior
soma_pares <- 0

Inteiro limite_inferior, limite_superior, contador, soma_pares

Se limite_inferior > limite_superior então
    Imprima("Digite um número para o limite inferior maior que o limite superior")
    abandone
Senão:
    Enquanto contador < limite_inferior + 1 faça
        Se limite_inferior > limite_superior então
            Imprime("Digite um número para o limite superior maior que o limite inferior")
            abandone
        Se contador % 2 ≠ 0 então
            Imprima(contador)
            soma_pares <- soma_pares + contador
        contador = contador - 1
Imprima(soma_pares)

"""
# corpo do código
limite_inferior = int(input("Digite o limite inferior: "))
limite_superior = int(input("Digite o limite superior: "))
contador = limite_superior
soma_pares = 0
if limite_inferior > limite_superior:
    print("Digite um número para o limite inferior maior que o limite superior")
    exit(0)
else:
    while contador < limite_inferior + 1:
        if limite_inferior > limite_superior:
            print("Digite um número para o limite superior maior que o limite inferior")
            exit(0)
        if contador % 2 != 0:
            print(contador)
            soma_pares = soma_pares + contador
        contador -= 1
print(soma_pares)