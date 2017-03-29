## Edge_1 [WEB 100]

>We found Edge inc's website! Take a look at it here.
>
>http://edge1.web.easyctf.com/ (page no longer available)

### EN / [PL](#rozwiązanie)

### Solution:

After a long time spent on the site and various attempts to discover some weaknesses, I finally got the idea to look for the `.git` directory.
It turned out that I had full access to it.

Once I've downloaded the entire page using `wget` and removed unnecessary html files that wget automatically dropped, I simply entered the `git show` command to view the last commit.

```
$ git show
commit ee9061b25d8a35bae8380339f187b44dc26f4999
Author: Michael <michael@easyctf.com>
Date:   Mon Mar 13 07:11:47 2017 +0000

    Whoops! Remove flag.

diff --git a/flag.txt b/flag.txt
deleted file mode 100644
index a1009d9..0000000
--- a/flag.txt
+++ /dev/null
@@ -1 +0,0 @@
-easyctf{w3_ev3n_u53_git}
```

### [EN](#solution) / PL

### Rozwiązanie:

Po dłuższym czasie spędzonym na stronie i różnych próbach odkrycia jakichś słabości wpadłem w końcu na pomysł, żeby poszukać katalogu `.git`.
Był to strzał w dziesiątkę, gdyż był do niego pełen dostęp.

Po pobraniu całej strony za pomocą `wget` i usunięciu z gita zbędnych plików html, które wget tam automatycznie wrzucił wystarczyło wpisać komendę `git show`, żeby podejrzeć ostatniego commita.

```
$ git show
commit ee9061b25d8a35bae8380339f187b44dc26f4999
Author: Michael <michael@easyctf.com>
Date:   Mon Mar 13 07:11:47 2017 +0000

    Whoops! Remove flag.

diff --git a/flag.txt b/flag.txt
deleted file mode 100644
index a1009d9..0000000
--- a/flag.txt
+++ /dev/null
@@ -1 +0,0 @@
-easyctf{w3_ev3n_u53_git}
```
