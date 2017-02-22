Zadanie z kategorii MISC za 100 punktów.

Treść zadania:

Santa walks into a bar and creates a friendship bound with you.
After some shots, he spells to you his secrets to delivery all gifts on Christmas: he has a magical linked list that inform the next kiddie to visit.
At the end of the night, he goes alway and left behind his wallet and the bag with the list of gifts to delivery. Try to discover if you will receive something.

Otrzymujemy paczkę:

   * [santa-id.png](santa-id.png)
   * [list.zip](list.zip)

W list.zip znajduje się 11001 plików png zawierających kody QR.
Przykładowy plik:
    0a2e44952d2224b800d189ac6808d5c7.png


Do rozkodowania plików posłużyłem się pythonowym modułem - qrtools.

```python
    import os
    import qrtools

    l = os.listdir('list')

    qr = qrtools.QR()

    for f in l:
        qr.decode('list/'+f)
        print qr.data
```

Po uruchomieniu w konsoli i odczekaniu prawie minuty:

```
    python qr.py > decoded_list.txt
```

dostałem listę Mikołaja:

    ...
    Now I have Kevin in 417125924b4ddfcd6a99a9e3a2029d0c
    Now I have Christopher in 7778dbc160ef9f961984eb9df4d92650
    A child in Alexander in acb65a6e82bc2c1d9bf04b2a1f047795
    Next name is William in b716e0a0b58867db52d58c93433e2773
    Now I have Zachary in 9e9ca32a899aae19c12ba53628d0d629
    I almost forgot Christopher in 8e551c09349d82fa57ab359200cc13b3
    A child in Kevin in e36a887b418fa5e0c0b7f20a0b33ec90
    I almost forgot Hunter in 158304513c274693f1a2556b7a5cb510
    A child in Quinn in 168f759e9f1c3ffba2aa243966c81fd5
    I almost forgot Hunter in 4ef21d939603627fcdbe67f5c15ccf36
    A child in Liam in 646935b787e3b490145c19170b082771
    A kid called Mason in 6bbd2fa7702fe10d0b2e48515a7ae13f
    A kid called Kevin in b49f444e3111f6df5afe84adcd1a5c25
    A child in Francisco in 702f92f1485802d02a48a3ae1841b6a2
    Now I have Liam in fe0182c5a15fb983ac0038a1638575dd
    I almost forgot Hunter in 3768b2302dc9402efca62747ad843d8a
    Now I have Benjamin in 2d4d369da8e7131e149973de49b4a297
    Next name is Mason in 2522c1e3eac6b3ead5b35b9507faf42c
    ...

Jak widać większość linii jest do siebie podobna.
Jednak nie wszystkie.
Część okazała się ciągami cyfr, np "09875142"

Po przefiltrowaniu całego pliku w poszukiwaniu tylko tych ciągów:

```python
    for line in open('decoded_list.txt', 'r'):
        if line[0].isdigit():
            print(line.strip())
```

otrzymałem:

    08164483
    08179883
    01778319
    09897793
    07571879
    07680373
    07838378
    09875142
    68160753
    06061869
    00748106
    04575748
    07137273
    04793348
    09875142
    07807176
    03716738
    08148186
    06831769
    08179883
    07581779
    04793348

Co okazało się ślepym zaułkiem.

Przeglądając jeszcze raz zdekodowaną listę natknąłem się przypadkiem na niepasujący do niczego wiersz:

    Ops!

Zmiana sposobu filtrowania:

```python
    for line in open('decoded_list.txt', 'r'):
        if any(line.startswith(i) for i in ['Now I have', 'A child', 'Next name', 'I almost', 'A kid', 'Next kiddie']):
            pass
        else:
            print(line.strip())
```

i...

    08164483
    08179883
    01778319
    09897793
    Ops!
    Wrong!
    07571879
    07680373
    07838378
    Y0ur gift is in goo.gl/wFGwqO inugky3leb2gqzjanruw42yk
    09875142
    68160753
    06061869
    00748106
    04575748
    07137273
    Fail
    04793348
    09875142
    07807176
    03716738
    08148186
    06831769
    Yu u no following right?
    08179883
    07581779
    04793348
    So wrong!

Jest!

```
    Y0ur gift is in goo.gl/wFGwqO inugky3leb2gqzjanruw42yk
```

Po wejściu na adres goo.gl/wFGwqO, dostajemy flagę:

```
    3DS{I_h0p3_th4t_Y0u_d1d_n0t_h4v3_ch4ck3d_OnE_by_0n3}
```
