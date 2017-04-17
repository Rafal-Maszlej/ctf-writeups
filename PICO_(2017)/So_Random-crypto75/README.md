## So_Random [CRYPTO 75]

>We found sorandom.py running at shell2017.picoctf.com:6479. It seems to be outputting the flag but randomizing all the characters first. Is there anyway to get back the original flag?

* [sorandom.py](sorandom.py)

### EN / [PL](#rozwiązanie)

We get the flag right away:

```
$ nc shell2017.picoctf.com 6479
Unguessably Randomized Flag: BNZQ:6m3bd631074ov60jxu1zov1380l3i959
```

Problem is that it is encrypted :-)

Looking at code `sorandom.py` you can see, that to every character from flag is added a random value `random.randrange(0,26)`. Or rather pseudo-random, and since it is also known seed `random.seed("random")`, we can recover the flag using the same settings and simply subtracting the values `random.randrange(0,26)` from the appropriate characters.

So much theories. In practice, I had some problems :-)

Rewritten with minor changes script `sorandom.py` which decrypts the flag:

```python
import random

FLAG = 'BNZQ:6m3bd631074ov60jxu1zov1380l3i959'


random.seed('random')

flag = ''

for c in FLAG:
  if c.islower():
    flag += chr((ord(c)-ord('a')-random.randrange(0,26))%26 + ord('a'))
  elif c.isupper():
    flag += chr((ord(c)-ord('A')-random.randrange(0,26))%26 + ord('A'))
  elif c.isdigit():
    flag += chr((ord(c)-ord('0')-random.randrange(0,10))%10 + ord('0'))
  else:
    flag += c


print(flag)
```

After running did not give expected results.

```
$ python3 decr.py 
LZTY:4o3lh261121ir87ckw4qdl0803t4d444
```

Then I spent some time looking for a non-existent bug, until I finally got an idea, to run the same script in python 2.7.

```
$ python decr.py 
FLAG:3b1fa718577cd90efb2fdf5832b6a849
```

And there is a flag :-)

Where do these divergences come from? It turns out that there are big differences in the `random` module in both versions.
Comparison of console sessions and some links to read [here](random_diff_2v3.md)

### Solution:

### [EN](#solution) / PL

### Rozwiązanie:

Flagę dostajemy od razu:

```
$ nc shell2017.picoctf.com 6479
Unguessably Randomized Flag: BNZQ:6m3bd631074ov60jxu1zov1380l3i959
```

Problem w tym, że jest zaszyfrowana :-)

Przeglądając kod `sorandom.py` można zauważyć, że do każdego znaku z flagi dodawana jest losowa wartość `random.randrange(0,26)`. A raczej pseudolosowa, a skoro ustalony jest również seed `random.seed("random")`, można odzyskać flagę używając tych samych ustawień i po prostu odejmując kolejne wartości `random.randrange(0,26)` od odpowiednich znaków.

Tyle teorii. W praktyce miałem pewne problemy :-)

Przepisany z drobnymi zmianami skrypt `sorandom.py` deszyfrujący flagę:

```python
import random

FLAG = 'BNZQ:6m3bd631074ov60jxu1zov1380l3i959'


random.seed('random')

flag = ''

for c in FLAG:
  if c.islower():
    flag += chr((ord(c)-ord('a')-random.randrange(0,26))%26 + ord('a'))
  elif c.isupper():
    flag += chr((ord(c)-ord('A')-random.randrange(0,26))%26 + ord('A'))
  elif c.isdigit():
    flag += chr((ord(c)-ord('0')-random.randrange(0,10))%10 + ord('0'))
  else:
    flag += c


print(flag)
```

Po uruchomieniu nie dał spodziewanych rezultatów.

```
$ python3 decr.py 
LZTY:4o3lh261121ir87ckw4qdl0803t4d444
```

Spędziłem następnie trochę czasu na szukaniu nieistniejącego buga, aż w końcu wpadłem na pomysł, żeby uruchomić ten sam skrypt w pythonie 2.7.

```
$ python decr.py 
FLAG:3b1fa718577cd90efb2fdf5832b6a849
```

I jest flaga :-)

Skąd te rozbieżności? Okazuje się, że są spore różnice w module `random` w obydwu wersjach.
Porównanie sesji w konsoli oraz kilka linków do poczytania [tutaj](random_diff_2v3.md)
