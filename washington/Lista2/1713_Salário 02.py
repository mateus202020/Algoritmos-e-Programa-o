# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1713
''' Faça um programa em Python que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
salário bruto, quanto pagou ao INSS, quanto pagou ao sindicato, o salário líquido
Não apresente mensagem alguma além daquilo que está sendo especificado, caso contrário, você receberá "Presentation Error".
Entrada
Um valor do tipo float representando o valor recebido por hora e outro valor, também do tipo float, representando o número de horas trabalhadas no mês.
Saída
Você deverá imprimir na tela (um valor por linha e com duas casas decimais): 
2) o valor pago de imposto
3) o valor pago de INSS
4) o valor pago para o sindicato
5) o valor do salário líquido, calculado após os descontos
OBS: atente-se para o espaço após cada sinal de dois pontos.
Samples Input	Samples Output
10.78
100
Salário bruto: R$1078.00
Imposto: R$118.58
INSS: R$86.24
Sindicato: R$53.90
Líquido: R$819.28
43.5
25.5
Salário bruto: R$1109.25
Imposto: R$122.02
INSS: R$88.74
Sindicato: R$55.46
Líquido: R$843.03'''

Rh = float(input())
nh = float(input())

Salario = Rh * nh
Inss = Salario * 0.08
Sindicato = Salario * 0.05
ImpRenda = Salario * 0.11
Saliquido = Salario - (Inss+Sindicato+ImpRenda)

print("Salário bruto: R$%.2f"%Salario)
print("Imposto: R$%.2f"%ImpRenda)
print("INSS: R$%.2f"%Inss)
print("Sindicato: R$%.2f"%Sindicato)
print("Líquido: R$%.2f"%Saliquido)