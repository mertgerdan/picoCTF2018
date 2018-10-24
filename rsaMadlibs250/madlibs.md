## RSA-madlibs

### Problem
We ran into some weird puzzles we think may mean something, can you help me solve one? Connect with nc 2018shell1.picoctf.com 50652

### Solution
Using the file plus a scientific calculator, I got most the madlibs correctly. When d comes out to be negative, know that you can switch it to become positive.

A negative d value will result in an error on my program, but modular arithmetic helps us overcome that.

Here is an example for how that's done:
5 = -7 (mod 12) -> Think about it like a clock, both 5 and -7 gives you 5am/pm on the 12 hour clock.
