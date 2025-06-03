import math
import emoji
import random
import time
import os
import threading
import tkinter as tk
 
def abrir_calculadora():
    principal = tk.Toplevel(janela)
    principal.title =('Calculadora')
    principal.geometry('350x400')
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
    if teste == '2':
        print('Vamos calcular seu IMC!')
        print('')
        peso = float(input('Digite seu peso: '))
        altura = float(input('Digite sua altura: '))   
        imc = peso / (altura **2)
        if imc < 18.5:
            print(f'Seu Imc é: {imc:.2f} e você está abaixo do peso')
        elif imc >= 18.5 and imc < 24.9:
            print(f'Seu Imc é: {imc:.2f} e você está com o peso normal')
        elif imc >= 25:
            print(f'Seu Imc é: {imc:.2f} e você está acima do peso')      
        print('')   

    if teste == '3':
        simbolos = ["🍒","🔔","💎","⭐","🍊","🍇"]
        def timezle():
            os.system('cls' if os.name == 'nt' else 'clear')

        print('bem-vindo ao jogo caça-níquel!')
        while True:
            input('Pressione enter para girar...')
        # Animação dos giros
            for _ in range(10):
                a, b, c = random.choices(simbolos, k=3)
                timezle()
                print(f"| {a} | {b} | {c} |")
                time.sleep(0.3)
        # Resultado do último giro
            print('\nResultado:')
            if a == b == c:
                print("🏆 Parábens!! Quanta Sorte!")
            elif a == b or a == c or b == c:
                print("✨ boa! Dois símbolos iguais!")
            else:
                print("😢 que pena! Tente novamente")
            break
    continuacao = input('Você quer continuar jogando? (sim/não): ')
    if continuacao != 'sim':
            print('Obrigado, tente novamente quando quiser!')
            break
janela = tk.Tk()




janela.mainloop()