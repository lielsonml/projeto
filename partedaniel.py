# Caixa Eletrônico Inteligente

valor = int(input('Qual será o valor a ser sacado? '))
resto = 0
while True:
    qcem = valor // 100
    resto = valor % 100
    qc = resto // 50
    resto = valor % 50
    qv = resto // 20
    resto = resto % 20
    qd = resto // 10
    resto = resto % 10
    qcinco = resto // 5
    resto = resto % 5
    qu = resto // 1
    resto = resto % 1
    if resto == 0:
        print(f'Serão entregues {qcem} cédulas de R$100.00, {qc} de R$50.00, {qv} de R$20.00, {qd} de R$10.00, {qcinco} de R$5.00 e {qu} moedas de R$1.00')
        break

