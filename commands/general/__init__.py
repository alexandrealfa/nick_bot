from datetime import date as dt
from typing import NoReturn

import discord
from discord.ext import commands as cmd

from config import BAD_WORDS_FILENAME, COMMANDS_FILENAME
from helpers.book_scraping_helper import BookAPI
from helpers.csv_helper import get_all_rows, get_words
from helpers.embed import EmbedHelper
from helpers.nasa_api_helper import NasaAPI


@cmd.command()
async def hi(ctx: discord) -> NoReturn:
    """Diga ola ao nick."""

    if name := ctx.author.mention:
        await ctx.send(f'ola, {name}')

    return


@cmd.command()
async def ping(ctx: discord, message=None) -> NoReturn:
    """Verifica se o bot está ativo."""
    if not message or len(message) == 0:
        await ctx.send('test')

        return

    if content := int(message):
        if content > 10:
            content = 10

        for i in range(content):
            await ctx.send('test')


@cmd.command()
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
        image='https://opengraph.githubassets.com/8014b1adfaa7268a0a95a15d163e795ba03a031d4de95932a900cd979f324977/alexandrealfa/nick_bot'
    )
    ebd.generate_embed()

    await ctx.send(embed=ebd.embed)

    return


@cmd.command()
async def nasa_apod(ctx: discord, message=None) -> NoReturn:
    """Mostra o APOD(Astronomy Picture of the Day) da nasa."""
    if result := NasaAPI().fetchAPOD(date=message):
        author = {
            'name': f"Image Copyright | {result.get('copyright') or 'nasa'}",
            'url': 'https://www.nasa.gov/'
        }
        ebd = EmbedHelper(
            title=result.get('date'),
            color=discord.Color.green(),
            url=result.get('hdurl') or result.get('url'),
            author=author,
            description=result.get('explanation'),
            image=result.get('hdurl') or result.get('url')
        )
        ebd.generate_embed()

        await ctx.send(embed=ebd.embed)


@cmd.command()
async def search_book(ctx: discord, message=None) -> NoReturn:
    """Mostra os 3 resultados para o livro pesquisado."""
    pass


@cmd.command()
async def commands(ctx: discord) -> NoReturn:
    """Mostra todos os Commands do nick bot"""

    if all_commands := get_all_rows(COMMANDS_FILENAME):
        list_of_fields = [{'name': row[0], 'value': row[1], 'inline': False} for row in all_commands]

        ebd = EmbedHelper("Lista de Comandos.", discord.Color.green(), fields=list_of_fields)
        ebd.generate_embed()

        await ctx.send(embed=ebd.embed)

        return

    await ctx.send('A lista de commandos, está vazia.')

    return


@cmd.command()
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


@cmd.command()
async def append_bad_word(ctx: discord, message=None) -> NoReturn:
    """Adiciona a palavra a lista de bloqueio"""
    pass


@cmd.command()
async def show_welcome_message(ctx: discord, message=None) -> NoReturn:
    """Mostra a mensagem de boas-vindas"""
    pass
