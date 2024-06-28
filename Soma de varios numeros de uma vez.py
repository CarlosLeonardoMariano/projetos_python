import time
print('='*70)
print('='*70)

print('='*10,'APERTE A TECLA 0 PARA SAIR DA OPERAÇÃO !','='*10)

print('='*70)
print('='*70) 
print( 'CARREGANDO ....')
time.sleep(2)

numero = cont = soma = 0
numero=int(input('Numeros digitados : '))
while numero != 0:
    soma+= numero
    cont+=1
    numero=int(input('Numeros digitados : '))


time.sleep(2)
print('Calculado Resultados ......')
print('voce digitou {} numeros e a soma entre eles foi {} !'.format(cont,soma))

