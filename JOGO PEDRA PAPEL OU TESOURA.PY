import time
import random
itens= 'Pedra','Papel','Tesoura'
computador= random.randint(0,2)
print('''SUAS OPÇÕES
      [ 0 ] PEDRA
      [ 1 ] PAPEL
      [ 2] TESOURA''')
jogador = int(input('QUAL É A SUA JOGADA ? '))

print('-='*60)

print('{:.^50}'.format (' JO '))
time.sleep(1)
print('{:.^50}'.format (' QUE '))
time.sleep(1)
print('{:.^50}'.format (' PO '))
time.sleep(1)


print('-='*60)

print('o computador escolheu o item {}'.format(itens[computador]))

print('o jogador escolheu o item {}'.format(itens[jogador]))
print('{:=^125}'.format(''))
print('Carregando Resultados .......')
time.sleep(3)

if jogador == computador:
    print('empate')
elif jogador == 0 and computador == 1:
    print('O Computador venceu')
elif jogador == 0 and computador == 2:
    print('O Jogador Venceu !!')
elif jogador == 1 and computador == 0:
    print('O Jogador Venceu !!')
elif jogador == 1 and computador == 2:
    print('O computador Venceu !!')
elif jogador == 2 and computador == 0:
    print('O computador Venceu !!')
elif jogador == 2 and computador == 1:
    print('O jogador  Venceu !!')
else:
    print('Jogada invalida !!')


