import discord
from discord.ext.commands import HelpCommand
from discord.ext import commands

# client = commands.Bot(command_prefix="$", intents=discord.Intents.all(), help_command=None)

# class MyHelpCommand(HelpCommand, commands.Cog):
#     async def bot_help(self, ctx):
#         embed_message = discord.Embed(title="Tuttli comandos!", description="A continuación tienes la lista de comandos disponibles de Tuttli:", color=discord.Color.yellow())
#         embed_message.set_author(name=f"Requested by. {ctx.author.name}", icon_url=ctx.author.avatar)

#         embed_message.add_field(name="$payito", value="Muestra un gif de una payito!", inline=False)
#         embed_message.add_field(name="$ye", value="Puto", inline=False)
#         embed_message.add_field(name="$yoelito", value="Muestra un gif de yoelito.", inline=False)

#         await ctx.send(embed=embed_message)

# client.HelpCommand = MyHelpCommand

# async def setup(client):
#     await client.add_cog(MyHelpCommand(client))