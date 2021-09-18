from cryptography.fernet import Fernet
tamanhoHash = 0
def enviar(mensagem, segredo, chave):
    mensagemMaisSegredo = mensagem + segredo
    mensagemHash = mensagem + str(hash(mensagemMaisSegredo))
    with open('teste.txt', 'wb') as encrypted_file:
        encrypted_file.write(bytes(mensagemHash, encoding='utf8')) 
    fernet = Fernet(chave)
    with open('teste.txt', 'rb') as file:
        original = file.read()
    encrypted = fernet.encrypt(original)
    with open('teste.txt', 'wb') as encrypted_file:
        encrypted_file.write(encrypted)
    global tamanhoHash 
    tamanhoHash = len(str(hash(mensagemMaisSegredo)))
    return str(encrypted)
def receber(mensagemCifrada, segredo, chave):
    fernet = Fernet(chave)
    with open('teste.txt', 'rb') as file:
        mensagemCifrada = file.read()
    decrypted = fernet.decrypt(mensagemCifrada)
    with open('teste.txt', 'wb') as dec_file:
        dec_file.write(decrypted)
    Hash = decrypted[-tamanhoHash: ]
    Hash = str(Hash)
    Hash = Hash.replace("b'", "")
    Hash = Hash.replace("'", "")
    mensagem = decrypted[0:-tamanhoHash]
    mensagem = str(mensagem)
    mensagem = mensagem.replace("b'", "")
    mensagem = mensagem.replace("'", "")
    mensagemMaisSegredo = str(mensagem) + segredo
    mensagemHash = str(hash(mensagemMaisSegredo))
    return (mensagem if mensagemHash == Hash else "NULL")
    
def main():
    key = Fernet.generate_key()
    with open('filekey.key', 'wb') as filekey:
        filekey.write(key)
    
    mensagemCifrada = enviar('abc','cde',key)
    print(receber(mensagemCifrada,'cde',key))

    
if __name__ == "__main__":
    main()
