## Risky_Business [EXP 100]

>We wanted to branch into the casino business, but human employees are too expensive so we decided to automate it. I feel like we missed something obvious though... Oh well! Here's the binary: [casino](casino)
>
>Solve this problem by logging into the shell server and navigating to /problems/casino.

### EN / [PL](#rozwiązanie)

### Solution:

This task I was able to solve without analyzing the executable file. I logged on to the shells on the cft site, launched the program, and ... so I got gambling that I finished after winning the flag ;-) What did not take too much time.

After launching the casino I was greeted and asked to bet:

```
user74638@easyctf:/problems/casino$ ./casino
Welcome to the EasyCTF 2017 Casino
Try your luck and gain access to our exclusive club!

Your net worth is: $100000
Please enter how much you would like to bet:
1
Sorry, I'm afraid you've lost :(
```

```
Your net worth is: $99997
Please enter how much you would like to bet:
99997
Congratulations, you won!
```

You could bet a certain amount and then win or lose. If we win we get 2x as much as we bet.

After several program launches it was noted that the winning and losing sequences are always the same.

Full game record [here](log)

Flag:

```
easyctf{m4by3_w3_c0u1d_h4v3_d0n3_th47_b3t7er}
```

### [EN](#solution) / PL

### Rozwiązanie:

To zadanie udało mi się zrobić bez analizy pliku wykonywalnego. Zalogowałem się na shella na stronie cftu, uruchomiłem program i... tak wciągnął mnie hazard, że skończyłem po zdobyciu flagi ;-) Co nie zajęło zbyt dużo czasu.

Po włączeniu kasyna zostałem przywitany i poproszony o obstawianie:

```
user74638@easyctf:/problems/casino$ ./casino
Welcome to the EasyCTF 2017 Casino
Try your luck and gain access to our exclusive club!

Your net worth is: $100000
Please enter how much you would like to bet:
1
Sorry, I'm afraid you've lost :(
```

```
Your net worth is: $99997
Please enter how much you would like to bet:
99997
Congratulations, you won!
```

Można obstawić pewną kwotę, a potem wygrać lub przegrać. W razie wygranej dostajemy 2x tyle ile obstawiliśmy.

Po kilku uruchomieniach programu dało się zauważyć, że sekwencje wygranych i przegranych są zawsze te same.

Pełny zapis gry [tutaj](log)

Flaga:

```
easyctf{m4by3_w3_c0u1d_h4v3_d0n3_th47_b3t7er}
```
