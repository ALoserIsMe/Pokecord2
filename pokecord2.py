# Custom classes
from pokedex import *
from player  import *

# Discord imports
from discord.ext import commands
import discord
# Both discord and discord.ext are required as far as I'm aware
# Some features don't work without discord, whereas the bot mostly uses discord.ext

# Miscellaneous imports
import asyncio
import random
import time

# Stores the current pokemon, as well as spawning a new one
class pokecord2:
    def __init__(self):
        self.currentPokemon = ""
        self.caught = False

        self.allPokemon = [bulbasaur(), charmander(), squirtle()]
        self.starterPokemon = [bulbasaur(), charmander(), squirtle(), chikorita(), cyndaquil(), totodile(), treecko(), torchic(), mudkip(), turtwig(), chimchar(), piplup(), snivy(), tepig(), oshawott(), chespin(), fennekin(), froakie(), rowlett(), litten(), popplio(), grookey(), scorbunny(), sobble()]

        self.players = {}

    def spawnPokemon(self):
        self.currentPokemon = random.choice(self.allPokemon)
        print("Current Pokemon:", self.currentPokemon.getSpecies())
        self.caught = False

pokecord = pokecord2()
bot = commands.Bot(command_prefix = "p!")

# Spawns a pokemon, then waits between 5 and 30 mins before repeating
async def background_loop():
    mins5  = 300        # Minimum time
    mins30 = 1800       # Maximim time
    await bot.wait_until_ready()
    print("background loop ready")
    while True:
        pokecord.spawnPokemon()
        channel = bot.get_channel(716961981579526308)

        # Sends image of the pokemon
        filename = "images/" + str(pokecord.currentPokemon.getPokedex()) + ".png"
        with open(filename, 'rb') as f:
            picture = discord.File(f)
            await channel.send("**A wild pokemon has appeared!** \nGuess the pokemon and type p!catch <pokemon> to catch it!\n", file= picture)

        # Waits a random amount of time between the minimum time and maximum time
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
        
@bot.command()
async def pick(ctx, arg):
    for x in range(len(pokecord.starterPokemon)):
        if pokecord.starterPokemon.getSpecies().lower() == arg:                                             # I know this is a mess. TODO: Tidy it up
            await ctx.send("Starter pokemon " + pokecord.starterPokemon.getSpecies() + " picked.")
            print(arg.author.id)
            pokecord.update({arg.author.id : player(arg.author.id, pokecord.starterPokemon[x])})
        else:
            await ctx.send("That is not a valid starter pokemon.")

@bot.event
async def on_ready():
    print("Ready")

@bot.event
async def on_guild_join():
    print(Guild.name)

bot.loop.create_task(background_loop())
bot.run("TOKEN", bot=True)
