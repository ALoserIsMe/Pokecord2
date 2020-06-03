from discord.ext import commands
from pokedex  import *
import asyncio
import random
import time

players = []

# Stores the current pokemon, as well as spawning a new one
class pokecord2:
    def __init__(self):
        self.currentPokemon = ""
        self.caught = False

        self.allPokemon = [bulbasaur(), charmander(), squirtle()]

    def spawnPokemon(self):
        self.currentPokemon = random.choice(self.allPokemon)
        print("Current Pokemon:", self.currentPokemon.getSpecies())
        self.caught = False

pokecord = pokecord2()
bot = commands.Bot(command_prefix = "p!")

# Spawns a pokemon, then waits between 5 and 30 mins before repeating
async def background_loop():
    mins5  = 300
    mins30 = 1800
    await bot.wait_until_ready()
    print("background loop ready")
    while True:
        pokecord.spawnPokemon()
        channel = bot.get_channel(716961981579526308)
#        await channel.send("```**A wild pokemon has appeared!** \nGuess the pokemon and type p!catch <pokemon> to catch it!\n" + str(pokecord.currentPokemon.getPokedex()) + "```")
        await channel.send("**A wild pokemon has appeared!** \nGuess the pokemon and type p!catch <pokemon> to catch it!\n" + str(pokecord.currentPokemon.getPokedex()))

        time = random.randint(mins5, mins30)
        print("Waiting", time, "seconds")
        await asyncio.sleep(time)

# If the user's message is the right name for the pokemon, congratulate them. Else, tell them they are wrong.
# If the pokemon has already been caught, tell the user.
@bot.command()
async def catch(ctx, arg):
    if pokecord.caught == False:
        if arg.lower() == pokecord.currentPokemon.getSpecies().lower():
            await ctx.send("caught: " + pokecord.currentPokemon.getSpecies())
            pokecord.caught = True
        else:
            await ctx.send("That is the wrong pokemon.")
    else:
        await ctx.send("The pokemon has already been caught")

@bot.event
async def on_ready():
    print("Ready")

@bot.event
async def on_guild_join():
    print(Guild.name)

bot.loop.create_task(background_loop())
bot.run("NzE3MDY4Mjc3NjY2MjgzNTUx.XtVX_Q.ljn3RE4DCR-yUp6kpaoI6XJU3qQ", bot=True)
