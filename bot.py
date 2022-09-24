import discord
import commands as ds_comands
import events

from discord.ext import commands

from config import TOKEN

bot = commands.Bot(command_prefix='--', intents=discord.Intents.all())
ds_comands.init(bot)
events.init(bot)

bot.run(TOKEN)
