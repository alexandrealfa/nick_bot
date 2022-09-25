from discord import Intents
from environs import Env

env = Env()
env.read_env()

TOKEN = env("DISCORD_TOKEN")
NASA_API_KEY = env("NASA_API_KEY")

ETERNAL_ROLES = {"moderadores", "bots", "Admin"}

ENABLE_CHANNELS = {
    "all_words": ['oi', 'ajuda'],
    'oi': {
        'content': 'oi',
        'ids': ["837111938965438514"],
        'message': 'Ola, em que podemos lhe ajudar ?'
    },
    'ajuda': {
        'ids': 'all',
        'message': '```Ola, digite --commands ou --help para saber em que podemos lhe ajudar!.```'
    }
}

ALLOWED_ROLES = {"ban": ["admin", "moderadores"]}

BAD_WORDS_FILENAME = 'data/bad_words.csv'
COMMANDS_FILENAME = 'data/commands.csv'

intents = Intents.default()
intents.members = True
intents.guilds = True
intents.members = True