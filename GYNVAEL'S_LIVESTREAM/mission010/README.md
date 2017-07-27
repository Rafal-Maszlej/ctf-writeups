## mission 006

>Usually we can blame our agents for weird security fails. Sadly not this time.<br>
>This time we shoulder the blame.
>
>We forgot the password to our secret message server.
>
>Therefore we kindly ask you to both:<br>
>- get the secret message waiting for us on the server (SECRET2),<br>
>- and recover our original shared secret if that is possible (SECRET1).
>
>Source code of the server: https://goo.gl/brzADf
>
>Address of the server: 31.133.0.131 9393 (tcp)
>
>Good luck!

### Solution:

I enjoyed this mission, I like python and I like sockets :-)

Ok, so we get the server source code: [server.py](server.py)<br>
The task is to recover two messages - one is waiting for us after logging in, the other is the password itself.

The first thing that comes to mind is that the server is very verbose. After entering invalid data at each stage we get messages what was wrong.

My first goal was to reach the message: ```Access Denied. Have a lovely day.```

Below the skeleton script I used to connect to the server.

```python
import socket

HOST = '31.133.0.131'
PORT = 9393

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
log = open('log.txt', 'w')

def send(data):
	data = data + '\n'
	print(data)
	log.write(data)
	data = bytes(data, 'utf-8')
	s.sendall(data)

def recv():
	data = s.recv(1024)
	data = str(data, 'utf-8')
	print(data)
	log.write(data)
	
	return data

# SOME CODE HERE

log.close()
```

Communication starts with the asking about the correct password mask: ```Enter shared secret mask you want to try:```

The first part of the code responsible for validating the entered mask:

```python
if len(mask) != len(PASSWORD):
  s.sendall("Mask too short. Bye.\n")
  return

for ch in mask:
  if ch not in "01":
    s.sendall("Meh.\n")
    return
```

So if the entered mask will be different length than the password length we get a message ```Mask too short. Bye.```<br>
Additionally, the entered characters may only be ```0``` or ```1```.

It's easy to find out what the password length is.

```python
i = 1
while True:
	send('a' * i)
	data = recv()
	
	if 'Mask too short.' in data:
		s.close()
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((HOST, PORT))
		recv()
		i += 1
		continue
		
	break

print(i)
```

The short log looks like this:

```
Enter shared secret mask you want to try:
a
Mask too short. Bye.
Enter shared secret mask you want to try:
aa
Mask too short. Bye.
Enter shared secret mask you want to try:
aaa
Mask too short. Bye.
Enter shared secret mask you want to try:
aaaa
...
Enter shared secret mask you want to try:
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa ... aaaa
Mask too short. Bye.
Enter shared secret mask you want to try:
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa ... aaaaa
Mask too short. Bye.
Enter shared secret mask you want to try:
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa ... aaaaaa
Meh.
560
```

So the mask has a length of 560, and the password itself consists of ```560 / 8 == 70``` characters.

Now the second part of the validation of the mask:

```python
mask = bytearray([int(x)&1 for x in mask])
mask_bits_set_cnt = sum(mask)
if mask_bits_set_cnt < 64:
  s.sendall(
      "If you want to authenticate, prove that you know at least 64 bits.\n")
  return
```

So we just have to send 560 characters, of which at least 64 characters are to be ```1``` :-)

Next: ```Alright, now send in the bits:```

Now you need to send the correct bits from the password.

And in general, with this mask we choose exactly which bits of the password we want to use for login.<br>

For example:

Password ```password```:

```
>>> ''.join(bin(ord(i))[2:][::-1] for i in 'password')
'00001111000011110011111001111110111111101101001110010011'
```

Our mask ```11100000000010100100000000000000000000000001000100000100``` pecifies which bits of the password we want to validate during validation.

If we now send ```000110110```, we will be able to log in.

Returning to our server - I send the mask and the first 64 bits (of course not correct):

```python
recv() # "Enter shared secret mask you want to try:
send(('1' * 64).zfill(560)[::-1])
recv() # "Alright, now send in the bits:
send('1'*64)
recv() # Access Denied / Access Granted
```

The asnwer:

```
Enter shared secret mask you want to try:

11111111111111111111111111111111111111111111111111111111111111110000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000

Alright, now send in the bits:

1111111111111111111111111111111111111111111111111111111111111111

Access Denied. Have a lovely day.
```

Now that the password is 70 characters long, and we have to send only 64 arbitrary bits chosen by us from this password, then from each character we can choose this one bit for which we have sureness.

Small test:

```python
from string import ascii_letters

for char in ascii_letters:
	print(char, bin(ord(char))[2:].zfill(8))
```

```
a 01100001
b 01100010
c 01100011
d 01100100
e 01100101
f 01100110
g 01100111
h 01101000
i 01101001
j 01101010
k 01101011
l 01101100
m 01101101
n 01101110
o 01101111
p 01110000
q 01110001
r 01110010
s 01110011
t 01110100
u 01110101
v 01110110
w 01110111
x 01111000
y 01111001
z 01111010
A 01000001
B 01000010
C 01000011
D 01000100
E 01000101
F 01000110
G 01000111
H 01001000
I 01001001
J 01001010
K 01001011
L 01001100
M 01001101
N 01001110
O 01001111
P 01010000
Q 01010001
R 01010010
S 01010011
T 01010100
U 01010101
V 01010110
W 01010111
X 01011000
Y 01011001
Z 01011010
```

All letters have the first bits off, and the second bit is lit.<br>
With this insight you can already log in by choosing only those bits that we are sure of.

```
Enter shared secret mask you want to try:
00000001000000010000000100000001000000010000000100000001000000010000000100000001000000010000000100000001000000010000000100000001000000010000000100000001000000010000000100000001000000010000000100000001000000010000000100000001000000010000000100000001000000010000000100000001000000010000000100000001000000010000000100000001000000010000000100000001000000010000000100000001000000010000000100000001000000010000000100000001000000010000000100000001000000010000000100000001000000010000000100000001000000010000000100000001000000000000000000000000000000000000000000000000

Alright, now send in the bits:
0000000000000000000000000000000000000000000000000000000000000000

Access Granted
You have received one secret message:
---
Just Another Secret Message
---
End of messages.
```

Using this observation you can also extract the whole password.

```python
SECRET1 = list('0' * 560)

bit = 0

while bit < 560:
	mask = list('00000001' * 70)
	
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((HOST, PORT))

	recv() # "Enter shared secret mask you want to try:
	
	mask[bit] = '1'
	mask = ''.join(mask)
	send(mask)
	
	recv() # "Alright, now send in the bits:
	
	secret1 = '0' * 71
	send(secret1)
	
	data = recv() # Access Denied / Access Granted
	
	if 'Access Denied' in data:
		SECRET1[bit] = '1'
	
	bit += 1
	
	s.close()


SECRET1 = ''.join(chr(int(''.join(SECRET1[i:i+8][::-1]), 2)) for i in range(0, 560, 8))
print(SECRET1)
```

The script iterates through all the bits and extracts the password :-)

```
This Crypto Is Absolutely Secure And There Will Be No Problem With It.
```
