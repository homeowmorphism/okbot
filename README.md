# OK Bot

*Status: Polished. Wanna swap this for a better bot later :)*

A bot that retweets you it's going to be ok when you need to hear it. 

Forked from [Abe Hmiel](https://gist.github.com/abehmiel)'s gist [streaming_boy.py](https://gist.github.com/abehmiel/da50b27796062f6b71c8585fa07d66c4).

## Requirements 
tweepy library.

```
$ pip install tweepy
```

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
If you are using a Mac, press Ctrl+Z or Ctrl \.

## Customize
There are three variables that need to changed for customization. 

The variable **matches** is the list of strings which the bot will retweet. The list is not case sensitive, so if you write 

```
matches = ["hello","bonjour"]
```

then "Hello", "hEllO" and "hello" all count as a match. Same with "Bonjour", "bOnJour" and "bonjour".

The variable **phrases** are the phrases the bot will reply, selected at random. Similarly to match, it is given as a list of strings.

```
phrases = ["Hello back!", "Hi!" ]
```
Finally, **stream.filter(track=[**inputs**], async=True)** prefilters the stream for potential matches. 

The OK Bot filters for the word "ok".

```
stream.filter(track=["ok"], async=True)
```
