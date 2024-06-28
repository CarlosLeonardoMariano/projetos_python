while True:
 numero=int(input('Digite um numero pra ver a tabuada : '))
 pessoa=input('Deseja continuar ? Aperte [S]im para continuar ou [N]ão para sair :')


 print('_____'*30)
 for c in range(1,11):

  print(f'{numero}X{c} = {numero*c}')


  if pessoa == ('n'):
   print('voce saiu do programa !')
   break
  elif pessoa == ('s'):
    continue
  

 print('_____'*30)

