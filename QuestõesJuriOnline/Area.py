# Escreva um programa que leia três valores com ponto flutuante de dupla precisão: A, B e C. Em seguida, calcule e mostre:
# a) a área do triângulo retângulo que tem A por base e C por altura.
# b) a área do círculo de raio C. (pi = 3.14159)
# c) a área do trapézio que tem A e B por bases e C por altura.
# d) a área do quadrado que tem lado B.
# e) a área do retângulo que tem lados A e B.


A ,B , C = map(float, input().split())

TRIANGULO = (A * C)/2

CIRCULO = 3.14159 * C**2

TRAPEZIO = ((A+B) * C)/2

QUADRADO = B * B

RETANGULO = B * A

print("TRIANGULO: %.3f"% TRIANGULO + "\n" + "CIRCULO: %.3f"% CIRCULO + "\n" +"TRAPEZIO: %.3f"% TRAPEZIO + "\n" +"QUADRADO: %.3f"% QUADRADO + "\n" +"RETANGULO: %.3f"% RETANGULO )


