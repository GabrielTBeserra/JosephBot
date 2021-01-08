from asyncio.windows_events import NULL
import re
import discord
from discord.ext import commands
from discord.utils import get


class SelfRole(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(brief='This is the brief description', description='Comando para habilitar ou desabilitar o AutoRole')
    async def selfrole(self, ctx, *args):
        if(len(args) == 0):
            return

        message_id = args[0]
        self.bot.database.set_selfrole_messageid(
            ctx.message.guild.id, int(message_id))
        await ctx.send(f'Voce definiu a mensagem com id {message_id} para self role')

    @commands.command(brief='This is the brief description', description='Comando para habilitar ou desabilitar o AutoRole')
    async def disableselfrole(self, ctx, *args):
        self.bot.database.disable_selfrole(
            ctx.message.guild.id)
        await ctx.send(f'Voce desativou o self role')

    @commands.command(brief='This is the brief description', description='Comando para habilitar ou desabilitar o AutoRole')
    async def setrole(self, ctx, *args):
        message_id = self.bot.database.get_selfrole_messageid(
            ctx.message.guild.id)

        if(message_id is NULL or message_id is None):
            await ctx.send("Voce nao possui uma mensagem configurada para self role")
            return

        if len(args) < 2:
            await ctx.send('Informe .setrole <cargo> <emoji>')
            return

        selfrole_message = await ctx.fetch_message(message_id)

        role_id = self.bot.filterid(args[0])

        self.bot.database.save_emoji_role(
            ctx.message.guild.id, args[1], role_id)
        await selfrole_message.add_reaction(args[1])
        await ctx.send(f'Voce associou o emoji {args[1]} ao cargo de {args[0]}')

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        message_id = self.bot.database.get_selfrole_messageid(
            payload.guild_id)

        if(message_id is NULL or message_id is None):
            return

        if int(message_id) == int(payload.message_id):
            role_id = self.bot.database.get_role_from_emoji(
                payload.guild_id, payload.emoji.name)

            guild = await self.bot.fetch_guild(int(payload.guild_id))
            role = discord.utils.get(guild.roles, id=role_id)
            await payload.member.add_roles(role)

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        message_id = self.bot.database.get_selfrole_messageid(
            payload.guild_id)

        if(message_id is NULL or message_id is None):
            return

        if int(message_id) == int(payload.message_id):
            role_id = self.bot.database.get_role_from_emoji(
                payload.guild_id, payload.emoji.name)

            guild = await self.bot.fetch_guild(int(payload.guild_id))
            member = await guild.fetch_member(int(payload.user_id))
            role = discord.utils.get(guild.roles, id=role_id)
            await member.remove_roles(role)


def setup(bot):
    bot.add_cog(SelfRole(bot))
