# Pedra, papel e tesoura

import random
import time

jkp = ('pedra', 'papel', 'tesoura')
print('Vamos jogar Jokenpô!')
maquina = random.choice(jkp)
user = input('Escolha entre pedra, papel e tesoura: ')
min = user.lower().replace(' ', '').strip()
print('Jo-Ken-Pô')
time.sleep(2)
print('A máquina escolheu {} e você {}' .format(maquina, min))
if maquina == 'pedra' and min == 'pedra':
    print('Empate!')
elif maquina == 'pedra' and min == 'papel':
    print('Papel venceu!')
elif maquina == 'pedra' and min == 'tesoura':
    print('Pedra venceu!')
elif maquina == 'papel' and min == 'pedra':
    print('Papel venceu!')
elif maquina == 'papel' and min == 'papel':
    print('Empate!')
elif maquina == 'papel' and min == 'tesoura':
    print('Tesoura venceu!')
elif maquina == 'tesoura' and min == 'pedra':
    print('Pedra venceu!')
elif maquina == 'tesoura' and min == 'papel':
    print('Tesoura venceu!')
elif maquina == 'tesoura' and min == 'tesoura':
    print('Empate!')