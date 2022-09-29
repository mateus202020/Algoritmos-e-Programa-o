# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1759

ano = int(input())
if ano > 2005:
    salario = 1000
    percentual = 1.5
    while ano >=2006:
        salario = salario + (salario * percentual / 100)
        percentual = percentual + 1
        ano = ano - 1
    print("Salário atual: R$%.2f" %salario)
else:
    print("O ano informado deverá ser > 2005!")