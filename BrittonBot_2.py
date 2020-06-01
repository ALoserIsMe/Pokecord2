
#created 26/02/2020

from discord.ext import commands
import random

bot = commands.Bot(command_prefix = "$")

@bot.command(name        = "8ball",
	     aliases     = ["eight_ball", "eightball", "8-ball"],
	     brief       = "Answers from the beyond",
	     description = "Answers a yes/no question"
)
async def eight_ball(ctx):
    possible_responses = [
	"Tat is a wesounding no",
	"Not wooking wikewy",
	"Too hard to tell",
	"Quite possibwe",
	"Definitewy"
    ]
    await ctx.send(random.choice(possible_responses) + ", " + ctx.message.author.mention)

@bot.event
async def on_ready():
    print("Ready")

try:
    bot.run("NDk0ODk4NDI3MDY3MzY3NDI2.XUmVNg.eyoOt-_sqWK3AgHlAMCwI4pBri8", bot=True)
except KeyboardInterrupt:
    print("Bot stopped due to Keyboard Interupt")

