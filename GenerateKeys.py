from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
from binascii import hexlify



def generate(file):
    #s="Public and Private keys encryption"
    #message = s.encode('ascii')  
    private_key = RSA.generate(4086)
    public_key = private_key.publickey()
    print(type(private_key), type(public_key))
    private_pem = private_key.export_key().decode()
    public_pem = public_key.export_key().decode()
    print(type(private_pem), type(public_pem))
    with open('Keys/'+file+'_sk.pem', 'w') as pr:
        pr.write(private_pem)
    with open('Keys/'+file+'_pk.pem', 'w') as pu:
        pu.write(public_pem)


def getkeys(file):
    pk="Keys/"+file+"_pk.pem"
    sk="Keys/"+file+"_sk.pem"


    pu_key = RSA.import_key(open(pk, 'r').read())
    pr_key = RSA.import_key(open(sk, 'r').read())
    print(type(pr_key), type(pu_key))
    return pu_key,pr_key

def encrypt(pk, message):
    cipher = PKCS1_OAEP.new(key=pk)
    #Encrypting the message with the PKCS1_OAEP object
    message = message.encode('ascii')  
    cipher_text = cipher.encrypt(message)
    print(type(cipher_text))
    return cipher_text

def decrypt(sk, cipher_text):
    decrypt = PKCS1_OAEP.new(key=sk)
    decrypted_message = decrypt.decrypt(cipher_text)
    print(decrypted_message.decode('ascii'))
    return decrypted_message.decode('ascii')


    


if __name__ == '__main__':
    generate('sajid24x7@gmail.com')
    pk,sk=getkeys('d4384c2e7aab2c22eb805c0f48852f23')
    #enc=encrypt(pk,'sajid')
    #decrypt(sk,enc)

"""    
  
    pr_key = RSA.import_key(open('private_pem.pem', 'r').read())
    pu_key = RSA.import_key(open('public_pem.pem', 'r').read())
    
    print(type(pr_key), type(pu_key))
    #Instantiating PKCS1_OAEP object with the public key for encryption
    cipher = PKCS1_OAEP.new(key=pu_key)
    #Encrypting the message with the PKCS1_OAEP object
    cipher_text = cipher.encrypt(message)
    print(cipher_text)
    #Instantiating PKCS1_OAEP object with the private key for decryption
    decrypt = PKCS1_OAEP.new(key=pr_key)
    #Decrypting the message with the PKCS1_OAEP object
    decrypted_message = decrypt.decrypt(cipher_text)
    print(decrypted_message.decode('ascii'))


"""