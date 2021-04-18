"""Criar um Algoritmo que leia os limites inferior e superior de um intervalo e imprima todos os números pares no intervalo aberto
e seu somatório. Suponha que os dados digitados são para um intervalo crescente, ou seja, o primeiro valor é menor que o
segundo, teste essa condição. """

limite_inferior = int(input("Digite o limíte inferior: "))
limite_superior = int(input("Digite o limite superior: "))
somatorio = 0
while limite_inferior != limite_superior + 1:
    if limite_inferior % 2 == 0:
        print(limite_inferior)
        somatorio = somatorio + limite_inferior
    limite_inferior += 1
print(somatorio)