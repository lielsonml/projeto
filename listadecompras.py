# Lista de compras


lista_compras = []

indice = 0

while True:
    print('Escolha uma das opções: ')
    print('[1] Adicionar item')
    print('[2] Remover item')
    print('[3] Mostrar lista')
    print('[4] Sair')
    opcao = int(input('>>> Escolha: '))
    if opcao == 1:
        add = input('Qual o nome do produto que você deseja adicionar? ')
        if add not in lista_compras:
            lista_compras.append(add)
        elif add in lista_compras:
            print('Esse produto já está na lista.')
    elif opcao == 2:
        rem = input('Qual o nome do produto que você deseja remover da lista? ')
        if rem in lista_compras:
            lista_compras.remove(rem)
        elif rem not in lista_compras:
            print('Esse item não está na lista.')
    elif opcao == 3:
        for item in lista_compras:
            indice += 1
            print(f'{indice}. {item} ')
    elif opcao == 4:
        print('Fim do programa. Até logo :)')
        break
    elif opcao != 4 and opcao != 3 and opcao != 2 and opcao != 1:
        print('Escolha uma das opções: ')
        print('[1] Adicionar item')
        print('[2] Remover item')
        print('[3] Mostrar lista')
        print('[4] Sair')
        opcao = int(input('>>> Escolha: '))