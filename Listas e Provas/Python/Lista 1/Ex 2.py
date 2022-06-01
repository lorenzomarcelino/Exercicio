ações = {}
while True:
    print("\nEscolha uma opção")
    print("1: cadastrar uma nova ação")
    print("2: informações de compra e venda de ativos")
    option = int(input("Opção: "))
    if option == 1:
        print("cadastrar uma nova ação: ")
        código = input("código da ação:")
        descrição = input("Descrição da ação:")
        histórico = []
        histórico = [int(input("Histórico de valores da ação: ")) for c in range(10)]       
        quantidade = input("Quantidade de ações compradas: ")
        ativos = {'código': código, 'descrição': descrição, 'histórico': histórico, 'quantidade': quantidade}
        ações[código] = ativos
    elif option == 2:
        codgação = input("informe o código da ação: ")
        ativos = ações.get(código, None)
        if código is not None:
            valor = input("informar o valor atual da ação")
            soma = sum(histórico)
            media = (soma / 11)
            if valor > media:
                print("VENDA")
            elif valor < media:
                print('COMPRAR')
            elif valor == media:
                print('COMPRAR')
            
            print('código: ', ativos['código'])
            print('descrição: ', ativos['descrição'])
            print('histórico: ', ativos['histórico'])
            print('quantidade: ', ativos['quantidade'])
        else:
            print('ação não encontrada.')
