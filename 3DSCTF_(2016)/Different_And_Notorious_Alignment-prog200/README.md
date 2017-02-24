Zadanie z kategorii PROG za 200 punktów.

Pierwsze z serii 4 bardzo podobnych zadań:

 * [Different And Notorious Alignment (prog 200)](Different_And_Notorious_Alignment-prog200)
 * [Return Of The Notorious Alignment (prog 300)](Return_Of_The_Notorious_Alignment-prog300)
 * [Fibonacci Calls (prog 400)](Fibonacci_Calls-prog400)
 * [Vibranium Circuit Challenge (prog 400)](Vibranium_Circuit_Challenge-prog400)

Treść zadania:

Access the server in 54.175.35.248:8001


Po połączeniu z serwerem `nc 54.175.35.248 8001` dostajemy właściwą treść zadania:

```
 [+] We steal a sample of an strange DNA and we need to know the difference
     between human DNA and the strange (maybe alien) material that we collect.

                          WWA
                         .'----------------.'WWW
                       .' |              .' |
               AWA   .'   |            .'   |
                   .'-----+----------.'     |
                   |      |          |      |
                   |      |          |      |
                   |      |          |      |
                   |      |          |      |
                   |      |          |      |
                   |     .'----------+-----.'WAW
                   |   .' WAA        |   .'
                   | .'              | .'
                   .'----------------.'
                AAA                  AAW

 [+] We will give to you some pair of samples and you need to awnswer if the
     differences are equal to the answers of our experts.

 [+] To receive the first pair type 36:
```

Chwila zabawy i po chwili wiadomo co trzeba zrobić:

```
 [+] To receive the first pair type 36:36
     OK, let's go!

 [+] Stage 1 -> Sample 01: AGAC - Sample 02: CCCT
     The answer is: true
 [-] Wrong!
     The expected answer was: 4
     Leaving the game...
```

```
 [+] Stage 1 -> Sample 01: GGAT - Sample 02: GATA
     The answer is: 3
 [+] Correct!

 [+] Stage 2 -> Sample 01: GCGA - Sample 02: GGTC
     The answer is: 6
 [-] Wrong!
     The expected answer was: 3
     Leaving the game...
```

Trzeba porównać indexami obydwie próbki i podać iloma znakami się różnią.

Oczywiście próbki robią się coraz dłuższe i pojawia się w nich znacznie więcej znaków niż tylko `AGCT`.

Poniżej skrypt komunikujący się z serwerem i odpowiadający na pytania + log.

* [client.py](client.py)
* [log.txt](log.txt)

Po porównaniu 100 próbek dostajemy flagę:

```
 [+] Congratulations, the flag is: 3DS{Y0u_4ch13v3d_h4mm1ng_D1st4nc3}
```
