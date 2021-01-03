import discord
from discord.ext import commands

class Rank(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def rank(self , ctx , *args):
        if ctx.message.author.bot:
            return

        userid = ctx.message.author.id
        if len(args) > 0:
            target_id = args[0]
            target_id = target_id.replace('<' , '')
            target_id = target_id.replace('>' , '')
            target_id = target_id.replace('@' , '')
            target_id = target_id.replace('&' , '')
            target_id = target_id.replace('!' , '')
            userid = self.bot.get_user(int(target_id))
            if userid.bot:
                return
            userid = userid.id
        
        xp = self.bot.database.get_xp(ctx.message.guild.id , userid)['xp']
        await ctx.send(xp)

    # Increment a xp in user
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return
        if len(message.attachments) > 0:
            self.bot.database.add_xp(message.guild.id 
            , message.author.id 
            , 20)
        else:
            self.bot.database.add_xp(message.guild.id , message.author.id , 10)

def setup(bot):
    bot.add_cog(Rank(bot))