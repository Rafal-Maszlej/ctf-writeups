## Petty_Difference [FOR 75]

>I found two files in a secret room. They look like jumbled letters with no patterns. I mean look at it! file1 is identical to file2, right?

* [file1](file1)
* [file2](file2)

### EN / [PL](#rozwiązanie)

### Solution:

Both files contain strings of 100k chars each.
They probably differ in several dozens of characters, which together form a flag.

Load contents of files to two strings:

```python
with open('file1', 'r') as f:
	file1 = f.read()
	
with open('file2', 'r') as f:
	file2 = f.read()
```

And compare their character by character. If there are any differences, then for now I take the characters from the first file.

```python
print(''.join([i for i, j in zip(file1, file2) if i != j]))
```

Result:

```
}4_gn1k00l_3r3w_u0y_3cn3r3ff1d_3ht_3b_y4m_s1ht{ftcysae
```

It turned out that it is enough :-) I got a flag saved backwards. A small patch and we have a solution.

The whole script:

```python
with open('file1', 'r') as f:
	file1 = f.read()
	
with open('file2', 'r') as f:
	file2 = f.read()

print(''.join([i for i, j in zip(file1, file2) if i != j][::-1]))
```

Flag:

```
easyctf{th1s_m4y_b3_th3_d1ff3r3nc3_y0u_w3r3_l00k1ng_4}
```

### [EN](#solution) / PL

### Rozwiązanie:

Obydwa pliki zawierają ciągi znaków o długości 100k każdy.
Prawdopodobnie różnią się kilkudziesięcioma znakami, które połączone razem tworzą flagę.

Załadowanie zawartości plików do dwóch stringów:

```python
with open('file1', 'r') as f:
	file1 = f.read()
	
with open('file2', 'r') as f:
	file2 = f.read()
```

I porównanie ich znak po znaku. Jeśli będą jakieś różnice, to na razie biorę znaki z pierwszego pliku.

```python
print(''.join([i for i, j in zip(file1, file2) if i != j]))
```

Wynik:

```
}4_gn1k00l_3r3w_u0y_3cn3r3ff1d_3ht_3b_y4m_s1ht{ftcysae
```

Okazało się, że to wystarczy :-) Dostałem flagę zapisaną wspak. Drobna poprawka i mamy rozwiązanie.

Cały skrypt:

```python
with open('file1', 'r') as f:
	file1 = f.read()
	
with open('file2', 'r') as f:
	file2 = f.read()

print(''.join([i for i, j in zip(file1, file2) if i != j][::-1]))
```

Flaga:

```
easyctf{th1s_m4y_b3_th3_d1ff3r3nc3_y0u_w3r3_l00k1ng_4}
```
