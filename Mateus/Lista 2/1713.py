
# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1713

valor_hora = float(input(""))
horas_trabalhadas = float(input(""))

salario_bruto = valor_hora*horas_trabalhadas
imposto = salario_bruto * 11/100
inss = salario_bruto * 8/100
sindicato = salario_bruto * 5/100
salario_liquido = salario_bruto-imposto-inss-sindicato
print("Salário bruto: R$%.2f\nImposto: R$%.2f\nINSS: R$%.2f\nSindicato: R$%.2f\nLíquido: R$%.2f" %(salario_bruto,imposto,inss,sindicato,salario_liquido))
