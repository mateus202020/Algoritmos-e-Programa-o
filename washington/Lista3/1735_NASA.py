# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1735
''' Utilizando a estrutura while faça um programa para escrever a contagem regressiva do lançamento de um foguete.
Entrada: O programa deverá receber dois valores inteiros: o primeiro, um valor que representa o valor inicial da contagem regressiva e o segundo, o valor final da contagem.
Saída: O programa deverá imprimir na tela a contagem regressiva partindo do valor inicial informado até o valor final informado (um número por linha) e ao final imprimir "Fogo!".
Samples Input	Samples Output
10
5
10 9 8 7 6 5 Fogo!

10
0
10 9 8 7 6 5 4 3 2 1 0 Fogo!'''


v1 = int(input())
v2 = int(input())

while v1 >= v2:
    print("%i"%(v1))
    v1 = v1-1
print("Fogo!")