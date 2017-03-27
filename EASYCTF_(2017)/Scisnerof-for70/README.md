## Scisnerof [FOR 70]

>I found weird file!

[elif](elif)

### EN / [PL](#rozwiązanie)

### Solution:

The first thing that caught my eye was the strange name of the task - "forensics" written backwards.

Check start and end of file:

```
>>> with open('elif', 'rb') as f:
...   data = f.read()
... 
>>> data[:20]
b'\x82`B\xaeDNEI\x00\x00\x00\x00\xb0\xb4&;\xed\xb0\x17.'
>>> data[-20:]
b'B\x02\x00\x00RDHI\r\x00\x00\x00\n\x1a\n\rGNP\x89'
```

At the beginning of the file there is a string `DNEI`, which means `IEND` reading backwards.

At the end there are `RDHI` and `GNP` strings, what gives respectively `IHDR` and `PNG`.

So probably it is a PNG file saved backwards :-)

Script:

```python
with open('elif', 'rb') as f:
	data = f.read()

data = data[::-1]

with open('file', 'wb') as f:
	f.write(data)
```

The result is a valid png file:

![file](file)

Flag:

```
easyctf{r3v3r5ed_4ensics}
```

### [EN](#solution) / PL

### Rozwiązanie:

Pierwsze co rzuciło mi się w oczy, to dziwna nazwa zadania - "forensics" pisane wspak.

Sprawdzenie początku i końca pliku:

```
>>> with open('elif', 'rb') as f:
...   data = f.read()
... 
>>> data[:20]
b'\x82`B\xaeDNEI\x00\x00\x00\x00\xb0\xb4&;\xed\xb0\x17.'
>>> data[-20:]
b'B\x02\x00\x00RDHI\r\x00\x00\x00\n\x1a\n\rGNP\x89'
```

Na początku pliku znajduje się ciąg znaków `DNEI`, co czytając od końca daje `IEND`.

Natomiast na końcu znajdują się ciągi `RDHI` i `GNP`, czyli odpowiednio `IHDR` i `PNG`.

Prawdopodobnie jest to więc plik PNG zapisany wspak :-)

Skrypt:

```python
with open('elif', 'rb') as f:
	data = f.read()

data = data[::-1]

with open('file', 'wb') as f:
	f.write(data)
```

Wynikiem jest poprawny plik png:

![file](file)

Flaga:

```
easyctf{r3v3r5ed_4ensics}
```
