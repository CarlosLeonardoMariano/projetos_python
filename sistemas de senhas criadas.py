import time
nome_usuario=input('Nome do Usuario : ').strip()
print('Cadastrando Nome.')
time.sleep(1)
print(f'\033[02;32m{nome_usuario} seu nome foi Cadastrado com Sucesso.')
senha=input('\033[02;37mCadastre sua Senha : ').strip()
print('Cadastrando a sua Senha.')
time.sleep(1)
print('\033[02;32mSenha Cadastrada com Sucesso.')
while True:
    senha_usuario = (input("\033[02;37mDigite uma senha: ").strip())
    print('Conferindo os dados.')
    time.sleep(1)
    if senha == senha_usuario:
        print('\033[02;32m__'*50)
        print(f'\033[02;32mSeja-Bem Vindo {nome_usuario} Seu Cadastro foi Autorizado e sua Entrada Será liberada.')
        print('\033[02;32m__'*50)
        break
    else:
        print('\033[02;31m__'*50)
        print(f"\033[02;31mDescupe {nome_usuario} Más sua Senha Está Incorreta.")
        print('\033[02;31m__'*50)

    