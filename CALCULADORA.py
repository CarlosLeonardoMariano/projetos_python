import time
opcao=0
while opcao !=5:
    n1=int(input('Digite o Primeiro Digito : '))
    n2=int(input('Digite o Segundo Digito : '))
    print(""" ESCOLHA UM ABAIXO 
          [ 1 ] SOMAR 
          [ 2 ] SUBTRAIR
          [ 3 ] MULTIPLICAÇÃO
          [ 4 ] DIVISÃO
          [ 5 ] SAIR DO PROGRAMA""")
    opcao = int(input('Qual opção acima deseja ? '))
    print('Carregando Resultados !!')
    time.sleep(2)
    if opcao ==1:
     n1+n2
     resultado=n1+n2
     print('A Soma do {} + {} = {}'.format(n1,n2,resultado))
    elif opcao == 2:
     n1-n2
     resultado=n1-n2
     print('A Subtração do {} - {} = {}'.format(n1,n2,resultado))
       
    elif opcao == 3 :
      n1*n2
      resultado=n1 * n2
      print('A Subtração do {} * {} = {}'.format(n1,n2,resultado))

    elif opcao == 4:
      n1 / n2
      resultado=n1/n2
      print('A Subtração do {} / {} = {}'.format(n1,n2,resultado))
    elif opcao == 5:
      print('VOCÊ SAIU DO PROGRAMA VOLTE SEMPRE !')
    else:
      print('OPÇÃO INVALIDA ! TENTE NOVAMENTE..')
print('=='* 50)

    