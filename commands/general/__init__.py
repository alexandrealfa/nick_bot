import discord
from typing import NoReturn

from discord.ext import commands


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
async def append_bad_word(ctx: discord, message=None) -> NoReturn:
    pass
