## Phunky_Python_1 [RE 30]

>The other day we happened upon a dusty old laptop covered in duct tape and surrounded by several papers with notes scrawled all over them. Upon inspection, we found that the laptop contained several python files labeled phunky.
>
>We've determined that each of the files contains a mini reversing challenge. The first task is simple: Find the value of x such that the program prints out easyctf.
>
>phunky1.py

```python
x = 0 # REDACTED
digs = [8407367755427688850, 8407367755427688846, 8407367755427688864, 8407367755427688870, 8407367755427688848, 8407367755427688865, 8407367755427688851]

out = ""
for letter in reversed(digs):
    out = chr(letter - x) + out
print out
```

### EN / [PL](#rozwiązanie)

### Solution:

We have a list of numbers that are slightly different from each other

```python
digs = [8407367755427688850, 
        8407367755427688846, 
        8407367755427688864, 
        8407367755427688870, 
        8407367755427688848, 
        8407367755427688865, 
        8407367755427688851]
```

And what does the for loop do?

```python
for letter in reversed(digs):
    out = chr(letter - x) + out
```

Items are taken from the digs list, but in reverse order reversed(digs).
An unknown value is subtracted from each element, and the whole is converted to a character chr(letter - x).
Finally, the character is added to the front of the resulting string out = chr(letter - x) + out.

The loop can be reduced to a more readable form:

```python
for letter in digs:
    out += chr(letter - x)
```

The program has to print "easyctf", so the first element from digs minus x must be equal to ord('e').

```
>>> 8407367755427688850 - ord('e')
8407367755427688749
```

And this is searched x.


### [EN](#solution) / PL

### Rozwiązanie:

Mamy listę liczb, które nieznacznie różnią się od siebie

```python
digs = [8407367755427688850, 
        8407367755427688846, 
        8407367755427688864, 
        8407367755427688870, 
        8407367755427688848, 
        8407367755427688865, 
        8407367755427688851]
```

A co robi pętla for?

```python
for letter in reversed(digs):
    out = chr(letter - x) + out
```

Brane są elementy z listy digs, ale w odwróconej kolejności reversed(digs).
Od każdego elementu odejmowana jest pewna wartość, a całość przekształcana jest na znak chr(letter - x).
Na końcu znak dodawany jest z przodu wynikowego stringa out = chr(letter - x) + out.

Całość można sprowadzić do nieco bardziej czytelnej postaci:

```python
for letter in digs:
    out += chr(letter - x)
```

Program ma wypisywać "easyctf", więc pierwszy element z digs minus x ma równać się ord('e').

```
>>> 8407367755427688850 - ord('e')
8407367755427688749
```

I to jest szukane x.
