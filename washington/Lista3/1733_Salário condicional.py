# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1733
''' Desenvolver um programa que receba o nome e a quantidade de horas extras trabalhadas por um funcionário, calcule e mostre o seu salário bruto e o salário líquido.
Valores conhecidos:
Salário mínimo = R$1192,40;
Valor da hora-extra = R$10,00.
Sabe-se que:
Salário hora-extra = horas-extras * Valor da hora-extra;
Salário bruto = 3 * Salário mínimo + Salário hora-extra;
Desconto INSS = 12% do salário bruto, se o salário bruto for maior que R$ 2000,00, ou 5% caso contrário;
Desconto do Imposto de Renda = 20% do salário bruto, se o salário bruto for maior que R$ 2500,00, 0% caso contrário;
Salário líquido = salário bruto – descontos
Dica 01
Para imprimir o nome utilize o print abaixo
print("Nome: %s" %(nome));
Entrada
Um valor do tipo string representando o nome do funcionário e um valor do tipo float representando o número de horas extras trabalhadas.
Saída
Você deverá imprimir, ao final do programa, o nome do funcionário, seu salário bruto e seu salário líquido. Vide exemplos.
Samples Input	Samples Output
Carlos Antônio
12.5
Nome: Carlos Antônio
Salário bruto: R$3702.20
Salário líquido: R$2517.50
João Paulo
80
Nome: João Paulo
Salário bruto: R$4377.20
Salário líquido: R$2976.50'''

Nome = input("")
horas = float(input(""))

salario_min = 1192.40
hora_ex = 10.00

salario_ex = horas * hora_ex

salario_bruto = (3 * salario_min) + salario_ex

if salario_bruto > 2000:
    inss = 0.12
else:
    inss = 0.05

if salario_bruto > 2500:
    irpf = 0.20
else:
    irpf = 0

salario_liq = salario_bruto - ((salario_bruto*inss)+(salario_bruto*irpf))

print("Nome: %s"%(Nome))
print("Salário bruto: R$%.2f"%(salario_bruto))
print("Salário líquido: R$%.2f"%(salario_liq))