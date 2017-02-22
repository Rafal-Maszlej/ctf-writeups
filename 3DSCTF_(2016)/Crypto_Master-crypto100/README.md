Zadanie z kategorii CRYPTO za 100 punktów.

Treść zadania:

Crypto Master?
John says that he is the master of his personal server. He created a script that talks to him as if it was his disciple. The problem is that in order to access the server, one needs to know the logic used by the script. Access the server and get the flag.
Server: 54.175.35.248:8002


Po połączeniu z serwerem zostajemy przywitani i poproszeni o "autoryzację"

```
    $ nc 54.175.35.248 8002
    Hi! Are you my master?
```

Oczekiwana odpowiedź, to oczywiście "Yes" ;-)

```
    $ nc 54.175.35.248 8002
    Hi! Are you my master?
    Yes
    So prove it! We have a secret code so we can talk secretly.
    I will give you a couple of hints!
    If you give me a C, I give you a W.
    If you give me a F, I give you a T.
    If you give me a Z, I give you a 0(zero).
    So, what if I give you an I? What should you give me?
```

Po podaniu błędnej odpowiedzi serwer zrywa połączenie.

```
    So, what if I give you an I? What should you give me?
    K
    Nah! Youre lame! Get out of here!!
```

Tutaj nie było zbyt wielu możliwości, więc metodą prób i błędów ustaliłem, że chodzi o "Q".

Skrypt przesłał dalszą treść:

```
    So, what if I give you an I? What should you give me?
    Q
    Nice! But this doesnt prove much.
    Translate the following and I shall give to you what youre looking for:
    QYMFRUMYGFUHKTWQJRUHG
```

Żeby ruszyć dalej trzeba było odkryć związek pomiędzy podanymi wcześniej literami:

```
    W --> C
    T --> F
    0 --> Z
    I --> Q
```


Spróbujmy xorowania:

```
>>> d = {'W':'C', 'T':'F', '0':'Z', 'I':'Q'}
>>> def xor(a, b):
...     return ord(a) ^ ord(b)
... 
>>> for item in d.items():
...     print(xor(*item))
... 
18
20
106
24
```

Raczej nie o to chodzi.

Próba różnych innych działań:


```
>>> def ord_calc(a, b):
...     return '+ -- > {}\n- --> {}\n* --> {}\n'.format((ord(a)+ord(b))%256, ord(a)-ord(b), (ord(a)*ord(b))%256) + '*'*15
... 
>>> for item in d.items():
...     print(ord_calc(*item))
... 
+ --> 154
- --> 14
* --> 248
***************
+ --> 154
- --> 20
* --> 197
***************
+ --> 138
- --> -42
* --> 224
***************
+ --> 154
- --> -8
* --> 25
***************
```

Już lepiej. Dla dodawania dostajemy taki sam wynik we wszystkich przypadkach, oprócz przekształcenia 0 (zero) --> Z
Jako, że w zaszyfrowanym tekście ("QYMFRUMYGFUHKTWQJRUHG") nie było żadnych cyfr, postanowiłem tę anomalię zignorować.

```
>>> def decrypt(char):
...     return chr(154-ord(char))
... 
>>> print(''.join(decrypt(char) for char in "QYMFRUMYGFUHKTWQJRUHG"))
IAMTHEMASTEROFCIPHERS
```

Trafienie :-)

Odpowiedź serwera z flagą:

```
    Hello my master! Here is what you seek: 3DS{M4st3r_My_455}.
```
