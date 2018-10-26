## Script Me

### Problem
Can you understand the language and answer the questions to retrieve the flag? Connect to the service with nc 2018shell1.picoctf.com 1542.

### Solution
The hint specifically said you should probably write a script, but being the arrogant fool I was, first tried to do it by hand.
I did 4 of 5 before getting timed out, but the fifth was so large I couldn't probably even write a random statement that large, so script writing time it was.


We have to understand the key rules in this language to program them as rules, so here are a few to break down:

() + () = ()() simple addition
(()()) + (()()) = (()())(()()) it's still simple addition

Think about them as different data types, you can only add ones that are the same type. So () and (()) are different types and cannot be directly added.

(()()) + () = (()()()) this is a merge from the right, it's like a smaller blob connecting to a larger body, with a membrane on the outside.

Same stuff for the one on left.

(())(()) + ((())) = ((())(())(())) this is an absorb merge. Think of these as layers. You can only add ones that are in the same layer, but to get them on the same layer, you have to first absorb it from the left.
So a ( ) is the outside layer, and then we have two (())'s adding to a third one. It's simple addition inside, and we have our answer.
Then, writing a script that automatically does this from left to right and printing out an answer to be copied will get us the flag.

