## Useless_Python [RE 50]

>Boredom took over, so I wrote this python file! I didn't want anyone to see it though because it doesn't actually run, so I used the coolest base-16 encoding to keep it secret.

[python](useless.py)

### EN / [PL](#rozwiązanie)

### Solution:

First of all, we need to decode the script.
Two lines in python handle the case:

```python
s = [s[i:i+2] for i in range(0, len(s), 2)]
s = ''.join(chr(int(i, base=16)) for i in s)
```

First line divides the encoded string into two-character parts and writes everything to a list.

Next, each item in the list is first converted to int in a decimal system, then to a char, and then the whole is combined into one string.

Result:

```python
exec(chr(101)+chr(120)+chr(101)+chr(99)+chr(40)+chr(99)+...+chr(49)+chr(41)+chr(41))
```

We have the `exec` function, which contains an unknown string.
After checking the first four characters can be seen that inside there is another exec.

```
>>> chr(101)+chr(120)+chr(101)+chr(99)
'exec'
```

As it is unknown how deeply nested exec's are, I created a loop, where in every iteration the `exec` part is cut off,
then the rest is processed into a list and then each item to a char. Finally, the whole is concatenated back into string.
I assumed here that `exec` has only `chr` functions inside it, otherwise the script would return an error.

Below the entire script:

```python
with open('useless.py', 'r') as f:
    data = f.read()

s = data.strip()
s = [s[i:i+2] for i in range(0, len(s), 2)]
s = ''.join(chr(int(i, base=16)) for i in s)

while True:
    print(s)
    
    if s.startswith('exec'):
        s = s[5:-1].split('+')
        s = ''.join([chr(int(i.strip('chr(').strip(')'))) for i in s])
    else:
        break
```

Just 4 iterations and got a decoded script with flag:

```python
flag = 'easyctf{python_3x3c_exec_3xec_ex3c}'
priint flag
```

### [EN](#solution) / PL

### Rozwiązanie:

Przede wszystkim trzeba rozkodować skrypt.
Dwie linie w pythonie załatwiają sprawę:

```python
s = [s[i:i+2] for i in range(0, len(s), 2)]
s = ''.join(chr(int(i, base=16)) for i in s)
```

Pierwsza linia dzieli zakodowany ciąg na dwuznakowe części i zapisuje wszystko do listy.

Dalej każdy element z listy jest najpierw zamieniany na inta w systemie dziesiętnym, potem na znak, a potem całość łączona jest w jeden napis.

Wynik:

```python
exec(chr(101)+chr(120)+chr(101)+chr(99)+chr(40)+chr(99)+...+chr(49)+chr(41)+chr(41))
```

Mamy funkję `exec`, wewnątrz której znajduje się nieznany ciąg znaków.
Po sprawdzeniu pierwszych czterech znaków widać, że wewnątrz jest jeszcze jeden exec.

```
>>> chr(101)+chr(120)+chr(101)+chr(99)
'exec'
```

Jako, że niewiadomo jak mocno zagnieżdżone są exec-i, stworzyłem pętlę, w której w każdej iteracji obcinana jest część `exec`, 
potem reszta przerabiana jest na listę i dalej każdy z elementów na znak. Na końcu całość sklejana jest spowrotem w napis.
Założyłem tutaj, że wewnątrz `exec` znajdują się same funkcje `chr`, w przeciwnym wypadku skrypt zwróciłby błąd.

Poniżej cały skrypt:

```python
with open('useless.py', 'r') as f:
    data = f.read()

s = data.strip()
s = [s[i:i+2] for i in range(0, len(s), 2)]
s = ''.join(chr(int(i, base=16)) for i in s)

while True:
    print(s)
    
    if s.startswith('exec'):
        s = s[5:-1].split('+')
        s = ''.join([chr(int(i.strip('chr(').strip(')'))) for i in s])
    else:
        break
```

Wystarczyły 4 iteracje i dostałem rozkodowany skrypt z flagą:

```python
flag = 'easyctf{python_3x3c_exec_3xec_ex3c}'
priint flag
```
