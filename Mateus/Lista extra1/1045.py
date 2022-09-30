# https://www.beecrowd.com.br/judge/pt/problems/view/1045

a,b,c= map(float,input().split()) 

if a<b:
    a, b = b, a
    
if a<c:
    a, c = c ,a
    
if b<c:
    b, c = c, b


if a >= b + c:
    print('NAO FORMA TRIANGULO')
elif a**2 == b**2 + c**2:
    print('TRIANGULO RETANGULO')
elif a**2 > b**2 + c**2:
    print('TRIANGULO OBTUSANGULO')
elif a**2 < b**2 + c**2:
    print('TRIANGULO ACUTANGULO')
if a == b == c:
    print('TRIANGULO EQUILATERO')
elif ((a == b) and (a != c)) or ((a == c) and (a != b)) or ((b == c) and (b != a)):
    print('TRIANGULO ISOSCELES')
