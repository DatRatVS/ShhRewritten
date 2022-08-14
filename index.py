import discord
import random
import os
import asyncio
from discord.ext import commands

from config.token import token
from config.strings import frases
from config.strings import activities
from config.strings import setChannelCommand
from config.strings import startCommand
from config.strings import stopCommand
from config.strings import pingCommand

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="=", intents=intents)

liberado = True

if os.path.exists("config/channel.txt"):
    channelConfig = open("config/channel.txt","r")
    channelCache = int(channelConfig.read())
    channelConfig.close()
else:
    channelCache = 1

@bot.event
async def on_ready():
    while True:
        await bot.change_presence(status=discord.Status.idle, activity=discord.Game(random.choice(activities)))
        await asyncio.sleep(6)

@bot.listen()
async def on_message(message):

    global liberado
    global channelCache

    if message.content.lower().startswith(setChannelCommand):

        if message.content[len(setChannelCommand) + 1:].isnumeric() and bot.get_channel(int(message.content[len(setChannelCommand) + 1:])) != "None":
            if not message.author.guild_permissions.manage_messages:
                await message.channel.send("menó, tu nem adm é kkkkkkkkkkkkkkj some")
                return
        else:
            await message.channel.send("menó, isso dai n é um canal não kkkkkkkkkj")
            return

        if os.path.exists("config/channel.txt"):
            os.remove("config/channel.txt")

        channelConfig = open("config/channel.txt","a+")
        channelConfig.write(message.content[len(setChannelCommand) + 1:])
        channelCache = int(message.content[len(setChannelCommand) + 1:])
        channelConfig.close()
        await message.channel.send(f"setei o canal pro <#{message.content[len(setChannelCommand) + 1:]}>")

    if message.content.lower().startswith(startCommand):
        if liberado:
            if not message.author.guild_permissions.manage_messages:
                await message.channel.send("menó, tu nem adm é kkkkkkkkkkkkkkj some")
                return
            liberado = not liberado
            await message.channel.send("é pra já kkkkkkkkkk")
            return
    
    if message.content.lower().startswith(stopCommand):
        if not liberado:
            if not message.author.guild_permissions.manage_messages:
                await message.channel.send("menó, tu nem adm é kkkkkkkkkkkkkkj some")
                return
            liberado = True
            await message.channel.send("beleza chefia tá liberado")
            return

    if message.content.lower().startswith(pingCommand):
        if not message.author.guild_permissions.manage_messages:
            return
        await message.channel.send(f"pongue porra: {round(bot.latency * 1000)}ms")
        return

    if liberado == False:
        if message.channel.id == channelCache:
            if message.author == bot.user:
                return

            await message.delete()
            await message.channel.send(f"{message.author.mention}, {random.choice(frases)}")

    return

bot.run(token)