# https://www.beecrowd.com.br/judge/pt/problems/view/1009

nome = input()
salario = float(input())
vendas = float(input())

total = salario + 0.15 * vendas 
print("TOTAL = R$ %.2f" %(total))