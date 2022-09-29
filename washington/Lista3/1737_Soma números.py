# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1737
''' Faça um programa que receba do usuário a quantidade de números que ele quer informar. Em seguida leia cada um dos números. Ao final mostre a soma de todos os números informados. Caso o usuário informe uma quantidade de números <= 0, mostre uma mensagem de erro.
Dica 1: utilize while.
Dica 2: mesmo se ele digitar que quer calcular a soma de 100 números, você não vai precisar de 100 variáveis, mas sim de apenas uma para guardar esses números (recebe um a cada rodada da repetição e utiliza acumuladores!).
Entrada: O programa deverá receber como entrada, primeiramente, a quantidade de números que o usuário deseja informar (int). Caso o valor informado seja maior que 0, em seguida o programa deverá receber cada um dos números informados pelo usuário (float). 
Saída : Caso a quantidade de números informada for maior que 0: o programa deverá imprimir, ao final do processamento, a frase "Soma dos números informados: " seguido pela soma calculado pelo programa, mostrando duas casas decimais.
Caso a quantidade de números informada for menor ou igual a 0: o programa não deverá fazer nenhum processamento e vai imprimir a frase "Informe uma quantidade > 0!". 
Samples Input	Samples Output
6 9 80 90 -500 3 6
Soma dos números informados: -312.00

3 1 2 3 
Soma dos números informados: 6.00

0
Informe uma quantidade > 0!

5 -1 50 6 9 -10
Soma dos números informados: 54.00'''


n = int(input())
if n > 0:
    soma = 0
    while n > 0:
        valor = float(input())
        soma = valor + soma
        n = n - 1
        if n == 0:
            print("Soma dos números informados: %.2f" % (soma))
else:
    print("Informe uma quantidade > 0!")