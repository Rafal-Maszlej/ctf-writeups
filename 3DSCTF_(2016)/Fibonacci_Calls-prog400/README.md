Zadanie z kategorii PROG za 400 punktów.

Trzecie z serii 4 bardzo podobnych zadań:

 * [Different And Notorious Alignment (prog 200)](Different_And_Notorious_Alignment-prog200)
 * [Return Of The Notorious Alignment (prog 300)](Return_Of_The_Notorious_Alignment-prog300)
 * [Fibonacci Calls (prog 400)](Fibonacci_Calls-prog400)
 * [Vibranium Circuit Challenge (prog 400)](Vibranium_Circuit_Challenge-prog400)

Treść zadania:

Access the server in 54.175.35.248:8000


`nc 54.175.35.248 8000` i treść zadania:

```
           +++         Fibonacci challenge               +++

 [+] A fibonacci serie can be represented by the following function:

     Fn = | 0                       if N = 0
          | 1                       if N = 1
          | Fn(N - 1) + Fn(N - 2)   if N > 1

 [+] Given a N value, we want to know how many recursive calls the program do.

 [+] Example with N equal to 3

                               +-------+
                         +-----+ fib 3 +-----+
                         |     +-------+     |  
                         |                   |
                     +---+---+           +---+---+
               +-----+ fib 2 +-----+     | fib 1 +------+
               |     +-------+     |     +-------+      |
               |                   |                    |
           +---+---+           +---+---+           +----+---+
    +------+ fib 1 |    +------+ fib 0 |           | return |
    |      +-------+    |      +-------+           +--------+
    |                   |
+---+----+          +---+----+
| return |          | return |
+--------+          +--------+

 [+] The answer is 4 recursive calls. (you only need to answer 4) 

 [+] To help the resolution, you can inform only the last three numbers
 
 [!] You have 25 seconds to answer each question. 

 [+] To start the challenge inform the number 20:
```

Odpowiedzią są trzy ostatnie cyfry całkowitej liczby wywołań rekurencyjnych funkcji fibonacciego.

W przypadku ciągu fibonacciego liczba wywołań rekurencyjnych rośnie bardzo szybko:

```python
import functools

@functools.lru_cache()
def fibo_count(n):
    if n < 2:
        return 1
    return fibo_count(n-2) + fibo_count(n-1)


for n in [3, 5, 10, 15, 20, 40, 100, 250, 500]:
	answer = str(fibo_count(n)*2-2)
	print('dla n={} ---> {}'.format(n, answer))
```

```
$ python3 count_req.py
dla n=3 ---> 4
dla n=5 ---> 14
dla n=10 ---> 176
dla n=15 ---> 1972
dla n=20 ---> 21890
dla n=40 ---> 331160280
dla n=100 ---> 1146295688027634168200
dla n=250 ---> 25553047145849465172074067789310063797319112894704496
dla n=500 ---> 451183032323872661745025390072144144092022649827516381177277732836949255477373766810031974105593936997250
dla n=1000 ---> 140660735422845631643670509754367099540362539672717465485209810174309074236393867159484498989125223466975500898483531982176372726530900447294212024106748242547734678222396278746251197535380183804490490646807000
```

Nieoceniony jest tutaj pythonowy dekorator `functools.lru_cache()`, który przechowuje wyniki poprzednich wywołań funkcji i w razie kolejnego wywołania funkcji z tymi samymi parametrami po prostu podstawia wynik bez ponownego dokonywania obliczeń.

Skrypt + log:

* [fibo.py](fibo.py)
* [log.txt](log.txt)

I flaga:

```
 [+] Congratulations, the flag is: 3DS{g00d4lgorithmsC4nSaveYourTime}
```
