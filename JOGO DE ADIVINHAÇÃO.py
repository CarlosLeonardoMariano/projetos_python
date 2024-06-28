import random
import time
computador=random.randint(1,10)
print('Sou seu computador ... Acabei de pensar em um numero entre 0 e 10, será que voce consegue adivinhar ? ')
time.sleep(2)
acertou=False
palpite= 0
while not acertou :
   jogador=int(input('Qual é seu palpite ?'))
   print('=-'*10,'CARREGANDO RESULTADOS ','=-'*10)
   time.sleep(0.5)
   palpite += 1
   if jogador == computador:
    acertou= True
   else:
        if jogador > computador :
           print('Palpite Errado, É um numero menor !')
           if jogador < palpite:
               print('Palpite Errado, É um numero maior !')
        
print('Voce acertou em {} tentativas , Meus Parabéns venceu a maquina ! '.format(palpite))