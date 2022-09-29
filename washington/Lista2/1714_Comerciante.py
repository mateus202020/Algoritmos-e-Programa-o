# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1714
''' Timelimit: 1
Um comerciante comprou um produto e quer vendê-lo com um lucro de 45% se o valor da compra for menor que R$ 20,00; caso contrário, o lucro será de 30%.
Dicas:
Utilize a estrutura if/else para realizar o cálculo.
Entrada
Um valor float representando o preço de compra do produto.
Saída
Imprima a mensagem "Valor de venda: R$" seguida pelo valor calculado para o preço de venda (mostre o valor com duas casas decimais). 
Samples Input	Samples Output
30.73
Valor de venda: R$39.95
15.80
Valor de venda: R$22.91 '''


Produto = float(input())

if Produto < 20:
    Produto = Produto + (Produto*0.45)
else:
    Produto = Produto +(Produto*0.30)

print("Valor de venda: R$%.2f"%Produto)