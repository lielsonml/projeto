# Caixa Eletrônico Inteligente

valor = int(input('Qual será o valor a ser sacado? '))
resto = 0
while True:
    notasdecem = valor // 100
    resto = valor % 100
    notasdecinquenta = resto // 50
    resto = valor % 50
    notasdevinte = resto // 20
    resto = resto % 20
    notasdedez = resto // 10
    resto = resto % 10
    notasdecinco = resto // 5
    resto = resto % 5
    moedasdeum = resto // 1
    resto = resto % 1
    if resto == 0:
        print(f'Serão entregues {notasdecem} cédulas de R$100.00, {notasdecinquenta} de R$50.00, {notasdevinte} de R$20.00, {notasdedez} de R$10.00, {notasdecinco} de R$5.00 e {moedasdeum} moedas de R$1.00')
        break

