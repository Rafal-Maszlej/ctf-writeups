http://stackoverflow.com/questions/38943038/difference-between-python-2-and-3-for-shuffle-with-a-given-seed
http://stackoverflow.com/questions/11929701/why-is-seeding-the-random-generator-not-stable-between-versions-of-python

###random.random()

```
$ python3
Python 3.4.2 (default, Oct  8 2014, 10:45:20) 
[GCC 4.9.1] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import random
>>> random.seed('aaaa', version=1)
>>> [random.random() for _ in range(10)]
[0.7364334750180912, 0.19527212939099625, 0.2391186082024619, 0.48770277408661444, 0.6624341987427449, 0.06431021231982137, 0.43620855551414794, 0.7412005251670937, 0.7341380808655814, 0.986786466423472]
>>> 
>>> random.seed('aaaa', version=2)
>>> [random.random() for _ in range(10)]
[0.9343055095747843, 0.4862179102811198, 0.42253440674650034, 0.6956651189859664, 0.043266353998476115, 0.22296999822800045, 0.038955842723416456, 0.09215674744035762, 0.12703178706690166, 0.8722132116291076]
>>> 
>>> random.seed(42)
>>> [random.random() for _ in range(10)]
[0.6394267984578837, 0.025010755222666936, 0.27502931836911926, 0.22321073814882275, 0.7364712141640124, 0.6766994874229113, 0.8921795677048454, 0.08693883262941615, 0.4219218196852704, 0.029797219438070344]
>>> 
```

```
$ python
Python 2.7.9 (default, Jun 29 2016, 13:08:31) 
[GCC 4.9.2] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> import random
>>> random.seed('aaaa')
>>> [random.random() for _ in range(10)]
[0.10279891578939493, 0.8065945195119997, 0.8364480166235572, 0.08997755796642748, 0.18088250122244154, 0.6713288974286677, 0.4379992622933452, 0.26213827248893584, 0.35048256566047487, 0.4737050095839809]
>>> 
>>> random.seed(42)
>>> [random.random() for _ in range(10)]
[0.6394267984578837, 0.025010755222666936, 0.27502931836911926, 0.22321073814882275, 0.7364712141640124, 0.6766994874229113, 0.8921795677048454, 0.08693883262941615, 0.4219218196852704, 0.029797219438070344]
```

###random.randrange()

```
$ python3
Python 3.4.2 (default, Oct  8 2014, 10:45:20) 
[GCC 4.9.1] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import random
>>> random.seed('aaaa', version=1)
>>> [random.randrange(1,100) for _ in range(10)]
[82, 40, 83, 71, 3, 60, 34, 66, 30, 71]
>>> 
>>> random.seed('aaaa', version=2)
>>> [random.randrange(1,100) for _ in range(10)]
[97, 63, 30, 55, 10, 90, 93, 6, 94, 29]
>>> 
>>> random.seed(42, version=1)
>>> [random.randrange(1,100) for _ in range(10)]
[82, 15, 4, 95, 36, 32, 29, 18, 95, 14]
>>> 
>>> random.seed(42, version=2)
>>> [random.randrange(1,100) for _ in range(10)]
[82, 15, 4, 95, 36, 32, 29, 18, 95, 14]
```

```
$ python
Python 2.7.9 (default, Jun 29 2016, 13:08:31) 
[GCC 4.9.2] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> import random
>>> random.seed('aaaa')
>>> [random.randrange(1,100) for _ in range(10)]
[11, 80, 83, 9, 18, 67, 44, 26, 35, 47]
>>> 
>>> random.seed(42)
>>> [random.randrange(1,100) for _ in range(10)]
[64, 3, 28, 23, 74, 68, 90, 9, 43, 3]
```
