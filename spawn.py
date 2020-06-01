from discord.ext import commands
from pokedex  import *
import random
import time

bot = commands.Bot(command_prefix = "p!")

async def catch(ctx, arg):
    await ctx.send(arg)

try:
    bot.run("NzE3MDY4Mjc3NjY2MjgzNTUx.XtVSdQ.KEmIjUy_54QPxm_dFHy97g6h1xE")
except KeyboardInterrupt:
    print("Bot Stopped Due to keyboard Interrupt.")
