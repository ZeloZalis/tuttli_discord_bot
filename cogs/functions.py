import discord
from discord.ext import commands
from discord.ext.commands import HelpCommand
import random

client = commands.Bot(command_prefix="$", intents=discord.Intents.all(), help_command=None)
class Functions(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("Cogs is ready!")
    
    @commands.command()
    async def ehlipin(self, ctx):
        with open("resources\ehlipin.txt", "r") as file:
            response_list = file.readlines()
            response = random.choice(response_list)
        await ctx.send(f"Presenta a tu hermana.\n{response}")
    
    @commands.command()
    async def yoelito(self, ctx):
        with open("resources\yoelito.txt", "r") as file:
            response_list = file.readlines()
            response = random.choice(response_list)
        await ctx.send(response)

    @commands.command()    
    async def urielito(self, ctx):
        with open(r"resources\urielito.txt", "r") as file:
            response_list = file.readlines()
            response = random.choice(response_list)
        await ctx.send(response)

    @commands.command(aliases = ["ye", "yé"])
    async def yes(self, ctx):
        await ctx.send("Puto.")

    @commands.command()
    async def freddy(self, ctx):
        await ctx.send("https://tenor.com/view/simp-simping-yelling-meryl-streep-shouting-gif-17852144")

    @commands.command(aliases=["luí"])
    async def lui(self, ctx):
        await ctx.send("https://tenor.com/view/super-saiyan-blue-god-goku-gif-18775110")

    @commands.command(aliases=["payo"])
    async def payito(self, ctx):
        with open("resources\payito.txt", "r") as file:
            response_list = file.readlines()
            response = random.choice(response_list)
        await ctx.send(response)

    @commands.command(aliases=["valkie", "valkiria"])
    async def valki(self, ctx):
        with open("resources\valki.txt", "r") as file:
            response_list = file.readlines()
            response = random.choice(response_list)
        await ctx.send(response)

    @commands.command()
    async def help(self, ctx):
        embed_message = discord.Embed(title="Tuttli comandos!", description="A continuación tienes la lista de comandos disponibles de Tuttli:", color=discord.Color.yellow())
        embed_message.set_author(name=f"Requested by. {ctx.author.name}", icon_url=ctx.author.avatar)
        # embed_message.set_thumbnail(url="https://tenor.com/view/hedgehog-cute-animals-animal-gif-26682283")
        # embed_message.set_image(url=ctx.guild.icon)

        embed_message.add_field(name="$payito", value="Muestra un gif de una payito!", inline=False)
        embed_message.add_field(name="$ye", value="Puto", inline=False)
        embed_message.add_field(name="$yoelito", value="Muestra un gif de yoelito.", inline=False)

        # embed_message.set_footer(text="This is the footer", icon_url=ctx.author.avatar)
        await ctx.send(embed=embed_message)
        
async def setup(client):
    await client.add_cog(Functions(client))