# https://www.beecrowd.com.br/judge/pt/problems/view/1065

n = 0
par = 0
while n < 5:
  n = n + 1
  x = int(input())
  if x%2 == 0:
    par = par + 1
print('%d valores pares' %par)