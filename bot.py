import os

from discord.ext import commands 
from dotenv import load_dotenv

import fate

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

bot = commands.Bot(command_prefix="!")

async def do_roll(ctx, modifier):
    who = ctx.author.name
    roll = fate.command(modifier)
    await ctx.send(f"@{who} `{roll}`")

@bot.command(name="fate")
async def roll_fate(ctx, modifier="0"):
    await do_roll(ctx, modifier)

@bot.command(name="f")
async def roll_fate(ctx, modifier="0"):
    await do_roll(ctx, modifier)


if __name__ == "__main__":
    bot.run(TOKEN)