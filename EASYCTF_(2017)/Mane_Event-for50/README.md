## Mane_Event [FOR 50]

>My friend just got back from the plains and he took this picture with his new camera. He also told me there's a flag hidden in it - can you check it out for me?

[lion.jpg](lion.jpg)

### EN / [PL](#rozwiązanie)

### Solution:

The flag is hidden in the picture's metadata.

In my case search was limited to

```
$ strings lion.jpg | grep easyctf
@12 - Photo Contests,easyctf{pride_in_african_engin33ring},2011 B
```

### [EN](#solution) / PL

### Rozwiązanie:

Flaga ukryta jest w metadanych zdjęcia.

W moim przypadku poszukiwania ograniczyły się do

```
$ strings lion.jpg | grep easyctf
@12 - Photo Contests,easyctf{pride_in_african_engin33ring},2011 B
```
