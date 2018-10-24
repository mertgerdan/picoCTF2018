## Buffer Overflow 0

### Problem

Let's start off simple, can you overflow the right buffer in this program to get the flag? You can also find it in /problems/buffer-overflow-0_4_ab1efebbee9446039487c64b88d38631 on the shell server. Source.

### Solution

After examining vuln.c, we see that ```char buf[16]```is present. We have to overflow the buffer by entering more characters than it allows.
