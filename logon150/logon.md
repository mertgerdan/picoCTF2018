## Logon

This one is the first sort of technical one.

**Problem**
I made a website so now you can log on to! I don't seem to have the admin password. See if you can't get to the flag. 
```http://2018shell1.picoctf.com:5477```

**Solution**
It only lets you see the flag when you are an admin, and the check can be found in the post request. 
Simply logging in with an username and password then changing ```Admin=False``` to ```Admin=True``` yields the flag.
