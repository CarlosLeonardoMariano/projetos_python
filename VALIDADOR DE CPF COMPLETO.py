import time
import re
cpf_cliente=input('DIGITE SEU CPF PARA A CONSULTA : ')
cpf_cliente=re.sub(r'[^0-9]','',cpf_cliente)
print('_____'*32)
nove=cpf_cliente[:9]
contador=11
resultado=0

for digito in nove:
    contador-=1
    variavel=int(digito)*contador
    resultado+=variavel
    final=(resultado*10)%11
    final=final if final <=9 else 0
print(final)
dez=cpf_cliente[:9] +str(final)
contador2=12
resultado2=0
for digito2 in dez:
    contador-=1
    variavel2=int(digito2)*contador2
    resultado2+=variavel2
    final2=(resultado2*10)%11
    final2=final2 if final2 <=9 else 0
print(final2)
calculo_cpf_sistema=f'{nove}{final}{final2}'
if cpf_cliente == calculo_cpf_sistema:
    print('_____'*30)
    print(' '*44,'CONSULTADO DADOS DO CPF','AGUARDE UM MOMENTO !')
    time.sleep(3)
    print(' '*50,f'\033[2;32m CPF : {cpf_cliente} É VÁLIDO !')
    print('\033[2;37m_____'*30)
    print('_____'*30)

else:
    print('_____'*30)
    print(' '*44,'CONSULTADO DADOS DO CPF','AGUARDE UM MOMENTO !')
    ''''''
    time.sleep(3)
    print(' '*46,f'\033[2;31mO CPF: {cpf_cliente} CONSTA INVÁLIDO !')
    print('\033[2;37m_____'*30)
    print('_____'*30)