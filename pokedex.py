# "this is pokecord 2.0 bitch" - UndeadInside (23:04, 31/05/2020, regretting everything already)
import random

# creates an empty pokemon class which each individual pokemon will inherit from
class pokemon:
    def __init__(self):
        self.pokedex       = 0
        self.species       = ""
        self.nature        = ""
        self.nickname      = ""
        self.type          = []
        self.maxLevel      = 0
        self.level         = 0
        self.hp            = 0
        self.attack        = 0
        self.defense       = 0
        self.spAtk         = 0
        self.spDef         = 0
        self.speed         = 0
        self.friend        = 0
        self.experience    = 0
        self.gender        = False
        self.abilities     = []
        self.ability       = ""
        self.hiddenAbility = ""
        self.hidAbBool     = False

    def generateNature(self):
        natures = ["Hardy", "Lonely", "Brave", "Adamant", "Naughty", "Bold", "Docile", "Relaxed", "Impish", "Lax", "Timid", "Hasty", "Serious", "Jolly", "Naive", "Modest", "Mild", "Quiet", "Bashful", "Rash", "Calm", "Gentle", "Sassy", "Careful", "Quirky"]
        return random.choice(natures)

    def setNickname(self, toSet):
        self.nickname = toSet

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

    def getNickname(self):
        return self.nickname

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

    def describe(self):
        message = """"""
        message += "**Level %i %s**\n" % (self.getLevel(), self.getSpecies())
        message += "**Nature: **"      + self.getNature()       + "\n"
        message += "**HP: **"          + str(self.getHP())      + "\n"
        message += "**Attack: **"      + str(self.getAttack())  + "\n"
        message += "**Defense: **"     + str(self.getDefense()) + "\n"
        message += "**Sp. Atk: **"     + str(self.getSpAtk())   + "\n"
        message += "**Dp. Def: **"     + str(self.getSpDef())   + "\n"
        message += "**Speed: **"       + str(self.getSpeed())   + "\n"
        return message

class missingNo(pokemon):                                            # Pokemon name beginning with lower case. Subsequent words are capitalized on the first letter
    def __init__(self): 
        self.pokedex       = 0.0                                     # Pokedex number
        self.species       = "MissingNo"                             # Pokemon name with first letter capitalized
        self.nature        = self.generateNature()
        self.type          = ["Bird", "Normal"]                      # Pokemon types
        #self.maxLevel      = 16                                      # The level which this pokemon evolves
        #self.level         = self.generateLevel(1, self.maxLevel-1)  # Level the pokemon evolveds from, one less than the level the pokemon evolves at
        self.hp            = 45                                      # base hp
        self.attack        = 49                                      # base attack
        self.defense       = 49                                      # base defense
        self.spAtk         = 65                                      # base special attack
        self.spDef         = 65                                      # base special defense
        self.speed         = 45                                      # base speed
        self.friend        = 70                                      # base friend
        self.gender        = self.generateGender(87.5)               # chance for male
        self.abilities     = []                                      # list of abilities
        self.ability       = "Overgrow"                              # selected ability
        self.hiddenAbility = "Chlorophyll"                           # Hidden Ability
        self.hidAbBool     = False                                   # Leave as False

class bulbasaur(pokemon):
    def __init__(self):
        self.pokedex       = 1.0
        self.species       = "Bulbasaur"
        self.nature        = self.generateNature()
        self.type          = ["Grass", "Poison"]
        #self.maxLevel      = 16
        #self.level         = self.generateLevel(1, self.maxLevel - 1)
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
    def __init__(self):
        self.pokedex       = 2.0
        self.species       = "Ivysaur"
        self.nature        = self.generateNature()
        self.type          = ["Grass", "Poison"]
        #self.maxLevel      = 32
        #self.level         = self.generateLevel(16, self.maxLevel - 1)
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
    def __init__(self):
        self.pokedex       = 3.0
        self.species       = "Venusaur"
        self.nature        = self.generateNature()
        self.type          = ["Grass", "Poison"]
        #self.maxLevel      = 100
        #self.level         = self.generateLevel(32, self.maxLevel)
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
    def __init__(self):
        self.pokedex       = 4.0
        self.species       = "Charmander"
        self.nature        = self.generateNature()
        self.type          = ["Fire"]
        #self.maxLevel      = 16
        #self.level         = self.generateLevel(1, self.maxLevel - 1)
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
    def __init__(self):
        self.pokedex       = 5.0
        self.species       = "Charmeleon"
        self.nature        = self.generateNature()
        self.type          = ["Fire"]
        #self.maxLevel      = 36
        #self.level         = self.generateLevel(16, self.maxLevel -1)
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
    def __init__(self):
        self.pokedex       = 6.0
        self.species       = "Charizard"
        self.nature        = self.generateNature()
        self.type          = ["Fire"]
        #self.maxLevel      = 100
        #self.level         = self.generateLevel(36, self.maxLevel)
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

class squirtle(pokemon):
    def __init__(self):
        self.pokedex       = 7.0
        self.species       = "Squirtle"
        self.nature        = self.generateNature()
        self.type          = ["Water"]
        #self.maxLevel      = 16
        #self.level         = self.generateLevel(1, self.maxLevel - 1)
        self.hp            = 44
        self.attack        = 48
        self.defense       = 65
        self.spAtk         = 50
        self.spDef         = 64
        self.speed         = 43
        self.friend        = 70
        self.gender        = self.generateGender(87.5)
        self.abilities     = []
        self.ability       = "Torrent"
        self.hiddenAbility = "Rain Dish"
        self.hidAbBool     = False

class wartortle(pokemon):
    def __init__(self):
        self.pokedex       = 8.0
        self.species       = "Wartortle"
        self.nature        = self.generateNature()
        self.type          = ["Water"]
        #self.maxLevel      = 36
        #self.level         = self.generateLevel(16, self.maxLevel - 1)
        self.hp            = 59
        self.attack        = 63
        self.defense       = 80
        self.spAtk         = 65
        self.spDef         = 80
        self.speed         = 58
        self.friend        = 70
        self.gender        = self.generateGender(87.5)
        self.abilities     = []
        self.ability       = "Torrent"
        self.hiddenAbility = "Rain Dish"
        self.hidAbBool     = False

class blastoise(pokemon):
    def __init__(self):
        self.pokedex       = 9.0
        self.species       = "Blastoise"
        self.nature        = self.generateNature()
        self.type          = ["Water"]
        #self.maxLevel      = 100
        #self.level         = self.generateLevel(36, self.maxLevel)
        self.hp            = 79
        self.attack        = 83
        self.defense       = 100
        self.spAtk         = 85
        self.spDef         = 105
        self.speed         = 78
        self.friend        = 70
        self.gender        = self.generateGender(87.5)
        self.abilities     = []
        self.ability       = "Torrent"
        self.hiddenAbility = "Rain Dish"
        self.hidAbBool     = False
        
class caterpie(pokemon):                                      
    def __init__(self): 
        self.pokedex       = 10.0                                   
        self.species       = "Caterpie"                        
        self.nature        = self.generateNature()
        self.type          = ["Bug"]                
        #self.level         = self.generateLevel(1, 6)           
        self.hp            = 45                                 
        self.attack        = 30                                 
        self.defense       = 35                                 
        self.spAtk         = 20                                 
        self.spDef         = 20                               
        self.speed         = 45                                 
        self.friend        = 70                                 
        self.gender        = self.generateGender(50)          
        self.abilities     = []                                 
        self.ability       = "Shield Dust"                         
        self.hiddenAbility = "Run Away"                      
        self.hidAbBool     = False   
        
class metapod(pokemon):                                      
    def __init__(self): 
        self.pokedex       = 11.0                                    
        self.species       = "Metapod"                        
        self.nature        = self.generateNature()
        self.type          = ["Bug"]                
        #self.level         = self.generateLevel(7, 9)           
        self.hp            = 50                                
        self.attack        = 20                               
        self.defense       = 55                                
        self.spAtk         = 25                              
        self.spDef         = 25                       
        self.speed         = 30                              
        self.friend        = 70                                 
        self.gender        = self.generateGender(50)          
        self.abilities     = []                                 
        self.ability       = "Shed Skin"                         
        self.hiddenAbility = ""                      
        self.hidAbBool     = False
        
class butterfree(pokemon):                                      
    def __init__(self): 
        self.pokedex       = 12.0                                 
        self.species       = "Butterfree"                        
        self.nature        = self.generateNature()
        self.type          = ["Bug", "Flying"]                
        #self.level         = self.generateLevel(10, 100)           
        self.hp            = 60                                
        self.attack        = 45                                
        self.defense       = 50                                
        self.spAtk         = 90                                
        self.spDef         = 80                               
        self.speed         = 70                                
        self.friend        = 70                                 
        self.gender        = self.generateGender(50)          
        self.abilities     = []                                 
        self.ability       = "Compound Eyes"                         
        self.hiddenAbility = "Tinted Lens"                      
        self.hidAbBool     = False   
        
class weedle(pokemon):                                      
    def __init__(self): 
        self.pokedex       = 13.0                                    
        self.species       = "Weedle"                        
        self.nature        = self.generateNature()
        self.type          = ["Bug", "Poison"]                
        #self.level         = self.generateLevel(1, 6)           
        self.hp            = 40                                
        self.attack        = 35                               
        self.defense       = 30                                
        self.spAtk         = 20                                 
        self.spDef         = 20                               
        self.speed         = 50                                
        self.friend        = 70                                 
        self.gender        = self.generateGender(50)          
        self.abilities     = []                                 
        self.ability       = "Shield Dust"                         
        self.hiddenAbility = "Run Away"                      
        self.hidAbBool     = False   
        
class kakuna(pokemon):                                      
    def __init__(self): 
        self.pokedex       = 14.0                                  
        self.species       = "Kakuna"                        
        self.nature        = self.generateNature()
        self.type          = ["Bug", "Poison"]                
        #self.level         = self.generateLevel(7, 9)           
        self.hp            = 45                                 
        self.attack        = 25                                
        self.defense       = 50                                
        self.spAtk         = 25                                
        self.spDef         = 25                               
        self.speed         = 35                                 
        self.friend        = 70                                 
        self.gender        = self.generateGender(50)          
        self.abilities     = []                                 
        self.ability       = "Shed Skin"                         
        self.hiddenAbility = ""                      
        self.hidAbBool     = False
        
class beedrill(pokemon):                                      
    def __init__(self): 
        self.pokedex       = 15.0                                 
        self.species       = "Beedrill"                        
        self.nature        = self.generateNature()
        self.type          = ["Bug", "Poison"]                
        #self.level         = self.generateLevel(10, 100)           
        self.hp            = 65                                 
        self.attack        = 90                                
        self.defense       = 40                                 
        self.spAtk         = 45                                
        self.spDef         = 80                              
        self.speed         = 75                                 
        self.friend        = 70                                 
        self.gender        = self.generateGender(50)          
        self.abilities     = []                                 
        self.ability       = "Swarm"                         
        self.hiddenAbility = "Sniper"                      
        self.hidAbBool     = False   
        
class pidgey(pokemon):                                      
    def __init__(self): 
        self.pokedex       = 16.0                                 
        self.species       = "Pidgey"                        
        self.nature        = self.generateNature()
        self.type          = ["Normal", "Flying"]                
        #self.level         = self.generateLevel(1, 17)           
        self.hp            = 40                                 
        self.attack        = 45                               
        self.defense       = 40                                 
        self.spAtk         = 35                               
        self.spDef         = 35                              
        self.speed         = 56                                
        self.friend        = 70                                 
        self.gender        = self.generateGender(50)          
        self.abilities     = ["Keen Eye", "Tangled Feet"]                                 
        self.ability       = ""                         
        self.hiddenAbility = "Big Pecks"                      
        self.hidAbBool     = False   
        
class pidgeotto(pokemon):                                      
    def __init__(self): 
        self.pokedex       = 17.0                                 
        self.species       = "Pidgeotto"                        
        self.nature        = self.generateNature()
        self.type          = ["Normal", "Flying"]                
      #  self.level         = self.generateLevel(18, 35)           
        self.hp            = 63                                 
        self.attack        = 60                               
        self.defense       = 55                                 
        self.spAtk         = 50                               
        self.spDef         = 50                             
        self.speed         = 71                                
        self.friend        = 70                                 
        self.gender        = self.generateGender(50)          
        self.abilities     = ["Keen Eye", "Tangled Feet"]                                 
        self.ability       = ""                         
        self.hiddenAbility = "Big Pecks"                      
        self.hidAbBool     = False   

class pidgeot(pokemon):                                      
    def __init__(self): 
        self.pokedex       = 18.0                                 
        self.species       = "Pidgeot"                        
        self.nature        = self.generateNature()
        self.type          = ["Normal", "Flying"]                
     #   self.level         = self.generateLevel(36, 100)           
        self.hp            = 83                                 
        self.attack        = 80                                
        self.defense       = 75                                
        self.spAtk         = 70                               
        self.spDef         = 70                             
        self.speed         = 101                                 
        self.friend        = 70                                 
        self.gender        = self.generateGender(50)          
        self.abilities     = ["Keen Eye", "Tangled Feet"]                                 
        self.ability       = ""                         
        self.hiddenAbility = "Big Pecks"                      
        self.hidAbBool     = False   

class rattata(pokemon):                                      
    def __init__(self): 
        self.pokedex       = 19.0                                
        self.species       = "Rattata"                        
        self.nature        = self.generateNature()
        self.type          = ["Normal"]                
     #   self.level         = self.generateLevel(1, 19)           
        self.hp            = 30                                 
        self.attack        = 56                              
        self.defense       = 35                                 
        self.spAtk         = 25                               
        self.spDef         = 35                              
        self.speed         = 72                                
        self.friend        = 70                                 
        self.gender        = self.generateGender(50)          
        self.abilities     = ["Run Away", "Guts"]                                 
        self.ability       = ""                         
        self.hiddenAbility = "Hustle"                      
        self.hidAbBool     = False   
        
class alolanRattata(pokemon):                                      
    def __init__(self): 
        self.pokedex       = 19.5                                
        self.species       = "Alolan Rattata"                        
        self.nature        = self.generateNature()
        self.type          = ["Dark", "Normal"]                
      #  self.level         = self.generateLevel(1, 19)           
        self.hp            = 30                                 
        self.attack        = 56                              
        self.defense       = 35                                 
        self.spAtk         = 25                               
        self.spDef         = 35                              
        self.speed         = 72                                
        self.friend        = 70                                 
        self.gender        = self.generateGender(50)          
        self.abilities     = ["Gluttony", "Hustle"]                                 
        self.ability       = ""                         
        self.hiddenAbility = "Thick Fat"                      
        self.hidAbBool     = False 
        
class raticate(pokemon):                                      
    def __init__(self): 
        self.pokedex       = 20.0                                
        self.species       = "Raticate"                        
        self.nature        = self.generateNature()
        self.type          = ["Normal"]                
      #  self.level         = self.generateLevel(20, 100)           
        self.hp            = 55                              
        self.attack        = 81                             
        self.defense       = 60                                 
        self.spAtk         = 50                              
        self.spDef         = 70                             
        self.speed         = 97                                
        self.friend        = 70                                 
        self.gender        = self.generateGender(50)          
        self.abilities     = ["Run Away", "Guts"]                                 
        self.ability       = ""                         
        self.hiddenAbility = "Hustle"                      
        self.hidAbBool     = False 

class alolanRaticate(pokemon):                                      
    def __init__(self): 
        self.pokedex       = 20.5                              
        self.species       = "Alolan Raticate"                        
        self.nature        = self.generateNature()
        self.type          = ["Dark", "Normal"]                
       # self.level         = self.generateLevel(20, 100)           
        self.hp            = 75                                
        self.attack        = 71                              
        self.defense       = 70                                
        self.spAtk         = 40                               
        self.spDef         = 80                              
        self.speed         = 77                               
        self.friend        = 70                                 
        self.gender        = self.generateGender(50)          
        self.abilities     = ["Gluttony", "Hustle"]                                 
        self.ability       = ""                         
        self.hiddenAbility = "Thick Fat"                      
        self.hidAbBool     = False 
        
class spearow(pokemon):                                      
    def __init__(self): 
        self.pokedex       = 21.0                               
        self.species       = "Spearow"                        
        self.nature        = self.generateNature()
        self.type          = ["Normal", "Flying"]                
       # self.level         = self.generateLevel(1, 19)           
        self.hp            = 40                                 
        self.attack        = 60                              
        self.defense       = 30                                 
        self.spAtk         = 31                               
        self.spDef         = 31                              
        self.speed         = 70                                
        self.friend        = 70                                 
        self.gender        = self.generateGender(50)          
        self.abilities     = []                                 
        self.ability       = "Keen Eye"                         
        self.hiddenAbility = "Sniper"                      
        self.hidAbBool     = False 
        
class fearow(pokemon):                                      
    def __init__(self): 
        self.pokedex       = 22.0                               
        self.species       = "Fearow"                        
        self.nature        = self.generateNature()
        self.type          = ["Normal", "Flying"]                
       # self.level         = self.generateLevel(20, 100)           
        self.hp            = 65                                 
        self.attack        = 90                              
        self.defense       = 65                                 
        self.spAtk         = 61                               
        self.spDef         = 61                             
        self.speed         = 100                                
        self.friend        = 70                                 
        self.gender        = self.generateGender(50)          
        self.abilities     = []                                 
        self.ability       = "Keen Eye"                         
        self.hiddenAbility = "Sniper"                      
        self.hidAbBool     = False 
        
class ekans(pokemon):                                      
    def __init__(self): 
        self.pokedex       = 23.0                                 
        self.species       = "Ekans"                        
        self.nature        = self.generateNature()
        self.type          = ["Poison"]                
     #   self.level         = self.generateLevel(1, 21)           
        self.hp            = 35                                 
        self.attack        = 60                                
        self.defense       = 44                                 
        self.spAtk         = 40                                
        self.spDef         = 54                              
        self.speed         = 55                                 
        self.friend        = 70                                 
        self.gender        = self.generateGender(50)          
        self.abilities     = ["Intimidate", "Shed Skin"]                                 
        self.ability       = ""                         
        self.hiddenAbility = "Unnerve"                      
        self.hidAbBool     = False  

        

class arbok(pokemon):                                      
    def __init__(self): 
        self.pokedex       = 24.0                                 
        self.species       = "Arbok"                        
        self.nature        = self.generateNature()
        self.type          = ["Poison"]                
        #self.level         = self.generateLevel(1, 21)           
        self.hp            = 60                                 
        self.attack        = 95                                
        self.defense       = 69                                 
        self.spAtk         = 65                                
        self.spDef         = 79                              
        self.speed         = 80                                 
        self.friend        = 70                                 
        self.gender        = self.generateGender(50)          
        self.abilities     = ["Intimidate", "Shed Skin"]                                 
        self.ability       = ""                         
        self.hiddenAbility = "Unnerve"                      
        self.hidAbBool     = False  

        

class pikachu(pokemon):                                      
    def __init__(self): 
        self.pokedex       = 25.0                                 
        self.species       = "Pikachu"                        
        self.nature        = self.generateNature()
        self.type          = ["Electric"]                
        #self.level         = self.generateLevel(1, 100)           
        self.hp            = 35                                 
        self.attack        = 55                                
        self.defense       = 40                                 
        self.spAtk         = 50                                
        self.spDef         = 50                              
        self.speed         = 90                                 
        self.friend        = 70                                 
        self.gender        = self.generateGender(50)          
        self.abilities     = []                                 
        self.ability       = "Static"                         
        self.hiddenAbility = "Lightning Rod"                      
        self.hidAbBool     = False  
       
class pikachu(pokemon):                                      
    def __init__(self): 
        self.pokedex       = 25.0                                 
        self.species       = "Pikachu"                        
        self.nature        = self.generateNature()
        self.type          = ["Electric"]                
        #self.level         = self.generateLevel(1, 100)           
        self.hp            = 35                                 
        self.attack        = 55                                
        self.defense       = 40                                 
        self.spAtk         = 50                                
        self.spDef         = 50                              
        self.speed         = 90                                 
        self.friend        = 70                                 
        self.gender        = self.generateGender(50)          
        self.abilities     = []                                 
        self.ability       = "Static"                         
        self.hiddenAbility = "Lightning Rod"                      
        self.hidAbBool     = False  
         

class raichu(pokemon):                                      
    def __init__(self): 
        self.pokedex       = 26.0                                 
        self.species       = "Raichu"                        
        self.nature        = self.generateNature()
        self.type          = ["Electric"]                
        #self.level         = self.generateLevel(1, 100)           
        self.hp            = 60                                 
        self.attack        = 90                                
        self.defense       = 55                                 
        self.spAtk         = 90                                
        self.spDef         = 80                              
        self.speed         = 110                                 
        self.friend        = 70                                 
        self.gender        = self.generateGender(50)          
        self.abilities     = []                                 
        self.ability       = "Static"                         
        self.hiddenAbility = "Lightning Rod"                      
        self.hidAbBool     = False 
        
class alolanRaichu(pokemon):                                      
    def __init__(self): 
        self.pokedex       = 26.5                                 
        self.species       = "Alolan Raichu"                        
        self.nature        = self.generateNature()
        self.type          = ["Electric", "Psychic"]                
        #self.level         = self.generateLevel(1, 100)           
        self.hp            = 60                                 
        self.attack        = 85                                
        self.defense       = 50                                 
        self.spAtk         = 95                                
        self.spDef         = 85                              
        self.speed         = 110                                 
        self.friend        = 70                                 
        self.gender        = self.generateGender(50)          
        self.abilities     = []                                 
        self.ability       = "Surge Surfer"                         
        self.hiddenAbility = ""                      
        self.hidAbBool     = False 
        
class sandshrew(pokemon):                                      
    def __init__(self): 
        self.pokedex       = 27.0                                 
        self.species       = "Sandshrew"                        
        self.nature        = self.generateNature()
        self.type          = ["Ground"]                
        #self.level         = self.generateLevel(1, 21)           
        self.hp            = 50                                 
        self.attack        = 75                               
        self.defense       = 85                                 
        self.spAtk         = 20                               
        self.spDef         = 30                             
        self.speed         = 40                                
        self.friend        = 70                                 
        self.gender        = self.generateGender(50)          
        self.abilities     = []                                 
        self.ability       = "Sand Veil"                         
        self.hiddenAbility = "Sand Rush"                      
        self.hidAbBool     = False 
        
class alolanSandshrew(pokemon):                                      
    def __init__(self): 
        self.pokedex       = 27.5                                 
        self.species       = "Alolan Sandshrew"                        
        self.nature        = self.generateNature()
        self.type          = ["Ice", "Steel"]                
        #self.level         = self.generateLevel(1, 100)           
        self.hp            = 50                                 
        self.attack        = 75                                
        self.defense       = 90                                 
        self.spAtk         = 10                                
        self.spDef         = 35                              
        self.speed         = 40                                 
        self.friend        = 70                                 
        self.gender        = self.generateGender(50)          
        self.abilities     = []                                 
        self.ability       = "Snow Cloak"                         
        self.hiddenAbility = "Slush Rush"                      
        self.hidAbBool     = False 
        
class sandslash(pokemon):                                      
    def __init__(self): 
        self.pokedex       = 28.0                                 
        self.species       = "Sandslash"                        
        self.nature        = self.generateNature()
        self.type          = ["Ground"]                
        #self.level         = self.generateLevel(22, 100)           
        self.hp            = 75                                 
        self.attack        = 100                                
        self.defense       = 110                                
        self.spAtk         = 45                                
        self.spDef         = 55                              
        self.speed         = 65                                
        self.friend        = 70                                 
        self.gender        = self.generateGender(50)          
        self.abilities     = []                                 
        self.ability       = "Sand Veil"                         
        self.hiddenAbility = "Sand Rush"                      
        self.hidAbBool     = False 
   
class alolanSandslash(pokemon):                                      
    def __init__(self): 
        self.pokedex       = 28.5                                 
        self.species       = "Alolan Sandslash"                        
        self.nature        = self.generateNature()
        self.type          = ["Ice", "Steel"]                
        #self.level         = self.generateLevel(1, 100)           
        self.hp            = 75                                 
        self.attack        = 100                                
        self.defense       = 120                                 
        self.spAtk         = 25                                
        self.spDef         = 65                              
        self.speed         = 65                                 
        self.friend        = 70                                 
        self.gender        = self.generateGender(50)          
        self.abilities     = []                                 
        self.ability       = "Sand Veil"                         
        self.hiddenAbility = "Sand Rush"                      
        self.hidAbBool     = False 
        
class nidoran(pokemon):                                      
    def __init__(self): 
        self.pokedex       = 29.0                                 
        self.species       = "Nidoran♀"                        
        self.nature        = self.generateNature()
        self.type          = ["Poison"]                
        #self.level         = self.generateLevel(1, 15)           
        self.hp            = 55                                 
        self.attack        = 47                                
        self.defense       = 52                                 
        self.spAtk         = 40                                
        self.spDef         = 40                              
        self.speed         = 41                                 
        self.friend        = 70                                 
        self.gender        = self.generateGender(0)          
        self.abilities     = ["Poison Point", "Rivalry"]                                 
        self.ability       = ""                         
        self.hiddenAbility = "Hustle"                      
        self.hidAbBool     = False 
        
class nidorina(pokemon):                                      
    def __init__(self): 
        self.pokedex       = 30.0                                 
        self.species       = "Nidorina"                        
        self.nature        = self.generateNature()
        self.type          = ["Poison"]                
       # self.level         = self.generateLevel(16, 100)           
        self.hp            = 70                                 
        self.attack        = 62                                
        self.defense       = 67                                 
        self.spAtk         = 55                                
        self.spDef         = 55                              
        self.speed         = 56                                 
        self.friend        = 70                                 
        self.gender        = self.generateGender(0)          
        self.abilities     = ["Poison Point", "Rivalry"]                                 
        self.ability       = ""                         
        self.hiddenAbility = "Hustle"                      
        self.hidAbBool     = False 
        
class nidoqueen(pokemon):                                      
    def __init__(self): 
        self.pokedex       = 31.0                                 
        self.species       = "Nidoqueen"                        
        self.nature        = self.generateNature()
        self.type          = ["Poison", "Ground"]                
      #  self.level         = self.generateLevel(16, 100)           
        self.hp            = 90                                 
        self.attack        = 92                                
        self.defense       = 87                                 
        self.spAtk         = 75                                
        self.spDef         = 85                              
        self.speed         = 76                                 
        self.friend        = 70                                 
        self.gender        = self.generateGender(0)          
        self.abilities     = ["Poison Point", "Rivalry"]                                 
        self.ability       = ""                         
        self.hiddenAbility = "Sheer Force"                      
        self.hidAbBool     = False 
        
class nidoran(pokemon):                                      
    def __init__(self): 
        self.pokedex       = 32.0                                 
        self.species       = "Nidoran♂"                        
        self.nature        = self.generateNature()
        self.type          = ["Poison"]                
       # self.level         = self.generateLevel(1, 15)           
        self.hp            = 46                                 
        self.attack        = 57                                
        self.defense       = 40                                 
        self.spAtk         = 40                                
        self.spDef         = 40                              
        self.speed         = 50                                 
        self.friend        = 70                                 
        self.gender        = self.generateGender(100)          
        self.abilities     = ["Poison Point", "Rivalry"]                                 
        self.ability       = ""                         
        self.hiddenAbility = "Hustle"                      
        self.hidAbBool     = False 
        
class nidorino(pokemon):                                      
    def __init__(self): 
        self.pokedex       = 33.0                                 
        self.species       = "Nidorino"                        
        self.nature        = self.generateNature()
        self.type          = ["Poison"]                
       # self.level         = self.generateLevel(16, 100)           
        self.hp            = 61                                 
        self.attack        = 72                                
        self.defense       = 57                                 
        self.spAtk         = 55                                
        self.spDef         = 55                              
        self.speed         = 65                                 
        self.friend        = 70                                 
        self.gender        = self.generateGender(100)          
        self.abilities     = ["Poison Point", "Rivalry"]                                 
        self.ability       = ""                         
        self.hiddenAbility = "Hustle"                      
        self.hidAbBool     = False 
        
class nidoking(pokemon):                                      
    def __init__(self): 
        self.pokedex       = 34.0                                 
        self.species       = "Nidoking"                        
        self.nature        = self.generateNature()
        self.type          = ["Poison", "Ground"]                
       # self.level         = self.generateLevel(16, 100)           
        self.hp            = 81                                 
        self.attack        = 102                                
        self.defense       = 77                                 
        self.spAtk         = 85                                
        self.spDef         = 75                              
        self.speed         = 85                                 
        self.friend        = 70                                 
        self.gender        = self.generateGender(100)          
        self.abilities     = ["Poison Point", "Rivalry"]                                 
        self.ability       = ""                         
        self.hiddenAbility = "Sheer Force"                      
        self.hidAbBool     = False 
        
class clefairy(pokemon):                                      
    def __init__(self): 
        self.pokedex       = 35.0                                 
        self.species       = "Clefairy"                        
        self.nature        = self.generateNature()
        self.type          = ["Fairy"]                
      #  self.level         = self.generateLevel(1, 100)           
        self.hp            = 70                                 
        self.attack        = 45                                
        self.defense       = 48                                 
        self.spAtk         = 60                                
        self.spDef         = 65                              
        self.speed         = 35                                 
        self.friend        = 140                                 
        self.gender        = self.generateGender(25)          
        self.abilities     = ["Cute Charm", "Magic Guard"]                                 
        self.ability       = ""                         
        self.hiddenAbility = "Friend Guard"                      
        self.hidAbBool     = False 
        
class clefable(pokemon):                                      
    def __init__(self): 
        self.pokedex       = 36.0                                 
        self.species       = "Clefable"                        
        self.nature        = self.generateNature()
        self.type          = ["Fairy"]                
        #self.level         = self.generateLevel(1, 100)           
        self.hp            = 95                                 
        self.attack        = 70                                
        self.defense       = 73                                 
        self.spAtk         = 95                                
        self.spDef         = 90                              
        self.speed         = 60                                 
        self.friend        = 140                                 
        self.gender        = self.generateGender(25)          
        self.abilities     = ["Cute Charm", "Magic Guard"]                                 
        self.ability       = ""                         
        self.hiddenAbility = "Unaware"                      
        self.hidAbBool     = False
        
class vulpix(pokemon):                                      
    def __init__(self): 
        self.pokedex       = 37.0                                 
        self.species       = "Vulpix"                        
        self.nature        = self.generateNature()
        self.type          = ["Fire"]                
        #self.level         = self.generateLevel(1, 100)           
        self.hp            = 38                                 
        self.attack        = 41                                
        self.defense       = 40                                 
        self.spAtk         = 50                                
        self.spDef         = 65                              
        self.speed         = 65                                 
        self.friend        = 70                                 
        self.gender        = self.generateGender(25)          
        self.abilities     = []                                 
        self.ability       = "Flash Fire"                         
        self.hiddenAbility = "Drought"                      
        self.hidAbBool     = False 
        
class alolanVulpix(pokemon):                                      
    def __init__(self): 
        self.pokedex       = 37.5                                 
        self.species       = "Alolan Vulpix"                        
        self.nature        = self.generateNature()
        self.type          = ["Ice"]                
       # self.level         = self.generateLevel(1, 100)           
        self.hp            = 38                                 
        self.attack        = 41                                
        self.defense       = 40                                 
        self.spAtk         = 50                                
        self.spDef         = 65                              
        self.speed         = 65                                 
        self.friend        = 70                                 
        self.gender        = self.generateGender(25)          
        self.abilities     = []                                 
        self.ability       = "Snow Cloak"                         
        self.hiddenAbility = "Snow Warning"                      
        self.hidAbBool     = False 
        
class ninetales(pokemon):                                      
    def __init__(self): 
        self.pokedex       = 38.0                                 
        self.species       = "Ninetales"                        
        self.nature        = self.generateNature()
        self.type          = ["Fire"]                
       # self.level         = self.generateLevel(1, 100)           
        self.hp            = 73                                
        self.attack        = 76                               
        self.defense       = 75                                 
        self.spAtk         = 81                                
        self.spDef         = 100                              
        self.speed         = 100                                 
        self.friend        = 70                                 
        self.gender        = self.generateGender(25)          
        self.abilities     = []                                 
        self.ability       = "Flash Fire"                         
        self.hiddenAbility = "Drought"                      
        self.hidAbBool     = False 
        
class alolanNinetales(pokemon):                                      
    def __init__(self): 
        self.pokedex       = 38.5                                 
        self.species       = "Ninetales"                        
        self.nature        = self.generateNature()
        self.type          = ["Ice", "Fairy"]                
       # self.level         = self.generateLevel(1, 100)           
        self.hp            = 73                                
        self.attack        = 67                               
        self.defense       = 75                                 
        self.spAtk         = 81                                
        self.spDef         = 100                              
        self.speed         = 109                                
        self.friend        = 70                                 
        self.gender        = self.generateGender(25)          
        self.abilities     = []                                 
        self.ability       = "Snow Cloak"                         
        self.hiddenAbility = "Snow Warning"                      
        self.hidAbBool     = False 
        
class jigglypuff(pokemon):                                      
    def __init__(self): 
        self.pokedex       = 39.0                                 
        self.species       = "Jigglypuff"                        
        self.nature        = self.generateNature()
        self.type          = ["Normal", "Fairy"]                
        #self.level         = self.generateLevel(1, 100)           
        self.hp            = 115                                
        self.attack        = 45                               
        self.defense       = 20                                 
        self.spAtk         = 45                                
        self.spDef         = 25                              
        self.speed         = 20                                 
        self.friend        = 70                                 
        self.gender        = self.generateGender(25)          
        self.abilities     = ["Cute Charm", "Competitive"]                                 
        self.ability       = ""                         
        self.hiddenAbility = "Friend Guard"                      
        self.hidAbBool     = False 
        
class wigglytuff(pokemon):                                      
    def __init__(self): 
        self.pokedex       = 40.0                                 
        self.species       = "Wigglytuff"                        
        self.nature        = self.generateNature()
        self.type          = ["Normal", "Fairy"]                
        #self.level         = self.generateLevel(1, 100)           
        self.hp            = 140                                
        self.attack        = 70                               
        self.defense       = 45                                 
        self.spAtk         = 85                                
        self.spDef         = 50                              
        self.speed         = 45                                 
        self.friend        = 70                                 
        self.gender        = self.generateGender(25)          
        self.abilities     = ["Cute Charm", "Competitive"]                                 
        self.ability       = ""                         
        self.hiddenAbility = "Frisk"                      
        self.hidAbBool     = False 
        
class zubat(pokemon):                                      
    def __init__(self): 
        self.pokedex       = 41.0                                 
        self.species       = "Zubat"                        
        self.nature        = self.generateNature()
        self.type          = ["Poison", "Flying"]                
        #self.level         = self.generateLevel(1, 21)           
        self.hp            = 40                                
        self.attack        = 45                               
        self.defense       = 35                                 
        self.spAtk         = 30                                
        self.spDef         = 40                              
        self.speed         = 55                                 
        self.friend        = 70                                 
        self.gender        = self.generateGender(50)          
        self.abilities     = []                                 
        self.ability       = "Inner Focus"                         
        self.hiddenAbility = "Infiltrator"                      
        self.hidAbBool     = False 
        
class golbat(pokemon):                                      
    def __init__(self): 
        self.pokedex       = 42.0                                 
        self.species       = "Golbat"                        
        self.nature        = self.generateNature()
        self.type          = ["Poison", "Flying"]                
       # self.level         = self.generateLevel(22, 100)           
        self.hp            = 75                                
        self.attack        = 80                               
        self.defense       = 70                                 
        self.spAtk         = 65                                
        self.spDef         = 75                              
        self.speed         = 90                                 
        self.friend        = 70                                 
        self.gender        = self.generateGender(50)          
        self.abilities     = []                                 
        self.ability       = "Inner Focus"                         
        self.hiddenAbility = "Infiltrator"                       
        self.hidAbBool     = False 

class oddish(pokemon):                                      
    def __init__(self): 
        self.pokedex       = 43.0                                 
        self.species       = "Oddish"                        
        self.nature        = self.generateNature()
        self.type          = ["Grass", "Poison"]                
       # self.level         = self.generateLevel(1, 20)           
        self.hp            = 45                                
        self.attack        = 50                               
        self.defense       = 55                                 
        self.spAtk         = 75                                
        self.spDef         = 65                              
        self.speed         = 30                                 
        self.friend        = 70                                 
        self.gender        = self.generateGender(50)          
        self.abilities     = []                                 
        self.ability       = "Chlorophyll"                         
        self.hiddenAbility = "Run Away"                       
        self.hidAbBool     = False 
        
class gloom(pokemon):                                      
    def __init__(self): 
        self.pokedex       = 44.0                                 
        self.species       = "Gloom"                        
        self.nature        = self.generateNature()
        self.type          = ["Grass", "Poison"]                
       # self.level         = self.generateLevel(22, 100)           
        self.hp            = 60                                
        self.attack        = 65                               
        self.defense       = 70                                 
        self.spAtk         = 85                                
        self.spDef         = 75                              
        self.speed         = 40                                 
        self.friend        = 70                                 
        self.gender        = self.generateGender(50)          
        self.abilities     = []                                 
        self.ability       = "Chlorophyll"                         
        self.hiddenAbility = "Stench"                       
        self.hidAbBool     = False 
        
class vileplume(pokemon):                                      
    def __init__(self): 
        self.pokedex       = 45.0                                 
        self.species       = "Vileplume"                        
        self.nature        = self.generateNature()
        self.type          = ["Grass", "Poison"]                
       # self.level         = self.generateLevel(22, 100)           
        self.hp            = 75                                
        self.attack        = 80                               
        self.defense       = 85                                 
        self.spAtk         = 110                                
        self.spDef         = 90                              
        self.speed         = 50                                 
        self.friend        = 70                                 
        self.gender        = self.generateGender(50)          
        self.abilities     = []                                 
        self.ability       = "Chlorophyll"                         
        self.hiddenAbility = "Effect Spore"                       
        self.hidAbBool     = False 
        
class paras(pokemon):                                      
    def __init__(self): 
        self.pokedex       = 46.0                                 
        self.species       = "Paras"                        
        self.nature        = self.generateNature()
        self.type          = ["Bug", "Grass"]                
        #self.level         = self.generateLevel(1, 23)           
        self.hp            = 35                                
        self.attack        = 70                               
        self.defense       = 55                                 
        self.spAtk         = 45                                
        self.spDef         = 55                              
        self.speed         = 25                                 
        self.friend        = 70                                 
        self.gender        = self.generateGender(50)          
        self.abilities     = ["Effect Spore", "Dry Skin"]                                 
        self.ability       = ""                         
        self.hiddenAbility = "Damp"                       
        self.hidAbBool     = False 
        
class parasect(pokemon):                                      
    def __init__(self): 
        self.pokedex       = 47.0                                 
        self.species       = "Parasect"                        
        self.nature        = self.generateNature()
        self.type          = ["Bug", "Grass"]                
       # self.level         = self.generateLevel(24, 100)           
        self.hp            = 60                                
        self.attack        = 95                               
        self.defense       = 80                                 
        self.spAtk         = 60                                
        self.spDef         = 80                              
        self.speed         = 30                                 
        self.friend        = 70                                 
        self.gender        = self.generateGender(50)          
        self.abilities     = ["Effect Spore", "Dry Skin"]                                 
        self.ability       = ""                         
        self.hiddenAbility = "Damp"                       
        self.hidAbBool     = False 
        
class venonat(pokemon):                                      
    def __init__(self): 
        self.pokedex       = 48.0                                 
        self.species       = "Venonat"                        
        self.nature        = self.generateNature()
        self.type          = ["Bug", "Poison"]                
       # self.level         = self.generateLevel(1, 30)           
        self.hp            = 60                                
        self.attack        = 55                               
        self.defense       = 50                                 
        self.spAtk         = 40                                
        self.spDef         = 55                              
        self.speed         = 45                                 
        self.friend        = 70                                 
        self.gender        = self.generateGender(50)          
        self.abilities     = ["Compound Eyes", "Tinted Lens"]                                 
        self.ability       = ""                         
        self.hiddenAbility = "Run Away"                       
        self.hidAbBool     = False 
        
class venomoth(pokemon):                                      
    def __init__(self): 
        self.pokedex       = 49.0                                 
        self.species       = "Venomoth"                        
        self.nature        = self.generateNature()
        self.type          = ["Bug", "Poison"]                
        #self.level         = self.generateLevel(31, 100)           
        self.hp            = 70                                
        self.attack        = 65                               
        self.defense       = 60                                 
        self.spAtk         = 90                                
        self.spDef         = 75                              
        self.speed         = 90                                 
        self.friend        = 70                                 
        self.gender        = self.generateGender(50)          
        self.abilities     = ["Shield Dust", "Tinted Lens"]                                 
        self.ability       = ""                         
        self.hiddenAbility = "Wonder Skin"                       
        self.hidAbBool     = False 
        
class diglett(pokemon):                                      
    def __init__(self): 
        self.pokedex       = 50.0                                 
        self.species       = "Diglett"                        
        self.nature        = self.generateNature()
        self.type          = ["Ground"]                
       # self.level         = self.generateLevel(1, 25)           
        self.hp            = 10                                
        self.attack        = 55                               
        self.defense       = 25                                
        self.spAtk         = 35                                
        self.spDef         = 45                              
        self.speed         = 90                                 
        self.friend        = 70                                 
        self.gender        = self.generateGender(50)          
        self.abilities     = ["Sand Veil", "Arena Trap"]                                 
        self.ability       = ""                         
        self.hiddenAbility = "Sand Force"                       
        self.hidAbBool     = False 
        
class alolanDiglett(pokemon):                                      
    def __init__(self): 
        self.pokedex       = 50.5                                 
        self.species       = "Alolan Diglett"                        
        self.nature        = self.generateNature()
        self.type          = ["Ground", "Steel"]                
      #  self.level         = self.generateLevel(1, 25)           
        self.hp            = 10                                
        self.attack        = 55                               
        self.defense       = 30                                 
        self.spAtk         = 35                                
        self.spDef         = 45                              
        self.speed         = 90                                 
        self.friend        = 70                                 
        self.gender        = self.generateGender(50)          
        self.abilities     = ["Sand Veil", "Tangling Hair"]                                 
        self.ability       = ""                         
        self.hiddenAbility = "Sand Force"                       
        self.hidAbBool     = False 
        
class dugtrio(pokemon):                                      
    def __init__(self): 
        self.pokedex       = 51.0                                 
        self.species       = "Dugtrio"                        
        self.nature        = self.generateNature()
        self.type          = ["Ground"]                
      #  self.level         = self.generateLevel(26, 100)           
        self.hp            = 35                                
        self.attack        = 100                              
        self.defense       = 50                                 
        self.spAtk         = 50                                
        self.spDef         = 70                             
        self.speed         = 120                                
        self.friend        = 70                                 
        self.gender        = self.generateGender(50)          
        self.abilities     = ["Sand Veil", "Arena Trap"]                                 
        self.ability       = ""                         
        self.hiddenAbility = "Sand Force"                       
        self.hidAbBool     = False 
        
class alolanDugtrio(pokemon):                                      
    def __init__(self): 
        self.pokedex       = 51.5                                 
        self.species       = "Alolan Dugtrio"                        
        self.nature        = self.generateNature()
        self.type          = ["Ground", "Steel"]                
       # self.level         = self.generateLevel(26, 100)           
        self.hp            = 35                                
        self.attack        = 100                              
        self.defense       = 60                                 
        self.spAtk         = 50                                
        self.spDef         = 70                             
        self.speed         = 110                                
        self.friend        = 70                                 
        self.gender        = self.generateGender(50)          
        self.abilities     = ["Sand Veil", "Tangling Hair"]                                 
        self.ability       = ""                         
        self.hiddenAbility = "Sand Force"                       
        self.hidAbBool     = False 
        
class meowth(pokemon):                                      
    def __init__(self): 
        self.pokedex       = 52.0                                 
        self.species       = "Meowth"                        
        self.nature        = self.generateNature()
        self.type          = ["Normal"]                
       # self.level         = self.generateLevel(1, 27)           
        self.hp            = 40                                
        self.attack        = 45                              
        self.defense       = 35                                 
        self.spAtk         = 40                                
        self.spDef         = 40                             
        self.speed         = 90                                
        self.friend        = 70                                 
        self.gender        = self.generateGender(50)          
        self.abilities     = ["Pickup", "Technician"]                                 
        self.ability       = ""                         
        self.hiddenAbility = "Unnerve"                       
        self.hidAbBool     = False 
        
class alolanMeowth(pokemon):                                      
    def __init__(self): 
        self.pokedex       = 52.5                                 
        self.species       = "Alolan Meowth"                        
        self.nature        = self.generateNature()
        self.type          = ["Dark"]                
       # self.level         = self.generateLevel(1, 100)           
        self.hp            = 40                                
        self.attack        = 35                              
        self.defense       = 35                                 
        self.spAtk         = 50                                
        self.spDef         = 40                             
        self.speed         = 90                                
        self.friend        = 70                                 
        self.gender        = self.generateGender(50)          
        self.abilities     = ["Pickup", "Technician"]                                 
        self.ability       = ""                         
        self.hiddenAbility = "Rattled"                       
        self.hidAbBool     = False 
        
class galarianMeowth(pokemon):                                      
    def __init__(self): 
        self.pokedex       = 52.75                                 
        self.species       = "Galarian Meowth"                        
        self.nature        = self.generateNature()
        self.type          = ["Steel"]                
        #self.level         = self.generateLevel(1, 27)           
        self.hp            = 50                                
        self.attack        = 65                              
        self.defense       = 55                                 
        self.spAtk         = 40                                
        self.spDef         = 40                             
        self.speed         = 40                                
        self.friend        = 70                                 
        self.gender        = self.generateGender(50)          
        self.abilities     = ["Pickup", "Tough Claws"]                                 
        self.ability       = ""                         
        self.hiddenAbility = "Unnerve"                       
        self.hidAbBool     = False 
        
class persian(pokemon):                                      
    def __init__(self): 
        self.pokedex       = 53.0                                 
        self.species       = "Persian"                        
        self.nature        = self.generateNature()
        self.type          = ["Normal"]                
       # self.level         = self.generateLevel(28, 100)           
        self.hp            = 65                                
        self.attack        = 70                              
        self.defense       = 60                                 
        self.spAtk         = 65                                
        self.spDef         = 65                             
        self.speed         = 115                                
        self.friend        = 70                                 
        self.gender        = self.generateGender(50)          
        self.abilities     = ["Limber", "Technician"]                                 
        self.ability       = ""                         
        self.hiddenAbility = "Unnerve"                       
        self.hidAbBool     = False 
        
class alolanPersian(pokemon):                                      
    def __init__(self): 
        self.pokedex       = 53.5                                 
        self.species       = "Persian"                        
        self.nature        = self.generateNature()
        self.type          = ["Dark"]                
        #self.level         = self.generateLevel(1, 100)           
        self.hp            = 65                                
        self.attack        = 60                              
        self.defense       = 60                                 
        self.spAtk         = 75                                
        self.spDef         = 65                             
        self.speed         = 115                                
        self.friend        = 70                                 
        self.gender        = self.generateGender(50)          
        self.abilities     = ["Fur Coat", "Technician"]                                 
        self.ability       = ""                         
        self.hiddenAbility = "Rattled"                       
        self.hidAbBool     = False 
        
class psyduck(pokemon):                                      
    def __init__(self): 
        self.pokedex       = 54.0                                 
        self.species       = "Psyduck"                        
        self.nature        = self.generateNature()
        self.type          = ["Water"]                
       # self.level         = self.generateLevel(1, 32)           
        self.hp            = 50                                
        self.attack        = 52                              
        self.defense       = 48                                 
        self.spAtk         = 65                                
        self.spDef         = 50                             
        self.speed         = 55                                
        self.friend        = 70                                 
        self.gender        = self.generateGender(50)          
        self.abilities     = ["Damp", "Cloud Nine"]                                 
        self.ability       = ""                         
        self.hiddenAbility = "Swift Swim"                       
        self.hidAbBool     = False 
        
class golduck(pokemon):                                      
    def __init__(self): 
        self.pokedex       = 55.0                                 
        self.species       = "Golduck"                        
        self.nature        = self.generateNature()
        self.type          = ["Water"]                
       # self.level         = self.generateLevel(33, 100)           
        self.hp            = 80                                
        self.attack        = 82                              
        self.defense       = 78                                 
        self.spAtk         = 95                                
        self.spDef         = 80                             
        self.speed         = 85                                
        self.friend        = 70                                 
        self.gender        = self.generateGender(50)          
        self.abilities     = ["Damp", "Cloud Nine"]                                 
        self.ability       = ""                         
        self.hiddenAbility = "Swift Swim"                       
        self.hidAbBool     = False 
  
class mankey(pokemon):                                      
    def __init__(self): 
        self.pokedex       = 56.0                                 
        self.species       = "Mankey"                        
        self.nature        = self.generateNature()
        self.type          = ["Fighting"]                
       # self.level         = self.generateLevel(1, 27)           
        self.hp            = 40                                
        self.attack        = 80                              
        self.defense       = 35                                 
        self.spAtk         = 35                                
        self.spDef         = 45                             
        self.speed         = 70                                
        self.friend        = 70                                 
        self.gender        = self.generateGender(50)          
        self.abilities     = ["Vital Spirit", "Anger Point"]                                 
        self.ability       = ""                         
        self.hiddenAbility = "Defiant"                       
        self.hidAbBool     = False 
        
class primeape(pokemon):                                      
    def __init__(self): 
        self.pokedex       = 57.0                                 
        self.species       = "Primeape"                        
        self.nature        = self.generateNature()
        self.type          = ["Fighting"]                
       # self.level         = self.generateLevel(28, 100)           
        self.hp            = 65                                
        self.attack        = 105                              
        self.defense       = 60                                 
        self.spAtk         = 60                                
        self.spDef         = 70                            
        self.speed         = 95                               
        self.friend        = 70                                 
        self.gender        = self.generateGender(50)          
        self.abilities     = ["Vital Spirit", "Anger Point"]                                 
        self.ability       = ""                         
        self.hiddenAbility = "Defiant"                       
        self.hidAbBool     = False 
        
class growlithe(pokemon):                                      
    def __init__(self): 
        self.pokedex       = 58.0                                 
        self.species       = "Growlithe"                        
        self.nature        = self.generateNature()
        self.type          = ["Fire"]                
       # self.level         = self.generateLevel(1, 100)           
        self.hp            = 55                                
        self.attack        = 70                              
        self.defense       = 45                                 
        self.spAtk         = 70                                
        self.spDef         = 50                             
        self.speed         = 60                                
        self.friend        = 70                                 
        self.gender        = self.generateGender(75)          
        self.abilities     = ["Intimidate", "Flash Fire"]                                 
        self.ability       = ""                         
        self.hiddenAbility = "Justified"                       
        self.hidAbBool     = False 
        
class arcanine(pokemon):                                      
    def __init__(self): 
        self.pokedex       = 59.0                                 
        self.species       = "Arcanine"                        
        self.nature        = self.generateNature()
        self.type          = ["Fire"]                
       # self.level         = self.generateLevel(1, 100)           
        self.hp            = 90                                
        self.attack        = 110                              
        self.defense       = 80                                 
        self.spAtk         = 100                                
        self.spDef         = 80                             
        self.speed         = 95                                
        self.friend        = 70                                 
        self.gender        = self.generateGender(75)          
        self.abilities     = ["Intimidate", "Flash Fire"]                                 
        self.ability       = ""                         
        self.hiddenAbility = "Justified"                       
        self.hidAbBool     = False 
        
class poliwag(pokemon):                                      
    def __init__(self): 
        self.pokedex       = 60.0                                 
        self.species       = "Poliwag"                        
        self.nature        = self.generateNature()
        self.type          = ["Water"]                
        #self.level         = self.generateLevel(1, 24)           
        self.hp            = 65                               
        self.attack        = 65                             
        self.defense       = 65                                 
        self.spAtk         = 50                                
        self.spDef         = 50                            
        self.speed         = 90                                
        self.friend        = 70                                 
        self.gender        = self.generateGender(50)          
        self.abilities     = ["Water Absorb", "Damp"]                                 
        self.ability       = ""                         
        self.hiddenAbility = "Swift Swim"                       
        self.hidAbBool     = False 
             
class poliwhirl(pokemon):                                      
    def __init__(self): 
        self.pokedex       = 61.0                                 
        self.species       = "Poliwhirl"                        
        self.nature        = self.generateNature()
        self.type          = ["Water"]                
        #self.level         = self.generateLevel(25, 100)           
        self.hp            = 40                                
        self.attack        = 5                              
        self.defense       = 40                                 
        self.spAtk         = 40                                
        self.spDef         = 40                             
        self.speed         = 90                                
        self.friend        = 70                                 
        self.gender        = self.generateGender(50)          
        self.abilities     = ["Water Absorb", "Damp"]                                 
        self.ability       = ""                         
        self.hiddenAbility = "Swift Swim"                       
        self.hidAbBool     = False 
        
class poliwrath(pokemon):                                      
    def __init__(self): 
        self.pokedex       = 62.0                                 
        self.species       = "Poliwrath"                        
        self.nature        = self.generateNature()
        self.type          = ["Water", "Fighting"]                
       # self.level         = self.generateLevel(25, 100)           
        self.hp            = 90                                
        self.attack        = 95                             
        self.defense       = 95                                 
        self.spAtk         = 70                               
        self.spDef         = 90                             
        self.speed         = 70                                
        self.friend        = 70                                 
        self.gender        = self.generateGender(50)          
        self.abilities     = ["Water Absorb", "Damp"]                                 
        self.ability       = ""                         
        self.hiddenAbility = "Swift Swim"                       
        self.hidAbBool     = False 
        
class abra(pokemon):                                      
    def __init__(self): 
        self.pokedex       = 63.0                                 
        self.species       = "Abra"                        
        self.nature        = self.generateNature()
        self.type          = ["Psychic"]                
       # self.level         = self.generateLevel(1, 15)           
        self.hp            = 25                                
        self.attack        = 20                              
        self.defense       = 15                                 
        self.spAtk         = 105                                
        self.spDef         = 55                             
        self.speed         = 90                                
        self.friend        = 70                                 
        self.gender        = self.generateGender(75)          
        self.abilities     = ["Synchronize", "Inner Focus"]                                 
        self.ability       = ""                         
        self.hiddenAbility = "Magic Guard"                       
        self.hidAbBool     = False 
        
class kadabra(pokemon):                                      
    def __init__(self): 
        self.pokedex       = 64.0                                 
        self.species       = "Kadabra"                        
        self.nature        = self.generateNature()
        self.type          = ["Psychic"]                
       # self.level         = self.generateLevel(16, 100)           
        self.hp            = 40                                
        self.attack        = 35                              
        self.defense       = 30                                 
        self.spAtk         = 120                                
        self.spDef         = 70                             
        self.speed         = 105                                
        self.friend        = 70                                 
        self.gender        = self.generateGender(75)          
        self.abilities     = ["Synchronize", "Inner Focus"]                                 
        self.ability       = ""                         
        self.hiddenAbility = "Magic Guard"                       
        self.hidAbBool     = False 
        
class alakazam(pokemon):                                      
    def __init__(self): 
        self.pokedex       = 65.0                                 
        self.species       = "Alakazam"                        
        self.nature        = self.generateNature()
        self.type          = ["Psychic"]                
       # self.level         = self.generateLevel(16, 100)           
        self.hp            = 55                                
        self.attack        = 50                              
        self.defense       = 45                                 
        self.spAtk         = 135                                
        self.spDef         = 95                             
        self.speed         = 120                                
        self.friend        = 70                                 
        self.gender        = self.generateGender(75)          
        self.abilities     = ["Synchronize", "Inner Focus"]                                 
        self.ability       = ""                         
        self.hiddenAbility = "Magic Guard"                       
        self.hidAbBool     = False 
        
class machop(pokemon):                                      
    def __init__(self): 
        self.pokedex       = 66.0                                 
        self.species       = "Machop"                        
        self.nature        = self.generateNature()
        self.type          = ["Fighting"]                
      #  self.level         = self.generateLevel(1, 27)           
        self.hp            = 70                                
        self.attack        = 80                              
        self.defense       = 50                                 
        self.spAtk         = 35                                
        self.spDef         = 35                             
        self.speed         = 35                                
        self.friend        = 70                                 
        self.gender        = self.generateGender(75)          
        self.abilities     = ["Guts", "No Guard"]                                 
        self.ability       = ""                         
        self.hiddenAbility = "Steadfast"                       
        self.hidAbBool     = False 
        
class machoke(pokemon):                                      
    def __init__(self): 
        self.pokedex       = 67.0                                 
        self.species       = "Machoke"                        
        self.nature        = self.generateNature()
        self.type          = ["Fighting"]                
       # self.level         = self.generateLevel(28, 100)           
        self.hp            = 80                                
        self.attack        = 100                              
        self.defense       = 70                                 
        self.spAtk         = 50                                
        self.spDef         = 60                             
        self.speed         = 45                                
        self.friend        = 70                                 
        self.gender        = self.generateGender(75)          
        self.abilities     = ["Guts", "No Guard"]                                 
        self.ability       = ""                         
        self.hiddenAbility = "Steadfast"                       
        self.hidAbBool     = False 
        
class machamp(pokemon):                                      
    def __init__(self): 
        self.pokedex       = 68.0                                 
        self.species       = "Machamp"                        
        self.nature        = self.generateNature()
        self.type          = ["Fighting"]                
       # self.level         = self.generateLevel(28, 100)           
        self.hp            = 90                               
        self.attack        = 130                             
        self.defense       = 80                                
        self.spAtk         = 65                                
        self.spDef         = 85                             
        self.speed         = 55                                
        self.friend        = 70                                 
        self.gender        = self.generateGender(75)          
        self.abilities     = ["Guts", "No Guard"]                                 
        self.ability       = ""                         
        self.hiddenAbility = "Steadfast"                       
        self.hidAbBool     = False 
        
class bellsprout(pokemon):                                      
    def __init__(self): 
        self.pokedex       = 69.0                                 
        self.species       = "Bellsprout"                        
        self.nature        = self.generateNature()
        self.type          = ["Grass", "Poison"]                
       # self.level         = self.generateLevel(1, 20)           
        self.hp            = 50                                
        self.attack        = 75                              
        self.defense       = 35                                 
        self.spAtk         = 70                                
        self.spDef         = 30                             
        self.speed         = 40                                
        self.friend        = 70                                 
        self.gender        = self.generateGender(50)          
        self.abilities     = []                                 
        self.ability       = "Chlorophyll"                         
        self.hiddenAbility = "Gluttony"                       
        self.hidAbBool     = False 
        
class weepinbell(pokemon):                                      
    def __init__(self): 
        self.pokedex       = 70.0                                 
        self.species       = "Weepinbell"                        
        self.nature        = self.generateNature()
        self.type          = ["Grass", "Poison"]                
        #self.level         = self.generateLevel(21, 100)           
        self.hp            = 65                                
        self.attack        = 90                              
        self.defense       = 50                                 
        self.spAtk         = 85                                
        self.spDef         = 45                             
        self.speed         = 55                                
        self.friend        = 70                                 
        self.gender        = self.generateGender(50)          
        self.abilities     = []                                 
        self.ability       = "Chlorophyll"                         
        self.hiddenAbility = "Gluttony"                       
        self.hidAbBool     = False 
        
class victreebel(pokemon):                                      
    def __init__(self): 
        self.pokedex       = 71.0                                 
        self.species       = "Victreebel"                        
        self.nature        = self.generateNature()
        self.type          = ["Grass", "Poison"]                
        #self.level         = self.generateLevel(21, 100)           
        self.hp            = 80                                
        self.attack        = 105                              
        self.defense       = 65                                 
        self.spAtk         = 100                                
        self.spDef         = 70                             
        self.speed         = 70                                
        self.friend        = 70                                 
        self.gender        = self.generateGender(50)          
        self.abilities     = []                                 
        self.ability       = "Chlorophyll"                         
        self.hiddenAbility = "Gluttony"                       
        self.hidAbBool     = False 
        
class tentacool(pokemon):                                      
    def __init__(self): 
        self.pokedex       = 72.0                                 
        self.species       = "Tentacool"                        
        self.nature        = self.generateNature()
        self.type          = ["Water", "Poison"]                
       # self.level         = self.generateLevel(1, 29)           
        self.hp            = 40                                
        self.attack        = 40                              
        self.defense       = 35                                 
        self.spAtk         = 50                                
        self.spDef         = 100                             
        self.speed         = 70                                
        self.friend        = 70                                 
        self.gender        = self.generateGender(50)          
        self.abilities     = ["Clear Body", "Liquid Ooze"]                                 
        self.ability       = ""                         
        self.hiddenAbility = "Rain Dish"                       
        self.hidAbBool     = False 
        
class tentacruel(pokemon):                                      
    def __init__(self): 
        self.pokedex       = 73.0                                 
        self.species       = "Tentacruel"                        
        self.nature        = self.generateNature()
        self.type          = ["Water", "Poison"]                
        #self.level         = self.generateLevel(30, 100)           
        self.hp            = 80                                
        self.attack        = 70                              
        self.defense       = 65                                 
        self.spAtk         = 80                                
        self.spDef         = 120                             
        self.speed         = 100                                
        self.friend        = 70                                 
        self.gender        = self.generateGender(50)          
        self.abilities     = ["Clear Body", "Liquid Ooze"]                                 
        self.ability       = ""                         
        self.hiddenAbility = "Rain Dish"                       
        self.hidAbBool     = False  
        
class geodude(pokemon):                                      
    def __init__(self): 
        self.pokedex       = 74.0                                 
        self.species       = "Geodude"                        
        self.nature        = self.generateNature()
        self.type          = ["Rock", "Ground"]                
      #  self.level         = self.generateLevel(1, 24)           
        self.hp            = 40                                
        self.attack        = 80                              
        self.defense       = 100                                 
        self.spAtk         = 30                                
        self.spDef         = 30                             
        self.speed         = 20                                
        self.friend        = 70                                 
        self.gender        = self.generateGender(50)          
        self.abilities     = ["Rock Head", "Sturdy"]                                 
        self.ability       = ""                         
        self.hiddenAbility = "Sand Veil"                       
        self.hidAbBool     = False 
        
class alolanGeodude(pokemon):                                      
    def __init__(self): 
        self.pokedex       = 74.5                                 
        self.species       = "Alolan Geodude"                        
        self.nature        = self.generateNature()
        self.type          = ["Rock", "Electric"]                
      #  self.level         = self.generateLevel(1, 24)           
        self.hp            = 40                                
        self.attack        = 80                              
        self.defense       = 100                                 
        self.spAtk         = 30                                
        self.spDef         = 30                             
        self.speed         = 20                                
        self.friend        = 70                                 
        self.gender        = self.generateGender(50)          
        self.abilities     = ["Magnet Pull", "Sturdy"]                                 
        self.ability       = ""                         
        self.hiddenAbility = "Galvanize"                       
        self.hidAbBool     = False
        
class graveler(pokemon):                                      
    def __init__(self): 
        self.pokedex       = 75.0                                 
        self.species       = "Graveler"                        
        self.nature        = self.generateNature()
        self.type          = ["Rock", "Ground"]                
       # self.level         = self.generateLevel(25, 100)           
        self.hp            = 55                                
        self.attack        = 95                              
        self.defense       = 115                                 
        self.spAtk         = 45                                
        self.spDef         = 45                             
        self.speed         = 35                                
        self.friend        = 70                                 
        self.gender        = self.generateGender(50)          
        self.abilities     = ["Rock Head", "Sturdy"]                                 
        self.ability       = ""                         
        self.hiddenAbility = "Sand Veil"                       
        self.hidAbBool     = False
        
class alolanGraveler(pokemon):                                      
    def __init__(self): 
        self.pokedex       = 75.5                                 
        self.species       = "Alolan Graveler"                        
        self.nature        = self.generateNature()
        self.type          = ["Rock", "Electric"]                
       # self.level         = self.generateLevel(25, 100)           
        self.hp            = 55                                
        self.attack        = 95                              
        self.defense       = 115                                 
        self.spAtk         = 45                                
        self.spDef         = 45                             
        self.speed         = 35                                
        self.friend        = 70                                 
        self.gender        = self.generateGender(50)          
        self.abilities     = ["Magnet Pull", "Sturdy"]                                 
        self.ability       = ""                         
        self.hiddenAbility = "Galvanize"                       
        self.hidAbBool     = False
        
class golem(pokemon):                                      
    def __init__(self): 
        self.pokedex       = 76.0                                 
        self.species       = "Golem"                        
        self.nature        = self.generateNature()
        self.type          = ["Rock", "Ground"]                
       # self.level         = self.generateLevel(25, 100)           
        self.hp            = 80                                
        self.attack        = 120                              
        self.defense       = 130                                 
        self.spAtk         = 55                                
        self.spDef         = 65                             
        self.speed         = 45                                
        self.friend        = 70                                 
        self.gender        = self.generateGender(50)          
        self.abilities     = ["Rock Head", "Sturdy"]                                 
        self.ability       = ""                         
        self.hiddenAbility = "Sand Veil"                       
        self.hidAbBool     = False
        
class alolanGolem(pokemon):                                      
    def __init__(self): 
        self.pokedex       = 76.5                                 
        self.species       = "Alolan Golem"                        
        self.nature        = self.generateNature()
        self.type          = ["Rock", "Electric"]                
       # self.level         = self.generateLevel(25, 100)           
        self.hp            = 80                                
        self.attack        = 120                              
        self.defense       = 130                                 
        self.spAtk         = 55                                
        self.spDef         = 65                             
        self.speed         = 45                                
        self.friend        = 70                                 
        self.gender        = self.generateGender(50)          
        self.abilities     = ["Magnet Pull", "Sturdy"]                                 
        self.ability       = ""                         
        self.hiddenAbility = "Galvanize"                       
        self.hidAbBool     = False
        
class ponyta(pokemon):                                      
    def __init__(self): 
        self.pokedex       = 77.0                                 
        self.species       = "Ponyta"                        
        self.nature        = self.generateNature()
        self.type          = ["Fire"]                
        #self.level         = self.generateLevel(1, 39)           
        self.hp            = 50                                
        self.attack        = 85                              
        self.defense       = 55                                 
        self.spAtk         = 65                                
        self.spDef         = 65                             
        self.speed         = 90                                
        self.friend        = 70                                 
        self.gender        = self.generateGender(50)          
        self.abilities     = ["Run Away", "Flash Fire"]                                 
        self.ability       = ""                         
        self.hiddenAbility = "Flame Body"                       
        self.hidAbBool     = False
        
class galarainPonyta(pokemon):                                      
    def __init__(self): 
        self.pokedex       = 77.75                                 
        self.species       = "Galarian Ponyta"                        
        self.nature        = self.generateNature()
        self.type          = ["Psychic"]                
      #  self.level         = self.generateLevel(1, 39)           
        self.hp            = 50                                
        self.attack        = 85                              
        self.defense       = 55                                 
        self.spAtk         = 65                                
        self.spDef         = 65                             
        self.speed         = 90                                
        self.friend        = 70                                 
        self.gender        = self.generateGender(50)          
        self.abilities     = ["Run Away", "Pastel Veil"]                                 
        self.ability       = ""                         
        self.hiddenAbility = "Anticipation"                       
        self.hidAbBool     = False
        
class rapidash(pokemon):                                      
    def __init__(self): 
        self.pokedex       = 78.0                                 
        self.species       = "Rapidash"                        
        self.nature        = self.generateNature()
        self.type          = ["Fire"]                
      #  self.level         = self.generateLevel(40, 100)           
        self.hp            = 65                                
        self.attack        = 100                              
        self.defense       = 70                                 
        self.spAtk         = 80                                
        self.spDef         = 80                             
        self.speed         = 105                                
        self.friend        = 70                                 
        self.gender        = self.generateGender(50)          
        self.abilities     = ["Run Away", "Flash Fire"]                                 
        self.ability       = ""                         
        self.hiddenAbility = "Flame Body"                       
        self.hidAbBool     = False
        
class galarianRapidash(pokemon):                                      
    def __init__(self): 
        self.pokedex       = 78.75                                 
        self.species       = "Galarian Rapidash"                        
        self.nature        = self.generateNature()
        self.type          = ["Psychic"]                
       # self.level         = self.generateLevel(40, 100)           
        self.hp            = 65                                
        self.attack        = 100                              
        self.defense       = 70                                 
        self.spAtk         = 80                                
        self.spDef         = 80                             
        self.speed         = 105                                
        self.friend        = 70                                 
        self.gender        = self.generateGender(50)          
        self.abilities     = ["Run Away", "Pastel Veil"]                                 
        self.ability       = ""                         
        self.hiddenAbility = "Anticipation"                       
        self.hidAbBool     = False
        
class slowpoke(pokemon):                                      
    def __init__(self): 
        self.pokedex       = 79.0                                 
        self.species       = "Slowpoke"                        
        self.nature        = self.generateNature()
        self.type          = ["Water", "Psychic"]                
       # self.level         = self.generateLevel(1, 36)           
        self.hp            = 90                                
        self.attack        = 65                              
        self.defense       = 65                                 
        self.spAtk         = 40
        self.spDef         = 40                             
        self.speed         = 15                                
        self.friend        = 70                                 
        self.gender        = self.generateGender(50)          
        self.abilities     = ["Oblivious", "Own Tempo"]                                 
        self.ability       = ""                         
        self.hiddenAbility = "Regenerator"                       
        self.hidAbBool     = False
        
class slowbro(pokemon):                                      
    def __init__(self): 
        self.pokedex       = 80.0                                 
        self.species       = "Slowbro"                        
        self.nature        = self.generateNature()
        self.type          = ["Water", "Psychic"]                
      #  self.level         = self.generateLevel(37, 100)           
        self.hp            = 95                                
        self.attack        = 75                              
        self.defense       = 110                                 
        self.spAtk         = 100
        self.spDef         = 80                             
        self.speed         = 30                               
        self.friend        = 70                                 
        self.gender        = self.generateGender(50)          
        self.abilities     = ["Oblivious", "Own Tempo"]                                 
        self.ability       = ""                         
        self.hiddenAbility = "Regenerator"                       
        self.hidAbBool     = False
        
class magnemite(pokemon):                                      
    def __init__(self): 
        self.pokedex       = 81.0                                 
        self.species       = "Magnemite"                        
        self.nature        = self.generateNature()
        self.type          = ["Electric", "Steel"]                
      #  self.level         = self.generateLevel(1, 29)           
        self.hp            = 25                                
        self.attack        = 35                              
        self.defense       = 70                                 
        self.spAtk         = 95
        self.spDef         = 55                             
        self.speed         = 45                                
        self.friend        = 70                                 
        self.gender        = self.generateGender(0)          
        self.abilities     = ["Magnet Pull", "Sturdy"]                                 
        self.ability       = ""                         
        self.hiddenAbility = "Analytic"                       
        self.hidAbBool     = False
        
class magneton(pokemon):                                      
    def __init__(self): 
        self.pokedex       = 82.0                                 
        self.species       = "Magneton"                        
        self.nature        = self.generateNature()
        self.type          = ["Electric", "Steel"]                
       # self.level         = self.generateLevel(1, 29)           
        self.hp            = 50                                
        self.attack        = 60                              
        self.defense       = 95                                 
        self.spAtk         = 120
        self.spDef         = 70                             
        self.speed         = 70                                
        self.friend        = 70                                 
        self.gender        = self.generateGender(0)          
        self.abilities     = ["Magnet Pull", "Sturdy"]                                 
        self.ability       = ""                         
        self.hiddenAbility = "Analytic"                       
        self.hidAbBool     = False
        
class farfetchd(pokemon):                                      
    def __init__(self): 
        self.pokedex       = 83.0                                 
        self.species       = "Farfetch'd"                        
        self.nature        = self.generateNature()
        self.type          = ["Normal", "Flying"]                
       # self.level         = self.generateLevel(1, 100)           
        self.hp            = 52                                
        self.attack        = 90                              
        self.defense       = 55                                 
        self.spAtk         = 58
        self.spDef         = 62                             
        self.speed         = 60                                
        self.friend        = 70                                 
        self.gender        = self.generateGender(0)          
        self.abilities     = ["Keen Eye", "Inner Focus"]                                 
        self.ability       = ""                         
        self.hiddenAbility = "Defiant"                       
        self.hidAbBool     = False
        
class galarianFarfetchd(pokemon):                                      
    def __init__(self): 
        self.pokedex       = 83.75                                 
        self.species       = "Galarian Farfetch'd"                        
        self.nature        = self.generateNature()
        self.type          = ["Fighting"]                
      #  self.level         = self.generateLevel(1, 100)           
        self.hp            = 52                                
        self.attack        = 95                              
        self.defense       = 55                                 
        self.spAtk         = 58
        self.spDef         = 62                             
        self.speed         = 55                               
        self.friend        = 70                                 
        self.gender        = self.generateGender(0)          
        self.abilities     = []                                 
        self.ability       = "Steadfast"                         
        self.hiddenAbility = "Scrappy"                       
        self.hidAbBool     = False
        
class doduo(pokemon):                                      
    def __init__(self): 
        self.pokedex       = 84.0                                 
        self.species       = "Doduo"                        
        self.nature        = self.generateNature()
        self.type          = ["Normal", "Flying"]                
       # self.level         = self.generateLevel(1, 30)           
        self.hp            = 35                                
        self.attack        = 85                              
        self.defense       = 45                                 
        self.spAtk         = 35
        self.spDef         = 35                             
        self.speed         = 75                                
        self.friend        = 70                                 
        self.gender        = self.generateGender(0)          
        self.abilities     = ["Run Away", "Early Bird"]                                
        self.ability       = ""                         
        self.hiddenAbility = "Tangled Feet"                       
        self.hidAbBool     = False
        
class dodrio(pokemon):                                      
    def __init__(self): 
        self.pokedex       = 85.0                                 
        self.species       = "Dodrio"                        
        self.nature        = self.generateNature()
        self.type          = ["Normal", "Flying"]                
       # self.level         = self.generateLevel(31, 100)           
        self.hp            = 60                                
        self.attack        = 110                              
        self.defense       = 70                                 
        self.spAtk         = 60
        self.spDef         = 60                             
        self.speed         = 110                                
        self.friend        = 70                                 
        self.gender        = self.generateGender(0)          
        self.abilities     = ["Run Away", "Early Bird"]                                 
        self.ability       = ""                         
        self.hiddenAbility = "Tangled Feet"                       
        self.hidAbBool     = False
        
class seel(pokemon):
    def __init__(self):
        self.pokedex       = 86.0
        self.species       = "Seel"
        self.nature        = self.generateNature()
        self.type          = ["Water"]
      #  self.level         = self.generateLevel(1, 33)
        self.hp            = 65
        self.attack        = 45
        self.defense       = 55
        self.spAtk         = 45
        self.spDef         = 70
        self.speed         = 45
        self.friend        = 70
        self.gender        = self.generateGender(50)
        self.abilities     = ["Thick Fat", "Hydration"]
        self.ability       = ""
        self.hiddenAbility = "Ice Body"
        self.hidAbBool     = False
        
class dewgong(pokemon):
    def __init__(self):
        self.pokedex       = 87.0
        self.species       = "Dewgong"
        self.nature        = self.generateNature()
        self.type          = ["Water", "Ice"]
      #  self.level         = self.generateLevel(34, 100)
        self.hp            = 90
        self.attack        = 70
        self.defense       = 80
        self.spAtk         = 70
        self.spDef         = 95
        self.speed         = 70
        self.friend        = 70
        self.gender        = self.generateGender(50)
        self.abilities     = ["Thick Fat", "Hydration"]
        self.ability       = ""
        self.hiddenAbility = "Ice Body"
        self.hidAbBool     = False
        
class grimer(pokemon):
    def __init__(self):
        self.pokedex       = 88.0
        self.species       = "Grimer"
        self.nature        = self.generateNature()
        self.type          = ["Poison"]
      #  self.level         = self.generateLevel(1, 37)
        self.hp            = 80
        self.attack        = 80
        self.defense       = 50
        self.spAtk         = 40
        self.spDef         = 50
        self.speed         = 25
        self.friend        = 70
        self.gender        = self.generateGender(50)
        self.abilities     = ["Stench", "Sticky Hold"]
        self.ability       = ""
        self.hiddenAbility = "Poison Touch"
        self.hidAbBool     = False
        
class alolanGrimer(pokemon):
    def __init__(self):
        self.pokedex       = 88.5
        self.species       = "Alolan Grimer"
        self.nature        = self.generateNature()
        self.type          = ["Poison", "Dark"]
      #  self.level         = self.generateLevel(1, 37)
        self.hp            = 80
        self.attack        = 80
        self.defense       = 50
        self.spAtk         = 40
        self.spDef         = 50
        self.speed         = 25
        self.friend        = 70
        self.gender        = self.generateGender(50)
        self.abilities     = ["Poison Touch", "Gluttony"]
        self.ability       = ""
        self.hiddenAbility = "Power of Alchemy"
        self.hidAbBool     = False
        
class muk(pokemon):
    def __init__(self):
        self.pokedex       = 89.0
        self.species       = "Muk"
        self.nature        = self.generateNature()
        self.type          = ["Poison"]
       # self.level         = self.generateLevel(38, 100)
        self.hp            = 105
        self.attack        = 105
        self.defense       = 75
        self.spAtk         = 65
        self.spDef         = 100
        self.speed         = 50
        self.friend        = 70
        self.gender        = self.generateGender(50)
        self.abilities     = ["Stench", "Sticky Hold"]
        self.ability       = ""
        self.hiddenAbility = "Poison Touch"
        self.hidAbBool     = False
        
class alolanMuk(pokemon):
    def __init__(self):
        self.pokedex       = 89.5
        self.species       = "Alolan Muk"
        self.nature        = self.generateNature()
        self.type          = ["Poison", "Dark"]
       # self.level         = self.generateLevel(38, 100)
        self.hp            = 105
        self.attack        = 105
        self.defense       = 75
        self.spAtk         = 65
        self.spDef         = 100
        self.speed         = 50
        self.friend        = 70
        self.gender        = self.generateGender(50)
        self.abilities     = ["Poison Touch", "Gluttony"]
        self.ability       = ""
        self.hiddenAbility = "Power of Alchemy"
        self.hidAbBool     = False
        
class shellder(pokemon):
    def __init__(self):
        self.pokedex       = 90.0
        self.species       = "Shellder"
        self.nature        = self.generateNature()
        self.type          = ["Water"]
      #  self.level         = self.generateLevel(1, 100)
        self.hp            = 30
        self.attack        = 65
        self.defense       = 100
        self.spAtk         = 45
        self.spDef         = 25
        self.speed         = 40
        self.friend        = 70
        self.gender        = self.generateGender(50)
        self.abilities     = ["Shell Armor", "Skill Link"]
        self.ability       = ""
        self.hiddenAbility = "Overcoat"
        self.hidAbBool     = False
        
class cloyster(pokemon):
    def __init__(self):
        self.pokedex       = 91.0
        self.species       = "Cloyster"
        self.nature        = self.generateNature()
        self.type          = ["Water", "Ice"]
      #  self.level         = self.generateLevel(1, 100)
        self.hp            = 50
        self.attack        = 95
        self.defense       = 180
        self.spAtk         = 85
        self.spDef         = 45
        self.speed         = 70
        self.friend        = 70
        self.gender        = self.generateGender(50)
        self.abilities     = ["Shell Armor", "Skill Link"]
        self.ability       = ""
        self.hiddenAbility = "Overcoat"
        self.hidAbBool     = False
        
class gastly(pokemon):
    def __init__(self):
        self.pokedex       = 92.0
        self.species       = "Gastly"
        self.nature        = self.generateNature()
        self.type          = ["Ghost", "Poison"]
     #   self.level         = self.generateLevel(1, 24)
        self.hp            = 30
        self.attack        = 35
        self.defense       = 30
        self.spAtk         = 100
        self.spDef         = 35
        self.speed         = 80
        self.friend        = 70
        self.gender        = self.generateGender(50)
        self.abilities     = []
        self.ability       = "Levitate"
        self.hiddenAbility = ""
        self.hidAbBool     = False
        
class haunter(pokemon):
    def __init__(self):
        self.pokedex       = 93.0
        self.species       = "Haunter"
        self.nature        = self.generateNature()
        self.type          = ["Ghost", "Poison"]
       # self.level         = self.generateLevel(25, 100)
        self.hp            = 45
        self.attack        = 50
        self.defense       = 45
        self.spAtk         = 115
        self.spDef         = 55
        self.speed         = 95
        self.friend        = 70
        self.gender        = self.generateGender(50)
        self.abilities     = []
        self.ability       = "Levitate"
        self.hiddenAbility = ""
        self.hidAbBool     = False
        
class gengar(pokemon):
    def __init__(self):
        self.pokedex       = 94.0
        self.species       = "Gengar"
        self.nature        = self.generateNature()
        self.type          = ["Ghost", "Poison"]
      #  self.level         = self.generateLevel(25, 100)
        self.hp            = 60
        self.attack        = 65
        self.defense       = 60
        self.spAtk         = 130
        self.spDef         = 75
        self.speed         = 110
        self.friend        = 70
        self.gender        = self.generateGender(50)
        self.abilities     = []
        self.ability       = "Cursed Body"
        self.hiddenAbility = ""
        self.hidAbBool     = False
        
class onix(pokemon):
    def __init__(self):
        self.pokedex       = 95.0
        self.species       = "Onix"
        self.nature        = self.generateNature()
        self.type          = ["Rock", "Ground"]
      #  self.level         = self.generateLevel(1, 100)
        self.hp            = 35
        self.attack        = 45
        self.defense       = 160
        self.spAtk         = 30
        self.spDef         = 45
        self.speed         = 70
        self.friend        = 70
        self.gender        = self.generateGender(50)
        self.abilities     = ["Rock Head", "Sturdy"]
        self.ability       = ""
        self.hiddenAbility = "Weak Armor"
        self.hidAbBool     = False
        
class drowzee(pokemon):
    def __init__(self):
        self.pokedex       = 96.0
        self.species       = "Drowzee"
        self.nature        = self.generateNature()
        self.type          = ["Psychic"]
      #  self.level         = self.generateLevel(1, 25)
        self.hp            = 60
        self.attack        = 48
        self.defense       = 45
        self.spAtk         = 43
        self.spDef         = 90
        self.speed         = 42
        self.friend        = 70
        self.gender        = self.generateGender(50)
        self.abilities     = ["Insomnia", "Forewarn"]
        self.ability       = ""
        self.hiddenAbility = "Inner Focus"
        self.hidAbBool     = False
        
class hypno(pokemon):
    def __init__(self):
        self.pokedex       = 97.0
        self.species       = "Hypno"
        self.nature        = self.generateNature()
        self.type          = ["Psychic"]
     #   self.level         = self.generateLevel(26, 100)
        self.hp            = 85
        self.attack        = 73
        self.defense       = 70
        self.spAtk         = 73
        self.spDef         = 115
        self.speed         = 67
        self.friend        = 70
        self.gender        = self.generateGender(50)
        self.abilities     = ["Insomnia", "Forewarn"]
        self.ability       = ""
        self.hiddenAbility = "Inner Focus"
        self.hidAbBool     = False
        
class krabby(pokemon):
    def __init__(self):
        self.pokedex       = 98.0
        self.species       = "Krabby"
        self.nature        = self.generateNature()
        self.type          = ["Water"]
     #   self.level         = self.generateLevel(1, 27)
        self.hp            = 30
        self.attack        = 105
        self.defense       = 90
        self.spAtk         = 25
        self.spDef         = 25
        self.speed         = 50
        self.friend        = 70
        self.gender        = self.generateGender(50)
        self.abilities     = ["Hyper Cutter", "Shell Armor"]
        self.ability       = ""
        self.hiddenAbility = "Sheer Force"
        self.hidAbBool     = False
        
class kingler(pokemon):
    def __init__(self):
        self.pokedex       = 99.0
        self.species       = "Kingler"
        self.nature        = self.generateNature()
        self.type          = ["Water"]
      #  self.level         = self.generateLevel(28, 100)
        self.hp            = 55
        self.attack        = 130
        self.defense       = 115
        self.spAtk         = 50
        self.spDef         = 50
        self.speed         = 75
        self.friend        = 70
        self.gender        = self.generateGender(50)
        self.abilities     = ["Hyper Cutter", "Shell Armor"]
        self.ability       = ""
        self.hiddenAbility = "Sheer Force"
        self.hidAbBool     = False
        
class voltorb(pokemon):
    def __init__(self):
        self.pokedex       = 100.0
        self.species       = "Voltorb"
        self.nature        = self.generateNature()
        self.type          = ["Electric"]
      #  self.level         = self.generateLevel(1, 29)
        self.hp            = 40
        self.attack        = 30
        self.defense       = 50
        self.spAtk         = 55
        self.spDef         = 55
        self.speed         = 100
        self.friend        = 70
        self.gender        = self.generateGender(0)
        self.abilities     = ["Soundproof", "Static"]
        self.ability       = ""
        self.hiddenAbility = "Aftermath"
        self.hidAbBool     = False
        
class electrode(pokemon):
    def __init__(self):
        self.pokedex       = 101.0
        self.species       = "Electrode"
        self.nature        = self.generateNature()
        self.type          = ["Electric"]
      #  self.level         = self.generateLevel(30, 100)
        self.hp            = 60
        self.attack        = 50
        self.defense       = 70
        self.spAtk         = 80
        self.spDef         = 80
        self.speed         = 150
        self.friend        = 70
        self.gender        = self.generateGender(0)
        self.abilities     = ["Soundproof", "Static"]
        self.ability       = ""
        self.hiddenAbility = "Aftermath"
        self.hidAbBool     = False
        
class exeggcute(pokemon):
    def __init__(self):
        self.pokedex       = 102.0
        self.species       = "Exeggcute"
        self.nature        = self.generateNature()
        self.type          = ["Grass", "Psychic"]
      #  self.level         = self.generateLevel(1, 100)
        self.hp            = 60
        self.attack        = 40
        self.defense       = 80
        self.spAtk         = 60
        self.spDef         = 45
        self.speed         = 40
        self.friend        = 70
        self.gender        = self.generateGender(50)
        self.abilities     = []
        self.ability       = "Chlorophyll"
        self.hiddenAbility = "Harvest"
        self.hidAbBool     = False
        
class exeggutor(pokemon):
    def __init__(self):
        self.pokedex       = 103.0
        self.species       = "Exeggutor"
        self.nature        = self.generateNature()
        self.type          = ["Grass", "Psychic"]
      #  self.level         = self.generateLevel(1, 100)
        self.hp            = 95
        self.attack        = 95
        self.defense       = 85
        self.spAtk         = 125
        self.spDef         = 75
        self.speed         = 55
        self.friend        = 70
        self.gender        = self.generateGender(50)
        self.abilities     = []
        self.ability       = "Chlorophyll"
        self.hiddenAbility = "Harvest"
        self.hidAbBool     = False
        
class alolanExeggutor(pokemon):
    def __init__(self):
        self.pokedex       = 103.5
        self.species       = "Alolan Exeggutor"
        self.nature        = self.generateNature()
        self.type          = ["Grass", "Dragon"]
      #  self.level         = self.generateLevel(1, 100)
        self.hp            = 95
        self.attack        = 105
        self.defense       = 85
        self.spAtk         = 125
        self.spDef         = 75
        self.speed         = 45
        self.friend        = 70
        self.gender        = self.generateGender(50)
        self.abilities     = []
        self.ability       = "Frisk"
        self.hiddenAbility = "Harvest"
        self.hidAbBool     = False
        
class cubone(pokemon):
    def __init__(self):
        self.pokedex       = 104.0
        self.species       = "Cubone"
        self.nature        = self.generateNature()
        self.type          = ["Ground"]
      #  self.level         = self.generateLevel(1, 27)
        self.hp            = 50
        self.attack        = 50
        self.defense       = 95
        self.spAtk         = 40
        self.spDef         = 50
        self.speed         = 35
        self.friend        = 70
        self.gender        = self.generateGender(50)
        self.abilities     = ["Rock Head", "Lightning Rod"]
        self.ability       = ""
        self.hiddenAbility = "Battle Armor"
        self.hidAbBool     = False
        
class marowak(pokemon):
    def __init__(self):
        self.pokedex       = 105.0
        self.species       = "Marowak"
        self.nature        = self.generateNature()
        self.type          = ["Ground"]
       # self.level         = self.generateLevel(28, 100)
        self.hp            = 60
        self.attack        = 80
        self.defense       = 110
        self.spAtk         = 50
        self.spDef         = 80
        self.speed         = 45
        self.friend        = 70
        self.gender        = self.generateGender(50)
        self.abilities     = ["Rock Head", "Lightning Rod"]
        self.ability       = ""
        self.hiddenAbility = "Battle Armor"
        self.hidAbBool     = False
        
class alolanMarowak(pokemon):
    def __init__(self):
        self.pokedex       = 105.5
        self.species       = "Alolan Marowak"
        self.nature        = self.generateNature()
        self.type          = ["Fire", "Ghost"]
       # self.level         = self.generateLevel(28, 100)
        self.hp            = 60
        self.attack        = 80
        self.defense       = 110
        self.spAtk         = 50
        self.spDef         = 80
        self.speed         = 45
        self.friend        = 70
        self.gender        = self.generateGender(50)
        self.abilities     = ["Cursed Body", "Lightning Rod"]
        self.ability       = ""
        self.hiddenAbility = "Rock Head"
        self.hidAbBool     = False
        
class hitmonlee(pokemon):
    def __init__(self):
        self.pokedex       = 106.0
        self.species       = "Hitmonlee"
        self.nature        = self.generateNature()
        self.type          = ["Fighting"]
      #  self.level         = self.generateLevel(20, 100)
        self.hp            = 50
        self.attack        = 120
        self.defense       = 53
        self.spAtk         = 35
        self.spDef         = 110
        self.speed         = 87
        self.friend        = 70
        self.gender        = self.generateGender(100)
        self.abilities     = ["Limber", "Reckless"]
        self.ability       = ""
        self.hiddenAbility = "Unburden"
        self.hidAbBool     = False
        
class hitmonchan(pokemon):
    def __init__(self):
        self.pokedex       = 107.0
        self.species       = "Hitmonchan"
        self.nature        = self.generateNature()
        self.type          = ["Fighting"]
      #  self.level         = self.generateLevel(20, 100)
        self.hp            = 50
        self.attack        = 105
        self.defense       = 79
        self.spAtk         = 35
        self.spDef         = 110
        self.speed         = 76
        self.friend        = 70
        self.gender        = self.generateGender(100)
        self.abilities     = ["Keen Eye", "Iron Fist"]
        self.ability       = ""
        self.hiddenAbility = "Inner Focus"
        self.hidAbBool     = False
        
class lickitung(pokemon):
    def __init__(self):
        self.pokedex       = 108.0
        self.species       = "Lickitung"
        self.nature        = self.generateNature()
        self.type          = ["Normal"]
      #  self.level         = self.generateLevel(1, 100)
        self.hp            = 90
        self.attack        = 55
        self.defense       = 75
        self.spAtk         = 60
        self.spDef         = 75
        self.speed         = 30
        self.friend        = 70
        self.gender        = self.generateGender(50)
        self.abilities     = ["Own Tempo", "Oblivious"]
        self.ability       = ""
        self.hiddenAbility = "Cloud Nine"
        self.hidAbBool     = False
        
class koffing(pokemon):
    def __init__(self):
        self.pokedex       = 109.0
        self.species       = "Koffing"
        self.nature        = self.generateNature()
        self.type          = ["Poison"]
       # self.level         = self.generateLevel(1, 34)
        self.hp            = 40
        self.attack        = 65
        self.defense       = 95
        self.spAtk         = 60
        self.spDef         = 45
        self.speed         = 35
        self.friend        = 70
        self.gender        = self.generateGender(50)
        self.abilities     = ["Levitate", "Neutralizing Gas"]
        self.ability       = ""
        self.hiddenAbility = "Stench"
        self.hidAbBool     = False
        
class weezing(pokemon):
    def __init__(self):
        self.pokedex       = 110.0
        self.species       = "Weezing"
        self.nature        = self.generateNature()
        self.type          = ["Poison"]
       # self.level         = self.generateLevel(35, 100)
        self.hp            = 65
        self.attack        = 90
        self.defense       = 120
        self.spAtk         = 85
        self.spDef         = 70
        self.speed         = 60
        self.friend        = 70
        self.gender        = self.generateGender(50)
        self.abilities     = ["Levitate", "Neutralizing Gas"]
        self.ability       = ""
        self.hiddenAbility = "Stench"
        self.hidAbBool     = False
        
class galarianWeezing(pokemon):
    def __init__(self):
        self.pokedex       = 110.75
        self.species       = "Galarian Weezing"
        self.nature        = self.generateNature()
        self.type          = ["Poison", "Fairy"]
       # self.level         = self.generateLevel(35, 100)
        self.hp            = 65
        self.attack        = 90
        self.defense       = 120
        self.spAtk         = 85
        self.spDef         = 70
        self.speed         = 60
        self.friend        = 70
        self.gender        = self.generateGender(50)
        self.abilities     = ["Levitate", "Neutralizing Gas"]
        self.ability       = ""
        self.hiddenAbility = "Misty Surge"
        self.hidAbBool     = False
        
class rhyhorn(pokemon):
    def __init__(self):
        self.pokedex       = 111.0
        self.species       = "Rhyhorn"
        self.nature        = self.generateNature()
        self.type          = ["Ground", "Rock"]
      #  self.level         = self.generateLevel(1, 41)
        self.hp            = 80
        self.attack        = 85
        self.defense       = 95
        self.spAtk         = 30
        self.spDef         = 30
        self.speed         = 25
        self.friend        = 70
        self.gender        = self.generateGender(50)
        self.abilities     = ["Lightning Rod", "Rock Head"]
        self.ability       = ""
        self.hiddenAbility = "Reckless"
        self.hidAbBool     = False
        
class rhydon(pokemon):
    def __init__(self):
        self.pokedex       = 112.0
        self.species       = "Rhydon"
        self.nature        = self.generateNature()
        self.type          = ["Ground", "Rock"]
      #  self.level         = self.generateLevel(42, 100)
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
        
class chansey(pokemon):
    def __init__(self):
        self.pokedex       = 113.0
        self.species       = "Chansey"
        self.nature        = self.generateNature()
        self.type          = ["Normal"]
       # self.level         = self.generateLevel(1, 100)
        self.hp            = 250
        self.attack        = 5
        self.defense       = 5
        self.spAtk         = 35
        self.spDef         = 105
        self.speed         = 50
        self.friend        = 140
        self.gender        = self.generateGender(0)
        self.abilities     = ["Natural Cure", "Serene Grace"]
        self.ability       = ""
        self.hiddenAbility = "Healer"
        self.hidAbBool     = False
        
class tangela(pokemon):
    def __init__(self):
        self.pokedex       = 114.0
        self.species       = "Tangela"
        self.nature        = self.generateNature()
        self.type          = ["Grass"]
       # self.level         = self.generateLevel(1, 100)
        self.hp            = 65
        self.attack        = 55
        self.defense       = 115
        self.spAtk         = 100
        self.spDef         = 40
        self.speed         = 60
        self.friend        = 70
        self.gender        = self.generateGender(50)
        self.abilities     = ["Chlorophyll", "Leaf Guard"]
        self.ability       = ""
        self.hiddenAbility = "Regenerator"
        self.hidAbBool     = False
        
class kangaskhan(pokemon):
    def __init__(self):
        self.pokedex       = 115.0
        self.species       = "Kangaskhan"
        self.nature        = self.generateNature()
        self.type          = ["Normal"]
      #  self.level         = self.generateLevel(1, 100)
        self.hp            = 105
        self.attack        = 95
        self.defense       = 80
        self.spAtk         = 40
        self.spDef         = 80
        self.speed         = 90
        self.friend        = 70
        self.gender        = self.generateGender(0)
        self.abilities     = ["Early Bird", "Scrappy"]
        self.ability       = ""
        self.hiddenAbility = "Inner Focus"
        self.hidAbBool     = False
        
class horsea(pokemon):
    def __init__(self):
        self.pokedex       = 116.0
        self.species       = "Horsea"
        self.nature        = self.generateNature()
        self.type          = ["Water"]
       # self.level         = self.generateLevel(1, 31)
        self.hp            = 30
        self.attack        = 40
        self.defense       = 70
        self.spAtk         = 70
        self.spDef         = 25
        self.speed         = 60
        self.friend        = 70
        self.gender        = self.generateGender(50)
        self.abilities     = ["Swift Swim", "Sniper"]
        self.ability       = ""
        self.hiddenAbility = "Damp"
        self.hidAbBool     = False
        
class seadra(pokemon):
    def __init__(self):
        self.pokedex       = 117.0
        self.species       = "Seadra"
        self.nature        = self.generateNature()
        self.type          = ["Water"]
        #self.level         = self.generateLevel(32, 100)
        self.hp            = 55
        self.attack        = 65
        self.defense       = 95
        self.spAtk         = 95
        self.spDef         = 45
        self.speed         = 85
        self.friend        = 70
        self.gender        = self.generateGender(50)
        self.abilities     = ["Poison Point", "Sniper"]
        self.ability       = ""
        self.hiddenAbility = "Damp"
        self.hidAbBool     = False
        
class goldeen(pokemon):
    def __init__(self):
        self.pokedex       = 118.0
        self.species       = "Goldeen"
        self.nature        = self.generateNature()
        self.type          = ["Water"]
      #  self.level         = self.generateLevel(1, 32)
        self.hp            = 45
        self.attack        = 67
        self.defense       = 60
        self.spAtk         = 35
        self.spDef         = 50
        self.speed         = 63
        self.friend        = 70
        self.gender        = self.generateGender(50)
        self.abilities     = ["Swift Swim", "Water Veil"]
        self.ability       = ""
        self.hiddenAbility = "Lightning Rod"
        self.hidAbBool     = False
        
class seaking(pokemon):
    def __init__(self):
        self.pokedex       = 119.0
        self.species       = "Seaking"
        self.nature        = self.generateNature()
        self.type          = ["Water"]
       # self.level         = self.generateLevel(33, 100)
        self.hp            = 80
        self.attack        = 92
        self.defense       = 65
        self.spAtk         = 65
        self.spDef         = 80
        self.speed         = 68
        self.friend        = 70
        self.gender        = self.generateGender(50)
        self.abilities     = ["Swift Swim", "Water Veil"]
        self.ability       = ""
        self.hiddenAbility = "Lightning Rod"
        self.hidAbBool     = False
        
class staryu(pokemon):
    def __init__(self):
        self.pokedex       = 120.0
        self.species       = "Staryu"
        self.nature        = self.generateNature()
        self.type          = ["Water"]
       # self.level         = self.generateLevel(1, 100)
        self.hp            = 30
        self.attack        = 45
        self.defense       = 55
        self.spAtk         = 70
        self.spDef         = 55
        self.speed         = 85
        self.friend        = 70
        self.gender        = self.generateGender(0)
        self.abilities     = ["Illuminate", "Natural Cure"]
        self.ability       = ""
        self.hiddenAbility = "Analytic"
        self.hidAbBool     = False
        
class starmie(pokemon):
    def __init__(self):
        self.pokedex       = 121.0
        self.species       = "Starmie"
        self.nature        = self.generateNature()
        self.type          = ["Water", "Psychic"]
       # self.level         = self.generateLevel(1, 100)
        self.hp            = 60
        self.attack        = 75
        self.defense       = 85
        self.spAtk         = 100
        self.spDef         = 85
        self.speed         = 115
        self.friend        = 70
        self.gender        = self.generateGender(0)
        self.abilities     = ["Illuminate", "Natural Cure"]
        self.ability       = ""
        self.hiddenAbility = "Analytic"
        self.hidAbBool     = False
        
class mrMime(pokemon):
    def __init__(self):
        self.pokedex       = 122.0
        self.species       = "Mr. Mime"
        self.nature        = self.generateNature()
        self.type          = ["Psychic", "Fairy"]
      #  self.level         = self.generateLevel(1, 100)
        self.hp            = 40
        self.attack        = 45
        self.defense       = 65
        self.spAtk         = 100
        self.spDef         = 120
        self.speed         = 90
        self.friend        = 70
        self.gender        = self.generateGender(50)
        self.abilities     = ["Soundproof", "Filter"]
        self.ability       = ""
        self.hiddenAbility = "Technician"
        self.hidAbBool     = False
        
class galarianMrMime(pokemon):
    def __init__(self):
        self.pokedex       = 122.75
        self.species       = "Galarian Mr. Mime"
        self.nature        = self.generateNature()
        self.type          = ["Ice", "Psychic"]
     #   self.level         = self.generateLevel(1, 41)
        self.hp            = 50
        self.attack        = 65
        self.defense       = 65
        self.spAtk         = 90
        self.spDef         = 90
        self.speed         = 100
        self.friend        = 70
        self.gender        = self.generateGender(50)
        self.abilities     = ["Vital Spirit", "Screen Cleaner"]
        self.ability       = ""
        self.hiddenAbility = "Ice Body"
        self.hidAbBool     = False
        
class sycther(pokemon):
    def __init__(self):
        self.pokedex       = 123.0
        self.species       = "Scyther"
        self.nature        = self.generateNature()
        self.type          = ["Bug", "Flying"]
      #  self.level         = self.generateLevel(1, 100)
        self.hp            = 70
        self.attack        = 110
        self.defense       = 80
        self.spAtk         = 55
        self.spDef         = 80
        self.speed         = 105
        self.friend        = 70
        self.gender        = self.generateGender(50)
        self.abilities     = ["Swarm", "Technician"]
        self.ability       = ""
        self.hiddenAbility = "Steadfast"
        self.hidAbBool     = False
        
class jynx(pokemon):
    def __init__(self):
        self.pokedex       = 124.0
        self.species       = "Jynx"
        self.nature        = self.generateNature()
        self.type          = ["Ice", "Psychic"]
      #  self.level         = self.generateLevel(1, 29)
        self.hp            = 65
        self.attack        = 50
        self.defense       = 35
        self.spAtk         = 115
        self.spDef         = 95
        self.speed         = 95
        self.friend        = 70
        self.gender        = self.generateGender(0)
        self.abilities     = ["Oblivious", "Forewarn"]
        self.ability       = ""
        self.hiddenAbility = "Dry Skin"
        self.hidAbBool     = False
        
class electabuzz(pokemon):
    def __init__(self):
        self.pokedex       = 125.0
        self.species       = "Electabuzz"
        self.nature        = self.generateNature()
        self.type          = ["Electric"]
      #  self.level         = self.generateLevel(30, 100)
        self.hp            = 65
        self.attack        = 83
        self.defense       = 57
        self.spAtk         = 95
        self.spDef         = 85
        self.speed         = 105
        self.friend        = 70
        self.gender        = self.generateGender(75)
        self.abilities     = []
        self.ability       = "Static"
        self.hiddenAbility = "Vital Spirit"
        self.hidAbBool     = False
        
class magmar(pokemon):
    def __init__(self):
        self.pokedex       = 126.0
        self.species       = "Magmar"
        self.nature        = self.generateNature()
        self.type          = ["Fire"]
      #  self.level         = self.generateLevel(30, 100)
        self.hp            = 65
        self.attack        = 95
        self.defense       = 57
        self.spAtk         = 100
        self.spDef         = 85
        self.speed         = 93
        self.friend        = 70
        self.gender        = self.generateGender(75)
        self.abilities     = []
        self.ability       = "Flame Body"
        self.hiddenAbility = "Vital Spirit"
        self.hidAbBool     = False
        
class pinsir(pokemon):
    def __init__(self):
        self.pokedex       = 127.0
        self.species       = "Pinsir"
        self.nature        = self.generateNature()
        self.type          = ["Bug"]
     #   self.level         = self.generateLevel(1, 100)
        self.hp            = 65
        self.attack        = 125
        self.defense       = 100
        self.spAtk         = 55
        self.spDef         = 70
        self.speed         = 85
        self.friend        = 70
        self.gender        = self.generateGender(50)
        self.abilities     = ["Hyper Cutter", "Mold Breaker"]
        self.ability       = ""
        self.hiddenAbility = "Moxie"
        self.hidAbBool     = False
        
class tauros(pokemon):
    def __init__(self):
        self.pokedex       = 128.0
        self.species       = "Pinsir"
        self.nature        = self.generateNature()
        self.type          = ["Normal"]
     #   self.level         = self.generateLevel(1, 100)
        self.hp            = 75
        self.attack        = 100
        self.defense       = 95
        self.spAtk         = 40
        self.spDef         = 70
        self.speed         = 110
        self.friend        = 70
        self.gender        = self.generateGender(100)
        self.abilities     = ["Intimidate", "Anger Point"]
        self.ability       = ""
        self.hiddenAbility = "Sheer Force"
        self.hidAbBool     = False
        
class magikarp(pokemon):
    def __init__(self):
        self.pokedex       = 129.0
        self.species       = "Magikarp"
        self.nature        = self.generateNature()
        self.type          = ["Water"]
      #  self.level         = self.generateLevel(1, 19)
        self.hp            = 20
        self.attack        = 10
        self.defense       = 55
        self.spAtk         = 15
        self.spDef         = 20
        self.speed         = 80
        self.friend        = 70
        self.gender        = self.generateGender(50)
        self.abilities     = []
        self.ability       = "Swift Swim"
        self.hiddenAbility = "Rattled"
        self.hidAbBool     = False
        
class gyarados(pokemon):
    def __init__(self):
        self.pokedex       = 130.0
        self.species       = "Gyarados"
        self.nature        = self.generateNature()
        self.type          = ["Water", "Flying"]
     #   self.level         = self.generateLevel(20, 100)
        self.hp            = 95
        self.attack        = 125
        self.defense       = 79
        self.spAtk         = 60
        self.spDef         = 100
        self.speed         = 81
        self.friend        = 70
        self.gender        = self.generateGender(50)
        self.abilities     = []
        self.ability       = "Intimidate"
        self.hiddenAbility = "Moxie"
        self.hidAbBool     = False
        
class lapras(pokemon):
    def __init__(self):
        self.pokedex       = 131.0
        self.species       = "Lapras"
        self.nature        = self.generateNature()
        self.type          = ["Water", "Ice"]
     #   self.level         = self.generateLevel(1, 100)
        self.hp            = 135
        self.attack        = 85
        self.defense       = 80
        self.spAtk         = 85
        self.spDef         = 95
        self.speed         = 60
        self.friend        = 70
        self.gender        = self.generateGender(50)
        self.abilities     = ["Water Absorb", "Shell Armor"]
        self.ability       = ""
        self.hiddenAbility = "Hydration"
        self.hidAbBool     = False
       
class ditto(pokemon):
    def __init__(self):
        self.pokedex       = 132.0
        self.species       = "Ditto"
        self.nature        = self.generateNature()
        self.type          = ["Normal"]
    #    self.level         = self.generateLevel(1, 100)
        self.hp            = 48
        self.attack        = 48
        self.defense       = 48
        self.spAtk         = 48
        self.spDef         = 48
        self.speed         = 48
        self.friend        = 70
        self.gender        = self.generateGender(0)
        self.abilities     = []
        self.ability       = "Limber"
        self.hiddenAbility = "Imposter"
        self.hidAbBool     = False
        
class eevee(pokemon):
    def __init__(self):
        self.pokedex       = 133.0
        self.species       = "Eevee"
        self.nature        = self.generateNature()
        self.type          = ["Normal"]
    #    self.level         = self.generateLevel(1, 100)
        self.hp            = 55
        self.attack        = 55
        self.defense       = 50
        self.spAtk         = 45
        self.spDef         = 65
        self.speed         = 55
        self.friend        = 70
        self.gender        = self.generateGender(87.5)
        self.abilities     = ["Run Away", "Adaptability"]
        self.ability       = ""
        self.hiddenAbility = "Anticipation"
        self.hidAbBool     = False
        
class vaporeon(pokemon):
    def __init__(self):
        self.pokedex       = 134.0
        self.species       = "Vaporeon"
        self.nature        = self.generateNature()
        self.type          = ["Water"]
   #     self.level         = self.generateLevel(1, 100)
        self.hp            = 130
        self.attack        = 65
        self.defense       = 60
        self.spAtk         = 110
        self.spDef         = 95
        self.speed         = 65
        self.friend        = 70
        self.gender        = self.generateGender(87.5)
        self.abilities     = []
        self.ability       = "Water Absorb"
        self.hiddenAbility = "Hydration"
        self.hidAbBool     = False
        
class jolteon(pokemon):
    def __init__(self):
        self.pokedex       = 135.0
        self.species       = "Jolteon"
        self.nature        = self.generateNature()
        self.type          = ["Electric"]
    #    self.level         = self.generateLevel(1, 100)
        self.hp            = 65
        self.attack        = 65
        self.defense       = 60
        self.spAtk         = 110
        self.spDef         = 95
        self.speed         = 130
        self.friend        = 70
        self.gender        = self.generateGender(87.5)
        self.abilities     = []
        self.ability       = "Volt Absorb"
        self.hiddenAbility = "Quick Feet"
        self.hidAbBool     = False
        
class flareon(pokemon):
    def __init__(self):
        self.pokedex       = 136.0
        self.species       = "Flareon"
        self.nature        = self.generateNature()
        self.type          = ["Fire"]
     #   self.level         = self.generateLevel(1, 100)
        self.hp            = 65
        self.attack        = 130
        self.defense       = 60
        self.spAtk         = 95
        self.spDef         = 110
        self.speed         = 65
        self.friend        = 70
        self.gender        = self.generateGender(87.5)
        self.abilities     = []
        self.ability       = "Flash Fire"
        self.hiddenAbility = "Guts"
        self.hidAbBool     = False
        
class porygon(pokemon):
    def __init__(self):
        self.pokedex       = 137.0
        self.species       = "Porygon"
        self.nature        = self.generateNature()
        self.type          = ["Normal"]
      #  self.level         = self.generateLevel(1, 100)
        self.hp            = 65
        self.attack        = 60
        self.defense       = 70
        self.spAtk         = 85
        self.spDef         = 75
        self.speed         = 40
        self.friend        = 70
        self.gender        = self.generateGender(0)
        self.abilities     = ["Trace", "Download"]
        self.ability       = ""
        self.hiddenAbility = "Analytic"
        self.hidAbBool     = False
        
class omanyte(pokemon):
    def __init__(self):
        self.pokedex       = 138.0
        self.species       = "Omanyte"
        self.nature        = self.generateNature()
        self.type          = ["Rock", "Water"]
     #   self.level         = self.generateLevel(1, 39)
        self.hp            = 35
        self.attack        = 40
        self.defense       = 100
        self.spAtk         = 90
        self.spDef         = 55
        self.speed         = 35
        self.friend        = 70
        self.gender        = self.generateGender(87.5)
        self.abilities     = ["Swift Swim", "Shell Armor"]
        self.ability       = ""
        self.hiddenAbility = "Weak Armor"
        self.hidAbBool     = False
        
class omastar(pokemon):
    def __init__(self):
        self.pokedex       = 139.0
        self.species       = "Omastar"
        self.nature        = self.generateNature()
        self.type          = ["Rock", "Water"]
       # self.level         = self.generateLevel(40, 100)
        self.hp            = 70
        self.attack        = 60
        self.defense       = 125
        self.spAtk         = 115
        self.spDef         = 70
        self.speed         = 55
        self.friend        = 70
        self.gender        = self.generateGender(87.5)
        self.abilities     = ["Swift Swim", "Shell Armor"]
        self.ability       = ""
        self.hiddenAbility = "Weak Armor"
        self.hidAbBool     = False
        
class kabuto(pokemon):
    def __init__(self):
        self.pokedex       = 140.0
        self.species       = "Kabuto"
        self.nature        = self.generateNature()
        self.type          = ["Rock", "Water"]
     #   self.level         = self.generateLevel(1, 39)
        self.hp            = 30
        self.attack        = 80
        self.defense       = 90
        self.spAtk         = 55
        self.spDef         = 45
        self.speed         = 55
        self.friend        = 70
        self.gender        = self.generateGender(87.5)
        self.abilities     = ["Swift Swim", "Battle Armor"]
        self.ability       = ""
        self.hiddenAbility = "Weak Armor"
        self.hidAbBool     = False
        
class kabutops(pokemon):
    def __init__(self):
        self.pokedex       = 141.0
        self.species       = "Kabutops"
        self.nature        = self.generateNature()
        self.type          = ["Rock", "Water"]
     #   self.level         = self.generateLevel(40, 100)
        self.hp            = 60
        self.attack        = 115
        self.defense       = 105
        self.spAtk         = 65
        self.spDef         = 70
        self.speed         = 80
        self.friend        = 70
        self.gender        = self.generateGender(87.5)
        self.abilities     = ["Swift Swim", "Battle Armor"]
        self.ability       = ""
        self.hiddenAbility = "Weak Armor"
        self.hidAbBool     = False
        
class aerodactyl(pokemon):
    def __init__(self):
        self.pokedex       = 142.0
        self.species       = "Aerodactyl"
        self.nature        = self.generateNature()
        self.type          = ["Rock", "Flying"]
      #  self.level         = self.generateLevel(1, 100)
        self.hp            = 80
        self.attack        = 105
        self.defense       = 65
        self.spAtk         = 60
        self.spDef         = 75
        self.speed         = 130
        self.friend        = 70
        self.gender        = self.generateGender(87.5)
        self.abilities     = ["Rock Head", "Pressure"]
        self.ability       = ""
        self.hiddenAbility = "Unnerve"
        self.hidAbBool     = False
        
class snorlax(pokemon):
    def __init__(self):
        self.pokedex       = 143.0
        self.species       = "Snorlax"
        self.nature        = self.generateNature()
        self.type          = ["Rock", "Flying"]
     #   self.level         = self.generateLevel(1, 100)
        self.hp            = 160
        self.attack        = 110
        self.defense       = 65
        self.spAtk         = 65
        self.spDef         = 110
        self.speed         = 30
        self.friend        = 70
        self.gender        = self.generateGender(87.5)
        self.abilities     = ["Immunity", "Thick Fat"]
        self.ability       = ""
        self.hiddenAbility = "Gluttony"
        self.hidAbBool     = False
        
class articuno(pokemon):
    def __init__(self):
        self.pokedex       = 144.0
        self.species       = "Articuno"
        self.nature        = self.generateNature()
        self.type          = ["Ice", "Flying"]
       # self.level         = self.generateLevel(1, 100)
        self.hp            = 90
        self.attack        = 85
        self.defense       = 100
        self.spAtk         = 95
        self.spDef         = 125
        self.speed         = 85
        self.friend        = 70
        self.gender        = self.generateGender(0)              
        self.abilities     = [""]
        self.ability       = "Pressure"
        self.hiddenAbility = "Snow Cloak"
        self.hidAbBool     = False
        
class zapdos(pokemon):
    def __init__(self):
        self.pokedex       = 145.0
        self.species       = "Zapdos"
        self.nature        = self.generateNature()
        self.type          = ["Electric", "Flying"]
      #  self.level         = self.generateLevel(1, 100)
        self.hp            = 90
        self.attack        = 90
        self.defense       = 85
        self.spAtk         = 125
        self.spDef         = 90
        self.speed         = 100
        self.friend        = 70
        self.gender        = self.generateGender(0)              
        self.abilities     = [""]
        self.ability       = "Pressure"
        self.hiddenAbility = "Static"
        self.hidAbBool     = False
        
class moltres(pokemon):
    def __init__(self):
        self.pokedex       = 146.0
        self.species       = "Moltres"
        self.nature        = self.generateNature()
        self.type          = ["Fire", "Flying"]
       # self.level         = self.generateLevel(1, 100)
        self.hp            = 90
        self.attack        = 100
        self.defense       = 90
        self.spAtk         = 125
        self.spDef         = 85
        self.speed         = 90
        self.friend        = 70
        self.gender        = self.generateGender(0)              
        self.abilities     = [""]
        self.ability       = "Pressure"
        self.hiddenAbility = "Flame Body"
        self.hidAbBool     = False
        
class dratini(pokemon):
    def __init__(self):
        self.pokedex       = 147.0
        self.species       = "Dratini"
        self.nature        = self.generateNature()
        self.type          = ["Dragon"]
      #  self.level         = self.generateLevel(1, 29)
        self.hp            = 41
        self.attack        = 64
        self.defense       = 45
        self.spAtk         = 50
        self.spDef         = 50
        self.speed         = 50
        self.friend        = 35
        self.gender        = self.generateGender(50)
        self.abilities     = []
        self.ability       = "Shed Skin"
        self.hiddenAbility = "Marvel Scale"
        self.hidAbBool     = False
        
class dragonair(pokemon):
    def __init__(self):
        self.pokedex       = 148.0
        self.species       = "Dragonair"
        self.nature        = self.generateNature()
        self.type          = ["Dragon"]
      #  self.level         = self.generateLevel(30, 54)
        self.hp            = 61
        self.attack        = 84
        self.defense       = 65
        self.spAtk         = 70
        self.spDef         = 70
        self.speed         = 70
        self.friend        = 35
        self.gender        = self.generateGender(50)
        self.abilities     = []
        self.ability       = "Shed Skin"
        self.hiddenAbility = "Marvel Scale"
        self.hidAbBool     = False
        
    def __init__(self):
        self.pokedex       = 149.0
        self.species       = "Dragonite"
        self.nature        = self.generateNature()
        self.type          = ["Dragon", "Flying"]
       # self.level         = self.generateLevel(55, 100)
        self.hp            = 91
        self.attack        = 134
        self.defense       = 95
        self.spAtk         = 100
        self.spDef         = 100
        self.speed         = 80
        self.friend        = 35
        self.gender        = self.generateGender(50)
        self.abilities     = []
        self.ability       = "Inner Focus"
        self.hiddenAbility = "Multiscale"
        self.hidAbBool     = False

        
class mewtwo(pokemon):
    def __init__(self):
        self.pokedex       = 150.0
        self.species       = "Mewtwo"
        self.nature        = self.generateNature()
        self.type          = ["Psychic"]
      #  self.level         = self.generateLevel(1, 100)
        self.hp            = 106
        self.attack        = 110
        self.defense       = 90
        self.spAtk         = 154
        self.spDef         = 90
        self.speed         = 130
        self.friend        = 70
        self.gender        = self.generateGender(0)              
        self.abilities     = [""]
        self.ability       = "Pressure"
        self.hiddenAbility = "Unnerve"
        self.hidAbBool     = False

class mew(pokemon):
    def __init__(self):
        self.pokedex       = 151.0
        self.species       = "Mew"
        self.nature        = self.generateNature()
        self.type          = ["Psychic"]
      #  self.level         = self.generateLevel(1, 100)
        self.hp            = 100
        self.attack        = 100
        self.defense       = 100
        self.spAtk         = 100
        self.spDef         = 100
        self.speed         = 100
        self.friend        = 70
        self.gender        = self.generateGender(0)              
        self.abilities     = [""]
        self.ability       = "Synchronize"
        self.hiddenAbility = ""
        self.hidAbBool     = False

class chikorita(pokemon):
    def __init__(self):
        self.pokedex       = 152.0
        self.species       = "Chikorita"
        self.nature        = self.generateNature()
        self.type          = ["Grass"]
        #self.maxLevel      = 16
        #self.level         = self.generateLevel(1, self.maxLevel - 1)
        self.hp            = 45
        self.attack        = 49
        self.defense       = 65
        self.spAtk         = 49
        self.spDef         = 65
        self.speed         = 45
        self.friend        = 70
        self.gender        = self.generateGender(87.5)
        self.abilities     = []
        self.ability       = "Overgrow"
        self.hiddenAbility = "Leaf Guard"
        self.hidAbBool     = False
        
class bayleef(pokemon):
    def __init__(self):
        self.pokedex       = 153.0
        self.species       = "Bayleef"
        self.nature        = self.generateNature()
        self.type          = ["Grass"]
      # self.maxLevel      = 16
       # self.level         = self.generateLevel(1, self.maxLevel - 1)
        self.hp            = 60
        self.attack        = 62
        self.defense       = 80
        self.spAtk         = 63
        self.spDef         = 80
        self.speed         = 60
        self.friend        = 70
        self.gender        = self.generateGender(87.5)
        self.abilities     = []
        self.ability       = "Overgrow"
        self.hiddenAbility = "Leaf Guard"
        self.hidAbBool     = False
        
class meganium(pokemon):
    def __init__(self):
        self.pokedex       = 154.0
        self.species       = "Meganium"
        self.nature        = self.generateNature()
        self.type          = ["Grass"]
      # self.maxLevel      = 16
       # self.level         = self.generateLevel(1, self.maxLevel - 1)
        self.hp            = 80
        self.attack        = 82
        self.defense       = 100
        self.spAtk         = 83
        self.spDef         = 100
        self.speed         = 80
        self.friend        = 70
        self.gender        = self.generateGender(87.5)
        self.abilities     = []
        self.ability       = "Overgrow"
        self.hiddenAbility = "Leaf Guard"
        self.hidAbBool     = False

class cyndaquil(pokemon):
    def __init__(self):
        self.pokedex       = 155.0
        self.species       = "Cyndaquil"
        self.nature        = self.generateNature()
        self.type          = ["Fire"]
       # self.maxLevel      = 14
       # self.level         = self.generateLevel(1, self.maxLevel - 1)
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
        self.hiddenAbility = "Flash Fire"
        self.hidAbBool     = False
        
class quilava(pokemon):
    def __init__(self):
        self.pokedex       = 156.0
        self.species       = "Quilava"
        self.nature        = self.generateNature()
        self.type          = ["Fire"]
      # self.maxLevel      = 16
       # self.level         = self.generateLevel(1, self.maxLevel - 1)
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
        self.hiddenAbility = "Flash Fire"
        self.hidAbBool     = False
        
class typhlosion(pokemon):
    def __init__(self):
        self.pokedex       = 157.0
        self.species       = "Typhlosion"
        self.nature        = self.generateNature()
        self.type          = ["Fire"]
      # self.maxLevel      = 16
       # self.level         = self.generateLevel(1, self.maxLevel - 1)
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
        self.hiddenAbility = "Flash Fire"
        self.hidAbBool     = False

class totodile(pokemon):
    def __init__(self):
        self.pokedex       = 158.0
        self.species       = "Totodile"
        self.nature        = self.generateNature()
        self.type          = ["Water"]
      #  self.maxLevel      = 18
       # self.level         = self.generateLevel(1, self.maxLevel - 1)
        self.hp            = 50
        self.attack        = 65
        self.defense       = 64
        self.spAtk         = 44
        self.spDef         = 48
        self.speed         = 43
        self.friend        = 70
        self.gender        = self.generateGender(87.5)
        self.abilities     = []
        self.ability       = "Torrent"
        self.hiddenAbility = "Sheer Force"
        self.hidAbBool     = False
        
class croconaw(pokemon):
    def __init__(self):
        self.pokedex       = 159.0
        self.species       = "Croconaw"
        self.nature        = self.generateNature()
        self.type          = ["Water"]
      #  self.maxLevel      = 18
       # self.level         = self.generateLevel(1, self.maxLevel - 1)
        self.hp            = 65
        self.attack        = 80
        self.defense       = 80
        self.spAtk         = 59
        self.spDef         = 63
        self.speed         = 58
        self.friend        = 70
        self.gender        = self.generateGender(87.5)
        self.abilities     = []
        self.ability       = "Torrent"
        self.hiddenAbility = "Sheer Force"
        self.hidAbBool     = False
        
class feraligatr(pokemon):
    def __init__(self):
        self.pokedex       = 160.0
        self.species       = "Feraligatr"
        self.nature        = self.generateNature()
        self.type          = ["Water"]
      #  self.maxLevel      = 18
       # self.level         = self.generateLevel(1, self.maxLevel - 1)
        self.hp            = 85
        self.attack        = 105
        self.defense       = 100
        self.spAtk         = 79
        self.spDef         = 83
        self.speed         = 78
        self.friend        = 70
        self.gender        = self.generateGender(87.5)
        self.abilities     = []
        self.ability       = "Torrent"
        self.hiddenAbility = "Sheer Force"
        self.hidAbBool     = False
        
class sentret(pokemon):
    def __init__(self):
        self.pokedex       = 161.0
        self.species       = "sentret"
        self.nature        = self.generateNature()
        self.type          = ["Normal"]
      #  self.maxLevel      = 18
       # self.level         = self.generateLevel(1, self.maxLevel - 1)
        self.hp            = 35
        self.attack        = 46
        self.defense       = 34
        self.spAtk         = 35
        self.spDef         = 45
        self.speed         = 20
        self.friend        = 70
        self.gender        = self.generateGender(50)
        self.abilities     = ["Run Away", "Keen Eye"]
        self.ability       = ""
        self.hiddenAbility = "Frisk"
        self.hidAbBool     = False
        
class furret(pokemon):
    def __init__(self):
        self.pokedex       = 162.0
        self.species       = "Furret"
        self.nature        = self.generateNature()
        self.type          = ["Normal"]
      #  self.maxLevel      = 18
       # self.level         = self.generateLevel(1, self.maxLevel - 1)
        self.hp            = 85
        self.attack        = 76
        self.defense       = 64
        self.spAtk         = 45
        self.spDef         = 55
        self.speed         = 90
        self.friend        = 70
        self.gender        = self.generateGender(50)
        self.abilities     = ["Run Away", "Keen Eye"]
        self.ability       = ""
        self.hiddenAbility = "Frisk"
        self.hidAbBool     = False
       
class hoothoot(pokemon):
    def __init__(self):
        self.pokedex       = 163.0
        self.species       = "Hoothoot"
        self.nature        = self.generateNature()
        self.type          = ["Normal", "Flying"]
      #  self.maxLevel      = 18
       # self.level         = self.generateLevel(1, self.maxLevel - 1)
        self.hp            = 60
        self.attack        = 30
        self.defense       = 30
        self.spAtk         = 36
        self.spDef         = 56
        self.speed         = 50
        self.friend        = 70
        self.gender        = self.generateGender(50)
        self.abilities     = ["Insomnia", "Keen Eye"]
        self.ability       = ""
        self.hiddenAbility = "Tinted Lens"
        self.hidAbBool     = False
        
class noctowl(pokemon):
    def __init__(self):
        self.pokedex       = 164.0
        self.species       = "Noctowl"
        self.nature        = self.generateNature()
        self.type          = ["Normal", "Flying"]
      #  self.maxLevel      = 18
       # self.level         = self.generateLevel(1, self.maxLevel - 1)
        self.hp            = 100
        self.attack        = 50
        self.defense       = 50
        self.spAtk         = 76
        self.spDef         = 96
        self.speed         = 70
        self.friend        = 70
        self.gender        = self.generateGender(50)
        self.abilities     = ["Insomnia", "Keen Eye"]
        self.ability       = ""
        self.hiddenAbility = "Tinted Lens"
        self.hidAbBool     = False
        
class ledyba(pokemon):
    def __init__(self):
        self.pokedex       = 165.0
        self.species       = "Ledyba"
        self.nature        = self.generateNature()
        self.type          = ["Bug", "Flying"]
      #  self.maxLevel      = 18
       # self.level         = self.generateLevel(1, self.maxLevel - 1)
        self.hp            = 40
        self.attack        = 20
        self.defense       = 30
        self.spAtk         = 40
        self.spDef         = 80
        self.speed         = 55
        self.friend        = 70
        self.gender        = self.generateGender(50)
        self.abilities     = ["Swarm", "Early Bird"]
        self.ability       = ""
        self.hiddenAbility = "Rattled"
        self.hidAbBool     = False
        
class ledian(pokemon):
    def __init__(self):
        self.pokedex       = 166.0
        self.species       = "Ledian"
        self.nature        = self.generateNature()
        self.type          = ["Bug", "Flying"]
      #  self.maxLevel      = 18
       # self.level         = self.generateLevel(1, self.maxLevel - 1)
        self.hp            = 55
        self.attack        = 35
        self.defense       = 50
        self.spAtk         = 55
        self.spDef         = 110
        self.speed         = 85
        self.friend        = 70
        self.gender        = self.generateGender(50)
        self.abilities     = ["Swarm", "Early Bird"]
        self.ability       = ""
        self.hiddenAbility = "Iron Fist"
        self.hidAbBool     = False
        
class spinarak(pokemon):
    def __init__(self):
        self.pokedex       = 167.0
        self.species       = "Spinarak"
        self.nature        = self.generateNature()
        self.type          = ["Bug", "Poison"]
      #  self.maxLevel      = 18
       # self.level         = self.generateLevel(1, self.maxLevel - 1)
        self.hp            = 40
        self.attack        = 60
        self.defense       = 40
        self.spAtk         = 40
        self.spDef         = 40
        self.speed         = 30
        self.friend        = 70
        self.gender        = self.generateGender(50)
        self.abilities     = ["Swarm", "Insomnia"]
        self.ability       = ""
        self.hiddenAbility = "Sniper"
        self.hidAbBool     = False

class ariados(pokemon):
    def __init__(self):
        self.pokedex       = 168.0
        self.species       = "Ariados"
        self.nature        = self.generateNature()
        self.type          = ["Bug", "Poison"]
      #  self.maxLevel      = 18
       # self.level         = self.generateLevel(1, self.maxLevel - 1)
        self.hp            = 70
        self.attack        = 90
        self.defense       = 70
        self.spAtk         = 60
        self.spDef         = 60
        self.speed         = 40
        self.friend        = 70
        self.gender        = self.generateGender(50)
        self.abilities     = ["Swarm", "Insomnia"]
        self.ability       = ""
        self.hiddenAbility = "Sniper"
        self.hidAbBool     = False
        
class crobat(pokemon):
    def __init__(self):
        self.pokedex       = 169.0
        self.species       = "Crobat"
        self.nature        = self.generateNature()
        self.type          = ["Poison", "Flying"]
      #  self.maxLevel      = 18
       # self.level         = self.generateLevel(1, self.maxLevel - 1)
        self.hp            = 85
        self.attack        = 90
        self.defense       = 80
        self.spAtk         = 70
        self.spDef         = 80
        self.speed         = 130
        self.friend        = 70
        self.gender        = self.generateGender(50)
        self.abilities     = [""]
        self.ability       = "Inner Focus"
        self.hiddenAbility = "Infiltrator"
        self.hidAbBool     = False
        
class chinchou(pokemon):
    def __init__(self):
        self.pokedex       = 170.0
        self.species       = "Chinchou"
        self.nature        = self.generateNature()
        self.type          = ["Water", "Electric"]
      #  self.maxLevel      = 18
       # self.level         = self.generateLevel(1, self.maxLevel - 1)
        self.hp            = 75
        self.attack        = 38
        self.defense       = 38
        self.spAtk         = 56
        self.spDef         = 56
        self.speed         = 67
        self.friend        = 70
        self.gender        = self.generateGender(50)
        self.abilities     = ["Volt Absorb", "Illuminate"]
        self.ability       = ""
        self.hiddenAbility = "Water Absorb"
        self.hidAbBool     = False
        
class lanturn(pokemon):
    def __init__(self):
        self.pokedex       = 171.0
        self.species       = "Lanturn"
        self.nature        = self.generateNature()
        self.type          = ["Water", "Electric"]
      #  self.maxLevel      = 18
       # self.level         = self.generateLevel(1, self.maxLevel - 1)
        self.hp            = 125
        self.attack        = 58
        self.defense       = 58
        self.spAtk         = 76
        self.spDef         = 76
        self.speed         = 67
        self.friend        = 70
        self.gender        = self.generateGender(50)
        self.abilities     = ["Volt Absorb", "Illuminate"]
        self.ability       = ""
        self.hiddenAbility = "Water Absorb"
        self.hidAbBool     = False
        
class pichu(pokemon):
    def __init__(self):
        self.pokedex       = 172.0
        self.species       = "Pichu"
        self.nature        = self.generateNature()
        self.type          = ["Electric"]
      #  self.maxLevel      = 18
       # self.level         = self.generateLevel(1, self.maxLevel - 1)
        self.hp            = 20
        self.attack        = 40
        self.defense       = 15
        self.spAtk         = 35
        self.spDef         = 35
        self.speed         = 60
        self.friend        = 70
        self.gender        = self.generateGender(50)
        self.abilities     = [""]
        self.ability       = "Static"
        self.hiddenAbility = "Lightning Rod"
        self.hidAbBool     = False
        
class cleffa(pokemon):
    def __init__(self):
        self.pokedex       = 173.0
        self.species       = "Cleffa"
        self.nature        = self.generateNature()
        self.type          = ["Fairy"]
      #  self.maxLevel      = 18
       # self.level         = self.generateLevel(1, self.maxLevel - 1)
        self.hp            = 50
        self.attack        = 25
        self.defense       = 28
        self.spAtk         = 45
        self.spDef         = 55
        self.speed         = 15
        self.friend        = 140
        self.gender        = self.generateGender(25)
        self.abilities     = ["Cute Charm", "Magic Guard"]
        self.ability       = ""
        self.hiddenAbility = "Friend Guard"
        self.hidAbBool     = False
        
class igglybuff(pokemon):
    def __init__(self):
        self.pokedex       = 173.0
        self.species       = "Igglybuff"
        self.nature        = self.generateNature()
        self.type          = ["Normal", "Fairy"]
      #  self.maxLevel      = 18
       # self.level         = self.generateLevel(1, self.maxLevel - 1)
        self.hp            = 90
        self.attack        = 30
        self.defense       = 15
        self.spAtk         = 40
        self.spDef         = 20
        self.speed         = 15
        self.friend        = 70
        self.gender        = self.generateGender(25)
        self.abilities     = ["Cute Charm", "Competitive"]
        self.ability       = ""
        self.hiddenAbility = "Friend Guard"
        self.hidAbBool     = False
        
class togepi(pokemon):
    def __init__(self):
        self.pokedex       = 174.0
        self.species       = "Togepi"
        self.nature        = self.generateNature()
        self.type          = ["Fairy"]
      #  self.maxLevel      = 18
       # self.level         = self.generateLevel(1, self.maxLevel - 1)
        self.hp            = 35
        self.attack        = 20
        self.defense       = 65
        self.spAtk         = 40
        self.spDef         = 65
        self.speed         = 20
        self.friend        = 70
        self.gender        = self.generateGender(87.5)
        self.abilities     = ["Hustle", "Serene Grace"]
        self.ability       = ""
        self.hiddenAbility = "Super Luck"
        self.hidAbBool     = False
        
class togetic(pokemon):
    def __init__(self):
        self.pokedex       = 175.0
        self.species       = "Togetic"
        self.nature        = self.generateNature()
        self.type          = ["Fairy", "Flying"]
      #  self.maxLevel      = 18
       # self.level         = self.generateLevel(1, self.maxLevel - 1)
        self.hp            = 55
        self.attack        = 40
        self.defense       = 85
        self.spAtk         = 80
        self.spDef         = 105
        self.speed         = 40
        self.friend        = 70
        self.gender        = self.generateGender(87.5)
        self.abilities     = ["Hustle", "Serene Grace"]
        self.ability       = ""
        self.hiddenAbility = "Super Luck"
        self.hidAbBool     = False
        
class raikou(pokemon):
    def __init__(self):
        self.pokedex       = 243.0
        self.species       = "Raikou"
        self.nature        = self.generateNature()
        self.type          = ["Electric"]
       # self.level         = self.generateLevel(1, 100)
        self.hp            = 90
        self.attack        = 85
        self.defense       = 75
        self.spAtk         = 115
        self.spDef         = 100
        self.speed         = 115
        self.friend        = 70
        self.gender        = self.generateGender(0)              
        self.abilities     = [""]
        self.ability       = "Pressure"
        self.hiddenAbility = "Inner Focus"
        self.hidAbBool     = False

class entei(pokemon):
    def __init__(self):
        self.pokedex       = 244.0
        self.species       = "Entei"
        self.nature        = self.generateNature()
        self.type          = ["Fire"]
       # self.level         = self.generateLevel(1, 100)
        self.hp            = 115
        self.attack        = 115
        self.defense       = 85
        self.spAtk         = 90
        self.spDef         = 75
        self.speed         = 100
        self.friend        = 70
        self.gender        = self.generateGender(0)              
        self.abilities     = [""]
        self.ability       = "Pressure"
        self.hiddenAbility = "Inner Focus"
        self.hidAbBool     = False

class suicune(pokemon):
    def __init__(self):
        self.pokedex       = 245.0
        self.species       = "Suicune"
        self.nature        = self.generateNature()
        self.type          = ["Water"]
       # self.level         = self.generateLevel(1, 100)
        self.hp            = 100
        self.attack        = 75
        self.defense       = 115
        self.spAtk         = 90
        self.spDef         = 115
        self.speed         = 85
        self.friend        = 70
        self.gender        = self.generateGender(0)              
        self.abilities     = [""]
        self.ability       = "Pressure"
        self.hiddenAbility = "Inner Focus"
        self.hidAbBool     = False

class lugia(pokemon):
    def __init__(self):
        self.pokedex       = 249.0
        self.species       = "Lugia"
        self.nature        = self.generateNature()
        self.type          = ["Psychic", "Flying"]
      #  self.level         = self.generateLevel(1, 100)
        self.hp            = 106
        self.attack        = 90
        self.defense       = 130
        self.spAtk         = 90
        self.spDef         = 154
        self.speed         = 110
        self.friend        = 70
        self.gender        = self.generateGender(0)              
        self.abilities     = [""]
        self.ability       = "Pressure"
        self.hiddenAbility = "Multiscale"
        self.hidAbBool     = False

class hoOh(pokemon):
    def __init__(self):
        self.pokedex       = 250.0
        self.species       = "Ho-Oh"
        self.nature        = self.generateNature()
        self.type          = ["Fire", "Flying"]
       # self.level         = self.generateLevel(1, 100)
        self.hp            = 106
        self.attack        = 130
        self.defense       = 90
        self.spAtk         = 110
        self.spDef         = 154
        self.speed         = 90
        self.friend        = 70
        self.gender        = self.generateGender(0)              
        self.abilities     = [""]
        self.ability       = "Pressure"
        self.hiddenAbility = "Regenerator"
        self.hidAbBool     = False

class celebi(pokemon):
    def __init__(self):
        self.pokedex       = 251.0
        self.species       = "Celebi"
        self.nature        = self.generateNature()
        self.type          = ["Psychic", "Grass"]
       # self.level         = self.generateLevel(1, 100)
        self.hp            = 100
        self.attack        = 100
        self.defense       = 100
        self.spAtk         = 100
        self.spDef         = 100
        self.speed         = 100
        self.friend        = 70
        self.gender        = self.generateGender(0)              
        self.abilities     = [""]
        self.ability       = "Natural Cure"
        self.hiddenAbility = ""
        self.hidAbBool     = False

class treecko(pokemon):
    def __init__(self):
        self.pokedex       = 252.0
        self.species       = "Treecko"
        self.nature        = self.generateNature()
        self.type          = ["Grass"]
       # self.maxLevel      = 16
       # self.level         = self.generateLevel(1, self.maxLevel - 1)
        self.hp            = 40
        self.attack        = 45
        self.defense       = 35
        self.spAtk         = 65
        self.spDef         = 55
        self.speed         = 70
        self.friend        = 70
        self.gender        = self.generateGender(87.5)
        self.abilities     = []
        self.ability       = "Overgrow"
        self.hiddenAbility = "Unburden"
        self.hidAbBool     = False

class torchic(pokemon):
    def __init__(self):
        self.pokedex       = 255.0
        self.species       = "Torchic"
        self.nature        = self.generateNature()
        self.type          = ["Fire"]
       # self.maxLevel      = 16
       # self.level         = self.generateLevel(1, self.maxLevel - 1)
        self.hp            = 45
        self.attack        = 60
        self.defense       = 40
        self.spAtk         = 70
        self.spDef         = 50
        self.speed         = 45
        self.friend        = 70
        self.gender        = self.generateGender(87.5)
        self.abilities     = []
        self.ability       = "Blaze"
        self.hiddenAbility = "Speed Boost"
        self.hidAbBool     = False

class mudkip(pokemon):
    def __init__(self):
        self.pokedex       = 258.0
        self.species       = "Mudkip"
        self.nature        = self.generateNature()
        self.type          = ["Water"]
       # self.maxLevel      = 16
       # self.level         = self.generateLevel(1, self.maxLevel - 1)
        self.hp            = 50
        self.attack        = 70
        self.defense       = 50
        self.spAtk         = 50
        self.spDef         = 50
        self.speed         = 40
        self.friend        = 70
        self.gender        = self.generateGender(87.5)
        self.abilities     = []
        self.ability       = "Torrent"
        self.hiddenAbility = "Damp"
        self.hidAbBool     = False

class regirock(pokemon):
    def __init__(self):
        self.pokedex       = 377.0
        self.species       = "Regirock"
        self.nature        = self.generateNature()
        self.type          = ["Rock"]
       # self.level         = self.generateLevel(1, 100)
        self.hp            = 80
        self.attack        = 100
        self.defense       = 200
        self.spAtk         = 50
        self.spDef         = 100
        self.speed         = 50
        self.friend        = 70
        self.gender        = self.generateGender(0)              
        self.abilities     = [""]
        self.ability       = "Clear Body"
        self.hiddenAbility = "Sturdy"
        self.hidAbBool     = False

class regice(pokemon):
    def __init__(self):
        self.pokedex       = 378.0
        self.species       = "Regice"
        self.nature        = self.generateNature()
        self.type          = ["Ice"]
      #  self.level         = self.generateLevel(1, 100)
        self.hp            = 80
        self.attack        = 50
        self.defense       = 100
        self.spAtk         = 100
        self.spDef         = 200
        self.speed         = 50
        self.friend        = 70
        self.gender        = self.generateGender(0)              
        self.abilities     = [""]
        self.ability       = "Clear Body"
        self.hiddenAbility = "Ice Body"
        self.hidAbBool     = False

class registeel(pokemon):
    def __init__(self):
        self.pokedex       = 379.0
        self.species       = "Registeel"
        self.nature        = self.generateNature()
        self.type          = ["Steel"]
     #   self.level         = self.generateLevel(1, 100)
        self.hp            = 80
        self.attack        = 75
        self.defense       = 150
        self.spAtk         = 75
        self.spDef         = 150
        self.speed         = 50
        self.friend        = 70
        self.gender        = self.generateGender(0)              
        self.abilities     = [""]
        self.ability       = "Clear Body"
        self.hiddenAbility = "Light Metal"
        self.hidAbBool     = False

class latias(pokemon):
    def __init__(self):
        self.pokedex       = 380.0
        self.species       = "Latias"
        self.nature        = self.generateNature()
        self.type          = ["Dragon", "Psychic"]
      #  self.level         = self.generateLevel(1, 100)
        self.hp            = 80
        self.attack        = 80
        self.defense       = 90
        self.spAtk         = 110
        self.spDef         = 130
        self.speed         = 110
        self.friend        = 70
        self.gender        = self.generateGender(0)              
        self.abilities     = [""]
        self.ability       = "Levitate"
        self.hiddenAbility = ""
        self.hidAbBool     = False

class latios(pokemon):
    def __init__(self):
        self.pokedex       = 381.0
        self.species       = "Latios"
        self.nature        = self.generateNature()
        self.type          = ["Dragon", "Psychic"]
     #   self.level         = self.generateLevel(1, 100)
        self.hp            = 80
        self.attack        = 90
        self.defense       = 80
        self.spAtk         = 130
        self.spDef         = 110
        self.speed         = 110
        self.friend        = 70
        self.gender        = self.generateGender(100)              
        self.abilities     = [""]
        self.ability       = "Levitate"
        self.hiddenAbility = ""
        self.hidAbBool     = False

class kyogre(pokemon):
    def __init__(self):
        self.pokedex       = 382.0
        self.species       = "Kyogre"
        self.nature        = self.generateNature()
        self.type          = ["Water"]
      #  self.level         = self.generateLevel(1, 100)
        self.hp            = 100
        self.attack        = 100
        self.defense       = 90
        self.spAtk         = 150
        self.spDef         = 140
        self.speed         = 90
        self.friend        = 70
        self.gender        = self.generateGender(0)              
        self.abilities     = [""]
        self.ability       = "Drizzle"
        self.hiddenAbility = ""
        self.hidAbBool     = False

class groudon(pokemon):
    def __init__(self):
        self.pokedex       = 383.0
        self.species       = "Groudon"
        self.nature        = self.generateNature()
        self.type          = ["Ground"]
       # self.level         = self.generateLevel(1, 100)
        self.hp            = 100
        self.attack        = 150
        self.defense       = 140
        self.spAtk         = 100
        self.spDef         = 90
        self.speed         = 90
        self.friend        = 70
        self.gender        = self.generateGender(0)              
        self.abilities     = [""]
        self.ability       = "Drought"
        self.hiddenAbility = ""
        self.hidAbBool     = False

class rayquaza(pokemon):
    def __init__(self):
        self.pokedex       = 384.0
        self.species       = "Rayquaza"
        self.nature        = self.generateNature()
        self.type          = ["Dragon", "Flying"]
       # self.level         = self.generateLevel(1, 100)
        self.hp            = 105
        self.attack        = 150
        self.defense       = 90
        self.spAtk         = 150
        self.spDef         = 90
        self.speed         = 95
        self.friend        = 70
        self.gender        = self.generateGender(0)              
        self.abilities     = [""]
        self.ability       = "Air Lock"
        self.hiddenAbility = ""
        self.hidAbBool     = False

class jirachi(pokemon):
    def __init__(self):
        self.pokedex       = 385.0
        self.species       = "Jirachi"
        self.nature        = self.generateNature()
        self.type          = ["Steel", "Psychic"]
      #  self.level         = self.generateLevel(1, 100)
        self.hp            = 100
        self.attack        = 100
        self.defense       = 100
        self.spAtk         = 100
        self.spDef         = 100
        self.speed         = 100
        self.friend        = 70
        self.gender        = self.generateGender(0)              
        self.abilities     = [""]
        self.ability       = "Serene Grace"
        self.hiddenAbility = ""
        self.hidAbBool     = False

class deoxys(pokemon):
    def __init__(self):
        self.pokedex       = 386.0
        self.species       = "Deoxys"
        self.nature        = self.generateNature()
        self.type          = ["Psychic"]
      #  self.level         = self.generateLevel(1, 100)
        self.hp            = 50
        self.attack        = 150
        self.defense       = 50
        self.spAtk         = 150
        self.spDef         = 50
        self.speed         = 150
        self.friend        = 70
        self.gender        = self.generateGender(0)              
        self.abilities     = [""]
        self.ability       = "Pressure"
        self.hiddenAbility = ""
        self.hidAbBool     = False

class turtwig(pokemon):
    def __init__(self):
        self.pokedex       = 387.0
        self.species       = "Turtwig"
        self.nature        = self.generateNature()
        self.type          = ["Grass"]
       # self.maxLevel      = 18
       # self.level         = self.generateLevel(1, self.maxLevel - 1)
        self.hp            = 55
        self.attack        = 68
        self.defense       = 64
        self.spAtk         = 45
        self.spDef         = 55
        self.speed         = 31
        self.friend        = 70
        self.gender        = self.generateGender(87.5)
        self.abilities     = []
        self.ability       = "Overgrow"
        self.hiddenAbility = "Shell Armor"
        self.hidAbBool     = False

class chimchar(pokemon):
    def __init__(self):
        self.pokedex       = 390.0
        self.species       = "Chimchar"
        self.nature        = self.generateNature()
        self.type          = ["Fire"]
       # self.maxLevel      = 14
      #  self.level         = self.generateLevel(1, self.maxLevel - 1)
        self.hp            = 44
        self.attack        = 58
        self.defense       = 44
        self.spAtk         = 58
        self.spDef         = 44
        self.speed         = 61
        self.friend        = 70
        self.gender        = self.generateGender(87.5)
        self.abilities     = []
        self.ability       = "Blaze"
        self.hiddenAbility = "Iron Fist"
        self.hidAbBool     = False

class piplup(pokemon):
    def __init__(self):
        self.pokedex       = 393.0
        self.species       = "Piplup"
        self.nature        = self.generateNature()
        self.type          = ["Water"]
       # self.maxLevel      = 16
      #  self.level         = self.generateLevel(1, self.maxLevel - 1)
        self.hp            = 53
        self.attack        = 51
        self.defense       = 53
        self.spAtk         = 61
        self.spDef         = 56
        self.speed         = 40
        self.friend        = 70
        self.gender        = self.generateGender(87.5)
        self.abilities     = []
        self.ability       = "Torrent"
        self.hiddenAbility = "Defiant"
        self.hidAbBool     = False

class uxie(pokemon):
    def __init__(self):
        self.pokedex       = 480.0
        self.species       = "Uxie"
        self.nature        = self.generateNature()
        self.type          = ["Psychic"]
       # self.level         = self.generateLevel(1, 100)
        self.hp            = 75
        self.attack        = 75
        self.defense       = 130
        self.spAtk         = 75
        self.spDef         = 130
        self.speed         = 95
        self.friend        = 70
        self.gender        = self.generateGender(0)              
        self.abilities     = [""]
        self.ability       = "Levitate"
        self.hiddenAbility = ""
        self.hidAbBool     = False

class mesprit(pokemon):
    def __init__(self):
        self.pokedex       = 481.0
        self.species       = "Mesprit"
        self.nature        = self.generateNature()
        self.type          = ["Psychic"]
       # self.level         = self.generateLevel(1, 100)
        self.hp            = 80
        self.attack        = 105
        self.defense       = 105
        self.spAtk         = 105
        self.spDef         = 105
        self.speed         = 80
        self.friend        = 70
        self.gender        = self.generateGender(0)              
        self.abilities     = [""]
        self.ability       = "Levitate"
        self.hiddenAbility = ""
        self.hidAbBool     = False

class azelf(pokemon):
    def __init__(self):
        self.pokedex       = 482.0
        self.species       = "Azelf"
        self.nature        = self.generateNature()
        self.type          = ["Psychic"]
       # self.level         = self.generateLevel(1, 100)
        self.hp            = 75
        self.attack        = 125
        self.defense       = 70
        self.spAtk         = 125
        self.spDef         = 70
        self.speed         = 115
        self.friend        = 70
        self.gender        = self.generateGender(0)              
        self.abilities     = [""]
        self.ability       = "Levitate"
        self.hiddenAbility = ""
        self.hidAbBool     = False

class dialga(pokemon):
    def __init__(self):
        self.pokedex       = 483.0
        self.species       = "Dialga"
        self.nature        = self.generateNature()
        self.type          = ["Steel", "Dragon"]
       # self.level         = self.generateLevel(1, 100)
        self.hp            = 100
        self.attack        = 120
        self.defense       = 120
        self.spAtk         = 150
        self.spDef         = 100
        self.speed         = 90
        self.friend        = 70
        self.gender        = self.generateGender(0)              
        self.abilities     = [""]
        self.ability       = "Pressure"
        self.hiddenAbility = "Telepathy"
        self.hidAbBool     = False

class palkia(pokemon):
    def __init__(self):
        self.pokedex       = 484.0
        self.species       = "Palkia"
        self.nature        = self.generateNature()
        self.type          = ["Water", "Dragon"]
       # self.level         = self.generateLevel(1, 100)
        self.hp            = 90
        self.attack        = 120
        self.defense       = 100
        self.spAtk         = 150
        self.spDef         = 120
        self.speed         = 100
        self.friend        = 70
        self.gender        = self.generateGender(0)              
        self.abilities     = [""]
        self.ability       = "Pressure"
        self.hiddenAbility = "Telepathy"
        self.hidAbBool     = False

class heatran(pokemon):
    def __init__(self):
        self.pokedex       = 485.0
        self.species       = "Heatran"
        self.nature        = self.generateNature()
        self.type          = ["Fire", "Steel"]
      #  self.level         = self.generateLevel(1, 100)
        self.hp            = 91
        self.attack        = 90
        self.defense       = 106
        self.spAtk         = 130
        self.spDef         = 106
        self.speed         = 77
        self.friend        = 70
        self.gender        = self.generateGender(0)              
        self.abilities     = [""]
        self.ability       = "Flash Fire"
        self.hiddenAbility = "Flame Body"
        self.hidAbBool     = False

class regigigas(pokemon):
    def __init__(self):
        self.pokedex       = 486.0
        self.species       = "Regigigas"
        self.nature        = self.generateNature()
        self.type          = ["Normal"]
       # self.level         = self.generateLevel(1, 100)
        self.hp            = 110
        self.attack        = 160
        self.defense       = 110
        self.spAtk         = 80
        self.spDef         = 110
        self.speed         = 100
        self.friend        = 70
        self.gender        = self.generateGender(0)              
        self.abilities     = [""]
        self.ability       = "Slow Start"
        self.hiddenAbility = ""
        self.hidAbBool     = False

class giratina(pokemon):
    def __init__(self):
        self.pokedex       = 487.0
        self.species       = "Giratina"
        self.nature        = self.generateNature()
        self.type          = ["Ghost", "Dragon"]
        #self.level         = self.generateLevel(1, 100)
        self.hp            = 150
        self.attack        = 100
        self.defense       = 120
        self.spAtk         = 100
        self.spDef         = 120
        self.speed         = 90
        self.friend        = 70
        self.gender        = self.generateGender(0)              
        self.abilities     = [""]
        self.ability       = "Pressure"
        self.hiddenAbility = "Telepathy"
        self.hidAbBool     = False

class cresselia(pokemon):
    def __init__(self):
        self.pokedex       = 488.0
        self.species       = "Cresselia"
        self.nature        = self.generateNature()
        self.type          = ["Psychic"]
       # self.level         = self.generateLevel(1, 100)
        self.hp            = 120
        self.attack        = 70
        self.defense       = 120
        self.spAtk         = 75
        self.spDef         = 130
        self.speed         = 85
        self.friend        = 70
        self.gender        = self.generateGender(0)              
        self.abilities     = [""]
        self.ability       = "Levitate"
        self.hiddenAbility = ""
        self.hidAbBool     = False

class phione(pokemon):
    def __init__(self):
        self.pokedex       = 489.0
        self.species       = "Phione"
        self.nature        = self.generateNature()
        self.type          = ["Water"]
      #  self.level         = self.generateLevel(1, 100)
        self.hp            = 80
        self.attack        = 80
        self.defense       = 80
        self.spAtk         = 80
        self.spDef         = 80
        self.speed         = 80
        self.friend        = 70
        self.gender        = self.generateGender(0)              
        self.abilities     = [""]
        self.ability       = "Hydration"
        self.hiddenAbility = ""
        self.hidAbBool     = False

class manaphy(pokemon):
    def __init__(self):
        self.pokedex       = 490.0
        self.species       = "Manaphy"
        self.nature        = self.generateNature()
        self.type          = ["Water"]
      #  self.level         = self.generateLevel(1, 100)
        self.hp            = 100
        self.attack        = 100
        self.defense       = 100
        self.spAtk         = 100
        self.spDef         = 100
        self.speed         = 100
        self.friend        = 70
        self.gender        = self.generateGender(0)              
        self.abilities     = [""]
        self.ability       = "Hydration"
        self.hiddenAbility = ""
        self.hidAbBool     = False

class darkrai(pokemon):
    def __init__(self):
        self.pokedex       = 491.0
        self.species       = "Darkrai"
        self.nature        = self.generateNature()
        self.type          = ["Dark"]
       # self.level         = self.generateLevel(1, 100)
        self.hp            = 70
        self.attack        = 90
        self.defense       = 90
        self.spAtk         = 135
        self.spDef         = 90
        self.speed         = 125
        self.friend        = 70
        self.gender        = self.generateGender(0)              
        self.abilities     = [""]
        self.ability       = "Bad Dreams"
        self.hiddenAbility = ""
        self.hidAbBool     = False

class shaymin(pokemon):
    def __init__(self):
        self.pokedex       = 492.0
        self.species       = "Shaymin"
        self.nature        = self.generateNature()
        self.type          = ["Grass"]
      #  self.level         = self.generateLevel(1, 100)
        self.hp            = 100
        self.attack        = 100
        self.defense       = 100
        self.spAtk         = 100
        self.spDef         = 100
        self.speed         = 100
        self.friend        = 70
        self.gender        = self.generateGender(0)              
        self.abilities     = [""]
        self.ability       = "Natural Cure"
        self.hiddenAbility = ""
        self.hidAbBool     = False

class arceus(pokemon):
    def __init__(self):
        self.pokedex       = 493.0
        self.species       = "Arceus"
        self.nature        = self.generateNature()
        self.type          = ["Normal"]
       # self.level         = self.generateLevel(1, 100)
        self.hp            = 120
        self.attack        = 120
        self.defense       = 120
        self.spAtk         = 120
        self.spDef         = 120
        self.speed         = 120
        self.friend        = 70
        self.gender        = self.generateGender(0)              
        self.abilities     = [""]
        self.ability       = "Multitype"
        self.hiddenAbility = ""
        self.hidAbBool     = False

class victini(pokemon):
    def __init__(self):
        self.pokedex       = 494.0
        self.species       = "Victini"
        self.nature        = self.generateNature()
        self.type          = ["Psychic", "Fire"]
      #  self.level         = self.generateLevel(1, 100)
        self.hp            = 100
        self.attack        = 100
        self.defense       = 100
        self.spAtk         = 100
        self.spDef         = 100
        self.speed         = 100
        self.friend        = 70
        self.gender        = self.generateGender(0)              
        self.abilities     = [""]
        self.ability       = "Victory Star"
        self.hiddenAbility = ""
        self.hidAbBool     = False

class snivy(pokemon):
    def __init__(self):
        self.pokedex       = 495.0
        self.species       = "Snivy"
        self.nature        = self.generateNature()
        self.type          = ["Grass"]
       # self.maxLevel      = 17
       # self.level         = self.generateLevel(1, self.maxLevel - 1)
        self.hp            = 45
        self.attack        = 45
        self.defense       = 55
        self.spAtk         = 45
        self.spDef         = 55
        self.speed         = 63
        self.friend        = 70
        self.gender        = self.generateGender(87.5)
        self.abilities     = []
        self.ability       = "Overgrow"
        self.hiddenAbility = "Contrary"
        self.hidAbBool     = False

class tepig(pokemon):
    def __init__(self):
        self.pokedex       = 498.0
        self.species       = "Tepig"
        self.nature        = self.generateNature()
        self.type          = ["Fire"]
       # self.maxLevel      = 17
       # self.level         = self.generateLevel(1, self.maxLevel - 1)
        self.hp            = 65
        self.attack        = 63
        self.defense       = 45
        self.spAtk         = 45
        self.spDef         = 45
        self.speed         = 45
        self.friend        = 70
        self.gender        = self.generateGender(87.5)
        self.abilities     = []
        self.ability       = "Blaze"
        self.hiddenAbility = "Thick Fat"
        self.hidAbBool     = False

class oshawott(pokemon):
    def __init__(self):
        self.pokedex       = 501.0
        self.species       = "Oshawott"
        self.nature        = self.generateNature()
        self.type          = ["Water"]
      #  self.maxLevel      = 17
      #  self.level         = self.generateLevel(1, self.maxLevel - 1)
        self.hp            = 55
        self.attack        = 55
        self.defense       = 45
        self.spAtk         = 63
        self.spDef         = 45
        self.speed         = 45
        self.friend        = 70
        self.gender        = self.generateGender(87.5)
        self.abilities     = []
        self.ability       = "Torrent"
        self.hiddenAbility = "Shell Armor"
        self.hidAbBool     = False

class cobalion(pokemon):
    def __init__(self):
        self.pokedex       = 638.0
        self.species       = "Coballion"
        self.nature        = self.generateNature()
        self.type          = ["Steel", "Fight"]
        #self.level         = self.generateLevel(1, 100)
        self.hp            = 91
        self.attack        = 90
        self.defense       = 129
        self.spAtk         = 90
        self.spDef         = 72
        self.speed         = 108
        self.friend        = 70
        self.gender        = self.generateGender(0)              
        self.abilities     = [""]
        self.ability       = "Justified"
        self.hiddenAbility = ""
        self.hidAbBool     = False

class terrakion(pokemon):
    def __init__(self):
        self.pokedex       = 639.0
        self.species       = "Terrakion"
        self.nature        = self.generateNature()
        self.type          = ["Rock", "Fight"]
       # self.level         = self.generateLevel(1, 100)
        self.hp            = 91
        self.attack        = 129
        self.defense       = 90
        self.spAtk         = 72
        self.spDef         = 90
        self.speed         = 108
        self.friend        = 70
        self.gender        = self.generateGender(0)              
        self.abilities     = [""]
        self.ability       = "Justified"
        self.hiddenAbility = ""
        self.hidAbBool     = False

class virizion(pokemon):
    def __init__(self):
        self.pokedex       = 640.0
        self.species       = "Virizion"
        self.nature        = self.generateNature()
        self.type          = ["Grass", "Fight"]
      #  self.level         = self.generateLevel(1, 100)
        self.hp            = 91
        self.attack        = 90
        self.defense       = 72
        self.spAtk         = 90
        self.spDef         = 129
        self.speed         = 108
        self.friend        = 70
        self.gender        = self.generateGender(0)              
        self.abilities     = [""]
        self.ability       = "Justified"
        self.hiddenAbility = ""
        self.hidAbBool     = False

class tornadus(pokemon):
    def __init__(self):
        self.pokedex       = 641.0
        self.species       = "Tornadus"
        self.nature        = self.generateNature()
        self.type          = ["Flying"]
       # self.level         = self.generateLevel(1, 100)
        self.hp            = 79
        self.attack        = 115
        self.defense       = 70
        self.spAtk         = 125
        self.spDef         = 80
        self.speed         = 111
        self.friend        = 70
        self.gender        = self.generateGender(0)              
        self.abilities     = [""]
        self.ability       = "Prankster"
        self.hiddenAbility = "Defiant"
        self.hidAbBool     = False

class thundurus(pokemon):
    def __init__(self):
        self.pokedex       = 642.0
        self.species       = "Thundurus"
        self.nature        = self.generateNature()
        self.type          = ["Electric", "Flying"]
        #self.level         = self.generateLevel(1, 100)
        self.hp            = 79
        self.attack        = 115
        self.defense       = 70
        self.spAtk         = 125
        self.spDef         = 80
        self.speed         = 111
        self.friend        = 70
        self.gender        = self.generateGender(0)              
        self.abilities     = [""]
        self.ability       = "Prankster"
        self.hiddenAbility = "Defiant"
        self.hidAbBool     = False

class reshiram(pokemon):
    def __init__(self):
        self.pokedex       = 643.0
        self.species       = "Reshiram"
        self.nature        = self.generateNature()
        self.type          = ["Dragon", "Fire"]
       # self.level         = self.generateLevel(1, 100)
        self.hp            = 100
        self.attack        = 120
        self.defense       = 100
        self.spAtk         = 150
        self.spDef         = 120
        self.speed         = 90
        self.friend        = 70
        self.gender        = self.generateGender(0)              
        self.abilities     = [""]
        self.ability       = "Turboblaze"
        self.hiddenAbility = ""
        self.hidAbBool     = False

class zekrom(pokemon):
    def __init__(self):
        self.pokedex       = 644.0
        self.species       = "Zekrom"
        self.nature        = self.generateNature()
        self.type          = ["Dragon", "Electric"]
       # self.level         = self.generateLevel(1, 100)
        self.hp            = 100
        self.attack        = 150
        self.defense       = 120
        self.spAtk         = 120
        self.spDef         = 100
        self.speed         = 90
        self.friend        = 70
        self.gender        = self.generateGender(0)              
        self.abilities     = [""]
        self.ability       = "Terabolt"
        self.hiddenAbility = ""
        self.hidAbBool     = False

class landorus(pokemon):
    def __init__(self):
        self.pokedex       = 645.0
        self.species       = "Landorus"
        self.nature        = self.generateNature()
        self.type          = ["Electric", "Flying"]
      #  self.level         = self.generateLevel(1, 100)
        self.hp            = 89
        self.attack        = 125
        self.defense       = 90
        self.spAtk         = 115
        self.spDef         = 80
        self.speed         = 101
        self.friend        = 70
        self.gender        = self.generateGender(0)              
        self.abilities     = [""]
        self.ability       = "Sand Force"
        self.hiddenAbility = "Sheer Force"
        self.hidAbBool     = False

class kyurem(pokemon):
    def __init__(self):
        self.pokedex       = 646.0
        self.species       = "Kyurem"
        self.nature        = self.generateNature()
        self.type          = ["Dragon", "Ice"]
       # self.level         = self.generateLevel(1, 100)
        self.hp            = 125
        self.attack        = 130
        self.defense       = 90
        self.spAtk         = 130
        self.spDef         = 90
        self.speed         = 95
        self.friend        = 70
        self.gender        = self.generateGender(0)              
        self.abilities     = [""]
        self.ability       = "Pressure"
        self.hiddenAbility = ""
        self.hidAbBool     = False

class keldeo(pokemon):
    def __init__(self):
        self.pokedex       = 647.0
        self.species       = "Keldeo"
        self.nature        = self.generateNature()
        self.type          = ["Water", "Fight"]
       # self.level         = self.generateLevel(1, 100)
        self.hp            = 91
        self.attack        = 72
        self.defense       = 90
        self.spAtk         = 129
        self.spDef         = 90
        self.speed         = 108
        self.friend        = 70
        self.gender        = self.generateGender(0)              
        self.abilities     = [""]
        self.ability       = "Justified"
        self.hiddenAbility = ""
        self.hidAbBool     = False

class meloetta(pokemon):
    def __init__(self):
        self.pokedex       = 648.0
        self.species       = "Meloetta"
        self.nature        = self.generateNature()
        self.type          = ["Normal", "Psychic"]
      #  self.level         = self.generateLevel(1, 100)
        self.hp            = 100
        self.attack        = 77
        self.defense       = 77
        self.spAtk         = 128
        self.spDef         = 128
        self.speed         = 90
        self.friend        = 70
        self.gender        = self.generateGender(0)              
        self.abilities     = [""]
        self.ability       = "Serene Grace"
        self.hiddenAbility = ""
        self.hidAbBool     = False

class genesect(pokemon):
    def __init__(self):
        self.pokedex       = 649.0
        self.species       = "Genesect"
        self.nature        = self.generateNature()
        self.type          = ["Bug", "Steel"]
       # self.level         = self.generateLevel(1, 100)
        self.hp            = 71
        self.attack        = 120
        self.defense       = 95
        self.spAtk         = 120
        self.spDef         = 95
        self.speed         = 99
        self.friend        = 70
        self.gender        = self.generateGender(0)              
        self.abilities     = [""]
        self.ability       = "Download"
        self.hiddenAbility = ""
        self.hidAbBool     = False

class chespin(pokemon):
    def __init__(self):
        self.pokedex       = 650.0
        self.species       = "Chespin"
        self.nature        = self.generateNature()
        self.type          = ["Grass"]
      #  self.level         = self.generateLevel(1, 15)
        self.hp            = 56
        self.attack        = 61
        self.defense       = 65
        self.spAtk         = 48
        self.spDef         = 45
        self.speed         = 28
        self.friend        = 70
        self.gender        = self.generateGender(87.5)
        self.abilities     = []
        self.ability       = "Overgrow"
        self.hiddenAbility = "BulletProof"
        self.hidAbBool     = False

class quilladin(pokemon):
    def __init__(self):
        self.pokedex       = 651.0
        self.species       = "Quilladin"
        self.nature        = self.generateNature()
        self.type          = ["Grass"]
      #  self.level         = self.generateLevel(16, 35)
        self.hp            = 61
        self.attack        = 78
        self.defense       = 95
        self.spAtk         = 56
        self.spDef         = 58
        self.speed         = 57
        self.friend        = 70
        self.gender        = self.generateGender(87.5)
        self.abilities     = []
        self.ability       = "Overgrow"
        self.hiddenAbility = "BulletProof"
        self.hidAbBool     = False

class chesnaught(pokemon):
    def __init__(self):
        self.pokedex       = 652.0
        self.species       = "Chesnaught"
        self.nature        = self.generateNature()
        self.type          = ["Grass", "Fighting"]
       # self.level         = self.generateLevel(36, 100)
        self.hp            = 88
        self.attack        = 107
        self.defense       = 122
        self.spAtk         = 74
        self.spDef         = 75
        self.speed         = 64
        self.friend        = 70
        self.gender        = self.generateGender(87.5)
        self.abilities     = []
        self.ability       = "Overgrow"
        self.hiddenAbility = "BulletProof"
        self.hidAbBool     = False

class fennekin(pokemon):
    def __init__(self):
        self.pokedex       = 653.0
        self.species       = "Fennekin"
        self.nature        = self.generateNature()
        self.type          = ["Fire"]
      #  self.level         = self.generateLevel(1, 15)
        self.hp            = 40
        self.attack        = 45
        self.defense       = 40
        self.spAtk         = 62
        self.spDef         = 60
        self.speed         = 60
        self.friend        = 70
        self.gender        = self.generateGender(87.5)
        self.abilities     = []
        self.ability       = "Blaze"
        self.hiddenAbility = "Magician"
        self.hidAbBool     = False

class braixen(pokemon):
    def __init__(self):
        self.pokedex       = 654.0
        self.species       = "Braixen"
        self.nature        = self.generateNature()
        self.type          = ["Fire"]
        #self.level         = self.generateLevel(16,35)
        self.hp            = 59
        self.attack        = 59
        self.defense       = 58
        self.spAtk         = 90
        self.spDef         = 70
        self.speed         = 73
        self.friend        = 70
        self.gender        = self.generateGender(87.5)
        self.abilities     = []
        self.ability       = "Blaze"
        self.hiddenAbility = "Magician"
        self.hidAbBool     = False

class delphox(pokemon):
    def __init__(self):
        self.pokedex       = 655.0
        self.species       = "Delphox"
        self.nature        = self.generateNature()
        self.type          = ["Fire", "Psychic"]
       # self.level         = self.generateLevel(36, 100)
        self.hp            = 75
        self.attack        = 69
        self.defense       = 72
        self.spAtk         = 114
        self.spDef         = 100
        self.speed         = 104
        self.friend        = 70
        self.gender        = self.generateGender(87.5)
        self.abilities     = []
        self.ability       = "Blaze"
        self.hiddenAbility = "Magician"
        self.hidAbBool     = False

class froakie(pokemon):
    def __init__(self):
        self.pokedex       = 656.0
        self.species       = "Froakie"
        self.nature        = self.generateNature()
        self.type          = ["Water"]
      #  self.level         = self.generateLevel(1, 15)
        self.hp            = 41
        self.attack        = 56
        self.defense       = 40
        self.spAtk         = 62
        self.spDef         = 44
        self.speed         = 71
        self.friend        = 70
        self.gender        = self.generateGender(87.5)
        self.abilities     = []
        self.ability       = "Torrent"
        self.hiddenAbility = "Protean"
        self.hidAbBool     = False

class frogadier(pokemon):
    def __init__(self):
        self.pokedex       = 657.0
        self.species       = "Frogadier"
        self.nature        = self.generateNature()
        self.type          = ["Water"]
      #  self.level         = self.generateLevel(16, 35)
        self.hp            = 54
        self.attack        = 63
        self.defense       = 52
        self.spAtk         = 83
        self.spDef         = 56
        self.speed         = 97
        self.friend        = 70
        self.gender        = self.generateGender(87.5)
        self.abilities     = []
        self.ability       = "Torrent"
        self.hiddenAbility = "Protean"
        self.hidAbBool     = False

class greninja(pokemon):
    def __init__(self):
        self.pokedex       = 658.0
        self.species       = "Greninja"
        self.nature        = self.generateNature()
        self.type          = ["Water", "Dark"]
      #  self.level         = self.generateLevel(1, 15)
        self.hp            = 72
        self.attack        = 95
        self.defense       = 67
        self.spAtk         = 103
        self.spDef         = 71
        self.speed         = 122
        self.friend        = 70
        self.gender        = self.generateGender(87.5)
        self.abilities     = []
        self.ability       = "Torrent"
        self.hiddenAbility = "Protean"
        self.hidAbBool     = False

class bunnelby(pokemon):
    def __init__(self):
        self.pokedex       = 659.0
        self.species       = "Bunnelby"
        self.nature        = self.generateNature()
        self.type          = ["Normal"]
       # self.level         = self.generateLevel(1, 19)
        self.hp            = 38
        self.attack        = 36
        self.defense       = 38
        self.spAtk         = 32
        self.spDef         = 36
        self.speed         = 57
        self.friend        = 70
        self.gender        = self.generateGender(50)
        self.abilities     = ["Pickup", "Cheek Pouch"]
        self.ability       = ""
        self.hiddenAbility = "Huge Power"
        self.hidAbBool     = False

class diggersby(pokemon):
    def __init__(self):
        self.pokedex       = 660.0
        self.species       = "Diggersby"
        self.nature        = self.generateNature()
        self.type          = ["Normal", "Ground"]
      #  self.level         = self.generateLevel(20, 100)
        self.hp            = 85
        self.attack        = 56
        self.defense       = 77
        self.spAtk         = 50
        self.spDef         = 77
        self.speed         = 78
        self.friend        = 70
        self.gender        = self.generateGender(50)
        self.abilities     = ["Pickup", "Cheek Pouch"]
        self.ability       = ""
        self.hiddenAbility = "Huge Power"
        self.hidAbBool     = False

class fletchling(pokemon):
    def __init__(self):
        self.pokedex       = 661.0
        self.species       = "Fletchling"
        self.nature        = self.generateNature()
        self.type          = ["Normal", "Flying"]
       # self.level         = self.generateLevel(1, 16)
        self.hp            = 45
        self.attack        = 50
        self.defense       = 43
        self.spAtk         = 40
        self.spDef         = 38
        self.speed         = 62
        self.friend        = 70
        self.gender        = self.generateGender(50)
        self.abilities     = []
        self.ability       = "Big Pecks"
        self.hiddenAbility = "Gale Wings"
        self.hidAbBool     = False

class fletchinfer(pokemon):
    def __init__(self):
        self.pokedex       = 662.0
        self.species       = "Fletchinder"
        self.nature        = self.generateNature()
        self.type          = ["Fire", "Flying"]
       # self.level         = self.generateLevel(17, 34)
        self.hp            = 62
        self.attack        = 73
        self.defense       = 55
        self.spAtk         = 56
        self.spDef         = 52
        self.speed         = 84
        self.friend        = 70
        self.gender        = self.generateGender(50)
        self.abilities     = []
        self.ability       = "Flame Body"
        self.hiddenAbility = "Gale Wings"
        self.hidAbBool     = False

class talonflame(pokemon):
    def __init__(self):
        self.pokedex       = 663.0
        self.species       = "Talonflame"
        self.nature        = self.generateNature()
        self.type          = ["Fire", "Flying"]
      #  self.level         = self.generateLevel(35, 100)
        self.hp            = 78
        self.attack        = 81
        self.defense       = 71
        self.spAtk         = 74
        self.spDef         = 69
        self.speed         = 126
        self.friend        = 70
        self.gender        = self.generateGender(50)
        self.abilities     = []
        self.ability       = "Flame Body"
        self.hiddenAbility = "Gale Wings"
        self.hidAbBool     = False

class scatterbug(pokemon):
    def __init__(self):
        self.pokedex       = 664.0
        self.species       = "Scatterbug"
        self.nature        = self.generateNature()
        self.type          = ["Bug"]
       # self.level         = self.generateLevel(1, 8)
        self.hp            = 38
        self.attack        = 35
        self.defense       = 40
        self.spAtk         = 27
        self.spDef         = 25
        self.speed         = 35
        self.friend        = 70
        self.gender        = self.generateGender(50)
        self.abilities     = ["Sheild Dust", "Compound Eyes"]
        self.ability       = ""
        self.hiddenAbility = "Friend Guard"
        self.hidAbBool     = False

class spewpa(pokemon):
    def __init__(self):
        self.pokedex       = 665.0
        self.species       = "Spewpa"
        self.nature        = self.generateNature()
        self.type          = ["Bug"]
       # self.level         = self.generateLevel(9, 11)
        self.hp            = 45
        self.attack        = 22
        self.defense       = 60
        self.spAtk         = 27
        self.spDef         = 30
        self.speed         = 29
        self.friend        = 70
        self.gender        = self.generateGender(50)
        self.abilities     = []
        self.ability       = "Shed Skin"
        self.hiddenAbility = "Friend Guard"
        self.hidAbBool     = False

class vivillon(pokemon):
    def __init__(self):
        self.pokedex       = 666.0
        self.species       = "Vivillon"
        self.nature        = self.generateNature()
        self.type          = ["Bug", "Flying"]
       # self.level         = self.generateLevel(12, 100)
        self.hp            = 80
        self.attack        = 52
        self.defense       = 50
        self.spAtk         = 90
        self.spDef         = 50
        self.speed         = 89
        self.friend        = 70
        self.gender        = self.generateGender(50)
        self.abilities     = ["Sheild Dust", "Compound Eyes"]
        self.ability       = ""
        self.hiddenAbility = "Friend Guard"
        self.hidAbBool     = False

class litleo(pokemon):
    def __init__(self):
        self.pokedex       = 667.0
        self.species       = "Litleo"
        self.nature        = self.generateNature()
        self.type          = ["Fire", "Normal"]
       # self.level         = self.generateLevel(1, 34)
        self.hp            = 62
        self.attack        = 50
        self.defense       = 58
        self.spAtk         = 73
        self.spDef         = 54
        self.speed         = 72
        self.friend        = 70
        self.gender        = self.generateGender(12.5)
        self.abilities     = ["Rivalry", "Unnerve"]
        self.ability       = ""
        self.hiddenAbility = "Moxie"
        self.hidAbBool     = False

class pyroar(pokemon):
    def __init__(self):
        self.pokedex       = 668.0
        self.species       = "Pyraor"
        self.nature        = self.generateNature()
        self.type          = ["Fire", "Normal"]
       # self.level         = self.generateLevel(35, 100)
        self.hp            = 82
        self.attack        = 68
        self.defense       = 72
        self.spAtk         = 109
        self.spDef         = 66
        self.speed         = 106
        self.friend        = 70
        self.gender        = self.generateGender(12.5)
        self.abilities     = ["Rivalry", "Unnerve"]
        self.ability       = ""
        self.hiddenAbility = "Moxie"
        self.hidAbBool     = False

class flabebe(pokemon):
    def __init__(self):
        self.pokedex       = 669.0
        self.species       = "Flabébé"
        self.nature        = self.generateNature()
        self.type          = ["Fairy"]
       # self.level         = self.generateLevel(1, 18)
        self.hp            = 44
        self.attack        = 38
        self.defense       = 39
        self.spAtk         = 61
        self.spDef         = 79
        self.speed         = 42
        self.friend        = 70
        self.gender        = True                           # Flababes are always female
        self.abilities     = [""]
        self.ability       = "Flower Veil"
        self.hiddenAbility = "Symbiosis"
        self.hidAbBool     = False

class floette(pokemon):
    def __init__(self):
        self.pokedex       = 670.0
        self.species       = "Floette"
        self.nature        = self.generateNature()
        self.type          = ["Fairy"]
       # self.level         = self.generateLevel(19, 100)
        self.hp            = 54
        self.attack        = 45
        self.defense       = 47
        self.spAtk         = 75
        self.spDef         = 98
        self.speed         = 52
        self.friend        = 70
        self.gender        = True                           # Floettes are always female
        self.abilities     = [""]
        self.ability       = "Flower Veil"
        self.hiddenAbility = "Symbiosis"
        self.hidAbBool     = False

class florges(pokemon):
    def __init__(self):
        self.pokedex       = 671.0
        self.species       = "Florges"
        self.nature        = self.generateNature()
        self.type          = ["Fairy"]
       # self.level         = self.generateLevel(1, 100)     # TODO: Test this is correct
        self.hp            = 78
        self.attack        = 65
        self.defense       = 68
        self.spAtk         = 112
        self.spDef         = 154
        self.speed         = 75
        self.friend        = 70
        self.gender        = True                           # Florges are always female
        self.abilities     = [""]
        self.ability       = "Flower Veil"
        self.hiddenAbility = "Symbiosis"
        self.hidAbBool     = False
        
class skiddo(pokemon):
    def __init__(self):
        self.pokedex       = 672.0
        self.species       = "Skiddo"
        self.nature        = self.generateNature()
        self.type          = ["Grass"]
      #  self.level         = self.generateLevel(1, 31)
        self.hp            = 66
        self.attack        = 65
        self.defense       = 48
        self.spAtk         = 62
        self.spDef         = 57
        self.speed         = 52
        self.friend        = 70
        self.gender        = self.generateGender(50)              
        self.abilities     = [""]
        self.ability       = "Sap Sipper"
        self.hiddenAbility = "Grasse Pelt"
        self.hidAbBool     = False

class gogoat(pokemon):
    def __init__(self):
        self.pokedex       = 673.0
        self.species       = "Gogoat"
        self.nature        = self.generateNature()
        self.type          = ["Grass"]
       # self.level         = self.generateLevel(32, 100)
        self.hp            = 123
        self.attack        = 100
        self.defense       = 62
        self.spAtk         = 97
        self.spDef         = 81
        self.speed         = 68
        self.friend        = 70
        self.gender        = self.generateGender(50)              
        self.abilities     = [""]
        self.ability       = "Sap Sipper"
        self.hiddenAbility = "Grasse Pelt"
        self.hidAbBool     = False

class xerneas(pokemon):
    def __init__(self):
        self.pokedex       = 716.0
        self.species       = "Xerneas"
        self.nature        = self.generateNature()
        self.type          = ["Fairy"]
      #  self.level         = self.generateLevel(1, 100)
        self.hp            = 126
        self.attack        = 131
        self.defense       = 95
        self.spAtk         = 131
        self.spDef         = 98
        self.speed         = 99
        self.friend        = 70
        self.gender        = self.generateGender(0)              
        self.abilities     = [""]
        self.ability       = "Fairy Aura"
        self.hiddenAbility = ""
        self.hidAbBool     = False

class yveltal(pokemon):
    def __init__(self):
        self.pokedex       = 717.0
        self.species       = "Yveltal"
        self.nature        = self.generateNature()
        self.type          = ["Dark", "Flying"]
       # self.level         = self.generateLevel(1, 100)
        self.hp            = 126
        self.attack        = 131
        self.defense       = 95
        self.spAtk         = 131
        self.spDef         = 98
        self.speed         = 99
        self.friend        = 70
        self.gender        = self.generateGender(0)              
        self.abilities     = [""]
        self.ability       = "Dark Aura"
        self.hiddenAbility = ""
        self.hidAbBool     = False

class zygarde(pokemon):
    def __init__(self):
        self.pokedex       = 718.0
        self.species       = "Zygarde"
        self.nature        = self.generateNature()
        self.type          = ["Dragon", "Ground"]
      #  self.level         = self.generateLevel(1, 100)
        self.hp            = 108
        self.attack        = 100
        self.defense       = 121
        self.spAtk         = 81
        self.spDef         = 95
        self.speed         = 95
        self.friend        = 70
        self.gender        = self.generateGender(0)              
        self.abilities     = [""]
        self.ability       = "Aura Break"
        self.hiddenAbility = ""
        self.hidAbBool     = False

class diancie(pokemon):
    def __init__(self):
        self.pokedex       = 719.0
        self.species       = "Diancie"
        self.nature        = self.generateNature()
        self.type          = ["Rock", "Fairy"]
      #  self.level         = self.generateLevel(1, 100)
        self.hp            = 50
        self.attack        = 160
        self.defense       = 110
        self.spAtk         = 160
        self.spDef         = 110
        self.speed         = 110
        self.friend        = 70
        self.gender        = self.generateGender(0)              
        self.abilities     = [""]
        self.ability       = "Clear Body"
        self.hiddenAbility = ""
        self.hidAbBool     = False

class hoopa(pokemon):
    def __init__(self):
        self.pokedex       = 720.0
        self.species       = "Hoopa"
        self.nature        = self.generateNature()
        self.type          = ["Psychic", "Ghost"]
        #self.level         = self.generateLevel(1, 100)
        self.hp            = 80
        self.attack        = 110
        self.defense       = 60
        self.spAtk         = 150
        self.spDef         = 130
        self.speed         = 70
        self.friend        = 70
        self.gender        = self.generateGender(0)              
        self.abilities     = [""]
        self.ability       = "Magician"
        self.hiddenAbility = ""
        self.hidAbBool     = False

class volcanion(pokemon):
    def __init__(self):
        self.pokedex       = 721.0
        self.species       = "Volcanion"
        self.nature        = self.generateNature()
        self.type          = ["Fire", "Water"]
       # self.level         = self.generateLevel(1, 100)
        self.hp            = 80
        self.attack        = 110
        self.defense       = 120
        self.spAtk         = 130
        self.spDef         = 90
        self.speed         = 70
        self.friend        = 70
        self.gender        = self.generateGender(0)              
        self.abilities     = [""]
        self.ability       = "Water Absorb"
        self.hiddenAbility = ""
        self.hidAbBool     = False

class rowlet(pokemon):
    def __init__(self):
        self.pokedex       = 722.0
        self.species       = "Rowlet"
        self.nature        = self.generateNature()
        self.type          = ["Grass", "Flying"]
        self.maxLevel      = 17
        #self.level         = self.generateLevel(1, self.maxLevel - 1)
        self.hp            = 68
        self.attack        = 55
        self.defense       = 55
        self.spAtk         = 50
        self.spDef         = 50
        self.speed         = 42
        self.friend        = 70
        self.gender        = self.generateGender(87.5)
        self.abilities     = []
        self.ability       = "Overgrow"
        self.hiddenAbility = "Long Reach"
        self.hidAbBool     = False

class litten(pokemon):
    def __init__(self):
        self.pokedex       = 725.0
        self.species       = "Litten"
        self.nature        = self.generateNature()
        self.type          = ["Fire"]
        self.maxLevel      = 17
        #self.level         = self.generateLevel(1, self.maxLevel - 1)
        self.hp            = 45
        self.attack        = 65
        self.defense       = 40
        self.spAtk         = 60
        self.spDef         = 40
        self.speed         = 70
        self.friend        = 70
        self.gender        = self.generateGender(87.5)
        self.abilities     = []
        self.ability       = "Blaze"
        self.hiddenAbility = "Intimidate"
        self.hidAbBool     = False

class popplio(pokemon):
    def __init__(self):
        self.pokedex       = 728.0
        self.species       = "Popplio"
        self.nature        = self.generateNature()
        self.type          = ["Water"]
        self.maxLevel      = 17
        #self.level         = self.generateLevel(1, self.maxLevel - 1)
        self.hp            = 50
        self.attack        = 54
        self.defense       = 54
        self.spAtk         = 66
        self.spDef         = 56
        self.speed         = 40
        self.friend        = 70
        self.gender        = self.generateGender(87.5)
        self.abilities     = []
        self.ability       = "Torrent"
        self.hiddenAbility = "LiquidVoice"
        self.hidAbBool     = False

class typeNull(pokemon):
    def __init__(self):
        self.pokedex       = 772.0
        self.species       = "Type: Null"
        self.nature        = self.generateNature()
        self.type          = ["Normal"]
       # self.level         = self.generateLevel(1, 100)
        self.hp            = 95
        self.attack        = 95
        self.defense       = 95
        self.spAtk         = 95
        self.spDef         = 95
        self.speed         = 59
        self.friend        = 70
        self.gender        = self.generateGender(0)              
        self.abilities     = [""]
        self.ability       = "Battle Armor"
        self.hiddenAbility = ""
        self.hidAbBool     = False

class silvally(pokemon):
    def __init__(self):
        self.pokedex       = 773.0
        self.species       = "Silvally"
        self.nature        = self.generateNature()
        self.type          = ["Normal"]
       # self.level         = self.generateLevel(1, 100)
        self.hp            = 95
        self.attack        = 95
        self.defense       = 95
        self.spAtk         = 95
        self.spDef         = 95
        self.speed         = 95
        self.friend        = 70
        self.gender        = self.generateGender(0)     #Genderless              
        self.abilities     = [""]
        self.ability       = "Shields Down"
        self.hiddenAbility = ""
        self.hidAbBool     = False

class minior(pokemon):
    def __init__(self):
        self.pokedex       = 774.0
        self.species       = "Minior"
        self.nature        = self.generateNature()
        self.type          = ["Rock", "Flying"]
        #self.level         = self.generateLevel(1, 100)
        self.hp            = 60
        self.attack        = 100
        self.defense       = 60
        self.spAtk         = 100
        self.spDef         = 60
        self.speed         = 120
        self.friend        = 70
        self.gender        = self.generateGender(0)              
        self.abilities     = [""]
        self.ability       = "RKS System"
        self.hiddenAbility = ""
        self.hidAbBool     = False

class Komala(pokemon):
    def __init__(self):
        self.pokedex       = 775.0
        self.species       = "Komala"
        self.nature        = self.generateNature()
        self.type          = ["Normal"]
       # self.level         = self.generateLevel(1, 100)
        self.hp            = 65
        self.attack        = 115
        self.defense       = 65
        self.spAtk         = 75
        self.spDef         = 95
        self.speed         = 65
        self.friend        = 70
        self.gender        = self.generateGender(50)              
        self.abilities     = [""]
        self.ability       = "Comatose"
        self.hiddenAbility = ""
        self.hidAbBool     = False

class tapuKoko(pokemon):
    def __init__(self):
        self.pokedex       = 785.0
        self.species       = "Tapu Koko"
        self.nature        = self.generateNature()
        self.type          = ["Electric", "Fairy"]
       # self.level         = self.generateLevel(1, 100)
        self.hp            = 70
        self.attack        = 115
        self.defense       = 85
        self.spAtk         = 95
        self.spDef         = 75
        self.speed         = 130
        self.friend        = 70
        self.gender        = self.generateGender(0)              
        self.abilities     = [""]
        self.ability       = "Electric Surge"
        self.hiddenAbility = "Telepathy"
        self.hidAbBool     = False

class tapuLele(pokemon):
    def __init__(self):
        self.pokedex       = 786.0
        self.species       = "Tapu Lele"
        self.nature        = self.generateNature()
        self.type          = ["Psychic", "Fairy"]
       # self.level         = self.generateLevel(1, 100)
        self.hp            = 70
        self.attack        = 85
        self.defense       = 75
        self.spAtk         = 130
        self.spDef         = 115
        self.speed         = 95
        self.friend        = 70
        self.gender        = self.generateGender(0)              
        self.abilities     = [""]
        self.ability       = "Psychic Surge"
        self.hiddenAbility = "Telepathy"
        self.hidAbBool     = False

class tapuBulu(pokemon):
    def __init__(self):
        self.pokedex       = 787.0
        self.species       = "Tapu Bulu"
        self.nature        = self.generateNature()
        self.type          = ["Grass", "Fairy"]
       # self.level         = self.generateLevel(1, 100)
        self.hp            = 70
        self.attack        = 130
        self.defense       = 115
        self.spAtk         = 85
        self.spDef         = 95
        self.speed         = 75
        self.friend        = 70
        self.gender        = self.generateGender(0)              
        self.abilities     = [""]
        self.ability       = "Grassy Surge"
        self.hiddenAbility = "Telepathy"
        self.hidAbBool     = False

class tapuFini(pokemon):
    def __init__(self):
        self.pokedex       = 788.0
        self.species       = "Tapu Fini"
        self.nature        = self.generateNature()
        self.type          = ["Water", "Fairy"]
       # self.level         = self.generateLevel(1, 100)
        self.hp            = 70
        self.attack        = 75
        self.defense       = 115
        self.spAtk         = 95
        self.spDef         = 130
        self.speed         = 85
        self.friend        = 70
        self.gender        = self.generateGender(0)              
        self.abilities     = [""]
        self.ability       = "Misty Surge"
        self.hiddenAbility = "Telepathy"
        self.hidAbBool     = False

class cosmog(pokemon):
    def __init__(self):
        self.pokedex       = 789.0
        self.species       = "Cosmog"
        self.nature        = self.generateNature()
        self.type          = ["Psychic"]
       # self.level         = self.generateLevel(1, 100)
        self.hp            = 43
        self.attack        = 29
        self.defense       = 31
        self.spAtk         = 29
        self.spDef         = 31
        self.speed         = 37
        self.friend        = 70
        self.gender        = self.generateGender(0)              
        self.abilities     = [""]
        self.ability       = "Unaware"
        self.hiddenAbility = ""
        self.hidAbBool     = False

class cosmoem(pokemon):
    def __init__(self):
        self.pokedex       = 790.0
        self.species       = "Cosmoem"
        self.nature        = self.generateNature()
        self.type          = ["Psychic"]
      #  self.level         = self.generateLevel(1, 100)
        self.hp            = 43
        self.attack        = 29
        self.defense       = 131
        self.spAtk         = 29
        self.spDef         = 131
        self.speed         = 37
        self.friend        = 70
        self.gender        = self.generateGender(0)              
        self.abilities     = [""]
        self.ability       = "Sturdy"
        self.hiddenAbility = ""
        self.hidAbBool     = False

class solgaleo(pokemon):
    def __init__(self):
        self.pokedex       = 791.0
        self.species       = "Solgaleo"
        self.nature        = self.generateNature()
        self.type          = ["Psychic", "Steel"]
       # self.level         = self.generateLevel(1, 100)
        self.hp            = 137
        self.attack        = 137
        self.defense       = 107
        self.spAtk         = 113
        self.spDef         = 89
        self.speed         = 97
        self.friend        = 70
        self.gender        = self.generateGender(0)              
        self.abilities     = [""]
        self.ability       = "Full Metal Body"
        self.hiddenAbility = ""
        self.hidAbBool     = False

class lunala(pokemon):
    def __init__(self):
        self.pokedex       = 792.0
        self.species       = "Lunala"
        self.nature        = self.generateNature()
        self.type          = ["Psychic", "Ghost"]
        #self.level         = self.generateLevel(1, 100)
        self.hp            = 137
        self.attack        = 113
        self.defense       = 89
        self.spAtk         = 137
        self.spDef         = 107
        self.speed         = 97
        self.friend        = 70
        self.gender        = self.generateGender(0)              
        self.abilities     = [""]
        self.ability       = "Shadow Shield"
        self.hiddenAbility = ""
        self.hidAbBool     = False

class nihilego(pokemon):
    def __init__(self):
        self.pokedex       = 793.0
        self.species       = "Nihilego"
        self.nature        = self.generateNature()
        self.type          = ["Rock", "Poison"]
       # self.level         = self.generateLevel(1, 100)
        self.hp            = 109
        self.attack        = 53
        self.defense       = 47
        self.spAtk         = 127
        self.spDef         = 131
        self.speed         = 103
        self.friend        = 70
        self.gender        = self.generateGender(0)              
        self.abilities     = [""]
        self.ability       = "Beast Boost"
        self.hiddenAbility = ""
        self.hidAbBool     = False

class buzzwole(pokemon):
    def __init__(self):
        self.pokedex       = 794.0
        self.species       = "Buzzwole"
        self.nature        = self.generateNature()
        self.type          = ["Bug", "Fight"]
      #  self.level         = self.generateLevel(1, 100)
        self.hp            = 107
        self.attack        = 139
        self.defense       = 139
        self.spAtk         = 53
        self.spDef         = 53
        self.speed         = 79
        self.friend        = 70
        self.gender        = self.generateGender(0)              
        self.abilities     = [""]
        self.ability       = "Beast Boost"
        self.hiddenAbility = ""
        self.hidAbBool     = False

class pheromosa(pokemon):
    def __init__(self):
        self.pokedex       = 795.0
        self.species       = "Pheromosa"
        self.nature        = self.generateNature()
        self.type          = ["Bug", "Fight"]
       # self.level         = self.generateLevel(1, 100)
        self.hp            = 71
        self.attack        = 137
        self.defense       = 37
        self.spAtk         = 137
        self.spDef         = 37
        self.speed         = 151
        self.friend        = 70
        self.gender        = self.generateGender(0)              
        self.abilities     = [""]
        self.ability       = "Beast Boost"
        self.hiddenAbility = ""
        self.hidAbBool     = False

class xurkitree(pokemon):
    def __init__(self):
        self.pokedex       = 796.0
        self.species       = "Xurkitree"
        self.nature        = self.generateNature()
        self.type          = ["Electric"]
       # self.level         = self.generateLevel(1, 100)
        self.hp            = 83
        self.attack        = 89
        self.defense       = 71
        self.spAtk         = 173
        self.spDef         = 71
        self.speed         = 83
        self.friend        = 70
        self.gender        = self.generateGender(0)              
        self.abilities     = [""]
        self.ability       = "Beast Boost"
        self.hiddenAbility = ""
        self.hidAbBool     = False

class celesteela(pokemon):
    def __init__(self):
        self.pokedex       = 797.0
        self.species       = "Celesteela"
        self.nature        = self.generateNature()
        self.type          = ["Steel", "Flying"]
       # self.level         = self.generateLevel(1, 100)
        self.hp            = 97
        self.attack        = 101
        self.defense       = 103
        self.spAtk         = 107
        self.spDef         = 101
        self.speed         = 61
        self.friend        = 70
        self.gender        = self.generateGender(0)              
        self.abilities     = [""]
        self.ability       = "Beast Boost"
        self.hiddenAbility = ""
        self.hidAbBool     = False

class kartana(pokemon):
    def __init__(self):
        self.pokedex       = 798.0
        self.species       = "Kartana"
        self.nature        = self.generateNature()
        self.type          = ["Grass", "Steel"]
     #   self.level         = self.generateLevel(1, 100)
        self.hp            = 59
        self.attack        = 181
        self.defense       = 131
        self.spAtk         = 59
        self.spDef         = 31
        self.speed         = 109
        self.friend        = 70
        self.gender        = self.generateGender(0)              
        self.abilities     = [""]
        self.ability       = "Beast Boost"
        self.hiddenAbility = ""
        self.hidAbBool     = False

class guzzlord(pokemon):
    def __init__(self):
        self.pokedex       = 799.0
        self.species       = "Guzzlord"
        self.nature        = self.generateNature()
        self.type          = ["Dark", "Dragon"]
      #  self.level         = self.generateLevel(1, 100)
        self.hp            = 223
        self.attack        = 101
        self.defense       = 53
        self.spAtk         = 97
        self.spDef         = 53
        self.speed         = 43
        self.friend        = 70
        self.gender        = self.generateGender(0)              
        self.abilities     = [""]
        self.ability       = "Beast Boost"
        self.hiddenAbility = ""
        self.hidAbBool     = False
        
class necrozma(pokemon):
    def __init__(self):
        self.pokedex       = 800.0
        self.species       = "Necrozma"
        self.nature        = self.generateNature()
        self.type          = ["Psychic"]
      #  self.level         = self.generateLevel(1, 100)
        self.hp            = 97
        self.attack        = 107
        self.defense       = 101
        self.spAtk         = 127
        self.spDef         = 89
        self.speed         = 79
        self.friend        = 70
        self.gender        = self.generateGender(0)              
        self.abilities     = [""]
        self.ability       = "Prism Armor"
        self.hiddenAbility = ""
        self.hidAbBool     = False

class magearna(pokemon):
    def __init__(self):
        self.pokedex       = 801.0
        self.species       = "Magearna"
        self.nature        = self.generateNature()
        self.type          = ["Steel", "Fairy"]
     #   self.level         = self.generateLevel(1, 100)
        self.hp            = 80
        self.attack        = 95
        self.defense       = 115
        self.spAtk         = 130
        self.spDef         = 115
        self.speed         = 65
        self.friend        = 70
        self.gender        = self.generateGender(0)              
        self.abilities     = [""]
        self.ability       = "Soul-Heart"
        self.hiddenAbility = ""
        self.hidAbBool     = False

class marshadow(pokemon):
    def __init__(self):
        self.pokedex       = 802.0
        self.species       = "Marshadow"
        self.nature        = self.generateNature()
        self.type          = ["Fight", "Ghost"]
      #  self.level         = self.generateLevel(1, 100)
        self.hp            = 90
        self.attack        = 125
        self.defense       = 80
        self.spAtk         = 90
        self.spDef         = 90
        self.speed         = 125
        self.friend        = 70
        self.gender        = self.generateGender(0)              
        self.abilities     = [""]
        self.ability       = "Technician"
        self.hiddenAbility = ""
        self.hidAbBool     = False

class poipole(pokemon):
    def __init__(self):
        self.pokedex       = 803.0
        self.species       = "Poipole"
        self.nature        = self.generateNature()
        self.type          = ["Poison"]
      #  self.level         = self.generateLevel(1, 100)
        self.hp            = 67
        self.attack        = 73
        self.defense       = 67
        self.spAtk         = 73
        self.spDef         = 67
        self.speed         = 73
        self.friend        = 70
        self.gender        = self.generateGender(0)              
        self.abilities     = [""]
        self.ability       = "Beast Boost"
        self.hiddenAbility = ""
        self.hidAbBool     = False

class naganadel(pokemon):
    def __init__(self):
        self.pokedex       = 804.0
        self.species       = "Naganadel"
        self.nature        = self.generateNature()
        self.type          = ["Poison", "Dragon"]
       # self.level         = self.generateLevel(1, 100)
        self.hp            = 73
        self.attack        = 73
        self.defense       = 73
        self.spAtk         = 127
        self.spDef         = 73
        self.speed         = 121
        self.friend        = 70
        self.gender        = self.generateGender(0)              
        self.abilities     = [""]
        self.ability       = "Beast Boost"
        self.hiddenAbility = ""
        self.hidAbBool     = False

class stakataka(pokemon):
    def __init__(self):
        self.pokedex       = 805.0
        self.species       = "Stakataka"
        self.nature        = self.generateNature()
        self.type          = ["Rock", "Steel"]
       # self.level         = self.generateLevel(1, 100)
        self.hp            = 61
        self.attack        = 131
        self.defense       = 211
        self.spAtk         = 53
        self.spDef         = 101
        self.speed         = 13
        self.friend        = 70
        self.gender        = self.generateGender(0)              
        self.abilities     = [""]
        self.ability       = "Beast Boost"
        self.hiddenAbility = ""
        self.hidAbBool     = False

class blacephalon(pokemon):
    def __init__(self):
        self.pokedex       = 806.0
        self.species       = "Blacephalon"
        self.nature        = self.generateNature()
        self.type          = ["Fire", "Ghost"]
        #self.level         = self.generateLevel(1, 100)
        self.hp            = 53
        self.attack        = 127
        self.defense       = 53
        self.spAtk         = 151
        self.spDef         = 79
        self.speed         = 107
        self.friend        = 70
        self.gender        = self.generateGender(0)              
        self.abilities     = [""]
        self.ability       = "Beast Boost"
        self.hiddenAbility = ""
        self.hidAbBool     = False

class zeraora(pokemon):
    def __init__(self):
        self.pokedex       = 807.0
        self.species       = "Zeraora"
        self.nature        = self.generateNature()
        self.type          = ["Electric"]
       # self.level         = self.generateLevel(1, 100)
        self.hp            = 88
        self.attack        = 112
        self.defense       = 75
        self.spAtk         = 102
        self.spDef         = 80
        self.speed         = 143
        self.friend        = 70
        self.gender        = self.generateGender(0)              
        self.abilities     = [""]
        self.ability       = "Volt Absorb"
        self.hiddenAbility = ""
        self.hidAbBool     = False

class meltan(pokemon):
    def __init__(self):
        self.pokedex       = 808.0
        self.species       = "Meltan"
        self.nature        = self.generateNature()
        self.type          = ["Steel"]
       # self.level         = self.generateLevel(1, 100)
        self.hp            = 46
        self.attack        = 65
        self.defense       = 65
        self.spAtk         = 55
        self.spDef         = 35
        self.speed         = 34
        self.friend        = 70
        self.gender        = self.generateGender(0)              
        self.abilities     = [""]
        self.ability       = "Magnet Pull"
        self.hiddenAbility = ""
        self.hidAbBool     = False

class melmetal(pokemon):
    def __init__(self):
        self.pokedex       = 809.0
        self.species       = "Melmetal"
        self.nature        = self.generateNature()
        self.type          = ["Steel"]
       # self.level         = self.generateLevel(1, 100)
        self.hp            = 135
        self.attack        = 143
        self.defense       = 143
        self.spAtk         = 80
        self.spDef         = 65
        self.speed         = 34
        self.friend        = 70
        self.gender        = self.generateGender(0)              
        self.abilities     = [""]
        self.ability       = "Iron Fist"
        self.hiddenAbility = ""
        self.hidAbBool     = False

class grookey(pokemon):
    def __init__(self):
        self.pokedex       = 810.0
        self.species       = "Oshawott"
        self.nature        = self.generateNature()
        self.type          = ["Grass"]
        self.maxLevel      = 16
       # self.level         = self.generateLevel(1, self.maxLevel - 1)
        self.hp            = 50
        self.attack        = 65
        self.defense       = 50
        self.spAtk         = 40
        self.spDef         = 40
        self.speed         = 65
        self.friend        = 70
        self.gender        = self.generateGender(87.5)
        self.abilities     = []
        self.ability       = "Overgrow"
        self.hiddenAbility = "Grassey Surge"
        self.hidAbBool     = False

class scorbunny(pokemon):
    def __init__(self):
        self.pokedex       = 813.0
        self.species       = "Scorbunny"
        self.nature        = self.generateNature()
        self.type          = ["Fire"]
        self.maxLevel      = 16
       # self.level         = self.generateLevel(1, self.maxLevel - 1)
        self.hp            = 50
        self.attack        = 71
        self.defense       = 40
        self.spAtk         = 40
        self.spDef         = 40
        self.speed         = 69
        self.friend        = 70
        self.gender        = self.generateGender(87.5)
        self.abilities     = []
        self.ability       = "Blaze"
        self.hiddenAbility = "Libero"
        self.hidAbBool     = False

class sobble(pokemon):
    def __init__(self):
        self.pokedex       = 816.0
        self.species       = "Sobble"
        self.nature        = self.generateNature()
        self.type          = ["Water"]
        self.maxLevel      = 16
       # self.level         = self.generateLevel(1, self.maxLevel - 1)
        self.hp            = 50
        self.attack        = 40
        self.defense       = 40
        self.spAtk         = 70
        self.spDef         = 40
        self.speed         = 70
        self.friend        = 70
        self.gender        = self.generateGender(87.5)
        self.abilities     = []
        self.ability       = "Torrent"
        self.hiddenAbility = "Sniper"
        self.hidAbBool     = False

class zacian(pokemon):
    def __init__(self):
        self.pokedex       = 888.0
        self.species       = "Zacian"
        self.nature        = self.generateNature()
        self.type          = ["Fairy"]
      #  self.level         = self.generateLevel(1, 100)
        self.hp            = 92
        self.attack        = 130
        self.defense       = 115
        self.spAtk         = 80
        self.spDef         = 115
        self.speed         = 138
        self.friend        = 70
        self.gender        = self.generateGender(0)              
        self.abilities     = [""]
        self.ability       = "Intrepid Sword"
        self.hiddenAbility = ""
        self.hidAbBool     = False

class zamazenta(pokemon):
    def __init__(self):
        self.pokedex       = 889.0
        self.species       = "Zamazenta"
        self.nature        = self.generateNature()
        self.type          = ["Fight"]
       # self.level         = self.generateLevel(1, 100)
        self.hp            = 92
        self.attack        = 130
        self.defense       = 115
        self.spAtk         = 80
        self.spDef         = 115
        self.speed         = 138
        self.friend        = 70
        self.gender        = self.generateGender(0)              
        self.abilities     = [""]
        self.ability       = "Dauntless Shield"
        self.hiddenAbility = ""
        self.hidAbBool     = False

class eternatus(pokemon):
    def __init__(self):
        self.pokedex       = 890.0
        self.species       = "Eternatus"
        self.nature        = self.generateNature()
        self.type          = ["Poison", "Dragon"]
       # self.level         = self.generateLevel(1, 100)
        self.hp            = 255
        self.attack        = 115
        self.defense       = 250
        self.spAtk         = 125
        self.spDef         = 250
        self.speed         = 130
        self.friend        = 70
        self.gender        = self.generateGender(0)              
        self.abilities     = [""]
        self.ability       = "Pressure"
        self.hiddenAbility = ""
        self.hidAbBool     = False

        
pokemon = flabebe()
#pokemon.setNickname("Paul")
#print(pokemon.getNickname())
#print(pokemon.getPokedex())
#print(pokemon.getSpecies())
#print(pokemon.getNature())
#print(pokemon.getType())
#print(pokemon.getLevel())
#print(pokemon.getHP())
#print(pokemon.getAttack())
#print(pokemon.getDefense())
#print(pokemon.getSpAtk())
#print(pokemon.getSpDef())
#print(pokemon.getSpeed())
#print(pokemon.getFriend())
#print(pokemon.getGender())
#print(pokemon.getAbilities())
#print(pokemon.getAbility())
#print(pokemon.getHiddenAbility())
#print(pokemon.getHiddenBool())
pokemon.describe()

# note: spelling it flavour for now because in Sassi's words: "fuck america"

# TODO:
#  Synchronize
#  Mega 'mon
