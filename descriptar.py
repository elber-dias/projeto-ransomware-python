CRIAR ARQUIVO COM O CÓDIGO PARA DESCRIPTOGRAFAR

* As informações abaixo são para a criação do arquivo "descriptar.py"

(user-kaly@kali-vbox)-[~]
$ nano descriptar.py

import os
import pyaes

# ABRIR e LER o conteúdo do arquivo criptografado
arqv_name = "teste.txt.ransomwaretroll"
arqv = open(arqv_name, "rb")
arqv_data = arqv.read()
arqv.close()

# CRIAR chave de descriptografia
key = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(key)
decrypt_data = aes.decrypt(arqv_data)

## REMOVER o arquivo
os.remove(arqv_name)

# ESCREVER e SALVAR/SAIR o arquivo descriptografado
new_arqv = "teste.txt"
new_arqv = open(f'{new_arqv}', "wb")
new_arqv.write(decrypt_data)
new_arqv.close()

## SALVAR O ARQUIVO E SAIR DO NANO ##
ctrl o
crtl x
