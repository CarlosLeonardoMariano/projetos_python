import random
nove_digitos=''
print('______'*27)
for i in range (9):
    nove_digitos+=str(random.randint(0,12)) 

print(f'\033[2;37mNOVO NÚMERO DE CPF GERADO : \033[1;33m{nove_digitos}')
print('\033[2;37m______'*27)

    
contador=11
resultado=0
for digito in nove_digitos:
    contador-=1
    variavel=int(digito) * contador
    resultado+=variavel
    final=(resultado * 10)%11
    final=final if final <=9 else 0
dez_digitos=nove_digitos+str(final)
contador2=12
resultado2=0
for digito2 in dez_digitos:
    contador2-=1
    variavel2=int(digito2)*contador2
    resultado2+=variavel2
    final2=(resultado * 10)%11
    final2=final2 if final2 <=9 else 0
