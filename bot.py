import os

from discord.ext import commands 
from dotenv import load_dotenv

import fate

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

bot = commands.Bot(command_prefix="!")

@bot.command(name="fate")
async def roll_fate(ctx, modifier="0"):
    await ctx.send(fate.command(modifier))

@bot.command(name="f")
async def roll_fate(ctx, modifier="0"):
    await ctx.send(fate.command(modifier))


if __name__ == "__main__":
    bot.run(TOKEN)