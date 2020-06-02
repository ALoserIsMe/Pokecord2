from discord.ext import commands
from pokedex  import *
import asyncio
import random
import time

class pokecord2:
    def __init__(self):
        self.currentPokemon = ""
        self.allPokemon = [bulbasaur(), charmander(), squirtle()]

    def spawnPokemon(self):
        self.currentPokemon = random.choice(self.allPokemon)
        print("Current Pokemon:", self.currentPokemon.getSpecies())

'''allPokemon = [bulbasaur(), charmander(), squirtle()]
currentPokemon = ""'''

pokecord = pokecord2()
bot = commands.Bot(command_prefix = "p!")

async def background_loop():
    mins5  = 300
    mins30 = 1800
    await bot.wait_until_ready()
    print("background loop ready")
    while True:
        '''currentPokemon = random.choice(allPokemon)
        print("Pokemon:", currentPokemon.getPokedex())'''
        pokecord.spawnPokemon()
        channel = bot.get_channel(716961981579526308)
        await channel.send(pokecord.currentPokemon.getPokedex())

        time = random.randint(mins5, mins30)
        print("Waiting", time, "seconds")
        await asyncio.sleep(time)

@bot.command()
async def catch(ctx, arg):
    if arg.lower() == pokecord.currentPokemon.getSpecies().lower():
        await ctx.send("caught: " + pokecord.currentPokemon.getSpecies())
    else:
        await ctx.send("That is the wrong pokemon.")

@bot.command()
async def echo(ctx, arg):
    await ctx.send(arg)

@bot.event
async def on_ready():
    print("Ready")

bot.loop.create_task(background_loop())
bot.run("TOKEN", bot=True)
