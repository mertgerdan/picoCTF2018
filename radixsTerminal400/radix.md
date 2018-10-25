## Radix's Terminal

### Problem
Can you find the password to Radix's login? You can also find the executable in /problems/radix-s-terminal_3_ebd96675807277b0ab95a5d197ef3de9?

### Solution
Opening the file as ASCII, we are greeted with an .ELF file. What strikes me though is this part:

```cGljb0NURntiQXNFXzY0X2VOQ29EaU5nX2lTX0VBc1lfNzU3NDAyNTF9 Please provide a password! Congrats, now where's my flag? Incorrect Password!;```

The first part is a base64 encoded string. Decoding it will give us:
```picoCTF{bAsE_64_eNCoDiNg_iS_EAsY_75740251}```
