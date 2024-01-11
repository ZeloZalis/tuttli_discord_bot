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

    client.remove_command("help")

    @commands.command()
    async def help(self, ctx):
        embed_message = discord.Embed(title="Tuttli comandos!", description="A continuación tienes la lista de comandos disponibles de Tuttli:", color=discord.Color.green())
        embed_message.set_author(name=f"Requested by. {ctx.author.name}", icon_url=ctx.author.avatar)
        embed_message.add_field(name="$payito, $ehlipin, $yoelito, $urielito, $valki, $luí, $freddy", value="Muestra un gif del respectivo.", inline=False)
        await ctx.send(embed=embed_message)
        
    # @commands.command() #Comando para borrar X cantidad de mensajes
    # @commands.has_permissions(manage_messages=True)
    # async def clear(self, ctx, count: int):
    #     await ctx.channel.purge(limit=count)

    # @commands.command() #Comando para kickear/banear un miembro, sólo habría que cambiar {kick} por {ban}
    # @commands.has_permissions(kick_members=True)
    # async def kick(self, ctx, member: discord.member, *, modreason):
    #     await ctx.guild.kick(member)
    #     conf_embed = discord.Embed(title="Exitoso.", color=discord.color.green())
    #     conf_embed.add_field(name="Kickeado.", value=f"{member.mention} ha sido kickeado por {ctx.author.mention}", inline=False)
    #     conf_embed.add_field(name="Motivo:", value=modreason, inline=False)
    #     await ctx.send(embed=conf_embed)
    
    # @commands.command(name="unban") #Comando para desbanear.
    # @commands.guild_only()
    # @commands.has_permissions(ban_members=True)
    # async def unban(self, ctx, userID):
    #     user = discord.Object(id=userID)
    #     await ctx.guild.unban(user)
        
    #     confirmation_embed = discord.Embed(title="Exitoso.", color=discord.color.green())
    #     confirmation_embed.add_field(name="Desbaneado:", value=f"<@{userID}> ha sido desbaneado del server por {ctx.author.mention}", inline=False)
    #     await ctx.send(embed=confirmation_embed)

async def setup(client):
    await client.add_cog(Functions(client))