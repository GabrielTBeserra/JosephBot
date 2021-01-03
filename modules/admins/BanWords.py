import discord
from discord.ext import commands

class BanWords(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def banword(self , ctx , *args):
        print(args)
        


def setup(bot):
    bot.add_cog(BanWords(bot))