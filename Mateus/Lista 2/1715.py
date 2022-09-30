# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1715

tipo = int(input(""))
valor_compra = float(input(""))


if tipo == 1:
    desconto = valor_compra - 0
    print("Valor total a ser pago: R$%.2f"%desconto)

elif tipo == 2:
    desconto = (valor_compra * 13/100)
    calculo = (valor_compra - desconto)
    print("Valor total a ser pago: R$%.2f"%calculo)

elif tipo == 3:
    desconto = (valor_compra * 7/100)
    calculo = (valor_compra - desconto)
    print("Valor total a ser pago: R$%.2f"%calculo)

else:
    tipo>3
    print("OPÇÃO INVÁLIDA!")

