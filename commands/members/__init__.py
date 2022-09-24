import discord
from discord.ext import commands

from authorization import check_member
from config import ALLOWED_ROLES, ETERNAL_ROLES


@commands.command()
async def joined(ctx: discord, member: discord.Member = None):
    """Says when a member joined."""
    if member:
        await ctx.send(f"{member.name} joined in {member.joined_at.strftime('%d/%m/%y')}")

        return

    await ctx.send(f"{ctx.author.name} joined in {ctx.author.joined_at.strftime('%d/%m/%y')}")
