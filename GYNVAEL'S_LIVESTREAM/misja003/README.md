## misja003

>Tym razem nie trzeba nic robić. Wystarczy uruchomić poniższy skrypt, chwilkę<br>
>poczekać, a hasło zostanie wypisane. No, taką dłuższą chwilkę...

```python
#!/usr/bin/python
def magic1(a, b):
    o = 0
    i = 0
    while i < a:
        o += 1
        i += 1
    i = 0
    while i < b:
        o += 1
        i += 1
    return o
def magic2(a, b):
    o = 0
    i = 0
    while i < b:
        o = magic1(o, a)
        i += 1
    return o
n1 = int("2867279575674690971609643216365"
         "4161626212087501848651843132337"
         "3373323997065608342")
n2 = int("1240905467219837578349182398365"
         "3459812983123659128386518235966"
         "4109783723654812937")
n = magic2(magic1(n1, n2), 1337)
print hex(n)[2:-1].decode("hex").splitlines()[0]
```

### Rozwiązanie:

Żeby zmniejszyć nieco czas wykonania skryptu należy uprościć dwie funkcje `magic1` i `magic2`, wewnątrz których znajdują się aż trzy pętle 
`while`!<br>
W obydwu mamy zmienną `o`, która na początku przyjmuje wartość `0`, a po wykonaniu pewnych operacji jest zwracana.

```python
def magic1(a, b):
    o = 0
    i = 0
    while i < a:
        o += 1
        i += 1
    i = 0
    while i < b:
        o += 1
        i += 1
    return o
```

W pierwszym `while` zmienna `o` zwiększa się o jeden w każdej iteracji. Wyjście z pętli następuje w momencie kiedy `i == a`. Można zatem zamiast całej tej 
pętli zapisać `o += a`.<br>
Identyczna sytuacja wygląda z drugą pętla `while`, gdzie do otrzymanej poprzednio wartości `o` dodajemy `1` tyle razy, ile wynosi wartość `b`.

Uproszczona funkcja:

```python
def magic1(a, b):
    return a + b
```

Druga funkcja:

```python
def magic2(a, b):
    o = 0
    i = 0
    while i < b:
        o = magic1(o, a)
        i += 1
    return o
```

Tutaj wszystko wygląda prawie tak samo, z wyjątkiem tego, że zamiast `o += 1` mamy `o = magic1(o, a)`.<br>
Wiadomo już, że `magic1(o, a)` to tak naprawdę `o + a`.<br>
W `magic2` wartość `o` zwiększa się o `a` tyle razy, ile wynosi wartość `b`. Jest to więc zwykłe mnożenie :-)

Funkcja po uproszczeniu:

```python
def magic2(a, b):
    return a * b
```

Teraz już skrypt powinien mieć rozsądny czas wykonania i dać rozwiązanie :-)

```
$ python misja003_solution.py 
Haslo: "WolneOprogramowanie!"
```
