import discord
import random
from discord.ext import commands

class Poll(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(brief='This is the brief description' , description='This is the full description')
    async def poll(self , ctx , *args):
        rand_number = random.randrange(int(args[0]), int(args[1]), 1)
        print(rand_number)
        await ctx.send(f'<@{ctx.author.id}> {rand_number}')

def setup(bot):
    bot.add_cog(Poll(bot))