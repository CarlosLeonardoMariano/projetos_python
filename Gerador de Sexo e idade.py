sexo = str(input('Digite seu sexo [M / F] :')).strip().upper()[0]
idade = int (input('Digite sua idade :'))


while sexo  != 'M' and sexo != 'F' :
 sexo = str(input('DADOS INVALIDOS: POR FAVOR DIGITE SEU SEXO :')).strip().upper()[0]
print('SEXO {} CADASTRADO COM SUCESSO !  '.format(sexo))

while idade >= 200:
 idade = int(input('DADOS INVALIDOS: POR FAVOR DIGITE Sua idade :'))
print('VOCE TEM {} ANOS ! SUA IDADE FOI CADASTRADO COM SUCESSO !  '.format(idade))



