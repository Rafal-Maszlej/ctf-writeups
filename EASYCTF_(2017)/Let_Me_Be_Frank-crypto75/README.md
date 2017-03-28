## Let_Me_Be_Frank [CRYPTO 75]

>I was talking to one of my friends but I couldn't quite understand what he was saying. I think it might be important so here it is: 

```
Nwh whdjwh qm uepen, T tjb fsmt tixgi jsrsh sigm gs mpzp xwqf iahxpv iw fslkt. pehgpxf{qtextz_glacz_elt_neinrw_qsg_bums_dcp}
```

### EN / [PL](#rozwiązanie)

### Solution:

### [EN](#solution) / PL

### Rozwiązanie:

Hmm, do tego zadania był hint, ale niestety gdzieś go posiałem... Mówił o tym, że nazwa zadania może mieć znaczenie.

A więc wyszukując w google zapytanie "Frank crypto" dostałem w jednym z pierwszych wyników osobę związaną z kryptografią. 
[Frank Miller](https://en.wikipedia.org/wiki/Frank_Miller_%28cryptography%29) został uznany za twórcę tzw. [one-time pad](https://en.wikipedia.org/wiki/One-time_pad).
Jest to sposób szyfrowania używający jednorazowych kluczy. Zakładając, że długość klucza jest równa długości tekstu, który chcemy zaszyfrować, ten szyfr jest nie do złamania. 
Żeby zaszyfrować dany znak należy dodać do siebie indeks znaku i index odpowiedniego znaku z klucza, a następnie wykonać na tym operację modulo długość alfabetu.

Przykład:

Angielski alfabet ma 26 znaków. Szyfruję znak "g" za pomocą znaku "x":

```
>>> alphabet.find('g')
6
>>> alphabet.find('x')
23
>>> (6 + 23) % 26
3
>>> alphabet[3]
'd'
```

Zatem po zaszyfrowaniu "g" za pomocą klucza "x" otrzymałem "d".

Żeby teraz rozszyfrować wiadomość od zaszyfrowanego znaku trzeba odjąć znak z klucza i wykonać na tym modulo.

```
>>> alphabet.find('d')
3
>>> alphabet.find('x')
23
>>> (3 - 23) % 26
6
>>> alphabet[6]
'g'
```

Tutaj napisany przeze mnie krótki moduł zawierający trzy przydatne funkcje: [one_time_pad.py](one_time_pad.py)

Teraz można przystąpić do rozwiązania zadania :-)

Przede wszystkim od razu widać, że końcówka zaszyfrowanego tekstu to nasza flaga `pehgpxf{qtextz_glacz_elt_neinrw_qsg_bums_dcp}`. A zatem `pehgpxf` po rozszyfrowaniu ma dać `easyctf`.

```
>>> from one_time_pad import decrypt, crack
>>> crack('easyctf', 'pehgpxf')
'lepinea'
```

Spróbujmy użyć tego jako klucza dla całej wiadomości.

```
>>> key = 'lepinea'
>>> decrypt(cipher, key)
'Css ouzjld be haptj, E lwx fhie lvtgx fdjfd sxcx yf ipol iodb ipdihi ew uowcg. lewcaps{mttter_tharv_pdg_jexjco_dog_qqxk_qyp}'
```

Hmm, coś nie bardzo, nawet początek flagi się nie rozszyfrował. Spróbujmy rotacji klucza.

```
>>> decrypt(cipher, 'epineal')
'Jhz jddyss iz qeeay, L gfb uoxl gexve ukeoh here to meva pjmf xwspcr il bddxp. ptdrhkb{qiailm_clpyk_wyp_nteyjj_msv_xfef_zce}'
>>> 
>>> 
>>> decrypt(cipher, 'pineale')
'You shsfhz di utlpf, G pjq bdeg pimct bfnsw otyz cs blkh ksqu elzklv xs qkygt. easyctf{fpppgv_gawnr_rht_catfes_qhc_mmzo_drl}'
```

Działa :-) `easyctf` jest, rozszyfrował się też chyba początek wiadomości. Ale tylko 5 pierwszych znaków wydaje się mieć sens `You sh`. Czyli początek klucza to `pinea`, a część, która została przeniesiona z początku klucza na koniec `le` nie pasuje. Być może pomiędzy brakuje kilku znaków.

```
>>> decrypt(cipher, 'pinea_le')
'You sheyss iz qeqtj, E lwx ftbp eakci khndz fegn vo xhml xxfb tsutpw xs qkygt. qtdrhkb{qutter_thado_awl_aaiogs_bkt_xunh_znh}'
>>> 
>>> decrypt(cipher, 'pinea__le')
'You shekld be hapfo, I put somu uxtra worti here to mqae this eaiyer to sollu. easyctf{rutter_thada_the_frensx_for_this_ede}'
```

Prawie dobrze. W kluczu brakuje jeszcze dwóch znaków, a rozszyfrowany tekst zaczyna już mieć sens.

Na przykład część `I put somu` może znaczyć `I put some`. Spróbujmy znaleźć klucz dla "some".

```
>>> crack('some', 'fsmt')
'neap'
```

Klucz póki co wygląda tak: `pinea__le`, teraz dostajemy `neap`, czyli po połączeniu mamy kolejną literę: `pineap_le`.

Całość:

```
>>> decrypt(cipher, 'pineap_le')
'You shokld be happo, I put some uxtra wordi here to maae this easyer to solvu. easyctf{butter_thana_the_frencx_for_this_ode}'
```

Wygląda dobrze. Dalej część `I put some uxtra`, to raczej na pewno `I put some extra`. Spróbujmy więc podobnie jak wyżej znaleźć klucz dla "extra".

```
>>> crack('extra', 'tixgi')
'plepi'
```

Klucz: `pineap_le` + `plepi` daje `pineapple`, co chyba jest całym kluczem :-)

Sprawdźmy:

```
>>> decrypt(cipher, 'pineapple')
'You should be happy, I put some extra words here to make this easier to solve. easyctf{better_thank_the_french_for_this_one}'
```

I mamy flagę :-)
