Library to take in a string or multiple strings and generate a markov string from it. Words are delimited by spaces and passages are delimited by newlines ("\n")

```
$ pip install simple_markov
Collecting simple_markov
  Downloading simple_markov-1.0.tar.gz
Building wheels for collected packages: simple-markov
  Running setup.py bdist_wheel for simple-markov ... done
  Stored in directory: /Users/nobr/Library/Caches/pip/wheels/1a/b9/76/dc4ab8276ded2b6a3680130d6a536479b33e757fde5b26bf23
Successfully built simple-markov
Installing collected packages: simple-markov
Successfully installed simple-markov-1.0
$ python
Python 2.7.12 (default, Jun 29 2016, 14:05:02) 
[GCC 4.2.1 Compatible Apple LLVM 7.3.0 (clang-703.0.31)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from simple_markov import Markov
>>> text = "What the fuck did you just fucking say about me, you little bitch? I’ll have you know I graduated top of my class in the Navy Seals, and I’ve been involved in numerous secret raids on Al-Quaeda, and I have over 300 confirmed kills. I am trained in gorilla warfare and I’m the top sniper in the entire US armed forces. You are nothing to me but just another target. I will wipe you the fuck out with precision the likes of which has never been seen before on this Earth, mark my fucking words. You think you can get away with saying that shit to me over the Internet? Think again, fucker. As we speak I am contacting my secret network of spies across the USA and your IP is being traced right now so you better prepare for the storm, maggot. The storm that wipes out the pathetic little thing you call your life. You’re fucking dead, kid. I can be anywhere, anytime, and I can kill you in over seven hundred ways, and that’s just with my bare hands. Not only am I extensively trained in unarmed combat, but I have access to the entire arsenal of the United States Marine Corps and I will use it to its full extent to wipe your miserable ass off the face of the continent, you little shit. If only you could have known what unholy retribution your little “clever” comment was about to bring down upon you, maybe you would have held your fucking tongue. But you couldn’t, you didn’t, and now you’re paying the price, you goddamn idiot. I will shit fury all over you and you will drown in it. You’re fucking dead, kiddo."
>>> markov = Markov(text)
>>> markov.generate()
What the USA and I will drown in numerous secret raids on your fucking dead, kiddo.
>>> new_text = """Here's the thing. You said a "jackdaw is a crow."
Is it in the same family? Yes. No one's arguing that.
As someone who is a scientist who studies crows, I am telling you, specifically, in science, no one calls jackdaws crows. If you want to be "specific" like you said, then you shouldn't either. They're not the same thing.
If you're saying "crow family" you're referring to the taxonomic grouping of Corvidae, which includes things from nutcrackers to blue jays to ravens.
So your reasoning for calling a jackdaw a crow is because random people "call the black ones crows?" Let's get grackles and blackbirds in there, then, too.
Also, calling someone a human or an ape? It's not one or the other, that's not how taxonomy works. They're both. A jackdaw is a jackdaw and a member of the crow family. But that's not what you said. You said a jackdaw is a crow, which is not true unless you're okay with calling all members of the crow family crows, which means you'd call blue jays, ravens, and other birds crows, too. Which you said you don't.
It's okay to just admit you're wrong, you know?"""
>>> markov.add_text(new_text)
>>> markov.generate()
If you're saying that wipes out with my fucking say about me, you better prepare for the crow family. Yes. No one's arguing that.
```
