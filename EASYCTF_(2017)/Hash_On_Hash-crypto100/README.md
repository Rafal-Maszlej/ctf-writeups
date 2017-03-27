## Hash_On_Hash [CRYPTO 100]

>There's a lot of hex strings here. Maybe they're hiding a message?

[hexstrings](hexstrings)

### EN / [PL](#rozwiązanie)

### Solution:

The `hexstrings` file contains 1160 lines, each with a 32-character hexadecimal value.

Attempting to read the first line did not give anything interesting:

```
>>> s = 'dd 75 36 79 4b 63 bf 90 ec cf d3 7f 9b 14 7d 7f'.split(' ')
>>> ''.join(chr(int(i, base=16)) for i in s)
'Ýu6yKc¿\x90ìÏÓ\x7f\x9b\x14}\x7f'
```

However, the name itself suggests that the file contains a hashes.

To identify hash type useful was site [www.onlinehashcrack.com](https://www.onlinehashcrack.com/hash-identification.php):

The results suggest that it is highly probable that it is `md5`.

Trying to find plaintext for the first hash using [md5decrypt.net](http://md5decrypt.net/en/) was also a success.

```
"dd7536794b63bf90eccfd37f9b147d7f" == "I"
```

So in each line one character is encoded.
There is nothing else left but write the script:

```python
from hashlib import md5
from string import ascii_letters, digits, punctuation

alphabet = ascii_letters + digits + punctuation + ' ' + '\n'

hash_dict = {md5(bytes(letter, 'utf-8')).hexdigest(): letter for letter in alphabet}


text = ''

for line in open('hexstrings', 'r'):
    try:
        text += hash_dict[line.strip()]
    except KeyError:
        print(line)
        text += ' '
    

print(text)
```

The script first creates a hash dictionary for all printable characters, and then matches each line in `hexstrings` to the appropriate character.

We get a plaintext with a flag at the end.

```
Im far too lazy to put anything meaningful here. Instead, here's some information about what you just solved.
The MD5 algorithm is a widely used hash function producing a 128-bit hash value. Although MD5 was initially designed to be used as a cryptographic hash function, it has been found to suffer from extensive vulnerabilities. It can still be used as a checksum to verify data integrity, but only against unintentional corruption.
Like most hash functions, MD5 is neither encryption nor encoding. It can be cracked by brute-force attack and suffers from extensive vulnerabilities as detailed in the security section below.
MD5 was designed by Ronald Rivest in 1991 to replace an earlier hash function MD4.[3] The source code in RFC 1321 contains a "by attribution" RSA license. The abbreviation "MD" stands for "Message Digest."
The security of the MD5 has been severely compromised, with its weaknesses having been exploited in the field, most infamously by the Flame malware in 2012. The CMU Software Engineering Institute considers MD5 essentially "cryptographically broken and unsuitable for further use".[4]
easyctf{1_h0p3_y0u_d1dn7_d0_7h47_by_h4nd}
```

### [EN](#solution) / PL

### Rozwiązanie:

Plik `hexstrings` zawiera 1160 linii, w każdej jakaś 32-znakowa wartość w formacie hexadecymalnym.

Próba odczytania pierwszego wiersza nie dała nic ciekawego:

```
>>> s = 'dd 75 36 79 4b 63 bf 90 ec cf d3 7f 9b 14 7d 7f'.split(' ')
>>> ''.join(chr(int(i, base=16)) for i in s)
'Ýu6yKc¿\x90ìÏÓ\x7f\x9b\x14}\x7f'
```

Jednak sama nazwa zadania sugeruje, że w pliku znajdują się hashe.

Do identyfikacji hasha przydała się stronka [www.onlinehashcrack.com](https://www.onlinehashcrack.com/hash-identification.php):

Wyniki sugerują, że z dużym prawdopodobieństwem jest to `md5`.

Próba znalezienia tekstu dla pierwszego hasha za pomocą [md5decrypt.net](http://md5decrypt.net/en/) również zakończyła się sukcesem.

```
"dd7536794b63bf90eccfd37f9b147d7f" == "I"
```

A więc w każdej linii zakodowany jest jeden znak.
Nie pozostało już nic innego, jak napisać skrypt:

```python
from hashlib import md5
from string import ascii_letters, digits, punctuation

alphabet = ascii_letters + digits + punctuation + ' ' + '\n'

hash_dict = {md5(bytes(letter, 'utf-8')).hexdigest(): letter for letter in alphabet}


text = ''

for line in open('hexstrings', 'r'):
    try:
        text += hash_dict[line.strip()]
    except KeyError:
        print(line)
        text += ' '
    

print(text)
```

Skrypt tworzy najpierw słownik z hashami dla wszystkich znaków drukowalnych, a potem dopasowuje poszczególne linie z `hexstrings` do odpowiedniego znaku.

Otrzymujemy plaintext z flagą na końcu.

```
Im far too lazy to put anything meaningful here. Instead, here's some information about what you just solved.
The MD5 algorithm is a widely used hash function producing a 128-bit hash value. Although MD5 was initially designed to be used as a cryptographic hash function, it has been found to suffer from extensive vulnerabilities. It can still be used as a checksum to verify data integrity, but only against unintentional corruption.
Like most hash functions, MD5 is neither encryption nor encoding. It can be cracked by brute-force attack and suffers from extensive vulnerabilities as detailed in the security section below.
MD5 was designed by Ronald Rivest in 1991 to replace an earlier hash function MD4.[3] The source code in RFC 1321 contains a "by attribution" RSA license. The abbreviation "MD" stands for "Message Digest."
The security of the MD5 has been severely compromised, with its weaknesses having been exploited in the field, most infamously by the Flame malware in 2012. The CMU Software Engineering Institute considers MD5 essentially "cryptographically broken and unsuitable for further use".[4]
easyctf{1_h0p3_y0u_d1dn7_d0_7h47_by_h4nd}
```
