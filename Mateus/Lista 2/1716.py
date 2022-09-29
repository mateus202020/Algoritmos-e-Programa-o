# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1716

tipo_plano = input("")
salario_atual = float(input())



if tipo_plano == 'A':
       aumento = (salario_atual * 0.10) + salario_atual
       print("Novo salário: R$%.2f"%(aumento))

elif tipo_plano == 'B':
       aumento = (salario_atual * 0.15) + salario_atual
       print("Novo salário: R$%.2f"%(aumento))

elif tipo_plano == 'C':
       aumento = (salario_atual * 0.20) + salario_atual
       print("Novo salário: R$%.2f"%aumento)