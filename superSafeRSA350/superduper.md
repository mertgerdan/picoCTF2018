## Super Safe RSA

### Problem
Dr. Xernon made the mistake of rolling his own crypto.. Can you find the bug and decrypt the message? Connect with nc 2018shell1.picoctf.com 6262.

### Solution
The hint is a bit vague, but in order for us to decrypt this, we somehow need to find the prime factors of N.
Since N is a relatively small number (in terms of crypto), https://www.alpertron.com.ar/ECM.HTM 's integer factorization calculator gave me the result in a little over 9 hours.

After that, finding the totient (p-1)*(q-1), and plugging the value into the program I wrote in rsa madlibs gives us the ciphertext,
then a hex decode should do the trick.
