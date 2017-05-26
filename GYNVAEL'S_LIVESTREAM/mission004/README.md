## mission 004

>Thankfully agent Huffman decided to send us the message in plaintext this time.<br>
>While that's not great from a security standpoint, at least it allows us to read<br>
>it!<br>
>
>At least that's what we thought, until we got the message itself:<br>
>
>               E0 81 8F 76 65 72 C1 AC E0 81 AF E0 81 AE C1 A7
>               E0 80 A0 E0 81 95 C1 94 E0 81 86 2D E0 80 B8 E0
>               80 A0 F0 80 81 B7 C1 A1 73 20 C1 B3 F0 80 81 B5
>               63 C1 A8 20 E0 81 A1 F0 80 80 A0 E0 81 A6 F0 80
>               81 B5 F0 80 81 AE 20 E0 81 A6 E0 81 A5 F0 80 81
>               A1 C1 B4 75 E0 81 B2 E0 81 A5 F0 80 80 AE
>
>Of course we asked him "what the hell is that supposed to be?!" and he calmly<br>
>replied that it's UTF-8. But... uhm... somehow... we can't decode it.<br>
>
>In any case, decoding the message is your next task.<br>
>
>GOOD LUCK!

### Solution:

They were right! The message can not be decoded into a readable form byte by byte.

On site https://en.wikipedia.org/wiki/UTF-8#Description you can find information about the `UTF-8` character encoding.

It turns out that the same character can be encoded using 1 to 4 bytes.

For example `'a'` can be encoded as follows:

1 byte: `1100001`<br>
2 bytes: `11000001 10100001`<br>
3 bytes: `11100000 10000001 10100001`<br>
4 bytes: `11110000 10000000 10000001 10100001`

The first few bytes of the message:

```
>>> s = 'E0 81 8F 76 65 72 C1 AC'
>>> ' '.join(bin(int(i, base=16))[2:] for i in s.split())
'11100000 10000001 10001111 1110110 1100101 1110010 11000001 10101100'
```

You can see precisely this pattern at the beginning. The first byte suggests that the first character of the message has been encoded using 3 bytes.<br>
4th, 5th and 6th bytes have a length of 7, so each one is a separate character.<br>
Next we have a character encoded using 2 bytes.

As you can see the encoding methods are mixed, so you need to write a script. :-)

```python
enc = """E0 81 8F 76 65 72 C1 AC E0 81 AF E0 81 AE C1 A7
         E0 80 A0 E0 81 95 C1 94 E0 81 86 2D E0 80 B8 E0
         80 A0 F0 80 81 B7 C1 A1 73 20 C1 B3 F0 80 81 B5
         63 C1 A8 20 E0 81 A1 F0 80 80 A0 E0 81 A6 F0 80
         81 B5 F0 80 81 AE 20 E0 81 A6 E0 81 A5 F0 80 81
         A1 C1 B4 75 E0 81 B2 E0 81 A5 F0 80 80 AE"""

enc = enc.replace('\n', '').split()
enc = [bin(int(i, base=16))[2:] for i in enc]

message = ''


def take_bytes(n, seq):
    b = seq[:n]
    
    if n == 1:
        b = b[0]
    else:
        b = b[0][n:] + ''.join(b[i][2:] for i in range(1, n))

    return b, seq[n:]


while enc:
    
    if len(enc[0]) <= 7:
        b, enc = take_bytes(1, enc)

    elif enc[0].startswith('1111'):
        b, enc = take_bytes(4, enc)

    elif enc[0].startswith('111'):
        b, enc = take_bytes(3, enc)

    elif enc[0].startswith('11'):
        b, enc = take_bytes(2, enc)

    else:
        print('BREAK', enc)
        break
    
    message += chr(int(b, base=2))

print(message)
```

And the message:

```
$ python3 mission004.py 
Overlong UTF-8 was such a fun feature.
```
