import time
print('{:=^50}'.format(' LOJAS MARIANO '))
preço=float(input('Preço das compras ?'))
print('''FORMAS DE PAGAMENTOS
      [ 1 ] Á VISTÁ DINHEIRO OU CHEQUE !
      [ 2 ] Á VISTA NO CARTÃO !
      [ 3 ] 2X NO CARTÃO !
      [ 4 ] 3X OU MAIS NO CARTÃO !''')
pagamentos=int(input('Qual á forma de Pagamento ?'))
time.sleep(1)
print('carregando no sistema .....')

if pagamentos == 1:
    total= preço - (preço * 10/100)
    print(f'o valor da suas compras a vista é {preço :.2f} é tera um desconto o valor sairá {total :.2f} !!')
elif pagamentos == 2 :
    total= preço - (preço * 5/100)
    print(f'o valor da suas compras a vista é {preço :.2f} Reais e tera um desconto o valor sairá {total :.2f} Reais !!')
elif pagamentos == 3 :
    total = preço
    print(f'o valor da sua compra é {total:.2f} Reais !!')
elif pagamentos == 4:
    cartão= float(input('Em Quantas vezes o SR/A deseja Parcelar ?'))
    print('carregando no sistema .....')
    total= preço + (preço * 20/100)
    print(f'sua compra em {cartão:.0f}X sairá no valor de {total} Reais ! ')
    
else :
    print('Opção invalida de pagamento !')



    


