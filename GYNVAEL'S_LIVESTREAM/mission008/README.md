## mission 006

>Oh great. We received another message. "It's plaintext" - that's what he told us.<br>
>We knew better, but we still had hope that it will actually be plaintext. It <br>
>wasn't. It was just this huge number:
>
>    1087943696176439095600323762148055792209594928798662843208446383247024
>
>We called the agent and asked about it. Calmly. We didn't yell. Not at all. Maybe<br>
>A little.
>
>He told us it was plaintext. He just multiplied it by an unknown number. We will<br>
>just give it to you to decipher.
>
>On a more positive note, we have two new agents in training.
>
>GOOD LUCK!
>
>If you decode the answer, put it in the comments under this video! If you write<br>
>a blogpost / post your solution online, please add a link in the comments too!
>
>P.S. I'll show/explain the solution on the stream next week.<br>
>P.S.2. It's just two bytes. But there is a plot twist. Expect the unexpected.

### Solution:

This time rather quick solution. I go through the whole range and ... I'm afraid that I missed the "plot twist" :-P

```python
from libnum import n2s # or from libnum.strings import n2s
from string import printable

s = 1087943696176439095600323762148055792209594928798662843208446383247024

for num in range(2, 0xffff):
    text = n2s(s / num)
    
    if all(char in printable for char in text):
        print text, num
```

Running script:

```
$ python solver.py 
Text is just a long number. 31336
```

And there is only one solution for the number 31336: `Text is just a long number.`
