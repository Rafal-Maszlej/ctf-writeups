## RSA_2 [CRYPTO 80]

>Some more RSA! This time, there's no P and Q...

```
n: 94641754815453773628106187659966312140031
e: 65537
c: 90476214991558864375600465615980773995409
```

### EN / [PL](#rozwiązanie)

### Solution:

This time we have `n`, but there is no `p` and `q`, so we can not calculate `phi`.

Recall that `n = p * q`
In addition, the value `n` is not too large, so maybe it can be divided into factors?
Always worth look at [factordb.com](http://factordb.com/), which stores factorials of numbers.

We get `p` and `q` immediately:

```
p = 303398557233532183169
q = 311938710844317052799
```

So we have everything we need to decipher the message.

Python script:

```python
import libnum


n = 94641754815453773628106187659966312140031
e = 65537
c = 90476214991558864375600465615980773995409

p = 303398557233532183169
q = 311938710844317052799

phi = (p - 1) * (q - 1)
d = libnum.modular.invmod(e, phi)


print libnum.n2s(pow(c, d, n))
```

And the flag:

```
flag{l0w_n_a679}
```

### [EN](#solution) / PL

### Rozwiązanie:

Tym razem dane jest `n`, ale nie ma `p` i `q`, nie można więc policzyć `phi`.

Przypomnijmy, że `n == p * q`
Dodatkowo wartość `n` nie jest zbyt duża, może więc uda się ją rozłożyć na czynniki?
Zawsze warto zerknąć na stronę [factordb.com](http://factordb.com/), która przechowuje faktoryzacje liczb.

Po wpisaniu `n` dostajemy od razu `p` i `q`:

```
p = 303398557233532183169
q = 311938710844317052799
```

Mamy więc wszystko co jest potrzebne do rozszyfrowania wiadomości.

Skrypt w pythonie:

```python
import libnum


n = 94641754815453773628106187659966312140031
e = 65537
c = 90476214991558864375600465615980773995409

p = 303398557233532183169
q = 311938710844317052799

phi = (p - 1) * (q - 1)
d = libnum.modular.invmod(e, phi)


print libnum.n2s(pow(c, d, n))
```

I flaga:

```
flag{l0w_n_a679}
```
