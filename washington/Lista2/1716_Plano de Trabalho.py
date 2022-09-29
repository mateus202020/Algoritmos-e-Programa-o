# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1716
''' Um funcionário irá receber um aumento de acordo com o seu plano de trabalho, de acordo com a tabela abaixo:

Faça um programa que leia o plano de trabalho e o salário atual de um funcionário e calcula e imprime o seu novo salário. Use o comando elif.
Entrada
O programa deverá receber o código referente ao tipo de plano do funcionário (A, B ou C) que deverá ser armazenado em uma variável do tipo char (utilizar apenas input sem int ou float). Além disso, o programa também deverá receber o salário atual deste funcionário, que deverá ser armazenado em uma variável float.
Saída
O programa deverá exibir a frase "Novo salário: R$", seguido do valor do novo salário calculado pelo programa (deve-se mostrar o valor com duas casas decimais apenas). 
Samples Input	Samples Output
A
1500.75
Novo salário: R$1650.82
C
782.50
Novo salário: R$939.00'''


plano = input()
salario = float(input())

if plano == 'A':
    salario = salario + (salario*0.10)
elif plano == 'B':
    salario = salario + (salario*0.15)
elif plano == 'C':
    salario = salario + (salario*0.20)

print("Novo salário: R$%.2f"%salario)