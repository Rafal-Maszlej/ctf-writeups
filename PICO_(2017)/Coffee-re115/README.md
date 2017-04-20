## Coffee [RE 115]

>You found a suspicious USB drive in a jar of pickles. It contains this file file.
>
>HINTS
>
>Is there a way to get the source of the program?

* [freeThePickles.class](freeThePickles.class)

### EN / [PL](#rozwiązanie)

### Solution:

We have a compiled java file.

At address http://www.javadecompilers.com/ there is a nice decompiler available after use of which I got the source code:

```java
import java.util.Base64.Decoder;

public class problem {
  public problem() {}
  
  public static String get_flag() { String str1 = "Hint: Don't worry about the schematics";
    String str2 = "eux_Z]\\ayiqlog`s^hvnmwr[cpftbkjd";
    String str3 = "Zf91XhR7fa=ZVH2H=QlbvdHJx5omN2xc";
    byte[] arrayOfByte1 = str2.getBytes();
    byte[] arrayOfByte2 = str3.getBytes();
    byte[] arrayOfByte3 = new byte[arrayOfByte2.length];
    for (int i = 0; i < arrayOfByte2.length; i++)
    {
      arrayOfByte3[i] = arrayOfByte2[(arrayOfByte1[i] - 90)];
    }
    System.out.println(java.util.Arrays.toString(java.util.Base64.getDecoder().decode(arrayOfByte3)));
    return new String(java.util.Base64.getDecoder().decode(arrayOfByte3));
  }
  
  public static void main(String[] paramArrayOfString) {
    System.out.println("Nothing to see here");
  }
}
```

I'm not much a java expert, so with help of documentation I rewritten a `get_flag()` function on Python.

```python
import base64

def get_flag():
    str1 = "Hint: Don't worry about the schematics"
    str2 = "eux_Z]\\ayiqlog`s^hvnmwr[cpftbkjd"
    str3 = "Zf91XhR7fa=ZVH2H=QlbvdHJx5omN2xc"
    
    arrayOfByte1 = bytearray(str2, 'utf-8')
    arrayOfByte2 = bytearray(str3, 'utf-8')
    arrayOfByte3 = bytearray(0x01 * len(arrayOfByte2))
    
    for i in range(len(arrayOfByte2)):
        arrayOfByte3[i] = arrayOfByte2[(arrayOfByte1[i] - 90)];
    
    return str(base64.b64decode(arrayOfByte3), 'utf-8')


print(get_flag())
```

As expected, the function returns the flag :-)

```
flag_{pretty_cool_huh}
```

### [EN](#solution) / PL

### Rozwiązanie:

Do dyspozycji jest skompilowany plik javy.

Pod adresem http://www.javadecompilers.com/ dostępny jest fajny dekompilator, po użyciu którego dostałem kod źródłowy:

```java
import java.util.Base64.Decoder;

public class problem {
  public problem() {}
  
  public static String get_flag() { String str1 = "Hint: Don't worry about the schematics";
    String str2 = "eux_Z]\\ayiqlog`s^hvnmwr[cpftbkjd";
    String str3 = "Zf91XhR7fa=ZVH2H=QlbvdHJx5omN2xc";
    byte[] arrayOfByte1 = str2.getBytes();
    byte[] arrayOfByte2 = str3.getBytes();
    byte[] arrayOfByte3 = new byte[arrayOfByte2.length];
    for (int i = 0; i < arrayOfByte2.length; i++)
    {
      arrayOfByte3[i] = arrayOfByte2[(arrayOfByte1[i] - 90)];
    }
    System.out.println(java.util.Arrays.toString(java.util.Base64.getDecoder().decode(arrayOfByte3)));
    return new String(java.util.Base64.getDecoder().decode(arrayOfByte3));
  }
  
  public static void main(String[] paramArrayOfString) {
    System.out.println("Nothing to see here");
  }
}
```

Nie jestem raczej znawcą javy, więc posiłkując się dokumentacją przepisałem funkcję `get_flag()` na Pythona.

```python
import base64

def get_flag():
    str1 = "Hint: Don't worry about the schematics"
    str2 = "eux_Z]\\ayiqlog`s^hvnmwr[cpftbkjd"
    str3 = "Zf91XhR7fa=ZVH2H=QlbvdHJx5omN2xc"
    
    arrayOfByte1 = bytearray(str2, 'utf-8')
    arrayOfByte2 = bytearray(str3, 'utf-8')
    arrayOfByte3 = bytearray(0x01 * len(arrayOfByte2))
    
    for i in range(len(arrayOfByte2)):
        arrayOfByte3[i] = arrayOfByte2[(arrayOfByte1[i] - 90)];
    
    return str(base64.b64decode(arrayOfByte3), 'utf-8')


print(get_flag())
```

Zgodnie z przewidywaniami funkcja zwraca flagę :-)

```
flag_{pretty_cool_huh}
```
