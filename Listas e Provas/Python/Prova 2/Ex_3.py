# [Condicionais] Desenvolva um programa que tenha como
# dados de entrada à altura, o peso e o sexo de uma pessoa. Na sequência
# calcule o seu peso ideal, utilizando as seguintes fórmulas:
# Para homens: (72.7 * altura) – 58
# Para mulheres: (62.1 * altura) - 44.7

# Na sequência, verifique se ela está no peso ideal, acima ou abaixo.

altura = float(input('digite sua altura: '))
peso = float(input('digite seu peso: '))
sexo = input('digite seu sexo em m ou f: ')

if sexo == 'm':
    homem = (altura * 72.7) - 58
    peso_ideal = homem - peso
    if peso_ideal == 0:
        print('voce esta no peso ideal')
    elif peso_ideal > 0:
        print('voce esta abaixo do peso ideal')
    else:
        print('voce esta acima do peso ideal')
elif sexo == 'f':
    mulher = (altura * 62.1) - 44.7
    peso_ideal = mulher - peso
    if peso_ideal == 0:
        print('voce esta no peso ideal')
    elif peso_ideal > 0:
        print('voce esta abaixo do peso ideal')
    else:
        print('voce esta acima do peso ideal')
    
