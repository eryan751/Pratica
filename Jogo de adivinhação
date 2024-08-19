import random

print("Acerte um numero de 1 a 30")
#Numeros que estão valendo
numero_secreto = random.randint(1, 30)

#Define numero maximo de tentativas
tentativas_maximas = 10

#contador de tentativas
tentativas = 0

#Inicia o loop
while tentativas < tentativas_maximas:

    palpite = int(input("Escreva seu palpite de (1 a 30): "))
    
    if palpite == numero_secreto:
     print('Parabens, Você acertou o numero secreto')
     break
    elif palpite < numero_secreto:
     print('Seu palpite foi baixo, tente um mais alto')
    elif palpite > numero_secreto:
     print('Seu numero passou, tente um mais baixo')

#Aumenta o contador de tentativas
    tentativas += 1

#Acontece caso o jogador perda o jogo
if tentativas == tentativas_maximas:
    print(f"Você não conseguiu, o numero secreto era {numero_secreto}")
 
