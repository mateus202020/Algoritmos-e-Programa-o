# https://www.beecrowd.com.br/judge/pt/problems/view/1061 

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