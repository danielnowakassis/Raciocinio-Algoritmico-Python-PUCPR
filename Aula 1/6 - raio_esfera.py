"""Elaborar um algoritmo a app para calcular e imprimir o volume de uma
esfera, sendo que o raio da esfera deve ser lido.

Pi = 3,1415...

Leia(RaioEsfera)

Real RaioEsfera

VolumeEsferaPi = (4 * Pi * RaioEsfera) / 3
VolumeEsferaPi3 = (4 * 3 * RaioEsfera) / 3
VolumeEsferaPi5 = (4 * 5 * RaioEsfera) / 3
"""

#importar Bibliotecas
from math import pi

#Área das variáveis
raio_esfera = float(input("digite o raio da esfera: "))

#Corpo do código
volume_esfera_pi = (4 * pi * raio_esfera) / 3
volume_esfera_pi3 = (4 * 3 * raio_esfera) / 3
volume_esfera_pi5 = (4 * 5 * raio_esfera) / 3

print("volume da esfera com pi = 3,1415...:", volume_esfera_pi)
print("volume da esfera com pi = 3:", volume_esfera_pi3)
print("volume da esfera com pi = 5:", volume_esfera_pi5 )
