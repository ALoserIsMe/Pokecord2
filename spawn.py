from discord.py import commands
from pokedex  import *
import random

bot = commands.Bot(commapnd_prefix = "p!")

class pokecord2:
    def __init__(self):
        pass

    def spawnPokemon(self):
        pokemons = [bulbasaur(), charmander(), squirtle()] 
        spawn = random.choice(pokemons)

        print(spawn.getPokedex())
        playerGuess = input("> ")
        if playerGuess.lower() == spawn.getSpecies().lower():
            print("Caught " + spawn.getSpecies())
        else:
            print("Wrong pokemon")


