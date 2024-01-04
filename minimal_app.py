import discord
from decouple import config
from discord.ext import commands
import random

client = commands.Bot(command_prefix = "$", intents = discord.Intents.all())

@client.event
async def on_ready(): #Acción que realizará al conectarse en la consola.
    print("Tuttli connected to Discord succesfully.")

@client.command()
async def tuttli(ctx): #Comando $tuttli
    await ctx.send("https://tenor.com/view/turtle-turt-funny-vibe-le-vibe-gif-22183231") #Respuesta al comando
    # await ctx.author.send("Le gana.") #Respuesta al comando al priv del autor.

@client.command(aliases=["8ball", "bola ocho", "eight ball"])
async def magic_eightball(ctx):
    await ctx.send("Por los momentos no tengo respuestas asignadas.")

@client.command()
async def ping(ctx):
    bot_latency = round(client.latency*1000)
    await ctx.send(f"Tu ping es de {bot_latency} ms.")

@client.command()
async def ehlipin(ctx):
    await ctx.send("Presenta a tu hermana.\nhttps://www.ntrguadalajara.com/evidimg/2018-02-25_10-02-20___3661.jpg")
    # await ctx.send("https://www.ntrguadalajara.com/evidimg/2018-02-25_10-02-20___3661.jpg")

@client.command()
async def yoelito(ctx):
    await ctx.send("https://tenor.com/view/hitam-atau-black-laugh-white-teeth-gif-16766958")

@client.command()
async def urielito(ctx):
    await ctx.send("https://tenor.com/view/speech-bubble-discord-speech-bubble-midget-midget-speech-bubble-gif-9744429228458603953")

@client.command(aliases = ["ye", "yé"])
async def yes(ctx):
    await ctx.send("Puto.")

@client.command()
async def freddy(ctx):
    await ctx.send("https://tenor.com/view/simp-simping-yelling-meryl-streep-shouting-gif-17852144")

@client.command(aliases=["luí"])
async def lui(ctx):
    await ctx.send("https://tenor.com/view/super-saiyan-blue-god-goku-gif-18775110")

@client.command()
async def payito(ctx):
    await ctx.send("https://tenor.com/view/edgehog-microsoft-edge-hedgehog-hedgehogs-love-gif-5716336851784170441")

client.run(config("token"))