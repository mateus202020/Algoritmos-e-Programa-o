# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1714

valor = float(input())

if valor<20.00:
    calculo = valor*0.45+valor
    print("Valor de venda: R$%.2f" % calculo)

else:
    valor>20.00
    calculo = valor*0.30+valor
    print("Valor de venda: R$%.2f" %calculo)
