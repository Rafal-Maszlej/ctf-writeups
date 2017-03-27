## Decode_Me [CRYPTO 100]

>Someone I met today told me that they had a perfect encryption method. To prove that there is no such thing, I want you to decrypt this encrypted flag he gave me.

[flag.txt](flag.txt)

### EN / [PL](#rozwiązanie)

### Solution:

In the file we get a string that appears to be encoded in base64.

The console session confirms this:

```
>>> from base64 import b64decode
>>> with open('flag.txt', 'r') as f:
...   data = f.read()
... 
>>> b64decode(data)
b'Vm0wd2QyUXlVWGxWV0d4V1YwZDRWMVl3WkRSV01WbDNXa1JTVjAxV2JETlhhMUpUVmpBeFYySkVU\nbGhoTVVwVVZtcEJlRll5U2tWVQpiR2hvVFZWd1ZWWnFRbUZUTWxKSVZtdGtXQXBpUm5CUFdWZDBS\nbVZHV25SalJVcHNVbXhzTlZVeWRGZFdVW...
```

As a result we get the next base64 string.

A short script decodes the nesting sequences as long as there is something to decode:

```python
from base64 import b64decode

crypt = ''

for line in open('flag.txt', 'r'):
    crypt += line.strip()


while True:
    try:
        crypt2 = str(b64decode(crypt), 'utf-8')
    except:
        print(crypt)
        break
    
    crypt = crypt2
```

After 21 iterations we get the flag:

```
easyctf{what_1s_l0v3_bby_don7_hurt_m3}
```

### [EN](#solution) / PL

### Rozwiązanie:

W pliku dostajemy ciąg znaków, który na pierwszy rzut oka wydaje się być zakodowany w base64.

Sesja w konsoli to potwierdza:

```
>>> from base64 import b64decode
>>> with open('flag.txt', 'r') as f:
...   data = f.read()
... 
>>> b64decode(data)
b'Vm0wd2QyUXlVWGxWV0d4V1YwZDRWMVl3WkRSV01WbDNXa1JTVjAxV2JETlhhMUpUVmpBeFYySkVU\nbGhoTVVwVVZtcEJlRll5U2tWVQpiR2hvVFZWd1ZWWnFRbUZUTWxKSVZtdGtXQXBpUm5CUFdWZDBS\nbVZHV25SalJVcHNVbXhzTlZVeWRGZFdVW...
```

Dodatkowo w wyniku dostajemy następny string base64.

Krótki skrypt dekodujący kolejne zagnieżdżenia, dopóki jest coś do dekodowania:

```python
from base64 import b64decode

crypt = ''

for line in open('flag.txt', 'r'):
    crypt += line.strip()


while True:
    try:
        crypt2 = str(b64decode(crypt), 'utf-8')
    except:
        print(crypt)
        break
    
    crypt = crypt2
```

Po 21 iteracjach dostajemy flagę:

```
easyctf{what_1s_l0v3_bby_don7_hurt_m3}
```
