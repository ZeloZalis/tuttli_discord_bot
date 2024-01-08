import discord
from decouple import config
from discord.ext import commands, tasks
from resources import *
from itertools import cycle
import os
import asyncio

client = commands.Bot(command_prefix="$", intents=discord.Intents.all(), help_command=None)
bot_status = cycle(["Comiendo lechuguita.", "Paseando.", "Haciendo cosas extremas."])

async def load():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await client.load_extension(f"cogs.{filename[:-3]}")

async def main():
    async with client:
        await load()
        await client.start(config("token"))

@tasks.loop(minutes=1)
async def change_status():
    await client.change_presence(activity=discord.Game(next(bot_status)))

@client.event
async def on_ready(): #Acción que realizará al conectarse en la consola.
    print("Tuttli connected to Discord succesfully.")
    change_status.start()

asyncio.run(main())