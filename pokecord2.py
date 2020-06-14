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
import pickle
import random
import time
import os

class saveClass:
    def __init__(self, players):
        self.players = players
        pass

# Stores the current pokemon, as well as spawning a new one
class pokecord2:
    def __init__(self):
        self.currentPokemon = ""
        self.caught = False

        self.allPokemon = [bulbasaur(), charmander(), squirtle()]
        self.starterPokemon   = [bulbasaur(), charmander(), squirtle(), chikorita(), cyndaquil(), totodile(), treecko(), torchic(), mudkip(), turtwig(), chimchar(), piplup(), snivy(), tepig(), oshawott(), chespin(), fennekin(), froakie(), rowlett(), litten(), popplio(), grookey(), scorbunny(), sobble()]

        # Spawn rarity teirs
        # or tiers
        # however the fuck it's spelled
        # or is it spelt?
        self.commonPokemon    = []
        self.uncommonPokemon  = []
        self.rarePokemon      = [bulbasaur(), charmander(), squirtle(), chikorita(), cyndaquil(), totodile(), treecko(), torchic(), mudkip(), turtwig(), chimchar(), piplup(), snivy(), tepig(), oshawott(), chespin(), fennekin(), froakie(), rowlett(), litten(), popplio(), grookey(), scorbunny(), sobble()]
        # 10% chance to spawn.
        self.legendaryPokemon = [articuno(), zapdos(), moltres(), raiku(), entei(), suicune(), regirock(), regice(), registeel(), latias(), latios(), uxie(), mesprit(), azief(), heatran(), regigigas(), cresselia(), cobalion(), terrakion(), virizion(), tornadus(), thundurus(), landorus(), typeNull(), silvally(), tapuKoko(), tapuLele(), tapuBulu(), tapuFini(), nihilego(), buzzwole(), pheromosa(), xurkitree(), celesteela(), kartana(), guzzlord(), poipole(), neganadel(), stakataka(), blacephalon(), regidrago(), mewtwo(), lugia(), hoOh(), kyogre(), groudon(), rayquaza(), dialga(), palkia(), giratina(), reshiram(), zekrom(), kyurem(), xerneas(), yvetal(), zygarde(), cosmog(), cosmoem(), solgaleo(), lunala(), necrozma(), zacian(), zamazenta(), eternatus()]
        # 7% chance to spawn
        # 63 pokemon. ~1.587% chance each
        # total = 0.11%
        self.mythicalPokemon  = [mew(), celebi(), jirachi(), deoxys(), phione(), manaphy(), darkrai(), shaymin(), arceus(), victini(), keldeo(), meloetta(), genesect(), diancie(), hoopa(), volcanion(), magearna(), marshadow(), zeraora(), meltan(), melmetal()]
        # 3% chance to spawn
        # 21 pokemon. ~4.76% chance each
        # total = 0.14%

        try:
            self.saveFile = open('saveFile', 'rb+')
            self.players = pickle.load(self.saveFile)
            print("Reading save file")
        except FileNotFoundError:
            print("Save file not found, creating new one")
            self.saveFile = open('saveFile', 'wb')
            self.players = {}

    def spawnPokemon(self):
        spawnChance = random.randint(0, 100)
        if spawnChance > 50:
            tier = commonPokemon
        elif spawnChance <= 50 and spawnChance > 80:
            tier = uncommonPokemon
        elif spawnChance <= 80 and spawnChance > 90:
            tier = rarePokemon
        elif spawnChance <= 90 and spawnChance > 98:
            tier = legendaryPokemon
        elif spawnChance <= 98:
            tier = mythicalPokemon

        self.currentPokemon = random.choice(tier)
        print("Current Pokemon:", self.currentPokemon.getSpecies())
        self.caught = False

        '''self.currentPokemon = random.choice(self.allPokemon)
        print("Current Pokemon:", self.currentPokemon.getSpecies())
        self.caught = False'''                                                  # Old version, ICE

    def savePlayers(self):
        pickle.dump(self.players, self.saveFile)
        print("Game saved")
        self.saveFile.close()
        self.saveFile = open('saveFile', 'rb+')

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
        channel = bot.get_channel(716961981579526308)                   # General
        #channel = bot.get_channel(720225257746726973)                          # Workshop

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
            if hash(ctx.author) in pokecord.players:
                pokecord.players[hash(ctx.author)].addPokemon(pokecord.currentPokemon)
                pokecord.savePlayers()
                await ctx.send("caught: " + pokecord.currentPokemon.getSpecies())
                pokecord.caught = True
                #await ctx.send(pokecord.players[hash(ctx.author)].pokemon)
            else:
                await ctx.send("You are not registered! use p!pick <starter> to start playing")
        else:
            await ctx.send("That is the wrong pokemon.")
    else:
        await ctx.send("The pokemon has already been caught")

@bot.command()
async def hint(ctx):
    hint = ""
    for x in range(len(pokecord.currentPokemon.getSpecies())):
        if random.randint(0, 100) < 34:
            hint += "\_"
        else:
            hint += pokecord.currentPokemon.getSpecies()[x]
    await ctx.send(hint)

@bot.command()
async def pick(ctx, arg):
    selected = False
    print(pokecord.players)
    print(hash(ctx.author))
    if hash(ctx.author) not in pokecord.players:
        for x in range(len(pokecord.starterPokemon)):
            if pokecord.starterPokemon[x].getSpecies().lower() == arg.lower():                                             # I know this is a mess. TODO: Tidy it up
                await ctx.send("Starter pokemon " + pokecord.starterPokemon[x].getSpecies() + " picked.")
                print(ctx.author)
                playerObj = player(hash(ctx.author), pokecord.starterPokemon[x])
                newKey = hash(ctx.author)
                print(newKey)
                pokecord.players.update({newKey: playerObj})
                #pokecord.players.append([hash(ctx.author), playerObj])
                selected = True
                pokecord.savePlayers()
        if selected == False:
            await ctx.send("That is not a valid starter pokemon.")
    else:
        await ctx.send("You are already a registered player")

# Lists the player's pokemon.
@bot.command()
async def pokemon(ctx):
    playersPokemon = []

    playersPokemonRaw = pokecord.players[hash(ctx.author)].pokemon
    for x in range(len(playersPokemonRaw)):
        playersPokemon.append(playersPokemonRaw[x].getSpecies())

    playersPokemon = playersPokemon.sort()
    for x in range(playersPokemon):
        toOutput = ("%s - Level %i" % (playersPokemon[x].getSpecies(), playersPokemon[x].getLevel()))
    await ctx.send(toOutput)

@bot.command()
async def list(ctx):
   await ctx.send(pokecord.players)

@bot.event
async def on_ready():
    print("Ready")

bot.loop.create_task(background_loop())
try:
    bot.run("TOKEN" bot=True)
except RuntimeError:
    print("Bot stopped")
# If you're reading this code...
# I'm truly sorry
