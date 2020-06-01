# "this is pokecord 2.0 bitch" - UndeadInside (23:04, 31/05/2020, regretting everything already)
import random

# creates an empty pokemon class which each individual pokemon will inherit from
class pokemon:
    def __init__(self):
        self.pokedex       = 0
        self.species       = ""
        self.nature        = ""
        self.type          = []
        self.level         = 0
        self.hp            = 0
        self.attack        = 0
        self.defense       = 0
        self.spAtk         = 0
        self.spDef         = 0
        self.speed         = 0
        self.friend        = 0
        self.gender        = False
        self.abilities     = []
        self.ability       = ""
        self.hiddenAbility = ""
        self.hidAbBool     = False

    def generateNature(self):
        natures = ["Hardy", "Lonely", "Brave", "Adamant", "Naughty", "Bold", "Docile", "Relaxed", "Impish", "Lax", "Timid", "Hasty", "Serious", "Jolly", "Naive", "Modest", "Mild", "Quiet", "Bashful", "Rash", "Calm", "Gentle", "Sassy", "Careful", "Quirky"]
        return random.choice(natures)

    def generateLevel(self, upper, lower):
        return random.randint(upper, lower)
    
    def generateGender(self, maleChance):
        genderChance = random.uniform(1, 100)
        if genderChance <= maleChance:
            return False
        else:
            return True

    # 'get' subroutines
    # these are used to return the classes variables

    def getPokedex(self):
        return self.pokedex

    def getSpecies(self):
        return self.species

    def getNature(self):
        return self.nature

    def getType(self):
        return self.type

    def getLevel(self):
        return self.level

    def getHP(self):
        return self.hp

    def getAttack(self):
        return self.attack

    def getDefense(self):
        return self.defense

    def getSpAtk(self):
        return self.spAtk

    def getSpDef(self):
        return self.spDef

    def getSpeed(self):
        return self.speed

    def getFriend(self):
        return self.friend

    def getGender(self):
        return self.gender

    def getAbilities(self):
        return self.abilities

    def getAbility(self):
        return self.ability

    def getHiddenAbility(self):
        return self.hiddenAbility

    def getHiddenBool(self):
        return self.hidAbBool

    def getIncreasedStat(self):
        if self.nature == "Hardy" or self.nature == "Docile" or self.nature == "Serious" or self.nature == "Bashful" or self.nature == "Quirky":
            return "None"
        elif self.nature == "Lonely" or self.nature == "Brave" or self.nature == "Adamant" or self.nature == "Naughty":
            return "Attack"
        elif self.nature == "Bold" or self.nature == "Relaxed" or self.nature == "Impish" or self.nature == "Lax":
            return "Defense"
        elif self.nature == "Timid" or self.nature == "Hasty" or self.nature == "Jolly" or self.nature == "Naive":
            return "Speed"
        elif self.nature == "Modest" or self.nature == "Mild" or self.nature == "Quiet" or self.nature == "Rash":
            return "Sp. Attack"
        elif self.nature == "Calm" or self.nature == "Gentle" or self.nature == "Sassy" or self.nature == "Careful":
            return "Sp. Defense"

    def getDecreasedStat(self):
        if self.nature == "Hardy" or self.nature == "Docile" or self.nature == "Serious" or self.nature == "Bashful" or self.nature == "Quirky":
            return "None"
        elif self.nature == "Bold" or self.nature == "Timid" or self.nature == "Modest" or self.nature == "Calm":
            return "Attack"
        elif self.nature == "Lonely" or self.nature == "Hasty" or self.nature == "Mild" or self.nature == "Gentle":
            return "Defense"
        elif self.nature == "Brave" or self.nature == "Relaxed" or self.nature == "Quiet" or self.nature == "Sassy":
            return "Speed"
        elif self.nature == "Adamant" or self.nature == "Impish" or self.nature == "Jolly" or self.nature == "Careful":
            return "Sp. Attack"
        elif self.nature == "Naughty" or self.nature == "Lax" or self.nature == "Naive" or self.nature == "Rash":
            return "Sp. Defense"

    def getFavouriteFlavour(self):
        if self.nature == "Hardy" or self.nature == "Docile" or self.nature == "Serious" or self.nature == "Bashful" or self.nature == "Quirky":
            return "None"
        elif self.nature == "Lonely" or self.nature == "Brave" or self.nature == "Adamant" or self.nature == "Naughty":
            return "Spicy"
        elif self.nature == "Bold" or self.nature == "Relaxed" or self.nature == "Impish" or self.nature == "Lax":
            return "Sour"
        elif self.nature == "Timid" or self.nature == "Hasty" or self.nature == "Jolly" or self.nature == "Naive":
            return "Sweet"
        elif self.nature == "Modest" or self.nature == "Mild" or self.nature == "Quiet" or self.nature == "Rash":
            return "Dry"
        elif self.nature == "Calm" or self.nature == "Gentle" or self.nature == "Sassy" or self.nature == "Careful":
            return "Bitter"

    def getDislikedFlavour(self):
        if self.nature == "Hardy" or self.nature == "Docile" or self.nature == "Serious" or self.nature == "Bashful" or self.nature == "Quirky":
            return "None"
        elif self.nature == "Bold" or self.nature == "Timid" or self.nature == "Modest" or self.nature == "Calm":
            return "Spicy"
        elif self.nature == "Lonely" or self.nature == "Hasty" or self.nature == "Mild" or self.nature == "Gentle":
            return "Sour"
        elif self.nature == "Brave" or self.nature == "Relaxed" or self.nature == "Quiet" or self.nature == "Sassy":
            return "Sweet"
        elif self.nature == "Adamant" or self.nature == "Impish" or self.nature == "Jolly" or self.nature == "Careful":
            return "Dry"
        elif self.nature == "Naughty" or self.nature == "Lax" or self.nature == "Naive" or self.nature == "Rash":
            return "Bitter"       

class missingNo(pokemon):                                       # Pokemon name beginning with lower case. Subsequent words are capitalized on the first letter
    def __init__(self): 
        self.pokedex       = 0                                  # Pokedex number
        self.species       = "MissingNo"                        # Pokemon name with first letter capitalized
        self.nature        = self.generateNature()
        self.type          = ["Bird", "Normal"]                 # Pokemon types
        self.level         = self.generateLevel(1, 15)          # Level the pokemon evolveds from, one less than the level the pokemon evolves at
        self.hp            = 45                                 # base hp
        self.attack        = 49                                 # base attack
        self.defense       = 49                                 # base defense
        self.spAtk         = 65                                 # base special attack
        self.spDef         = 65                                 # base special defense
        self.speed         = 45                                 # base speed
        self.friend        = 70                                 # base friend
        self.gender        = self.generateGender(87.5)          # chance for male
        self.abilities     = []                                 # list of abilities
        self.ability       = "Overgrow"                         # selected ability
        self.hiddenAbility = "Chlorophyll"                      # Hidden Ability
        self.hidAbBool     = False                              # Leave as False

class bulbasaur(pokemon):
    def __init__(self):
        self.pokedex       = 1
        self.species       = "Bulbasaur"
        self.nature        = self.generateNature()
        self.type          = ["Grass", "Poison"]
        self.level         = self.generateLevel(1, 15)
        self.hp            = 45
        self.attack        = 49
        self.defense       = 49
        self.spAtk         = 65
        self.spDef         = 65
        self.speed         = 45
        self.friend        = 70
        self.gender        = self.generateGender(87.5)
        self.abilities     = []
        self.ability       = "Overgrow"
        self.hiddenAbility = "Chlorophyll"
        self.hidAbBool     = False

class ivysaur(pokemon):
        self.pokedex       = 2
        self.species       = "Ivysaur"
        self.nature        = self.generateNature()
        self.type          = ["Grass", "Poison"]
        self.level         = self.generateLevel(16, 31)
        self.hp            = 60
        self.attack        = 62
        self.defense       = 63
        self.spAtk         = 80
        self.spDef         = 80
        self.speed         = 60
        self.friend        = 70
        self.gender        = self.generateGender(87.5)
        self.abilities     = []
        self.ability       = "Overgrow"
        self.hiddenAbility = "Chlorophyll"
        self.hidAbBool     = False

class venusaur(pokemon):
        self.pokedex       = 3
        self.species       = "Venusaur"
        self.nature        = self.generateNature()
        self.type          = ["Grass", "Poison"]
        self.level         = self.generateLevel(32, 100)
        self.hp            = 80
        self.attack        = 82
        self.defense       = 83
        self.spAtk         = 100
        self.spDef         = 100
        self.speed         = 80
        self.friend        = 70
        self.gender        = self.generateGender(87.5)
        self.abilities     = []
        self.ability       = "Overgrow"
        self.hiddenAbility = "Chlorophyll"
        self.hidAbBool     = False

class charmander(pokemon):
        self.pokedex       = 4
        self.species       = "Charmander"
        self.nature        = self.generateNature()
        self.type          = ["Fire"]
        self.level         = self.generateLevel(1, 15)
        self.hp            = 39
        self.attack        = 52
        self.defense       = 43
        self.spAtk         = 60
        self.spDef         = 50
        self.speed         = 65
        self.friend        = 70
        self.gender        = self.generateGender(87.5)
        self.abilities     = []
        self.ability       = "Blaze"
        self.hiddenAbility = "Solar Power"
        self.hidAbBool     = False

class charmeleon(pokemon):
        self.pokedex       = 5
        self.species       = "Charmeleon"
        self.nature        = self.generateNature()
        self.type          = ["Fire"]
        self.level         = self.generateLevel(16, 35)
        self.hp            = 58
        self.attack        = 64
        self.defense       = 58
        self.spAtk         = 80
        self.spDef         = 65
        self.speed         = 80
        self.friend        = 70
        self.gender        = self.generateGender(87.5)
        self.abilities     = []
        self.ability       = "Blaze"
        self.hiddenAbility = "Solar Power"
        self.hidAbBool     = False

class charizard(pokemon):
        self.pokedex       = 6
        self.species       = "Charizard"
        self.nature        = self.generateNature()
        self.type          = ["Fire"]
        self.level         = self.generateLevel(36, 100)
        self.hp            = 78
        self.attack        = 84
        self.defense       = 78
        self.spAtk         = 109
        self.spDef         = 85
        self.speed         = 100
        self.friend        = 70
        self.gender        = self.generateGender(87.5)
        self.abilities     = []
        self.ability       = "Blaze"
        self.hiddenAbility = "Solar Power"
        self.hidAbBool     = False

class rhydon(pokemon):
    def __init__(self):
        self.pokedex       = 112
        self.species       = "Rhydon"
        self.nature        = self.generateNature()
        self.type          = ["Ground", "Rock"]
        self.level         = self.generateLevel(42, 100)
        self.hp            = 105
        self.attack        = 130
        self.defense       = 120
        self.spAtk         = 45
        self.spDef         = 45
        self.speed         = 40
        self.friend        = 70
        self.gender        = self.generateGender(50)
        self.abilities     = ["Lightning Rod", "Rock Head"]
        self.ability       = ""
        self.hiddenAbility = "Reckless"
        self.hidAbBool     = False

pokemon = rhydon()
print(pokemon.getPokedex())
print(pokemon.getSpecies())
print(pokemon.getNature())
print(pokemon.getType())
print(pokemon.getLevel())
print(pokemon.getHP())
print(pokemon.getAttack())
print(pokemon.getDefense())
print(pokemon.getSpAtk())
print(pokemon.getSpDef())
print(pokemon.getSpeed())
print(pokemon.getFriend())
print(pokemon.getGender())
print(pokemon.getAbilities())
print(pokemon.getAbility())
print(pokemon.getHiddenAbility())
print(pokemon.getHiddenBool())

# note: spelling it flavour for now because in Sassi's words: "fuck america"

# TODO:
#  Synchronize
#  Mega 'mon
