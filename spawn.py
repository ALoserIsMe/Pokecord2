from discord.ext import commands
from pokedex  import *
import random
import time

bot = commands.Bot(command_prefix = "p!")

async def catch(ctx, arg):
    await ctx.send(arg)

try:
    bot.run("Put Token Here")
except KeyboardInterrupt:
    print("Bot Stopped Due to keyboard Interrupt.")
