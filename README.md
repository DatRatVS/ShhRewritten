# About

The shh BOT is a Discord bot made in [discord.py](https://github.com/Rapptz/discord.py) that locks you from sending messages in a chat, and every time you try to do it, you get ratio'ed and roasted.

# Commands

`setar canal (channel id)` - Sets the bot's functionality to this channel<p></p>
`coloca eles no chinelo` - Starts doing it's thing<p></p>
`para com isso` - Stop doing it's thing<p></p>
Although, commands are customizable, if you're willing to customize them, head into `strings.py` and modificate them as you wish.<p></p>

# Adding more messages

Head into `strings.py`, and you may add, remove or modify them there.<p></p>
As long as each piece of phrase has one comma (,) at the end, they should be fine to work with the bot.<p></p>
You can do it with the bot's activities as well, do the same on the activities array instead.<p></p>

# How to use it

You'll have to clone this repository, and run `index.py` by yourself. Unfortunately, you'll have to modificate the administrator ID in `administrator.py`, just go there, replace my ID with yours, and you should be ready to go.<p></p>
After cloning this repository, head in `token.py.example`, fill in with the token of your bot, and rename the file to `token.py`, and after installing [discord.py](https://github.com/Rapptz/discord.py), you should be ready to start the bot.<p></p>
With it running, set the channel using `setar canal (channel id)`<p></p>
![image](https://user-images.githubusercontent.com/49768896/181671070-3551a5d5-7e5a-4d2c-b186-ca5ece77cb17.png)<p></p>
Start it by using `coloca eles no chinelo`<p></p>
![image](https://user-images.githubusercontent.com/49768896/181671569-9387e09d-b7f2-4d45-99f2-c0a77f50ce3d.png)<p></p>
And stop it by using `para com isso`<p></p>
![image](https://user-images.githubusercontent.com/49768896/181671651-794bec1a-780a-4e79-8cae-2f4e09e73208.png)<p></p>

And you should be ready to go!

# Example
![Discord_X2pMOfTRlo](https://user-images.githubusercontent.com/49768896/181671370-97a6d741-90e4-4e65-8847-2485ff87ce41.gif)

# WIP
- Between guilds compatibility (each instance works with only one channel in one guild);
- Multi id permission (as of right now, it only supports one user administrator to control the bot);
- Polishing, it is really, REALLY, **REALLY** slow.

# Disclaimer
This is a meme bot and it is barely coded well, so please, don't take it seriously.
