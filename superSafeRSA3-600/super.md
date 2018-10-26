## Super Safe RSA 3

### Problem
The more primes, the safer.. right.?.? Connect with nc 2018shell1.picoctf.com 35072

### Solution
https://www.alpertron.com.ar/ECM.HTM saves the day massively on this one. Since there are more than one prime, rather than taking 9 hours like the Super Safe RSA, this integer factorization calculator got me the answer in 1.6 seconds, listing all 32 prime factors.
It also automatically calculates the phi(n) value, so a simple copy paste of that into my rsa script and fixing that negative d issue (see rsaMadlibs250),
and you will obtain your flag with the decoded plaintext's hex value decoded as ASCII.

