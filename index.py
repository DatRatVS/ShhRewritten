import discord
import random
import os
import asyncio
from discord.ext import commands
from config.token import token

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="=", intents=intents)

liberado = True

@bot.event
async def on_ready():

    activities = [
      "calando boquinhas desde 21/02/2022",
      "fica xiu mano, to te vendo",
      "eu não quero conversar com você cara, some",
      "puta que pariu que cara chato",
      "https://bit.ly/36jQxzk",
      "cope",
      "ratio",
      "didn\'t ask",
      "cringe",
      "you fell off",
      "don\'t care",
      "skill issue",
      "cancelled",
      "quote tweet",
      "counter ratio",
      "blocked",
      "pinged owner",
      "erration",
      "cry about it"
    ]
    while True:
        await bot.change_presence(status=discord.Status.idle, activity=discord.Game(random.choice(activities)))
        await asyncio.sleep(6)

@bot.listen()
async def on_message(message):

    global liberado

    if message.content.lower().startswith("setar canal"):

        if message.content[12:].isnumeric() and bot.get_channel(int(message.content[12:])) != "None":
            if not message.author.id == 290293141666267136:
                await message.channel.send("menó, tu nem adm é kkkkkkkkkkkkkkj some")
                return
        else:
            await message.channel.send("menó, isso dai n é um canal não kkkkkkkkkj")
            return

        if os.path.exists("config/channel.txt"):
            os.remove("config/channel.txt")

        channelConfig = open("config/channel.txt","a+")
        channelConfig.write(message.content[12:])
        channelConfig.close()
        await message.channel.send(f"setei o canal pro <#{message.content[12:]}>")

    if message.content.lower().startswith("coloca eles no chinelo"):
        if liberado:
            if not message.author.id == 290293141666267136:
                await message.channel.send("menó, tu nem adm é kkkkkkkkkkkkkkj some")
                return
            liberado = not liberado
            await message.channel.send("é pra já kkkkkkkkkk")
            return
    
    if message.content.lower().startswith("para com isso"):
        if not liberado:
            if not message.author.id == 290293141666267136:
                await message.channel.send("menó, tu nem adm é kkkkkkkkkkkkkkj some")
                return
            liberado = True
            await message.channel.send("beleza chefia tá liberado")
            return

    channelConfig = open("config/channel.txt","r")

    if liberado == False and message.channel.id == int(channelConfig.read()):
        if message.author == bot.user:
            return
        frases = [
        "na minha epoca as pessoas não falavam, fica xiu",
        "vai dar meia hora de bunda com o relógio parado",
        "eu não quero conversar com você cara, some",
        "você só fala mano meu deus",
        "<https://bit.ly/36jQxzk>",
        "minha vontade é encher a sua boca na porrada",
        "CALA A BOCA PORRAAAAAAAAAAAAAAAAAAAAAAAAAA",
        "mano, acho que tu ja percebeu que eu quero que tu cale a porra da boca",
        "aooooo vai toma no cu google CALA A BOCA",
        "VOCÊ NÃO PODE SE AJUDAR A CALAR A BOCA?",
        "vai ser contratado pro vasco se continuar falando mlk, para logo",
        "uiuiui, um sistema unificado pras universidades, CALA A PORRA DA BOCA NINGUEM LIGA",
        "que corte de cabelo dahora mano, KKKKKKKKKKKKKKKKK AGORA TE CALA",
        "deu até ânsia de tanto que tu fala mlk, fica xiu",
        "mano tu parece o voyager 3, PARA, DE, FALAR",
        "tu tem problema mlk só pode",
        "kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk seu inútil, CALA A PORRA DA BOCA",
        "pindamonhangabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
        "🤫🤫🤫🤫🤫🤫🤫🤫",
        "parou?",
        "vai dormir caralho, tu tem que calar a porra da boca",
        "paraaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
        "meu deeeeeeeeeeeeeeeus vai arrumar algo pra fazer seu vagabundo inútil",
        "porra de rolê cosmico caralho, kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk",
        "vascoooooooooooooooo",
        "neeeee noooooo neeeeee nooooooo",
        "tu chega fede feijoada mano",
        "fala mais algo pra tu ver ai, duvido",
        "tenta dnv mano",
        "hoje não kkkkkkkkkkkkkk",
        "me manda um pix que eu te deixo falar",
        "falou tudo mas falou nada",
        "qual foi?",
        "tá ratiando mlk, só cala a boca",
        "pena é a nossa diferença de idade",
        "n sai filho da puta",
        "mastiga biscoito no meu ouvido mano, vai",
        "esse vermelho tá mais pra rosa, só calar a boquinha",
        "seu miserável (não desmerecendo sua história)",
    ]
        await message.delete()
        await message.channel.send(f"{message.author.mention}, {random.choice(frases)}")

    channelConfig.close()
    return

bot.run(token)