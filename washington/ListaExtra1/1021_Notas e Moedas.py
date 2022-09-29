# https://www.beecrowd.com.br/judge/pt/problems/view/1021
''' Leia um valor de ponto flutuante com duas casas decimais. Este valor representa um valor monetário. A seguir, calcule o menor número de notas e moedas possíveis no qual o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2. As moedas possíveis são de 1, 0.50, 0.25, 0.10, 0.05 e 0.01. A seguir mostre a relação de notas necessárias.

Entrada
O arquivo de entrada contém um valor de ponto flutuante N (0 ≤ N ≤ 1000000.00).

Saída
Imprima a quantidade mínima de notas e moedas necessárias para trocar o valor inicial, conforme exemplo fornecido.

Obs: Utilize ponto (.) para separar a parte decimal.

Exemplo de Entrada	Exemplo de Saída
576.73

NOTAS:
5 nota(s) de R$ 100.00
1 nota(s) de R$ 50.00
1 nota(s) de R$ 20.00
0 nota(s) de R$ 10.00
1 nota(s) de R$ 5.00
0 nota(s) de R$ 2.00
MOEDAS:
1 moeda(s) de R$ 1.00
1 moeda(s) de R$ 0.50
0 moeda(s) de R$ 0.25
2 moeda(s) de R$ 0.10
0 moeda(s) de R$ 0.05
3 moeda(s) de R$ 0.01

4.00

NOTAS:
0 nota(s) de R$ 100.00
0 nota(s) de R$ 50.00
0 nota(s) de R$ 20.00
0 nota(s) de R$ 10.00
0 nota(s) de R$ 5.00
2 nota(s) de R$ 2.00
MOEDAS:
0 moeda(s) de R$ 1.00
0 moeda(s) de R$ 0.50
0 moeda(s) de R$ 0.25
0 moeda(s) de R$ 0.10
0 moeda(s) de R$ 0.05
0 moeda(s) de R$ 0.01

91.01

NOTAS:
0 nota(s) de R$ 100.00
1 nota(s) de R$ 50.00
2 nota(s) de R$ 20.00
0 nota(s) de R$ 10.00
0 nota(s) de R$ 5.00
0 nota(s) de R$ 2.00
MOEDAS:
1 moeda(s) de R$ 1.00
0 moeda(s) de R$ 0.50
0 moeda(s) de R$ 0.25
0 moeda(s) de R$ 0.10
0 moeda(s) de R$ 0.05
1 moeda(s) de R$ 0.01'''
n = float(input())
umC = 0
cinC = 0
dezC = 0
vincinC = 0
cinqC = 0
umR = 0
doisR = 0
cinR = 0
dezR = 0
vintR = 0
cinqR = 0
cemR = 0
cemR = n // 100
resto = n % 100
cinqR = resto // 50
resto = resto % 50
vintR = resto // 20
resto = resto % 20
dezR = resto // 10
resto = resto % 10
cinR = resto // 5
resto = resto % 5
doisR = resto // 2
resto = resto % 2
umR = resto // 1
resto = resto % 1
cinqC = resto // 0.50
resto = resto % 0.50
vincinC = resto // 0.25
resto = resto % 0.25
dezC = resto // 0.10
resto = resto % 0.10
cinC = resto // 0.05
resto = resto % 0.05
umC = resto

print("NOTAS:")
print("%i nota(s) de R$ 100.00"%(cemR))
print("%i nota(s) de R$ 50.00"%(cinqR))
print("%i nota(s) de R$ 20.00"%(vintR))
print("%i nota(s) de R$ 10.00"%(dezR))
print("%i nota(s) de R$ 5.00"%(cinR))
print("%i nota(s) de R$ 2.00"%(doisR))
print("MOEDAS:")
print("%i moeda(s) de R$ 1.00"%(umR))
print("%i moeda(s) de R$ 0.50"%(cinqC))
print("%i moeda(s) de R$ 0.25"%(vincinC))
print("%i moeda(s) de R$ 0.10"%(dezC))
print("%i moeda(s) de R$ 0.05"%(cinC))
print("%i moeda(s) de R$ 0.01"%(umC))
