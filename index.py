import discord
from decouple import config
from discord.ext import commands, tasks
from resources import *
from itertools import cycle
import os
import asyncio
import json

def get_server_prefix(client, message):
    with open("prefixes.json", "r") as f:
        prefix = json.load(f)
    return prefix[str(message.guild.id)]

client = commands.Bot(command_prefix=get_server_prefix, intents=discord.Intents.all(), help_command=None)
bot_status = cycle(["Comiendo lechuguita.", "$help"])

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

@client.event
async def on_guild_join(guild):
    with open("prefixes.json", "r") as f:
        prefix = json.load(f)
    
    prefix[str(guild.id)] = "$"

    with open("prefixes.json", "w") as f:
        json.dump(prefix, f, indent=4)

@client.event
async def on_guild_remove(guild):
    with open("prefixes.json", "r") as f:
        prefix = json.load(f)
    
    prefix.pop(str(guild.id))

    with open("prefixes.json", "w") as f:
        json.dump(prefix, f, indent=4)

@client.command()
async def setprefix(ctx, *, newprefix: str):
    with open("prefixes.json", "r") as f:
        prefix = json.load(f)
    
    prefix[str(ctx.guild.id)] = newprefix

    with open("prefixes.json", "w") as f:
        json.dump(prefix, f, indent=4)

asyncio.run(main())