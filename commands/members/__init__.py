import discord
from discord.ext import commands

from authorization import check_member
from config import ALLOWED_ROLES, ETERNAL_ROLES


@commands.command()
async def joined(ctx: discord, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f"{member.name} joined in {member.joined_at}")
