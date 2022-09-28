# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1711
''' Faça um programa que solicite ao usuário o lado de um quadrado (pode conter casas decimais), em seguida calcula e mostra a área (também pode conter casas decimais) deste quadro para o usuário.
OBS: area = lado * lado
Entrada
Um valor do tipo float representando a área do quadrado.
Saída
Imprima a mensagem "A área do quadrado de lado " seguido pelo valor do lado do quadrado (mostrar o valor com duas casas decimais), continue a mensagem com "é igual a " seguido do valor da variável que armazena o cálculo da área do quadrado (mostrar o valor com duas casas decimais).
Samples Input	Samples Output
9.78
A área do quadrado de lado 9.78 é igual a 95.65
5
A área do quadrado de lado 5.00 é igual a 25.00'''

l=float(input())
a = l*l

print("A área do quadrado de lado %.2f é igual a %.2f" %(l, a))