# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1761
''' O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora possui uma loja de conveniências. Faça um programa em Python que implemente uma caixa registradora rudimentar. O programa deverá receber um número desconhecido de valores referentes aos preços das mercadorias. Um valor zero deve ser informado pelo operador para indicar o final da compra. O programa deve então mostrar o total da compra e perguntar o valor em dinheiro que o cliente forneceu, para então calcular e mostrar o valor do troco.
Entrada: O programa deverá solicitar os valores dos produtos comprados (float) enquanto não receber um valor 0. Ao receber o valor 0, o programa deverá então receber o valor pago pelo cliente (float).
Saída: Após o processamento, o programa deverá exibir na tela, conforme os exemplos:
* Valor total da compra
* Valor pago
* Troco
Samples Input	Samples Output
3.78 9.56 12.52 0
50
Total da compra: R$25.86
Valor pago: R$50.00
Troco: R$24.14
10 100 50 30 60 250 0
1000
Total da compra: R$500.00
Valor pago: R$1000.00
Troco: R$500.00'''


valor = 1
total = 0
while valor != 0:
    valor = float(input())
    total = total + valor
valorPago = float(input())
troco = valorPago - total
print("Total da compra: R$%.2f"%(total))
print("Valor pago: R$%.2f"%(valorPago))
print("Troco: R$%.2f"%(troco))
