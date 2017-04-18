## Yarn [MISC 55]

>I was told to use the linux strings command on yarn, but it doesn't work. Can you help? I lost the flag in the binary somewhere, and would like it back
>
>HINTS
>
>What does the strings command use to determine if something is a string?
>
>Is there an option to change the length of what strings considers as valid?

* [yarn](yarn)

### EN / [PL](#rozwiązanie)

### Solution:

By default, `strings` searches for sequences of at least 4 printable characters in the file.
To change this, just add `-n` option, eg. `strings -n 3 <file>`.

In this case, using the command `hexdump -C` works also quite well :-)

```
$ hexdump -C yarn > hexdump
```

In hexdump, you can find the flag easily:

```
00000000  7f 45 4c 46 01 01 01 00  00 00 00 00 00 00 00 00  |.ELF............|
00000010  02 00 03 00 01 00 00 00  00 83 04 08 34 00 00 00  |............4...|
00000020  3c 0f 00 00 00 00 00 00  34 00 20 00 08 00 28 00  |<.......4. ...(.|
00000030  1e 00 1b 00 06 00 00 00  34 00 00 00 34 80 04 08  |........4...4...|
00000040  34 80 04 08 00 01 00 00  00 01 00 00 05 00 00 00  |4...............|
00000050  04 00 00 00 03 00 00 00  34 01 00 00 34 81 04 08  |........4...4...|
00000060  34 81 04 08 13 00 00 00  13 00 00 00 04 00 00 00  |4...............|
...
00000510  c3 eb 0d 90 90 90 90 90  90 90 90 90 90 90 90 90  |................|
00000520  f3 c3 00 00 53 83 ec 08  e8 03 fe ff ff 81 c3 17  |....S...........|
00000530  12 00 00 83 c4 08 5b c3  03 00 00 00 01 00 02 00  |......[.........|
00000540  53 75 62 00 6d 69 74 00  5f 6d 65 00 5f 66 6f 00  |Sub.mit._me._fo.|
00000550  72 5f 49 00 5f 61 6d 00  5f 74 68 00 65 5f 66 00  |r_I._am._th.e_f.|
00000560  6c 61 67 00 01 1b 03 3b  28 00 00 00 04 00 00 00  |lag....;(.......|
00000570  5c fd ff ff 44 00 00 00  97 fe ff ff 68 00 00 00  |\...D.......h...|
00000580  4c ff ff ff 94 00 00 00  bc ff ff ff d0 00 00 00  |L...............|
...
```

Flag is `Submit_me_for_I_am_the_flag`

### [EN](#solution) / PL

### Rozwiązanie:

Domyślnie polecenie `strings` wyszukuje w pliku sekwencje co najmniej 4 drukowalnych znaków. 
Żeby to zmienić wystarczy dodać opcję `-n` np. `strings -n 3 <plik>`.

W tym przypadku użycie polecenia `hexdump -C` działa również całkiem nieźle :-)

```
$ hexdump -C yarn > hexdump
```

W hexdumpie bez problemu można znaleźć flagę:

```
00000000  7f 45 4c 46 01 01 01 00  00 00 00 00 00 00 00 00  |.ELF............|
00000010  02 00 03 00 01 00 00 00  00 83 04 08 34 00 00 00  |............4...|
00000020  3c 0f 00 00 00 00 00 00  34 00 20 00 08 00 28 00  |<.......4. ...(.|
00000030  1e 00 1b 00 06 00 00 00  34 00 00 00 34 80 04 08  |........4...4...|
00000040  34 80 04 08 00 01 00 00  00 01 00 00 05 00 00 00  |4...............|
00000050  04 00 00 00 03 00 00 00  34 01 00 00 34 81 04 08  |........4...4...|
00000060  34 81 04 08 13 00 00 00  13 00 00 00 04 00 00 00  |4...............|
...
00000510  c3 eb 0d 90 90 90 90 90  90 90 90 90 90 90 90 90  |................|
00000520  f3 c3 00 00 53 83 ec 08  e8 03 fe ff ff 81 c3 17  |....S...........|
00000530  12 00 00 83 c4 08 5b c3  03 00 00 00 01 00 02 00  |......[.........|
00000540  53 75 62 00 6d 69 74 00  5f 6d 65 00 5f 66 6f 00  |Sub.mit._me._fo.|
00000550  72 5f 49 00 5f 61 6d 00  5f 74 68 00 65 5f 66 00  |r_I._am._th.e_f.|
00000560  6c 61 67 00 01 1b 03 3b  28 00 00 00 04 00 00 00  |lag....;(.......|
00000570  5c fd ff ff 44 00 00 00  97 fe ff ff 68 00 00 00  |\...D.......h...|
00000580  4c ff ff ff 94 00 00 00  bc ff ff ff d0 00 00 00  |L...............|
...
```

Flaga to `Submit_me_for_I_am_the_flag`
