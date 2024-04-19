import rsa
from rsa import key, common



def convert(public_key_str, private_key_str):
	print(public_key_str)


	pk="-----BEGIN RSA PUBLIC KEY-----\n..."+public_key_str+"...\n-----END RSA PUBLIC KEY-----";
	sk="-----BEGIN RSA PRIVATE KEY-----\n..."+private_key_str+"...\n-----END RSA PRIVATE KEY-----";

	# Convert the strings to PublicKey and PrivateKey objects
	public_key = key.PublicKey.load_pkcs1_openssl_pem(pk.encode('utf-8'))
	private_key = key.PrivateKey.load_pkcs1(sk.encode('utf-8'))

	print(type(public_key))
	return publicKey, privateKey


publicKey, privateKey = rsa.newkeys(512)
#pk=str(publicKey)
#sk=str(privateKey)
#pk, sk=convert(pk,sk)
message = "hello geeks"


encMessage = rsa.encrypt(message.encode(),pk)

print("original string: ", message)
print("encrypted string: ", encMessage)

decMessage = rsa.decrypt(encMessage, sk).decode()

print("decrypted string: ", decMessage)

