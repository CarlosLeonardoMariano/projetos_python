import secrets
import time     
while secrets.token_hex :
    time.sleep(2)
    print('\033[1;40mSUA NOVA SENHA É : {}'.format(secrets.token_hex(12)))
