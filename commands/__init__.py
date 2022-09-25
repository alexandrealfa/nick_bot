from discord.ext.commands import Bot

from commands.general import (append_bad_word, hi, ping, repository,
                              show_bad_words, commands, nasa_apod, search_book)
from commands.members import joined


def init(bot: Bot):
    bot.add_command(ping)
    bot.add_command(hi)
    bot.add_command(joined)
    bot.add_command(append_bad_word)
    bot.add_command(repository)
    bot.add_command(show_bad_words)
    bot.add_command(commands)
    bot.add_command(nasa_apod)
    bot.add_command(search_book)

