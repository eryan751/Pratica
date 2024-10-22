from random import choice

p = str(input('Primeiro aluno: '))
l = str(input('segundo aluno: '))
e = str(input('terceiro aluno: '))
m = str(input('Quarto aluno: '))

lista = [p, l, e, m]
#choice = escolha aleatoria
escolido = choice(lista)

print(f'O Aluno(a) sorteado foi {escolido} ')
