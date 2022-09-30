# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1761

total=0
produto=1
while produto != 0:
    produto = float(input(''))
    total = total + produto

pago = float(input(''))
troco = pago - total

    
print("\nTotal da compra: R$%.2f \nValor pago: R$%.2f \nTroco: R$%.2f"%(total,pago,troco))
