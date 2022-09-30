# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1733

nome = input("")
horas_extras = float(input(""))

salario_minimo = 1192.40
valor_horas_extra = 10
salario_horas_extra = horas_extras * valor_horas_extra
salario_bruto = (3 * salario_minimo) + salario_horas_extra

print("Nome: %s"%nome)
print("Salário bruto: R$%.2f"%salario_bruto)


if (salario_bruto>2000) and (salario_bruto>2500):
       desconto_Inss = salario_bruto-(salario_bruto*32/100)
       print("Salário líquido: R$%.2f"%desconto_Inss)
elif salario_bruto<2000:
       desconto_Inss = salario_bruto-(salario_bruto*0.05)
       print("Salário líquido: R$%.2f"%desconto_Inss)
