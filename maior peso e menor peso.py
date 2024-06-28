maior=0
menor=0

for peso in range(1,4):
    pergunta=float(input('qual é seu peso ?'))
    if peso == 1:
        maior=pergunta
        menor=pergunta
    else:
        if pergunta > peso:
         maior = pergunta  
         if pergunta <peso:
            menor = pergunta  
print('maior peso {} '.format(maior))
print('menor peso {} '.format(menor))