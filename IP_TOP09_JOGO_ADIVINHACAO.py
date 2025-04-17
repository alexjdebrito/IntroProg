from random import randint

print('Escolha um número de 1 a 100!')

numero = randint(a=1, b=100)
tentativas = int(input('Escolha quantas tentativas:'))

for i in range (tentativas):
    palpite = int(input('Qual seu palpite:'))

    if numero == palpite:
        print('Você acertou!')
        break
    elif palpite < numero:
        print('O seu palpite foi ABAIXO do número!')
    elif palpite > palpite:
        print('O seu palpite foi ACIMA do número!')