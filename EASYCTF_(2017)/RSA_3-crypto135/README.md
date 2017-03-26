## RSA_3 [CRYPTO 135]

>We came across another message that follows the same cryptographic schema as those other RSA messages. Take a look and see if you can crack it.
>
>hint:
>You might want to read up on how RSA works.

```
{N : e : c}
{0x27335d21ca51432fa000ddf9e81f630314a0ef2e35d81a839584c5a7356b94934630ebfc2ef9c55b111e8c373f2db66ca3be0c0818b1d4eda7d53c1bd0067f66a12897099b5e322d85a8da45b72b828813af23L : 0x10001 : 0x9b9c138e0d473b6e6cf44acfa3becb358b91d0ba9bfb37bf11effcebf9e0fe4a86439e8217819c273ea5c1c5acfd70147533aa550aa70f2e07cc98be1a1b0ea36c0738d1c994c50b1bd633e3873fc0cb377e7L}
```

### EN / [PL](#rozwiązanie)

### Solution:

Task very similar to the previous one [RSA_2](https://github.com/h4stoor/ctf/tree/master/EASYCTF_%282017%29/RSA_2-crypto80). The only difference is that the values `n`, `e` and `c` are given as hexadecimal numbers.
After converting them to a decimal, the solution looks the same.

Again handy turned out to be the site [factordb.com](http://factordb.com/), thanks to which we get `n` factorized on two twin primes.

Script:

```python
import libnum

n = '27335d21ca51432fa000ddf9e81f630314a0ef2e35d81a839584c5a7356b94934630ebfc2ef9c55b111e8c373f2db66ca3be0c0818b1d4eda7d53c1bd0067f66a12897099b5e322d85a8da45b72b828813af23'
e = '10001'
c = '9b9c138e0d473b6e6cf44acfa3becb358b91d0ba9bfb37bf11effcebf9e0fe4a86439e8217819c273ea5c1c5acfd70147533aa550aa70f2e07cc98be1a1b0ea36c0738d1c994c50b1bd633e3873fc0cb377e7'

n = int(n, base=16)
e = int(e, base=16)
c = int(c, base=16)

p = 3423616853305296708261404925903697485956036650315221001507285374258954087994492532947084586412780869
q = 3423616853305296708261404925903697485956036650315221001507285374258954087994492532947084586412780871

phi = (p - 1) * (q - 1)
d = libnum.modular.invmod(e, phi)

print libnum.n2s(pow(c, d, n))
```

And the flag:

```
easyctf{tw0_v3ry_merrry_tw1n_pr1m35!!_417c0d}
```

### [EN](#solution) / PL

### Rozwiązanie:

Zadanie bardzo podobne do poprzedniego [RSA_2](https://github.com/h4stoor/ctf/tree/master/EASYCTF_%282017%29/RSA_2-crypto80). Jedyna różnica jest taka, że wartości `n`, `e` i `c` podane są jako liczby szesnastkowe.
Po przekonwertowaniu ich na system dziesiętny rozwiązanie wygląda tak samo.

Znowu przydatna okazała się strona [factordb.com](http://factordb.com/), dzięki której dostajemy rozkład `n` na bliźniacze liczby pierwsze.

Skrypt:

```python
import libnum

n = '27335d21ca51432fa000ddf9e81f630314a0ef2e35d81a839584c5a7356b94934630ebfc2ef9c55b111e8c373f2db66ca3be0c0818b1d4eda7d53c1bd0067f66a12897099b5e322d85a8da45b72b828813af23'
e = '10001'
c = '9b9c138e0d473b6e6cf44acfa3becb358b91d0ba9bfb37bf11effcebf9e0fe4a86439e8217819c273ea5c1c5acfd70147533aa550aa70f2e07cc98be1a1b0ea36c0738d1c994c50b1bd633e3873fc0cb377e7'

n = int(n, base=16)
e = int(e, base=16)
c = int(c, base=16)

p = 3423616853305296708261404925903697485956036650315221001507285374258954087994492532947084586412780869
q = 3423616853305296708261404925903697485956036650315221001507285374258954087994492532947084586412780871

phi = (p - 1) * (q - 1)
d = libnum.modular.invmod(e, phi)

print libnum.n2s(pow(c, d, n))
```

I flaga:

```
easyctf{tw0_v3ry_merrry_tw1n_pr1m35!!_417c0d}
```
