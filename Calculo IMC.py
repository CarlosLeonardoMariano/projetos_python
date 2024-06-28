import time

nome=str(input('Qual é o seu nome ? '))
peso=float(input('QUAL É O SEU PESO ?'))
altura=float(input('QUAL É A SUA ALTURA ? '))
imc= peso/(altura * altura)

print('O Resultado do seu imc é : {:.3f}'.format(imc))
print('CARREGANDO RESULTADOS ..... ')
time.sleep(1.50)
if imc <= 18.5:
    print('voce esta abaixo do peso ideal {} ...'.format(nome))
elif imc >=18.6 and imc <=24.9 :
    print('VOCE ESTA MEDIA IDEAL {} ...'.format(nome))
elif imc >=25.0 and imc <= 29.9:
    print('VOCE ESTÁ UM POUCO ACIMA DO SEU PESO IDEAL {} ... '.format(nome))
elif imc >= 30.0 and imc <= 34.9:
    print('VOCE ESTÁ EM OBESIDADE GRAU I {} ...'.format(nome))
elif imc >=35.0 and imc <=39.0:
    print('VOCE ESTA EM OBESIDADE GRAU II {} ...'.format(nome))

else:
    print('VOCE ESTÁ EM OBESIDADE GRAU III {} ...'.format(nome))
