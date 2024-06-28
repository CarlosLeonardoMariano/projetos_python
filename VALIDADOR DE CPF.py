text= 'VALIDADOR DE CPF '
meio= text.center(150) 
print("-----"*33)
print(meio)
print("-----"*33)
cpf = input( 'DIGITE SEU CPF : ')
nove_digitos = cpf[:9]
contador = 10
resultado = 0

intermediarios = []

for digito in nove_digitos:
    intermediario = int(digito) * contador
    intermediarios.append(intermediario)
    resultado += intermediario
    contador -= 1
digito=(resultado*10)%11
digito=digito if digito <= 9 else 0
print(contador)



