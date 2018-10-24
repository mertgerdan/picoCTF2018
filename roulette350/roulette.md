## Roulette

### Problem
This Online Roulette Service is in Beta. Can you find a way to win $1,000,000,000 and get the flag? Source. Connect with nc 2018shell1.picoctf.com 26662

### Solution
Uh, this one. This took me quite some time to find and was pretty annoying.

Hint tells us there are two bugs in the source code. Upon examining it, something strikes me.

They only seed the random function once, and that seed is the money you start with.
Therefore, I ran a seperate online c compiler. I mirrored the actual program with my online one basically.

I first entered the seed and played on the online one, got a bogus result, and then it showed me the correct roulette spin after losing. 

After that, I bet all my money on the correct number to double it. However, after doing this once, the random pattern
started to fade. Turns out the problem was on:



```if (spin == choice) {
    cash += 2*bet;
    puts(win_msgs[rand()%NUM_WIN_MSGS]);
    wins += 1;
  }
  else {
    puts(lose_msgs1[rand()%NUM_LOSE_MSGS]);
    puts(lose_msgs2[rand()%NUM_LOSE_MSGS]);
  }
  ```
  
It executed rand() twice when losing and once when winning, so after losing on the online one and winning on the real one, they desynchronized.
I simply deleted one of the rand() calls on _else_ in my mirror program and I was good to go. Or so I thought.

The real program timed me out before I could reach 1 billion $ like this, even when I did it as fast as it was possible.
Then I saw this piece of code:

```
if (wins >= MAX_WINS) {
	printf("Wow you won %lu times? Looks like its time for you cash you out.\n", wins);
	printf("Congrats you made $%lu. See you next time!\n", cash);
	exit(-1);
      }
 ```
      
This tells me that if you win more than 16 times, the program exits.
_5000(max possible money)*2^16_ only yields 327 million, so something was up.

The second bug was yet to be found, and it had something to do with how much money you could bet.
I knew that the _get_long()_ method was funky, so I deeply examined it.

```
long get_long() {
    printf("> ");
    uint64_t l = 0;
    char c = 0;
    while(!is_digit(c))
      c = getchar();
    while(is_digit(c)) {
      if(l >= LONG_MAX) {
	l = LONG_MAX;
	break;
      }
      l *= 10;
      l += c - '0';
      c = getchar();
    }
    while(c != '\n')
      c = getchar();
    return l;
}
```

And I found it!
LONG_MAX was equal to 2147483647 but l, the variable was a unsigned int! Unsigned ints have a max value of 4294967295.
So after three successful wins and then betting more money than you have and losing yields the flag.

What a long one this was!
