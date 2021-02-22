# Python 3.6+ only
import discord
import os

from pathlib import Path
from core import database
from os import listdir
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv(verbose=True)

default_prefixes = '.'
custom_prefixes = {}
players = {}
queue = []

intents = discord.Intents.default()
intents.members = True
intents.reactions = True
intents.messages = True

# Funcao para acessar os comandos de acordo com o prefix do servidor que esta solicitando


def filter_id(id):
    role_id = id
    role_id = role_id.replace('<', '')
    role_id = role_id.replace('>', '')
    role_id = role_id.replace('@', '')
    role_id = role_id.replace('&', '')
    role_id = role_id.replace('!', '')
    return role_id


game = discord.Game("twitch.tv/1Urso")


async def determine_prefix(bot, message):
    return bot.database.read_out(message.guild.id)['prefix']

# Definicao das variavis
bot = commands.Bot(command_prefix=determine_prefix,
                   case_insensitive=True, intents=intents)
bot.change_presence(status=discord.Status.online, activity=game)

bot.database = database.Database()
bot.players = players
bot.queue = queue
bot.teste = {}
bot.filterid = filter_id


@bot.event
async def on_ready():
    print('Bot logado usando a tag: {0.user}'.format(bot))

# Responsavel por carregar os modulos de acordo com as pastas
if __name__ == "__main__":
    for fou in listdir('./modules/'):
        for cmd in listdir(f'./modules/{fou}'):
            if cmd.endswith('.py'):
                #print(f"Carregando o comando {cmd.split('.')[0]}")
                try:
                    bot.load_extension(f'modules.{fou}.{cmd.split(".")[0]}')
                    print(f"Modulo {cmd.split('.')[0]} carregado! ✅")
                except Exception as exce:
                    print(
                        f"\nFalha no carregamento do modulo {type(exce).__name__}!\n{exce} ❌")


bot.run(os.getenv("TOKEN"))
