# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1734
''' Faça um programa que receba do usuário um valor inteiro N. Calcule e mostre o resultado de seu fatorial.
Saiba que:
N! = 1 x 2 x 3 .... x (N -1) x N
0! = 1
Dicas:
Utilize a estrutura de repetição while.
Entrada
O programa deverá receber um único valor inteiro, o valor de n, que será utilizado para calcular o fatorial de n.
Saída
Ao final do processamento e calculo do fatorial de n, o programa deverá imprimir a frase "n! = x", onde: n deverá ser o valor digitado pelo usuário (usar %i) e x o valor do fatorial de n calculado pelo programa (usar %i). 
Samples Input	Samples Output
9
9! = 362880
3
3! = 6
0
0! = 1'''


n = int(input())
pf = n
if n == 0:
    f = 1
else:
    f = 1
    while pf > 1:
        f = pf * f
        pf = pf-1
print("%i! = %i"%(n, f))