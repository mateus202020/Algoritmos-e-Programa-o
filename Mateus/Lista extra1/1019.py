# https://www.beecrowd.com.br/judge/pt/problems/view/1019

segundos = int(input(""))

horas = segundos//3600
segundos-=horas*3600
minutos = segundos//60
segundos-=minutos*60

print("%i:%i:%i"%(horas,minutos,segundos))
