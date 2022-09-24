from typing import NoReturn

import discord
from discord.ext import commands

from config import BAD_WORDS_FILENAME, COMMANDS_FILENAME
from helpers.csv_helper import get_words, get_all_rows
from helpers.embed import EmbedHelper


@commands.command()
async def hi(ctx: discord) -> NoReturn:
    """Diga ola ao nick."""

    if name := ctx.author.name:
        await ctx.send(f'ola, {name}')

    return


@commands.command()
async def ping(ctx: discord, message=None) -> NoReturn:
    """Verifica se o bot está ativo."""
    if not message or len(message) == 0:
        await ctx.send('test')

        return

    if content := int(message):
        for i in range(content):
            await ctx.send('test')


@commands.command()
async def repository(ctx: discord) -> NoReturn:
    """Mostra o repositorio do nickbot no Github."""
    author = {
        'name': 'Alexandre Alfa',
        'icon_url': 'https://avatars.githubusercontent.com/u/46616348?v=4',
        'url': 'https://github.com/alexandrealfa'
    }

    ebd = EmbedHelper(
        "Repositorio do Nickbot.",
        discord.Color.green(),
        url='https://github.com/alexandrealfa/nick_bot',
        author=author,
        thumb='https://opengraph.githubassets.com/8014b1adfaa7268a0a95a15d163e795ba03a031d4de95932a900cd979f324977/alexandrealfa/nick_bot'
    )
    ebd.generate_embed()

    await ctx.send(embed=ebd.embed)

    return


@commands.command()
async def help_commands(ctx: discord) -> NoReturn:
    """Mostra todos os Commands do nick bot"""

    if all_commands := get_all_rows(COMMANDS_FILENAME):
        list_of_fields = [{'name': row[0], 'value': row[1], 'inline': False} for row in all_commands]

        ebd = EmbedHelper("Lista de Comandos.", discord.Color.green(), fields=list_of_fields)
        ebd.generate_embed()

        await ctx.send(embed=ebd.embed)

        return

    await ctx.send('A lista de commandos, está vazia.')

    return


@commands.command()
async def show_bad_words(ctx: discord) -> NoReturn:
    """Mostra a lista de palavras bloqueadas."""

    if bad_words_list := get_words(BAD_WORDS_FILENAME):
        list_of_fields = [{'name': name, 'value': 'Bloqueado', 'inline': False} for name in bad_words_list]

        ebd = EmbedHelper("Palavras Bloqueadas.", discord.Color.green(), fields=list_of_fields)
        ebd.generate_embed()

        await ctx.send(embed=ebd.embed)

        return

    await ctx.send('A lista de palavras bloqueadas, está vazia.')

    return


@commands.command()
async def append_bad_word(ctx: discord, message=None) -> NoReturn:
    """Adiciona a palavra a lista de bloqueio"""
    pass
