import discord
from discord.ext import commands
from config import ETERNAL_ROLES, ALLOWED_ROLES
from authorization import check_member


@commands.command()
async def joined(ctx: discord, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f"{member.name} joined in {member.joined_at}")
