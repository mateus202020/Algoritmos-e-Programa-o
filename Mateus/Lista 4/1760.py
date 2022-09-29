# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1760

idade = 0
peso = 0
pessoas_acima_90kg = 0
contador = 1
soma_idade = 0

while contador <= 4:
    idade = int(input(''))
    peso = float(input(''))
    contador = contador + 1
    soma_idade = soma_idade + idade

    if peso > 90:
        pessoas_acima_90kg = pessoas_acima_90kg + 1

media_idade = soma_idade / 4

print('Qtd pessoas > 90Kg: %i' % pessoas_acima_90kg)
print('Idade média: %.2f' % media_idade)