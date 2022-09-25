from discord.ext.commands import Bot

from commands.general import (append_bad_word, commands, hi, nasa_apod, ping,
                              repository, search_book, show_bad_words,
                              show_welcome_message)
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
    bot.add_command(show_welcome_message)

