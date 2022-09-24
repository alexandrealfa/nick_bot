from typing import NoReturn

import discord
from discord.ext import commands

from config import BAD_WORDS_FILENAME
from helper import get_words


@commands.command()
async def hi(ctx: discord) -> NoReturn:
    if name := ctx.author.name:
        await ctx.send(f'ola, {name}')

    return


@commands.command()
async def ping(ctx: discord, message=None) -> NoReturn:
    if not message or len(message) == 0:
        await ctx.send('test')

        return

    if content := int(message):
        for i in range(content):
            await ctx.send('test')


@commands.command()
async def repository(ctx: discord) -> NoReturn:
    await ctx.send('```NickBot Repository:``` https://github.com/alexandrealfa/nick_bot')

    return


@commands.command()
async def show_bad_words(ctx: discord, message=None) -> NoReturn:

    if bad_words_list := get_words(BAD_WORDS_FILENAME):
        embed = discord.Embed(
            title="Palavras Bloqueadas.",
            color=discord.Color.green()
        )

        [embed.add_field(name=name, value='Bloqueada', inline=False) for name in bad_words_list]

        await ctx.send(embed=embed)

        return

    await ctx.send('A lista de palavras bloqueadas, está vazia.')

    return


@commands.command()
async def append_bad_word(ctx: discord, message=None) -> NoReturn:
    pass
