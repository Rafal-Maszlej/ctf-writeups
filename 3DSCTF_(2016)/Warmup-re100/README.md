## Warmup [RE 100]

>Rev warmup.
>
>Flag format: "3DS{flag}"

* [rev1.rar](rev1.rar)

### EN / [PL](#rozwiązanie)

### Solution:

File command:

```
$ file rev1_merces
rev1_merces: ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, for GNU/Linux 2.6.32, BuildID[sha1]=eedc48838eeab0c2783bdd110128f75f41211d45, not stripped
```

When you run the program without any parameters, there is no output:

```
# ./rev1_merces
#
```

After giving any arguments the program writes a false flag:

```
# ./rev1_merces 221 dasdas
3DS{c0ruj0u}
#
```

When we open a file using IDA, we get a scheme of program.

The program first executes two `if` statements. If both return `false`, the false flag `3DS {c0ruj0u}` will be returned.

If they return `true`, the program will do a few operations:

In one block, puts several values in the stack and immediately prints the corresponding ascii characters: `'33', '44', '53', '7b', '30', '70', '31', '6e', '31', '40'`

```
>>> s=['33', '44', '53', '7b', '30', '70', '31', '6e', '31', '40']
>>> ''.join(chr(int(i, base=16)) for i in s)
'3DS{0p1n1@'
```

We have the first part of the flag.

In the next block a string will be added:

```
'_te_'
```

In the last block, first two values 3 and 3 are loaded on the stack.

And next the last element of the flag is attached to the string:

```
'pr%dnd%d}'
```

The characters `%d` are formatted characters indicating that digits are inserted in their place.
Probably it will be mentioned 3's:

```
'pr3nd3}'
```

Flag captured :-)

```
3DS{0p1n1@_te_pr3nd3}
```

### [EN](#solution) / PL

### Rozwiązanie:

Polecenie file:

```
$ file rev1_merces
rev1_merces: ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, for GNU/Linux 2.6.32, BuildID[sha1]=eedc48838eeab0c2783bdd110128f75f41211d45, not stripped
```

Po uruchomieniu programu bez żadnych parametrów nie ma żadnego outputu:

```
# ./rev1_merces
#
```

Po podaniu dowolnych argumentów program wypisuje fałszywą flagę:

```
# ./rev1_merces 221 dasdas
3DS{c0ruj0u}
#
```

Po otworzeniu pliku za pomocą IDA dostajemy schemat funkcji programu.

Program na początku wykonuje dwie instrukcje `if`. Jeśli obydwie zwrócą `false`, zostanie zwrócona fałszywa flaga `3DS{c0ruj0u}`

Jeśli zwrócą `true`, program wykona kilka operacji:

W jednym bloku wrzuci po kolei na stos kilka wartości i od razu wypisze odpowiadające im znaki ascii: `'33', '44', '53', '7b', '30', '70', '31', '6e', '31', '40'`

```
>>> s=['33', '44', '53', '7b', '30', '70', '31', '6e', '31', '40']
>>> ''.join(chr(int(i, base=16)) for i in s)
'3DS{0p1n1@'
```

Mamy pierwszą część flagi.

W kolejnym bloku zostaje doklejony string:

```
'_te_'
```

W ostatnim bloku najpierw na stos zostają wrzucone dwie wartości 3 i 3.

A następnie do stringa doklejany jest ostatni element flagi:

```
'pr%dnd%d}'
```

Znaki `%d` są znakami formatowania oznaczającymi, że w ich miejsce wstawiane są cyfry.
Zapewne będą to wspomniane trójki:

```
'pr3nd3}'
```

Flaga zdobyta :-)

```
3DS{0p1n1@_te_pr3nd3}
```
