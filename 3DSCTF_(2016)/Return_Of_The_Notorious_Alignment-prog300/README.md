Zadanie z kategorii PROG za 300 punktów.

Drugie z serii 4 bardzo podobnych zadań:

 * [Different And Notorious Alignment (prog 200)](Different_And_Notorious_Alignment-prog200)
 * [Return Of The Notorious Alignment (prog 300)](Return_Of_The_Notorious_Alignment-prog300)
 * [Fibonacci Calls (prog 400)](Fibonacci_Calls-prog400)
 * [Vibranium Circuit Challenge (prog 400)](Vibranium_Circuit_Challenge-prog400)

Treść zadania:

Solve the challenges given by our server in 209.190.1.131 9002


Łączenie z serwerem `nc 209.190.1.131 9002` i... dalszy ciąg porównywania obcego DNA :-)

```
           +++           Comparison Challenge          +++

 [+] With the sample of an strange DNA, now we need to know how near our
     samples are to this strange (maybe alien) sample that we collect.


              +-+     +-+     +-+     +-+     +-+     +-+
              |3|     |D|     |S|     |C|     |T|     |F|
              +-+     +-+     +-+     +++     +++     +++
                                       |       |       |
           +---------------------------+       |       |
           |       +---------------------------+       |
           |       |               +-----------+       |
           |       |               |                   |
           |       |       +---------------------------+
           |       |       |       |
          +++     +++     +++     +++     +-+     +-+     +-+
          |C|     |T|     |F|     |T|     |I|     |M|     |E|
          +-+     +-+     +-+     +-+     +-+     +-+     +-+

 [+] We will give to you some pair of samples and you need to awnswer the
     the size of the longest subsequence that are equal in both samples.

 [+] To receive the first pair type 76:
```

Kilka prób:

```
 [+] To receive the first pair type 76: 76
     OK, let's go!

 [+] Stage 1 -> Sample 01: UGACGG - Sample 02: GUU
     The answer is: 2
 [-] Wrong!
     The expected answer was: 1
     Leaving the game...
```

```
 [+] Stage 1 -> Sample 01: UGACA - Sample 02: ACCGC
     The answer is: 2
 [+] Correct!

 [+] Stage 2 -> Sample 01: CACCCA - Sample 02: CACA
     The answer is: 3
 [+] Correct!

 [+] Stage 3 -> Sample 01: UUUAU - Sample 02: CUCC
     The answer is: 1
 [+] Correct!

 [+] Stage 4 -> Sample 01: UGGGAC - Sample 02: GAA
     The answer is: 2
 [+] Correct!

 [+] Stage 5 -> Sample 01: ACCAAA - Sample 02: CCCC
     The answer is: 2
 [+] Correct!

 [+] Stage 6 -> Sample 01: UAUUAG - Sample 02: UCGCC
     The answer is: 1
 [+] Correct!

 [+] Stage 7 -> Sample 01: UUCUC - Sample 02: CUAUU
     The answer is: 2
 [+] Correct!

 [+] Stage 8 -> Sample 01: AAACAA - Sample 02: ACUAC
     The answer is: 2
 [+] Correct!
```

Trzeba porównać obydwie sekwencje i podać długość najdłuższego wspólnego ciągu znaków.

Skrypt komunikujący się z serwerem + log.

* [client.py](client.py)
* [log.txt](log.txt)

Po porównaniu 100 próbek dostajemy flagę:

```
 [+] Stage 100 -> Sample 01: GUGGGGCCUGAAGGCUACGUGAUCAGUUAGUUAGGAAUAGCUUAGCGCAAGGUCACCCUCUGUGACUGAAGAUUAAUAACUACUUUGCAUCCACCGUCGAACACAAGCGAUUAGUAUGCGAGCCUCCUUCUUGAUUUCUCCGAGGCGUUUCUGAUGGACCGGCGUGCAAACGGACAUAGCAGGUGCCCACACGUCAUCAGACAUACGCACCCGGUCAAUGACCGUUUGCAACCAUAACACGUCUACACGAUUCUCAACCACGCCUAAAUCGACUUAUGUUUGCAUUUGACUUUCUGAGGAGUGCAUCUGUCAUAAGAAAAUAUGAGACUUGUAGGUGAAUAUGGGUUUCAUGGGUUGAGGGCGUAAUUCAAUGCUUCAUCCUAUUGGCCUGAAGGCUCUUAGAUUCUGAGAUCGCACUCCUCUCCGUGAAAAAUGAUGUAGAGAGCAGCAAAAAUGGUUCCUAGAAUUGACCUUGCCCAUACCAAAAUGUUUCAGUUUGGGUCUCCGGGAAAUACCUUGACAGCUAUAAUGCGAAGGGUGUCAACAGGGAAUGUUCCUGGGAUGUAUCGCCCCAGCUCAAUUGUCGGUAUAUUGGUGGAA - Sample 02: CAUGCA|GGUGC.GAAAAUAAGAAA(GSU{GUG%AVUCAAUAU#UUCUUAA#AUCGGAGACAGACUUC`CGUCU`GCCU-AAGGAGAAUGAUCCY_XCAAG<AGGUGGC0UCUGCCUAGLAAAACUGUCACGGQUACGAACGGRG"GG1C)CAGBGGACAUCAUGCGG?GUCGUCAG5CAFGGUCCCA?ACUAAGUGCAACGUCU`CUUCCUAAAAUAAAHU!AAAACCG%UUGAUCUC\AACGGG}UAC>ZGUCCAUG3ZGOCGAGCCCUUAGC-GUGGAGUAACUJUXUGUAGC3UUGUUUUPAPA{UGUGUUGUAU
     The answer is: 8
 [+] Correct!
 [+] Congratulations, the flag is: 3DS{C0mp4ris0n_0f_substr1ngs_1s_c00l}
```
