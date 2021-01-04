import discord
from discord.ext import commands
from discord.utils import get


class AutoRole(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Envia uma mensagem para o dono do servidor quando entrar
    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        owner_id = guild.owner_id
        owner = await self.bot.fetch_user(int(owner_id))
        await owner.send(content=f"Obrigado por adicionar o {self.bot.user.name}\nPara Configurar o Bot digite !config")

    # Adiciona o cargo padrao aos novos membros
    @commands.Cog.listener()
    async def on_member_join(self, member):
        if self.bot.database.auto_role_is_enable(member.guild.id) is True:
            role_id = self.bot.database.get_auto_role_id(member.guild.id)
            role = discord.utils.get(member.guild.roles, id=role_id)
            await member.add_roles(role)

    # Comando para habilitar o auto role
    @commands.command(brief='This is the brief description', description='Comando para habilitar ou desabilitar o AutoRole')
    async def autorole(self, ctx, *args):
        if len(args) == 0:
            await ctx.send("Informe True ou False")
            return

        if args[0].lower() == 'true':
            self.bot.database.enable_auto_role(ctx.message.guild.id, True)
            await ctx.send(f'Voce habilitou o AutoRole')
        elif args[0].lower() == 'false':
            self.bot.database.enable_auto_role(ctx.message.guild.id, False)
            await ctx.send(f'Voce desabilitou o AutoRole')
        else:
            await ctx.send("Apenas true ou false")
            return

    # Comando para definir qual e o cargo do auto
    @commands.command(brief='This is the brief description', description='This is the full description')
    async def setautorole(self, ctx, *args):
        if len(args) == 0:
            await ctx.send("Informe um cargo valido")
            return

        role_id = args[0]
        role_id = role_id.replace('<', '')
        role_id = role_id.replace('>', '')
        role_id = role_id.replace('@', '')
        role_id = role_id.replace('&', '')
        role_id = role_id.replace('!', '')

        role_list = list(map((lambda a: a.id),
                             ctx.message.guild.roles))

        if int(role_id) not in role_list:
            await ctx.send("A tag informada nao e um cargo")
            return

        self.bot.database.set_auto_role(ctx.message.guild.id, int(role_id))
        await ctx.send(f'Voce definiu a tag de <@&{role_id}> como padrao')


def setup(bot):
    bot.add_cog(AutoRole(bot))
