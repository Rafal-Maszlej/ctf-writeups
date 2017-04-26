## Fzz_Buzz_2 [PROG 200]

>Oh no! Two of my keys are broken! Please help me make the same Fzz Buzz program, sans that one letter and queston marks.
>
>As a side note, use of eval() and exec() is also frowned upon and will be marked invalid.

### EN / [PL](#rozwiązanie)

### Solution:

There were 4 programming languages available: python, c, c ++ and java.

The task was to write `FizzBuzz` without using `?` and one letter, and judging by the name of the task, this letter was `i` :-)

On ctf there was also the task `Fizz_Buzz_1` - classically:

```python
n = int(input())

for i in range(1, n+1):
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)
```

Well, there is a lot of useful words containing `i`: `int`, `input`, `if`, `print`... Looking for a solution was fun :-)

The first thing that came to mind was `__builtins__`.

```
>>> __builtins__
<module 'builtins' (built-in)>
>>> dir(__builtins__)
['ArithmeticError', 'AssertionError', 'AttributeError', 
(...)
'abs', 'all', 'any', 'ascii', 'bin', 'bool', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit', 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip']
```

There is almost everything you need.

You just had to find a way to use these functions as strings that you can format.

```
>>> __builtins__.print('hello')
hello
>>> __builtins__.__dict__['print']('hello')
hello
>>> __builtins__.__dict__['pr{}nt'.format(chr(105))]('hello')
hello
```

And in this place I realized that I could not call `__builtins__` directly because it has two `and` in it...

Fortunately, there are as many as three dictionaries available, from which you can use any - `vars ()`, `locals ()` and `globals ()`.

```
>>> vars()
{'__package__': None, '__name__': '__main__', '__spec__': None, '__builtins__': <module 'builtins' (built-in)>, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__doc__': None}
>>> a = 'ala ma kota'
>>> vars()
{'__package__': None, 'a': 'ala ma kota', '__name__': '__main__', '__spec__': None, '__builtins__': <module 'builtins' (built-in)>, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__doc__': None}
>>> vars()['a']
'ala ma kota'
```

So further:

```
>>> vars()['__builtins__'].__dict__['pr{}nt'.format(chr(105))]('hello')
hello
>>> vars()['__bu{}lt{}ns__'.format(chr(105), chr(105))].__dict__['pr{}nt'.format(chr(105))]('hello')
hello
```

Now the biggest problem turned out to be `__dict__`...

Salvage has turned out to be a built-in function `getattr()`. It extracts from the given object the given attribute.

```
>>> getattr(__builtins__, 'print')
<built-in function print>
>>> getattr(__builtins__, 'print')('hello')
hello
>>> getattr(vars()['__bu{}lt{}ns__'.format(chr(105), chr(105))], 'pr{}nt'.format(chr(105)))('hello')
hello
```

A little python magic and the task almost done, `int` and `input` can be obtained in the same way :-)

There is still an issue of `if`.

In Python the conditions can be written in an interesting alternative way:

```
>>> if 1 < 2:
...   'true'
... 
'true'
>>> ('false', 'true')[1 < 2]
'true'
>>> ('false', 'true')[1 > 2]
'false'
```

And the script ready to solve the task :-)

```python
jnt = getattr(vars()['__bu{}lt{}ns__'.format(chr(105), chr(105))], '{}nt'.format(chr(105)))
jnput = getattr(vars()['__bu{}lt{}ns__'.format(chr(105), chr(105))], '{}nput'.format(chr(105)))
prjnt = getattr(vars()['__bu{}lt{}ns__'.format(chr(105), chr(105))], 'pr{}nt'.format(chr(105)))
n = jnt(jnput())
tuple(map(lambda j: prjnt((j,('', 'F{}zz'.format(chr(105)))[j%3==0] + ('', 'Buzz')[j%5==0] )[j%3==0 or j%5==0]), range(1, n+1)))
```

### [EN](#solution) / PL

### Rozwiązanie:

Dostępne były 4 języki programowania: python, c, c++ i java.

Zadanie polegało na napisaniu programu `FizzBuzz`, nie używając `?` i jednej litery, a sądząc po nazwie zadania tą literą było `i` :-)

Na ctfie było też zadanie `Fizz_Buzz_1` - klasycznie:

```python
n = int(input())

for i in range(1, n+1):
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)
```

Cóż, dużo tu przydatnych słów zawierających `i`: `int`, `input`, `if`, `print`... Szukanie rozwiązania było fajną zabawą :-)

Pierwsze co przyszło mi na myśl, to `__builtins__`.

```
>>> __builtins__
<module 'builtins' (built-in)>
>>> dir(__builtins__)
['ArithmeticError', 'AssertionError', 'AttributeError', 
(...)
'abs', 'all', 'any', 'ascii', 'bin', 'bool', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit', 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip']
```

Znajduje się tam prawie wszystko co potrzebne.

Trzeba było tylko znaleźć sposób na użycie słów kluczowych jako stringów, które można formatować.

```
>>> __builtins__.print('hello')
hello
>>> __builtins__.__dict__['print']('hello')
hello
>>> __builtins__.__dict__['pr{}nt'.format(chr(105))]('hello')
hello
```

I w tym miejscu zdałem sobie sprawę, że nie mogę wprost wywołać `__builtins__` bo ma w sobie przecież nawet dwie `i`...

Na szczęście łatwo dostępne są aż trzy słowniki, z których na potrzeby zadania można skorzystać z dowolnego: `vars()`, `locals()` i `globals()`.

```
>>> vars()
{'__package__': None, '__name__': '__main__', '__spec__': None, '__builtins__': <module 'builtins' (built-in)>, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__doc__': None}
>>> a = 'ala ma kota'
>>> vars()
{'__package__': None, 'a': 'ala ma kota', '__name__': '__main__', '__spec__': None, '__builtins__': <module 'builtins' (built-in)>, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__doc__': None}
>>> vars()['a']
'ala ma kota'
```

A więc dalej:

```
>>> vars()['__builtins__'].__dict__['pr{}nt'.format(chr(105))]('hello')
hello
>>> vars()['__bu{}lt{}ns__'.format(chr(105), chr(105))].__dict__['pr{}nt'.format(chr(105))]('hello')
hello
```

Teraz największym problemem okazał się `__dict__`...

Zbawienna okazała się wbudowana funkcja `getattr()`. Wyciąga z danego obiektu dany atrybut.

```
>>> getattr(__builtins__, 'print')
<built-in function print>
>>> getattr(__builtins__, 'print')('hello')
hello
>>> getattr(vars()['__bu{}lt{}ns__'.format(chr(105), chr(105))], 'pr{}nt'.format(chr(105)))('hello')
hello
```

Trochę pythonowej magii i zadanie prawie zrobione, `int` i `input` można pozyskać w ten sam sposób :-)

Pozostaje jeszcze kwestia `if`.

W Pythonie warunki można zapisać w pewien ciekawy alternatywny sposób:

```
>>> if 1 < 2:
...   'true'
... 
'true'
>>> ('false', 'true')[1 < 2]
'true'
>>> ('false', 'true')[1 > 2]
'false'
```

No i gotowy skrypt rozwiązujący zadanie :-)

```python
jnt = getattr(vars()['__bu{}lt{}ns__'.format(chr(105), chr(105))], '{}nt'.format(chr(105)))
jnput = getattr(vars()['__bu{}lt{}ns__'.format(chr(105), chr(105))], '{}nput'.format(chr(105)))
prjnt = getattr(vars()['__bu{}lt{}ns__'.format(chr(105), chr(105))], 'pr{}nt'.format(chr(105)))
n = jnt(jnput())
tuple(map(lambda j: prjnt((j,('', 'F{}zz'.format(chr(105)))[j%3==0] + ('', 'Buzz')[j%5==0] )[j%3==0 or j%5==0]), range(1, n+1)))
```
