# (Funções e Tratamento de Exceções – 20 pontos) Faça um programa que receba
# um valor em horas e dê duas opções ao usuário, converter em minutos ou em
# segundos. A partir da escolha do usuário, o programa deverá chamar a função
# específica de conversão. A função para converter horas em minutos deverá
# receber como parâmetro a hora e retornar o valor em minutos. A função para
# converter horas em segundos deverá receber como parâmetro a hora e retornar
# o valor em segundos. Por fim, o programa principal imprime o valor retornado
# pela função. Além disso, para essa questão trate possíveis exceções.

def min(num):
    num = horas * 60
    return num

def sec(num):
    num = horas * 3600
    return num

def isnumber(value):
    try:
        int(value)
    except ValueError:
         return False
    return True

while True:
    horas = input('Digite um valor em horas: ')
    if isnumber(horas) == True:
        horas = int(horas)
        break
    else:
        print('valor invalido')

print('0 - parar o programa')
print('1 - converter para minutos')
print('2 - converter para segundos')

while True:
    opcao = input('Digite sua Opção: ')
    if isnumber(opcao) == True:
        opcao = int(opcao)
        if opcao == 0:
            break
        elif opcao == 1:
            print('tempo em minutos: {}' .format(min(horas)))
            break
        elif opcao == 2:
            print('tempo em segundos: {}' .format(sec(horas)))
            break
        print('opção invalida')
    else:
        print('opção invalida')
print('programa finalizado')
