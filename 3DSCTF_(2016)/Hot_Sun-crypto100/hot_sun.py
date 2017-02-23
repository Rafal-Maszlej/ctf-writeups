
from string import ascii_letters

s = 'hv1g_f0h_1g_b0h_g0_V0h'

def shift_letters(text, i):
    s = ''
    for char in text:
        if char in ascii_letters:
            s += (2*ascii_letters)[ascii_letters.index(char)+i]
        else:
            s += char
    return s


n = 1
while n <= 11:
    s = shift_letters(s, -n)
    n += 1


print('3DS{%s}' % s)
