from discord import Intents
from environs import Env

env = Env()
env.read_env()

TOKEN = env("DISCORD_TOKEN")

ETERNAL_ROLES = {"moderadores", "bots", "Admin"}

ALLOWED_ROLES = {"ban": ["admin", "moderadores"]}

intents = Intents.default()
intents.members = True
intents.guilds = True
intents.members = True