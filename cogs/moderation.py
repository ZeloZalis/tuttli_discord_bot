import discord
from discord.ext import commands

class Expulse(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command() #Comando para kickear.
    @commands.has_permissions(kick_members=True)
    @commands.has_role("Mod")
    async def kick(self, ctx, member: discord.Member, *, modreason: str):
        await ctx.guild.kick(member)
        conf_embed = discord.Embed(title="A casa platita.", description=f"{member.mention} ha sido papiado por {ctx.author.mention}.", color=discord.Color.green())
        conf_embed.add_field(name="Motivo:", value=modreason, inline=False)
        conf_embed.set_image(url="https://c.tenor.com/TG5OF7UkLasAAAAC/tenor.gif")
        await ctx.send(embed=conf_embed)
    
    @commands.command() #Comando para banear.
    @commands.has_permissions(ban_members=True)
    @commands.has_role("Shōgun")
    async def ban(self, ctx, member: discord.Member, modreason: str):
        await ctx.guild.ban(member)

        conf_embed = discord.Embed(title="A casa platita.", description=f"{member.mention} ha sido evangelizado por {ctx.author.mention}.", color=discord.color.green())
        conf_embed.add_field(name="Motivo:", value=modreason, inline=False)
        await ctx.send(embed=conf_embed)


    @commands.command() #Comando para desbanear.
    @commands.guild_only()
    @commands.has_permissions(ban_members=True)
    @commands.has_role("Shōgun")
    async def unban(self, ctx, userID):
        user = discord.Object(id=userID)
        await ctx.guild.unban(user)
        
        confirmation_embed = discord.Embed(title="Exitoso.", color=discord.color.green())
        confirmation_embed.add_field(name="Desbaneado:", value=f"<@{userID}> ha sido desbaneado del server por {ctx.author.mention}", inline=False)
        await ctx.send(embed=confirmation_embed)


async def setup(client):
    await client.add_cog(Expulse(client))