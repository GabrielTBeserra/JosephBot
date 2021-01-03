import discord
from discord.ext import commands

import random

spam = (
    'Aumente seu pé em 10 cm',
    'Compre R$ 1 por R$ 200',
    'Emagreça 1 tonelada',
    'Repasse essa mensagem ou terá 500 anos de azar'
)

class Spam(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def spam(self , ctx):
        await ctx.send(spam[random.randint(0, len(spam) - 1)])

def setup(bot):
    bot.add_cog(Spam(bot))