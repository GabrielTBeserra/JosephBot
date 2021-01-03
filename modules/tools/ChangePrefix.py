import discord
from discord.ext import commands


class ChangePrefix(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['cp'] , description='This is the full description')
    async def ChangePrefix(self, ctx , *args):
        if ctx.message.author.guild_permissions.administrator:
            self.bot.database.change_prefix(ctx.message.guild.id , args[0])
            await ctx.send(f'You new prefix is `{args[0]}``')


def setup(bot):
    bot.add_cog(ChangePrefix(bot))
