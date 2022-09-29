# https://www.beecrowd.com.br/judge/pt/problems/view/1019
''' Leia um valor inteiro, que é o tempo de duração em segundos de um determinado evento em uma fábrica, e informe-o expresso no formato horas:minutos:segundos.
Entrada
O arquivo de entrada contém um valor inteiro N.
Saída
Imprima o tempo lido no arquivo de entrada (segundos), convertido para horas:minutos:segundos, conforme exemplo fornecido.
Exemplo de Entrada	Exemplo de Saída
556
0:9:16

1
0:0:1

140153
38:55:53'''
tempo = int(input())
i = 0
s = 0
m = 0
h = 0
if tempo < 60:
    s = tempo
else:
    while tempo > 0:
        s = s + 1
        if s > 59:
            m = m + 1
            s = 0
        if m > 59:
            h = h + 1
            m = 0
        tempo = tempo - 1
print("%i:%i:%i"%(h,m,s))