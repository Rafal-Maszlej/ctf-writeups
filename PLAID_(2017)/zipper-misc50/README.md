## zipper [MISC 50]

>Something doesn't seem quite right with this zip file.
>
>Can you fix it and get the flag?

* [zipper.zip](zipper.zip)

### EN / [PL](#rozwiązanie)

### Solution:

As expected, trying to unpack `zipper.zip` failed.

```
$ unzip zipper.zip 
Archive:  zipper.zip
warning:  filename too long--truncating.
:  bad extra field length (central)
```

But I got important information:

* name of the compressed file is too long
* there is some error in the `length` field value

Looking at the file in `hexdumpie`:

```
$ hexdump -C zipper.zip 
00000000  50 4b 03 04 14 00 02 00  08 00 fc 99 92 4a 3e a9  |PK...........J>.|
00000010  2e 53 46 00 00 00 f6 00  00 00 29 23 1c 00 00 00  |.SF.......)#....|
00000020  00 00 00 00 00 00 55 54  09 00 03 5b c8 f6 58 5b  |......UT...[..X[|
00000030  c8 f6 58 75 78 0b 00 01  04 e8 03 00 00 04 e8 03  |..Xux...........|
00000040  00 00 53 50 20 04 b8 14  08 2b f1 28 ad aa 4a cc  |..SP ....+.(..J.|
00000050  d0 51 a8 cc 2f 55 c8 48  2c 4b 55 48 4e 2c 28 29  |.Q../U.H,KUHN,()|
00000060  2d 4a 4d 51 28 c9 48 55  48 cb 49 4c b7 e2 0a 70  |-JMQ(.HUH.IL...p|
00000070  0e 71 ab 4e 33 28 4a cd  2b 36 4c 2e 8e af 4c ac  |.q.N3(J.+6L...L.|
00000080  ac 25 c3 26 ea 28 01 00  50 4b 01 02 1e 03 14 00  |.%.&.(..PK......|
00000090  02 00 08 00 fc 99 92 4a  3e a9 2e 53 46 00 00 00  |.......J>..SF...|
000000a0  f6 00 00 00 29 23 18 00  00 00 00 00 01 00 00 00  |....)#..........|
000000b0  b4 81 00 00 00 00 00 00  00 00 00 00 00 00 55 54  |..............UT|
000000c0  05 00 03 5b c8 f6 58 75  78 0b 00 01 04 e8 03 00  |...[..Xux.......|
000000d0  00 04 e8 03 00 00 50 4b  05 06 00 00 00 00 01 00  |......PK........|
000000e0  01 00 4e 00 00 00 88 00  00 00 00 00              |..N.........|
000000ec
```

Hmm, it looks like there is no file name here at all.

At this point I decided to educationally split this file into the first parts.

A lot of useful information I found under these links:

* http://mdfs.net/Docs/Comp/Archiving/Zip/ExtraField
* https://pkware.cachefly.net/webdocs/casestudies/APPNOTE.TXT
* https://users.cs.jmu.edu/buchhofp/forensics/formats/pkzip.html

The file `zipped.zip` spliting into parts:

**Source**: https://pkware.cachefly.net/webdocs/casestudies/APPNOTE.TXT

#### File header:

```
00000000  50 4b 03 04 14 00 02 00  08 00 fc 99 92 4a 3e a9  |PK...........J>.|
00000010  2e 53 46 00 00 00 f6 00  00 00 29 23 1c 00 00 00  |.SF.......)#....|
00000020  00 00 00 00 00 00 55 54  09 00 03 5b c8 f6 58 5b  |......UT...[..X[|
00000030  c8 f6 58 75 78 0b 00 01  04 e8 03 00 00 04 e8 03  |..Xux...........|
00000040  00 00                                             |..|
```

<pre>
local file header signature     4 bytes  50 4b 03 04
version needed to extract       2 bytes  14 00
general purpose bit flag        2 bytes  02 00
compression method              2 bytes  08 00
last mod file time              2 bytes  fc 99
last mod file date              2 bytes  92 4a
crc-32                          4 bytes  3e a9 2e 53
compressed size                 4 bytes  46 00 00 00
uncompressed size               4 bytes  f6 00 00 00
file name length                2 bytes  29 23
extra field length              2 bytes  1c 00

Extra fields:
extended timestamp id           2 bytes  55 54
extended timestamp length       2 bytes  09 00
timestamp                       9 bytes  03 5b c8 f6 58 5b c8 f6 58
Info-ZIP UNIX id                2 bytes  75 78
Info-ZIP UNIX length            2 bytes  0b 00
Info-ZIP UNIX                   11 bytes  01 04 e8 03 00 00 04 e8 03 00 00
</pre>

#### Compressed data:

```
00000040        53 50 20 04 b8 14  08 2b f1 28 ad aa 4a cc    |SP ....+.(..J.|
00000050  d0 51 a8 cc 2f 55 c8 48  2c 4b 55 48 4e 2c 28 29  |.Q../U.H,KUHN,()|
00000060  2d 4a 4d 51 28 c9 48 55  48 cb 49 4c b7 e2 0a 70  |-JMQ(.HUH.IL...p|
00000070  0e 71 ab 4e 33 28 4a cd  2b 36 4c 2e 8e af 4c ac  |.q.N3(J.+6L...L.|
00000080  ac 25 c3 26 ea 28 01 00                           |.%.&.(..|
```

#### Central file header

```
00000080                           50 4b 01 02 1e 03 14 00          |PK......|
00000090  02 00 08 00 fc 99 92 4a  3e a9 2e 53 46 00 00 00  |.......J>..SF...|
000000a0  f6 00 00 00 29 23 18 00  00 00 00 00 01 00 00 00  |....)#..........|
000000b0  b4 81 00 00 00 00 00 00  00 00 00 00 00 00 55 54  |..............UT|
000000c0  05 00 03 5b c8 f6 58 75  78 0b 00 01 04 e8 03 00  |...[..Xux.......|
000000d0  00 04 e8 03 00 00                                 |......|
```

<pre>
central file header signature   4 bytes  50 4b 01 02
version made by                 2 bytes  1e 03
version needed to extract       2 bytes  14 00
general purpose bit flag        2 bytes  02 00
compression method              2 bytes  08 00
last mod file time              2 bytes  fc 99
last mod file date              2 bytes  92 4a
crc-32                          4 bytes  3e a9 2e 53
compressed size                 4 bytes  46 00 00 00
uncompressed size               4 bytes  f6 00 00 00
file name length                2 bytes  29 23
extra field length              2 bytes  18 00
file comment length             2 bytes  00 00
disk number start               2 bytes  00 00
internal file attributes        2 bytes  01 00
external file attributes        4 bytes  00 00 b4 81
relative offset of local header 4 bytes  00 00 00 00
file name                       8 bytes  00 00 00 00 00 00 00 00

Extra field:
extended timestamp id           2 bytes  55 54
extended timestamp length       2 bytes  05 00
timestamp                       9 bytes  03 5b c8 f6 58
Info-ZIP UNIX id                2 bytes  75 78
Info-ZIP UNIX length            2 bytes  0b 00
Info-ZIP UNIX                   11 bytes  01 04 e8 03 00 00 04 e8 03 00 00
</pre>

#### End of central dir

```
000000d0                    50 4b  05 06 00 00 00 00 01 00  |      PK........|
000000e0  01 00 4e 00 00 00 88 00  00 00 00 00              |..N.........|
```

<pre>
end of central dir signature    4 bytes  50 4b 05 06
number of this disk             2 bytes  00 00
number of the disk with the
start of the central directory  2 bytes  00 00
total number of entries in the
central directory on this disk  2 bytes  01 00
total number of entries in
the central directory           2 bytes  01 00
size of the central directory   4 bytes  4e 00 00 00
offset of start of central
directory with respect to
the starting disk number        4 bytes  88 00 00 00
.ZIP file comment length        2 bytes  00 00
.ZIP file comment               0 bytes
</pre>

In `local file header` and `central file header` are repetitive fields. Especially two seems interesting: `file name length` with value `29 23` this is 9001 in decimal, and empty space of size 8 bytes for name.

These are the places to fix.

```python
with open('zipper.zip', 'rb') as z:
	data = bytearray(z.read())

data[30:38] = b'flag.txt'
data[182:190] = b'flag.txt'
data[26:28] = b'\x08\x00'
data[164:166] = b'\x08\x00'

with open('fixed.zip', 'wb') as f:
	f.write(data)
```

Another flag :-)

```
$ unzip fixed.zip 
Archive:  fixed.zip
  inflating: flag.txt                
$ ls
fixed.zip  flag.txt  zipper.zip
$ cat flag.txt 
                                  
                                  
Huzzah, you have captured the flag:
PCTF{f0rens1cs_yay}               
                                  
                                  
$                                  
```

### [EN](#solution) / PL

### Rozwiązanie:

Zgodnie z oczekiwaniami próba rozpakowania pliku `zipper.zip` nie powiodła się.

```
$ unzip zipper.zip 
Archive:  zipper.zip
warning:  filename too long--truncating.
:  bad extra field length (central)
```

Dostałem za to ważne informacje:

* nazwa spakowanego pliku jest za długa
* jest jakiś błąd w wartości pola `length`

Wygląd pliku w `hexdumpie`:

```
$ hexdump -C zipper.zip 
00000000  50 4b 03 04 14 00 02 00  08 00 fc 99 92 4a 3e a9  |PK...........J>.|
00000010  2e 53 46 00 00 00 f6 00  00 00 29 23 1c 00 00 00  |.SF.......)#....|
00000020  00 00 00 00 00 00 55 54  09 00 03 5b c8 f6 58 5b  |......UT...[..X[|
00000030  c8 f6 58 75 78 0b 00 01  04 e8 03 00 00 04 e8 03  |..Xux...........|
00000040  00 00 53 50 20 04 b8 14  08 2b f1 28 ad aa 4a cc  |..SP ....+.(..J.|
00000050  d0 51 a8 cc 2f 55 c8 48  2c 4b 55 48 4e 2c 28 29  |.Q../U.H,KUHN,()|
00000060  2d 4a 4d 51 28 c9 48 55  48 cb 49 4c b7 e2 0a 70  |-JMQ(.HUH.IL...p|
00000070  0e 71 ab 4e 33 28 4a cd  2b 36 4c 2e 8e af 4c ac  |.q.N3(J.+6L...L.|
00000080  ac 25 c3 26 ea 28 01 00  50 4b 01 02 1e 03 14 00  |.%.&.(..PK......|
00000090  02 00 08 00 fc 99 92 4a  3e a9 2e 53 46 00 00 00  |.......J>..SF...|
000000a0  f6 00 00 00 29 23 18 00  00 00 00 00 01 00 00 00  |....)#..........|
000000b0  b4 81 00 00 00 00 00 00  00 00 00 00 00 00 55 54  |..............UT|
000000c0  05 00 03 5b c8 f6 58 75  78 0b 00 01 04 e8 03 00  |...[..Xux.......|
000000d0  00 04 e8 03 00 00 50 4b  05 06 00 00 00 00 01 00  |......PK........|
000000e0  01 00 4e 00 00 00 88 00  00 00 00 00              |..N.........|
000000ec
```

Hmm, wygląda na to, że nie ma tu w ogóle żadnej nazwy pliku.

W tym miejscu, może trochę na wyrost, postanowiłem edukacyjnie rozłożyć ten plik na części pierwsze.

Dużo przydatnych informacji znalazłem pod tymi linkami:

* http://mdfs.net/Docs/Comp/Archiving/Zip/ExtraField
* https://pkware.cachefly.net/webdocs/casestudies/APPNOTE.TXT
* https://users.cs.jmu.edu/buchhofp/forensics/formats/pkzip.html

Plik `zipped.zip` z podziałem na części:

**Źródło**: https://pkware.cachefly.net/webdocs/casestudies/APPNOTE.TXT

#### File header:

```
00000000  50 4b 03 04 14 00 02 00  08 00 fc 99 92 4a 3e a9  |PK...........J>.|
00000010  2e 53 46 00 00 00 f6 00  00 00 29 23 1c 00 00 00  |.SF.......)#....|
00000020  00 00 00 00 00 00 55 54  09 00 03 5b c8 f6 58 5b  |......UT...[..X[|
00000030  c8 f6 58 75 78 0b 00 01  04 e8 03 00 00 04 e8 03  |..Xux...........|
00000040  00 00                                             |..|
```

<pre>
local file header signature     4 bytes  50 4b 03 04
version needed to extract       2 bytes  14 00
general purpose bit flag        2 bytes  02 00
compression method              2 bytes  08 00
last mod file time              2 bytes  fc 99
last mod file date              2 bytes  92 4a
crc-32                          4 bytes  3e a9 2e 53
compressed size                 4 bytes  46 00 00 00
uncompressed size               4 bytes  f6 00 00 00
file name length                2 bytes  29 23
extra field length              2 bytes  1c 00

Extra fields:
extended timestamp id           2 bytes  55 54
extended timestamp length       2 bytes  09 00
timestamp                       9 bytes  03 5b c8 f6 58 5b c8 f6 58
Info-ZIP UNIX id                2 bytes  75 78
Info-ZIP UNIX length            2 bytes  0b 00
Info-ZIP UNIX                   11 bytes  01 04 e8 03 00 00 04 e8 03 00 00
</pre>

#### Compressed data:

```
00000040        53 50 20 04 b8 14  08 2b f1 28 ad aa 4a cc    |SP ....+.(..J.|
00000050  d0 51 a8 cc 2f 55 c8 48  2c 4b 55 48 4e 2c 28 29  |.Q../U.H,KUHN,()|
00000060  2d 4a 4d 51 28 c9 48 55  48 cb 49 4c b7 e2 0a 70  |-JMQ(.HUH.IL...p|
00000070  0e 71 ab 4e 33 28 4a cd  2b 36 4c 2e 8e af 4c ac  |.q.N3(J.+6L...L.|
00000080  ac 25 c3 26 ea 28 01 00                           |.%.&.(..|
```

#### Central file header

```
00000080                           50 4b 01 02 1e 03 14 00          |PK......|
00000090  02 00 08 00 fc 99 92 4a  3e a9 2e 53 46 00 00 00  |.......J>..SF...|
000000a0  f6 00 00 00 29 23 18 00  00 00 00 00 01 00 00 00  |....)#..........|
000000b0  b4 81 00 00 00 00 00 00  00 00 00 00 00 00 55 54  |..............UT|
000000c0  05 00 03 5b c8 f6 58 75  78 0b 00 01 04 e8 03 00  |...[..Xux.......|
000000d0  00 04 e8 03 00 00                                 |......|
```

<pre>
central file header signature   4 bytes  50 4b 01 02
version made by                 2 bytes  1e 03
version needed to extract       2 bytes  14 00
general purpose bit flag        2 bytes  02 00
compression method              2 bytes  08 00
last mod file time              2 bytes  fc 99
last mod file date              2 bytes  92 4a
crc-32                          4 bytes  3e a9 2e 53
compressed size                 4 bytes  46 00 00 00
uncompressed size               4 bytes  f6 00 00 00
file name length                2 bytes  29 23
extra field length              2 bytes  18 00
file comment length             2 bytes  00 00
disk number start               2 bytes  00 00
internal file attributes        2 bytes  01 00
external file attributes        4 bytes  00 00 b4 81
relative offset of local header 4 bytes  00 00 00 00
file name                       8 bytes  00 00 00 00 00 00 00 00

Extra field:
extended timestamp id           2 bytes  55 54
extended timestamp length       2 bytes  05 00
timestamp                       9 bytes  03 5b c8 f6 58
Info-ZIP UNIX id                2 bytes  75 78
Info-ZIP UNIX length            2 bytes  0b 00
Info-ZIP UNIX                   11 bytes  01 04 e8 03 00 00 04 e8 03 00 00
</pre>

#### End of central dir

```
000000d0                    50 4b  05 06 00 00 00 00 01 00  |      PK........|
000000e0  01 00 4e 00 00 00 88 00  00 00 00 00              |..N.........|
```

<pre>
end of central dir signature    4 bytes  50 4b 05 06
number of this disk             2 bytes  00 00
number of the disk with the
start of the central directory  2 bytes  00 00
total number of entries in the
central directory on this disk  2 bytes  01 00
total number of entries in
the central directory           2 bytes  01 00
size of the central directory   4 bytes  4e 00 00 00
offset of start of central
directory with respect to
the starting disk number        4 bytes  88 00 00 00
.ZIP file comment length        2 bytes  00 00
.ZIP file comment               0 bytes
</pre>

W `local file header` i `central file header` są powtarzające się pola. Zwłaszcza dwa wydają się ciekawe: `file name length` o wartości `29 23` czyli 9001 i puste miejsce o rozmiarze 8 bajtów na nazwę.

To są miejsca, które trzeba naprawić.

```python
with open('zipper.zip', 'rb') as z:
	data = bytearray(z.read())

data[30:38] = b'flag.txt'
data[182:190] = b'flag.txt'
data[26:28] = b'\x08\x00'
data[164:166] = b'\x08\x00'

with open('fixed.zip', 'wb') as f:
	f.write(data)
```

Kolejna flaga :-)

```
$ unzip fixed.zip 
Archive:  fixed.zip
  inflating: flag.txt                
$ ls
fixed.zip  flag.txt  zipper.zip
$ cat flag.txt 
                                  
                                  
Huzzah, you have captured the flag:
PCTF{f0rens1cs_yay}               
                                  
                                  
$                                  
```
