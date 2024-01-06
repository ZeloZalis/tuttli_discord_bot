import discord
from decouple import config
from discord.ext import commands, tasks
import random
from resources import *
from itertools import cycle

client = commands.Bot(command_prefix = "$", intents = discord.Intents.all())

bot_status = cycle(["Comiendo lechuguita.", "Paseando.", "Haciendo cosas extremas."])

@tasks.loop(minutes=1)
async def change_status():
    await client.change_presence(activity=discord.Game(next(bot_status)))

@client.event
async def on_ready(): #Acción que realizará al conectarse en la consola.
    print("Tuttli connected to Discord succesfully.")
    change_status.start()

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
    await ctx.send(f"Mi ping es de {bot_latency} ms.")

@client.command()
async def ehlipin(ctx):
    with open("resources\ehlipin.txt", "r") as file:
        response_list = file.readlines()
        response = random.choice(response_list)
    await ctx.send(f"Presenta a tu hermana.\n{response}")

@client.command()
async def yoelito(ctx):
    with open("resources\yoelito.txt", "r") as file:
        response_list = file.readlines()
        response = random.choice(response_list)
    await ctx.send(response)

@client.command()
async def urielito(ctx):
    with open(r"resources\urielito.txt", "r") as file:
        response_list = file.readlines()
        response = random.choice(response_list)
    await ctx.send(response)

@client.command(aliases = ["ye", "yé"])
async def yes(ctx):
    await ctx.send("Puto.")

@client.command()
async def freddy(ctx):
    await ctx.send("https://tenor.com/view/simp-simping-yelling-meryl-streep-shouting-gif-17852144")

@client.command(aliases=["luí"])
async def lui(ctx):
    await ctx.send("https://tenor.com/view/super-saiyan-blue-god-goku-gif-18775110")

@client.command(aliases=["payo"])
async def payito(ctx):
    with open("resources\payito.txt", "r") as file:
        response_list = file.readlines()
        response = random.choice(response_list)
    await ctx.send(response)

@client.command(aliases=["valkie", "valkiria"])
async def valki(ctx):
    with open("resources\valki.txt", "r") as file:
        response_list = file.readlines()
        response = random.choice(response_list)
    await ctx.send(response)

client.run(config("token"))