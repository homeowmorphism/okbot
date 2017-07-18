# OK Bot

A bot that tells you it's ok when you need to hear it.

Forked from [Abe Hmiel](https://gist.github.com/abehmiel)'s gist [streaming_boy.py](https://gist.github.com/abehmiel/da50b27796062f6b71c8585fa07d66c4).

## How To Use
1. Create new app on [apps.twitter.com](https://apps.twitter.com/).

2. Go to Keys and Access Tokens.

3. In [creds.py](https://github.com/homeowmorphism/okbot/blob/master/creds.py), copy-paste the keys into the corresponding variables and save the file.

4. Test the bot, type in terminal
``` bash
$ python ok_bot.py
```
the console will print the sample response. 

5. To run the bot in real line, uncomment the line 

``` python
# api.update_status(status=statusMsg)
```

and run the code in python again.

``` bash
$ python ok_bot.py
```

## Exit
Ctrl+D should work if you are using Linux.
If you are using a Mac, press Ctrl+Z. 

## Requirements 
tweepy library.

```
$ pip install tweepy
```


