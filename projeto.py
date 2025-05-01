import emoji
while True:
    print(emoji.emojize('Bem-vindo ao nosso projeto! :smiley:', language='alias'))
    print('Digite 1 para usar calculadora')
    print('Digite 2 para calcular imc')
    print('Digite 3 para jogar jogo de adivinhação')
    print('digite 4 para descobrir tabuada de um número')
    print('')

    teste = input('Digite o número da opção desejada: ')
    if teste == '1':
        print('Qual opção você deseja?')
        print('')
        print('opção 1 = soma')
        print('opção 2 = subtração')
        print('opção 3 = multiplicação')
        print('opção 4 = divisão')
        print('opção 5 = raiz quadrada de um número')
        print('')
        
        calculadora = input('digite sua opção: ')
        print('')
        if calculadora == '1':
            num1 = float(input('Digite o primeiro número: '))
            num2 = float(input('Digite o segundo número:  '))
            resultado = num1 + num2
            print(f'O resultado da soma deu: {resultado}')
        elif calculadora == '2':
            num1 = float(input('Digite o primeiro número: '))
            num2 = float(input('Digite o segundo número:  '))
            resultado = num1 - num2
            print(f'O resultado da subtração deu: {resultado}')
        elif calculadora == '3':
            num1 = float(input('Digite o primeiro número: '))
            num2 = float(input('Digite o segundo número: '))
            resultado = num1 * num2
            print(f'O resultado da multiplicação deu: {resultado}')
        elif calculadora == '4':
            num1 = float(input('Digite o primeiro número: '))
            num2 = float(input('Digite o segundo número: '))
            resultado = num1 / num2
            print(f'O resultado da divisão deu: {resultado}')
        elif calculadora == '5':
            import math
            num1 = float(input('Digite o número: '))
            resultado = math.sqrt(num1)
            print(f'O resultado da raiz quadrada deu: {resultado}')
        else:
            print('Opção inválida')
        continuação = input('Deseja continuar? (sim/não): ').lower().strip()
        print('')
        if continuação == 'sim':
            print('Escolha qual alternativa você deseja? ')
        else:
            print('Obrigado, tente novamente quando quiser!')
            break
       


