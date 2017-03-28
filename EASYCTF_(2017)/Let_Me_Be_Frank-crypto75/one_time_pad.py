from string import ascii_lowercase
from itertools import cycle


alphabet = ascii_lowercase

def encrypt(plain, key):
	cipher = ''
	key = cycle(key)

	for i in plain:
		char = i
		i = alphabet.find(i.lower())

		if i == -1:
			cipher += char
			continue
			
		j = next(key)
		j = alphabet.find(j.lower())
		c = alphabet[(i + j) % 26]

		if char.isupper():
			c = c.upper()
		cipher += c

	return cipher

def decrypt(cipher, key):
	plain = ''
	key = cycle(key)

	for i in cipher:
		char = i
		i = alphabet.find(i.lower())

		if i == -1:
			plain += char
			continue
			
		j = next(key)
		j = alphabet.find(j.lower())
		c = alphabet[(i - j) % 26]

		if char.isupper():
			c = c.upper()
		plain += c

	return plain
	
def crack(plain, cipher):
	key = ''

	for i, j in zip(plain, cipher):
		i = alphabet.find(i.lower())
		j = alphabet.find(j.lower())

		if i == -1:
			continue

		for k in range(26):
			if (i + k) % 26 == j:
				key += alphabet[k]
				break
	
	for i in range(1, len(key)):
		if key[:i] == key[i:i+i]:
			if key[i-1] == key[i]:
				continue
			else:
				key = key[:i]
				break

	return key



if __name__ == '__main__':
	
	plain = 'HelLo W0rLd a Ala ma k0T4'
	key = 'secret'
	
	print('plaintext: ', plain)
	print('key: ', key)
	print('-'*40)
	
	cipher = encrypt(plain, key)
	print('ciphertext: ', cipher)
	
	plain = decrypt(cipher, key)
	print('decrypted: ', plain)
	
	key = crack(plain, cipher)
	print('cracked key: ', key)
