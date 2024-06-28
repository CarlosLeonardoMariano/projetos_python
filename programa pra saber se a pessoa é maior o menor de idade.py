import time
totalmaior=0
totalmenor=0
for i in range(1,5):
  nome=int(input('Qual ano a Pessoa nasceu {} :'.format(i)))
  idade=2024-18
  if nome <= idade :
   totalmaior+=1
  else:
    totalmenor+=1
print('ATUALIZANDO LISTAS DOS MAIORES DE IDADE ...')
time.sleep(2)
print('Na lista digitada {} Das Pessoas são maiores de idade e nasceram antes de {} !! '.format(totalmaior,idade))
print('=-'*60)
print('=-'*60)
print('ATUALIZANDO LISTAS DOS MENORES DE IDADE ...')
time.sleep(5)
print('Na Outra lista digitada {} Das Pessoas são menores de idade e nasceram depois de {} !! '.format(totalmenor,idade))
print('=-'*60)
print('=-'*60)