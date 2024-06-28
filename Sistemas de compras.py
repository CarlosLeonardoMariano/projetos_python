import os
import time


lista = []
while True:
    print('Selecione a opção abaixo : ')
    opção=input('[i]nserir [a]pagar , [l]istar : ')
    if opção == 'i':
     os.system('')
     valor= input('Produtos para adicionar : ')
     print('========'*15)
     lista.append(valor)
     print(f' voce adicionou {len(lista)} novos itens, sua lista foi atualizada  !')
     print('========'*15)
    elif opção == 'a':
     deletar= int(input('Escolha um item que deseja remover : '))
     print('========'*15)
     print(f'voce removeu {len(lista)} item da lista')
    
     print('========'*15)

     try:
      trocar_i_str=(deletar)
      del lista[trocar_i_str]
     except TypeError:
      print('Por favor digite um numero inteiro : ')
     except ValueError:
       print('Codigo inexistente !!')
    elif opção == 'l':
        os.system('')

        print('========'*15)
        if len(lista) == 0:
          print('Nada pra listar !')
        print('========'*15)
          
        print()
    else:
      print('========'*15)
      print('Codigo invalido ! ')
      print('========'*15)
      
    for i ,valor in enumerate (lista):
      print(i,valor)

