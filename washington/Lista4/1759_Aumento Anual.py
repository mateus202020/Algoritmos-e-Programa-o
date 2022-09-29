# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1759
''' Um funcionário de uma empresa recebe aumento salarial anualmente. Sabe-se que:
Esse funcionário foi contrato em 2005, com salário inicial de R$1000,00.
Em 2006, ele recebeu aumento de 1,5% sobre seu salário inicial.
A partir de 2007 (inclusive), os aumentos salariais sempre corresponderam ao percentual do ano anterior + 1%.
O aumento é feito em cima do salário do ano anterior.
Utilizando estrutura de repetição, faça um programa que receba o ano atual e determine o salário desse funcionário.
OBS: o ano informado não pode ser menor que 2006, caso seja, o programa deverá imprimir uma mensagem de erro e finalizar.
Entrada: Como entrada, o programa receberá apenas um valor inteiro referente ao ano atual informado pelo usuário.
Saída : Caso o ano atual, informado pelo usuário seja maior ou igual a 2006, o programa deverá imprimir a frase "Salário atual: R$", seguido do valor calculado para o salário no ano atual, mostrando duas casas decimais.
Caso o ano atual, informado pelo usuário, seja menor que 2006, o programa deverá imprimir a mensagem de erro "O ano informado deverá ser > 2005!". 
Samples Input	Samples Output
2022
Salário atual: R$4598.73
1999
O ano informado deverá ser > 2005!'''


ano = int(input())
SalContrato = 1000
SalIni = SalContrato + (SalContrato*0.015)
salario = 0

if ano < 2006:
    print("O ano informado deverá ser > 2005!")       
elif ano == 2006:
    print("Salário atual: R$%.2f"%(SalIni))
else:
    salario = SalIni
    aumento = 0.015
    while ano > 2006:
        aumento = aumento + 0.01
        salario = salario + (salario*aumento) 
        ano = ano -1
    print("Salário atual: R$%.2f"%(salario))