import discord
import random
import os
from discord.ext import commands
from config.token import token

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='-=-', intents=intents)

global liberado

@bot.event
async def on_message(message):

    # consertar problema do liberado
    
    try: liberado
    except NameError: liberado = True
    print(liberado)

    if message.content.lower().startswith("setar canal"):

        if os.path.exists("config/channel.txt"):
            os.remove("config/channel.txt")

        channelConfig = open("config/channel.txt","a+")
        channelConfig.write(message.content[12:])
        channelConfig.close()
        await message.channel.send(f"setei o canal pro <#{message.content[12:]}>")

    if message.content.lower().startswith("coloca eles no chinelo"):
        if liberado == True:
            await message.channel.send("é pra já kkkkkkkkkk")
            liberado = False
            print(liberado)
    
    if message.content.lower().startswith("para com isso"):
            await message.channel.send("beleza chefia tá liberado")
            liberado = True
            print(liberado)

    if message.content.lower().startswith("tá liberado ou não tá?"):
        await message.channel.send(liberado)
        print(liberado)

    return

bot.run(token)