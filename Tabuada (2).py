import time
print('=-' *50)
numero= int(input('DIGITE UM NUMERO ?'))

print('''CARREGANDO RESULTADOS.......
AGUARDE UM MOMENTO !!!'''
      )
time.sleep(3)
for c in range(1,11):

    time.sleep(0.5)
    print(' {} x {}  = {}'.format(numero,c,numero*c))
print('=-'*50)
