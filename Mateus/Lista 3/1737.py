# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1737

num = int(input(""))

soma = 0

if num > 0:
    while num > 0:
        soma += float(input(""))
        num -= 1
    print("Soma dos números informados: %.2f" % soma)
else:
    print("Informe uma quantidade > 0!")