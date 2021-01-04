import discord
from discord.ext import commands


class Config(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def config(self, ctx, *args):
        print(args)


def setup(bot):
    bot.add_cog(Config(bot))
