import random
v=0
while True:
    jogador= int(input('digite um numero :'))
    computador=random.randint(0,10)
    total=jogador+computador
    tipo=' '
    while tipo not in 'PpIi':
        tipo=str(input('Par ou Impar [P/I]: ')).strip().upper()
        
    print(f'Voce jogou o numero {jogador} e a maquina jogou o numero {computador} o resultado {total} ! ',end=' ')
    print('DEU PAR 'if total % 2 == 0 else 'Deu IMPAR')
    if tipo == 'P':
     if total %2==0:
      print('\033[2;32mVoce venceu ! Parabéns..')
      v+=1
     else:
        print('\033[2;31mPerdeu...')
        break
       
    elif tipo == 'I':
       if total % 2 == 1:
          print('\033[2;32mVoce venceu !')
          v+=1
       else:
             print('\033[2;31mvoce perdeu  ...')
             break
       print('vamos jogar novamente ?')
print(f'Game over ! voce venceu {v} vezes !')
          
