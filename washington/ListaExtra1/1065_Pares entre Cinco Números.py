# https://www.beecrowd.com.br/judge/pt/problems/view/1065
''' Faça um programa que leia 5 valores inteiros. Conte quantos destes valores digitados são pares e mostre esta informação.

Entrada
O arquivo de entrada contém 5 valores inteiros quaisquer.

Saída
Imprima a mensagem conforme o exemplo fornecido, indicando a quantidade de valores pares lidos.

Exemplo de Entrada	Exemplo de Saída
7
-5
6
-4
12

3 valores pares'''

n = 0
par = 0
while n < 5:
  n = n + 1
  x = int(input())
  if x%2 == 0:
    par = par + 1
print('%d valores pares' %par)