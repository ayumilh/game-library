from random import randint
from math import log

print('='*10, 'JOGO DA ADIVINHAÇÃO', '='*10)
sair = ''

while sair != 'S':
    print('')
    print('-'*10, "Inserindo valores:", '-'*10)
    print('')
    minimo = input(">>>Minimo a ser adivinhado: ")
    maximo = input(">>>Maximo a ser adivinhado: ")

    # Tem como melhorar??
    while not minimo.isnumeric():
        minimo = input(">>>Por favor insira um valor inteiro para o minimo: ")

    while not maximo.isnumeric():
        maximo = input(">>>Por favor insira um valor inteiro para o maximo: ")

    minimo = int(minimo)
    maximo = int(maximo)
    pc = randint(minimo, maximo)

    tentativas = 0
    chance = log(maximo - minimo + 1, 2)
    chance = round(chance)

    while True:
        chute = input(">>>Qual seu chute? ")
        while not chute.isnumeric():
            chute = input(">>>Por favor insira um valor inteiro para o chute: ")
        else:
            chute = int(chute)
        if chute == pc:
            print("Parabens! jogou bem")
            break
        else:
            if tentativas == round(chance):
                break
            elif chute <= pc:
                tentativas += 1
                print("Tente novamente! Voce adivinhou muito baixo")
            else:
                tentativas += 1
                print("Tente novamente! Voce adivinhou muito alto")
    sair = input('>>>Deseja sair? [S/N]').upper()
    while sair.isdigit():
        sair = input('>>>[S] -> Para sair e [N] -> Para continuar [S/N]').upper()

    print('')
    print('-' * 10, "FIM DO JOGO", '-' * 10)
    print('')
    print(f"Valor selecionado pelo computador: {pc}")
    print(f"Intervalo foi minimo: {minimo} e maximo: {maximo}")
    print(f"Tentativas: {tentativas}")
    print(f"Chances: {chance}")
