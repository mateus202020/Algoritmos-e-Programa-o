# https://www.beecrowd.com.br/judge/pt/problems/view/1021

n  = float(input())
umC  =  0
cinC  =  0
dezC  =  0
vinceC  =  0
cinqC  =  0
umR  =  0
doisR  =  0
cinR  =  0
dezR  =  0
vintR  =  0
cinqR  =  0
CEM  =  0
cem  =  n  //  100
resto  =  n  %  100
cinq =  resto  //  50
resto  =  resto  %  50
vint  =  resto  //  20
resto  =  resto  %  20
dez =  resto  //  10
resto  =  resto  %  10
cin  =  resto  //  5
resto  =  resto  %  5
dois  =  resto  //  2
resto  =  resto  %  2
um  =  resto  //  1
resto  =  resto  %  1
cinq =  resto  //  0.50
resto  =  resto  %  0.50
vincin  =  resto  //  0.25
resto  =  resto  %  0.25
dez  =  resto  //  0.10
resto  =  resto  %  0.10
cin =  resto  //  0.05
resto  =  resto  %  0.05
um  =  resto

print ( "NOTAS:")
print ( "%i nota(s) de R$ 100.00" % (cem))
print ( "%i nota(s) de R$ 50.00" % (cin))
print ( "%i nota(s) de R$ 20.00" % (vint))
print ( "%i nota(s) de R$ 10.00" % (dez))
print ( "%i nota(s) de R$ 5.00" % (cin))
print ( "%i nota(s) de R$ 2.00" % (dois))
print ( "MOEDAS:")
print ( "%i moeda(s) de R$ 1.00" % (um))
print ( "%i moeda(s) de R$ 0.50" % (cinq))
print ( "%i moeda(s) de R$ 0.25" % (vincin))
print ( "%i moeda(s) de R$ 0.10" % (dez))
print ( "%i moeda(s) de R$ 0.05" % (cin))
print ( "%i moeda(s) de R$ 0.01" % (um))