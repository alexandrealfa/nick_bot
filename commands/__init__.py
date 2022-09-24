from discord.ext.commands import Bot
from commands.general import ping, hi, append_bad_word
from commands.members import joined


def init(bot: Bot):
    bot.add_command(ping)
    bot.add_command(hi)
    bot.add_command(joined)
    bot.add_command(append_bad_word)
