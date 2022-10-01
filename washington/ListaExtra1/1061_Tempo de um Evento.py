# https://www.beecrowd.com.br/judge/pt/problems/view/1061
''' Pedrinho está organizando um evento em sua Universidade. O evento deverá ser no mês de Abril, iniciando e terminando dentro do mês. O problema é que Pedrinho quer calcular o tempo que o evento vai durar, uma vez que ele sabe quando inicia e quando termina o evento.

Sabendo que o evento pode durar de poucos segundos a vários dias, você deverá ajudar Pedrinho a calcular a duração deste evento.

Entrada
Como entrada, na primeira linha vai haver a descrição “Dia”, seguido de um espaço e o dia do mês no qual o evento vai começar. Na linha seguinte, será informado o momento no qual o evento vai iniciar, no formato hh : mm : ss. Na terceira e quarta linha de entrada haverá outra informação no mesmo formato das duas primeiras linhas, indicando o término do evento.

Saída
Na saída, deve ser apresentada a duração do evento, no seguinte formato:

W dia(s)
X hora(s)
Y minuto(s)
Z segundo(s)

Obs: Considere que o evento do caso de teste para o problema tem duração mínima de 1 minuto.

Exemplo de Entrada	Exemplo de Saída
Dia 5
08 : 12 : 23
Dia 9
06 : 13 : 23

3 dia(s)
22 hora(s)
1 minuto(s)
0 segundo(s)'''

diaI = int(input().split()[1])
hhI,mmI,ssI= map(int,input().split(":"))
diaF = int(input().split()[1])
hhF,mmF,ssF= map(int, input() .split(":")) 
t1 = ssI + mmI*60 + hhI*60*60 + diaI*24*60*60
t2 = ssF + mmF*60 + hhF*60*60 + diaF*24*60*60

dif = t2 - t1
diasf = dif//(24*60*60)
dif = dif%(24*60*60)

horasf = dif//(60*60)
dif = dif%(60*60)

minutosf = dif//(60)
dif = dif%(60)

segundosf = dif


print("%i dia(s)"%diasf)
print("%i hora(s)"%horasf)
print("%i minuto(s)"%minutosf)
print("%i segundo(s)"%segundosf)
