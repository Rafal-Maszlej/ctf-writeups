## Missing_Identity [FOR 100]

>Turns out, some of the files back from Master Challenge 1 were corrupted. Restore this one file and find the flag.
>
>HINTS
>
>What file is this?
>
>What do you expect to find in the file structure?
>
>All characters in the file are lower case or numberical. There will not be any zeros.

* [file](file)

### EN / [PL](#rozwiązanie)

### Solution:

After using the `hexdump -C file` command you will notice several things:

* first 6 bytes are edited

```
00000000  58 58 58 58 58 58 00 00  08 00 23 44 7f 4a 68 d5  |XXXXXX....#D.Jh.|
```

* whole file seems to consist of several linked `png` files

```
00000010  28 00 d1 8d 00 00 c2 8d  00 00 08 00 00 00 66 6c  |(.............fl|
00000020  61 67 2e 70 6e 67 00 64  40 9b bf 89 50 4e 47 0d  |ag.png.d@...PNG.|
00000030  0a 1a 0a 00 00 00 0d 49  48 44 52 00 00 02 54 00  |.......IHDR...T.|
00000040  00 00 3c 08 02 00 00 00  2f c2 b3 60 00 00 8d 89  |..<...../..`....|
00000050  49 44 41 54 78 9c ec fd  57 8f 25 59 96 26 8a ad  |IDATx...W.%Y.&..|
00000060  b5 b7 e9 63 47 b9 0e f7  d0 3a 23 43 a4 aa ca 12  |...cG....:#C....|
...
00008e10  00 0f 00 00 00 6e 6f 74  74 68 65 66 6c 61 67 31  |.....nottheflag1|
00008e20  2e 70 6e 67 00 60 40 9f  bf 89 50 4e 47 0d 0a 1a  |.png.`@...PNG...|
00008e30  0a 00 00 00 0d 49 48 44  52 00 00 03 ff 00 00 00  |.....IHDR.......|
00008e40  3c 08 02 00 00 00 bf f4  9d 86 00 00 e3 05 49 44  |<.............ID|
00008e50  41 54 78 9c ec fd d9 af  25 69 92 27 86 99 7d 9b  |ATx.....%i.'..}.|
00008e60  bb 9f fd dc 25 f6 cc 8c  5c 6b ed a9 5e 86 43 36  |....%...\k..^.C6|
00008e70  87 24 d4 23 52 10 87 e4  90 23 01 f3 30 43 41 2f  |.$.#R....#..0CA/|
...
0005e060  e9 00 00 0f 00 00 00 6e  6f 74 74 68 65 66 6c 61  |.......notthefla|
0005e070  67 37 2e 70 6e 67 00 55  40 aa bf 89 50 4e 47 0d  |g7.png.U@...PNG.|
0005e080  0a 1a 0a 00 00 00 0d 49  48 44 52 00 00 03 fe 00  |.......IHDR.....|
0005e090  00 00 3c 08 02 00 00 00  50 36 f6 b8 00 00 e9 1c  |..<.....P6......|
0005e0a0  49 44 41 54 78 9c ec fd  49 8c 65 49 96 25 88 dd  |IDATx...I.eI.%..|
0005e0b0  2b c3 9b fe ac f3 64 93  cf 1e e1 11 e9 11 39 54  |+.....d.......9T|
0005e0c0  65 56 66 0d dd 0d 76 11  20 73 d1 6b 82 e0 92 9b  |eVf...v. s.k....|
```

* at the end there is a section that appears to be a list of file content

```
0006c9d0  4d 8f 24 00 00 00 00 49  45 4e 44 ae 42 60 82 50  |M.$....IEND.B`.P|
0006c9e0  4b 01 02 14 03 14 00 00  00 08 00 23 44 7f 4a 68  |K..........#D.Jh|
0006c9f0  d5 28 00 d1 8d 00 00 c2  8d 00 00 08 00 00 00 00  |.(..............|
0006ca00  00 00 00 00 00 00 00 a4  81 00 00 00 00 66 6c 61  |.............fla|
0006ca10  67 2e 70 6e 67 50 4b 01  02 14 03 14 00 00 00 08  |g.pngPK.........|
0006ca20  00 23 44 7f 4a 3f 64 5c  22 52 e3 00 00 3e e3 00  |.#D.J?d\"R...>..|
0006ca30  00 0f 00 00 00 00 00 00  00 00 00 00 00 a4 81 f7  |................|
0006ca40  8d 00 00 6e 6f 74 74 68  65 66 6c 61 67 31 2e 70  |...nottheflag1.p|
0006ca50  6e 67 50 4b 01 02 14 03  14 00 00 00 08 00 23 44  |ngPK..........#D|
0006ca60  7f 4a 32 ef 70 ea 2b e5  00 00 32 e5 00 00 0f 00  |.J2.p.+...2.....|
0006ca70  00 00 00 00 00 00 00 00  00 00 a4 81 76 71 01 00  |............vq..|
0006ca80  6e 6f 74 74 68 65 66 6c  61 67 32 2e 70 6e 67 50  |nottheflag2.pngP|
0006ca90  4b 01 02 14 03 14 00 00  00 08 00 23 44 7f 4a 40  |K..........#D.J@|
0006caa0  6d d0 2b b1 ec 00 00 a0  ec 00 00 0f 00 00 00 00  |m.+.............|
0006cab0  00 00 00 00 00 00 00 a4  81 ce 56 02 00 6e 6f 74  |..........V..not|
0006cac0  74 68 65 66 6c 61 67 33  2e 70 6e 67 50 4b 01 02  |theflag3.pngPK..|
0006cad0  14 03 14 00 00 00 08 00  23 44 7f 4a b0 51 ee ff  |........#D.J.Q..|
0006cae0  5a d8 00 00 71 d8 00 00  0f 00 00 00 00 00 00 00  |Z...q...........|
0006caf0  00 00 00 00 a4 81 ac 43  03 00 6e 6f 74 74 68 65  |.......C..notthe|
0006cb00  66 6c 61 67 34 2e 70 6e  67 50 4b 01 02 14 03 14  |flag4.pngPK.....|
0006cb10  00 00 00 08 00 23 44 7f  4a 4e 17 14 bb 0f df 00  |.....#D.JN......|
0006cb20  00 fb de 00 00 0f 00 00  00 00 00 00 00 00 00 00  |................|
0006cb30  00 a4 81 33 1c 04 00 6e  6f 74 74 68 65 66 6c 61  |...3...notthefla|
0006cb40  67 35 2e 70 6e 67 50 4b  01 02 14 03 14 00 00 00  |g5.pngPK........|
0006cb50  08 00 23 44 7f 4a 5b 77  80 ac ad e4 00 00 0a e5  |..#D.J[w........|
0006cb60  00 00 0f 00 00 00 00 00  00 00 00 00 00 00 a4 81  |................|
0006cb70  6f fb 04 00 6e 6f 74 74  68 65 66 6c 61 67 36 2e  |o...nottheflag6.|
0006cb80  70 6e 67 50 4b 01 02 14  03 14 00 00 00 08 00 23  |pngPK..........#|
0006cb90  44 7f 4a 54 82 1a aa 69  e9 00 00 55 e9 00 00 0f  |D.JT...i...U....|
0006cba0  00 00 00 00 00 00 00 00  00 00 00 a4 81 49 e0 05  |.............I..|
0006cbb0  00 6e 6f 74 74 68 65 66  6c 61 67 37 2e 70 6e 67  |.nottheflag7.png|
0006cbc0  50 4b 05 06 00 00 00 00  08 00 08 00 e1 01 00 00  |PK..............|
0006cbd0  df c9 06 00 00 00                                 |......|
```

You can then deduce that `file` is probably some archive, eg. `zip` containing images.

Missing bytes from the header file can be easily found, eg. [here](https://users.cs.jmu.edu/buchhofp/forensics/formats/pkzip.html)

Replacing of values:

```python
with open('file', 'rb') as f:
	data = bytearray(f.read())

head = [0x50, 0x4b, 0x03, 0x04, 0x14, 0x00]

for i in range(6):
	data[i] = head[i]

with open('flag.zip', 'wb') as f:
	f.write(data)
```

And as a result, I got the correct file [flag.zip](flag.zip) which, among other images, contains the flag:

![flag.png](flag.png)

Flag:

```
zippidydOoda44282245
```

### [EN](#solution) / PL

### Rozwiązanie:

Po wydaniu polecenia `hexdump -C file` można zauważyć kilka rzeczy:

* pierwsze 6 bajtów jest wyedytowanych

```
00000000  58 58 58 58 58 58 00 00  08 00 23 44 7f 4a 68 d5  |XXXXXX....#D.Jh.|
```

* cały plik zdaje się składać z kilku połączonych plików `png`

```
00000010  28 00 d1 8d 00 00 c2 8d  00 00 08 00 00 00 66 6c  |(.............fl|
00000020  61 67 2e 70 6e 67 00 64  40 9b bf 89 50 4e 47 0d  |ag.png.d@...PNG.|
00000030  0a 1a 0a 00 00 00 0d 49  48 44 52 00 00 02 54 00  |.......IHDR...T.|
00000040  00 00 3c 08 02 00 00 00  2f c2 b3 60 00 00 8d 89  |..<...../..`....|
00000050  49 44 41 54 78 9c ec fd  57 8f 25 59 96 26 8a ad  |IDATx...W.%Y.&..|
00000060  b5 b7 e9 63 47 b9 0e f7  d0 3a 23 43 a4 aa ca 12  |...cG....:#C....|
...
00008e10  00 0f 00 00 00 6e 6f 74  74 68 65 66 6c 61 67 31  |.....nottheflag1|
00008e20  2e 70 6e 67 00 60 40 9f  bf 89 50 4e 47 0d 0a 1a  |.png.`@...PNG...|
00008e30  0a 00 00 00 0d 49 48 44  52 00 00 03 ff 00 00 00  |.....IHDR.......|
00008e40  3c 08 02 00 00 00 bf f4  9d 86 00 00 e3 05 49 44  |<.............ID|
00008e50  41 54 78 9c ec fd d9 af  25 69 92 27 86 99 7d 9b  |ATx.....%i.'..}.|
00008e60  bb 9f fd dc 25 f6 cc 8c  5c 6b ed a9 5e 86 43 36  |....%...\k..^.C6|
00008e70  87 24 d4 23 52 10 87 e4  90 23 01 f3 30 43 41 2f  |.$.#R....#..0CA/|
...
0005e060  e9 00 00 0f 00 00 00 6e  6f 74 74 68 65 66 6c 61  |.......notthefla|
0005e070  67 37 2e 70 6e 67 00 55  40 aa bf 89 50 4e 47 0d  |g7.png.U@...PNG.|
0005e080  0a 1a 0a 00 00 00 0d 49  48 44 52 00 00 03 fe 00  |.......IHDR.....|
0005e090  00 00 3c 08 02 00 00 00  50 36 f6 b8 00 00 e9 1c  |..<.....P6......|
0005e0a0  49 44 41 54 78 9c ec fd  49 8c 65 49 96 25 88 dd  |IDATx...I.eI.%..|
0005e0b0  2b c3 9b fe ac f3 64 93  cf 1e e1 11 e9 11 39 54  |+.....d.......9T|
0005e0c0  65 56 66 0d dd 0d 76 11  20 73 d1 6b 82 e0 92 9b  |eVf...v. s.k....|
```

* na końcu znajduje się część, która zdaje się być listą zawartości pliku

```
0006c9d0  4d 8f 24 00 00 00 00 49  45 4e 44 ae 42 60 82 50  |M.$....IEND.B`.P|
0006c9e0  4b 01 02 14 03 14 00 00  00 08 00 23 44 7f 4a 68  |K..........#D.Jh|
0006c9f0  d5 28 00 d1 8d 00 00 c2  8d 00 00 08 00 00 00 00  |.(..............|
0006ca00  00 00 00 00 00 00 00 a4  81 00 00 00 00 66 6c 61  |.............fla|
0006ca10  67 2e 70 6e 67 50 4b 01  02 14 03 14 00 00 00 08  |g.pngPK.........|
0006ca20  00 23 44 7f 4a 3f 64 5c  22 52 e3 00 00 3e e3 00  |.#D.J?d\"R...>..|
0006ca30  00 0f 00 00 00 00 00 00  00 00 00 00 00 a4 81 f7  |................|
0006ca40  8d 00 00 6e 6f 74 74 68  65 66 6c 61 67 31 2e 70  |...nottheflag1.p|
0006ca50  6e 67 50 4b 01 02 14 03  14 00 00 00 08 00 23 44  |ngPK..........#D|
0006ca60  7f 4a 32 ef 70 ea 2b e5  00 00 32 e5 00 00 0f 00  |.J2.p.+...2.....|
0006ca70  00 00 00 00 00 00 00 00  00 00 a4 81 76 71 01 00  |............vq..|
0006ca80  6e 6f 74 74 68 65 66 6c  61 67 32 2e 70 6e 67 50  |nottheflag2.pngP|
0006ca90  4b 01 02 14 03 14 00 00  00 08 00 23 44 7f 4a 40  |K..........#D.J@|
0006caa0  6d d0 2b b1 ec 00 00 a0  ec 00 00 0f 00 00 00 00  |m.+.............|
0006cab0  00 00 00 00 00 00 00 a4  81 ce 56 02 00 6e 6f 74  |..........V..not|
0006cac0  74 68 65 66 6c 61 67 33  2e 70 6e 67 50 4b 01 02  |theflag3.pngPK..|
0006cad0  14 03 14 00 00 00 08 00  23 44 7f 4a b0 51 ee ff  |........#D.J.Q..|
0006cae0  5a d8 00 00 71 d8 00 00  0f 00 00 00 00 00 00 00  |Z...q...........|
0006caf0  00 00 00 00 a4 81 ac 43  03 00 6e 6f 74 74 68 65  |.......C..notthe|
0006cb00  66 6c 61 67 34 2e 70 6e  67 50 4b 01 02 14 03 14  |flag4.pngPK.....|
0006cb10  00 00 00 08 00 23 44 7f  4a 4e 17 14 bb 0f df 00  |.....#D.JN......|
0006cb20  00 fb de 00 00 0f 00 00  00 00 00 00 00 00 00 00  |................|
0006cb30  00 a4 81 33 1c 04 00 6e  6f 74 74 68 65 66 6c 61  |...3...notthefla|
0006cb40  67 35 2e 70 6e 67 50 4b  01 02 14 03 14 00 00 00  |g5.pngPK........|
0006cb50  08 00 23 44 7f 4a 5b 77  80 ac ad e4 00 00 0a e5  |..#D.J[w........|
0006cb60  00 00 0f 00 00 00 00 00  00 00 00 00 00 00 a4 81  |................|
0006cb70  6f fb 04 00 6e 6f 74 74  68 65 66 6c 61 67 36 2e  |o...nottheflag6.|
0006cb80  70 6e 67 50 4b 01 02 14  03 14 00 00 00 08 00 23  |pngPK..........#|
0006cb90  44 7f 4a 54 82 1a aa 69  e9 00 00 55 e9 00 00 0f  |D.JT...i...U....|
0006cba0  00 00 00 00 00 00 00 00  00 00 00 a4 81 49 e0 05  |.............I..|
0006cbb0  00 6e 6f 74 74 68 65 66  6c 61 67 37 2e 70 6e 67  |.nottheflag7.png|
0006cbc0  50 4b 05 06 00 00 00 00  08 00 08 00 e1 01 00 00  |PK..............|
0006cbd0  df c9 06 00 00 00                                 |......|
```

Można po tym wywnioskować, że `plik` jest jakimś archiwum np. `zip` zawierającym obrazki.

Brakujące bajty z nagłówka pliku można łatwo znaleźć, np. [tutaj](https://users.cs.jmu.edu/buchhofp/forensics/formats/pkzip.html)

Podmiana wartości:

```python
with open('file', 'rb') as f:
	data = bytearray(f.read())

head = [0x50, 0x4b, 0x03, 0x04, 0x14, 0x00]

for i in range(6):
	data[i] = head[i]

with open('flag.zip', 'wb') as f:
	f.write(data)
```

I w efekcie dostałem poprawny plik [flag.zip](flag.zip), który między innymi zawiera flagę:

![flag.png](flag.png)

Flaga:

```
zippidydOoda44282245
```
