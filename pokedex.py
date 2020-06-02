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
        self.pokedex       = 1.0
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
    def __init__(self):
        self.pokedex       = 2.0
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
    def __init__(self):
        self.pokedex       = 3.0
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
    def __init__(self):
        self.pokedex       = 4.0
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
    def __init__(self):
        self.pokedex       = 5.0
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
    def __init__(self):
        self.pokedex       = 6.0
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

class squirtle(pokemon):
    def __init__(self):
        self.pokedex       = 7.0
        self.species       = "Squirtle"
        self.nature        = self.generateNature()
        self.type          = ["Water"]
        self.level         = self.generateLevel(1, 15)
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
        self.level         = self.generateLevel(16, 35)
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
        self.level         = self.generateLevel(36, 100)
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
        self.level         = self.generateLevel(1, 6)           
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
        self.level         = self.generateLevel(7, 9)           
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
        self.level         = self.generateLevel(10, 100)           
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
        self.level         = self.generateLevel(1, 6)           
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
        self.level         = self.generateLevel(7, 9)           
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
        self.level         = self.generateLevel(10, 100)           
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
        self.level         = self.generateLevel(1, 17)           
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
        self.level         = self.generateLevel(18, 35)           
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
        self.level         = self.generateLevel(36, 100)           
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
        self.level         = self.generateLevel(1, 19)           
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
        self.level         = self.generateLevel(1, 19)           
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
        self.level         = self.generateLevel(20, 100)           
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
        self.level         = self.generateLevel(20, 100)           
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
        self.level         = self.generateLevel(1, 19)           
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
        self.level         = self.generateLevel(20, 100)           
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
        self.level         = self.generateLevel(1, 21)           
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
        self.level         = self.generateLevel(1, 21)           
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
        self.level         = self.generateLevel(1, 100)           
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
        self.level         = self.generateLevel(1, 100)           
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
        self.level         = self.generateLevel(1, 100)           
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
        self.level         = self.generateLevel(1, 100)           
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
        self.level         = self.generateLevel(1, 21)           
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
        self.level         = self.generateLevel(1, 100)           
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
        self.level         = self.generateLevel(22, 100)           
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
        self.level         = self.generateLevel(1, 100)           
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
        self.level         = self.generateLevel(1, 15)           
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
        self.level         = self.generateLevel(16, 100)           
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
        self.level         = self.generateLevel(16, 100)           
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
        self.level         = self.generateLevel(1, 15)           
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
        self.level         = self.generateLevel(16, 100)           
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
        self.level         = self.generateLevel(16, 100)           
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
        self.level         = self.generateLevel(1, 100)           
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
        self.level         = self.generateLevel(1, 100)           
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
        self.level         = self.generateLevel(1, 100)           
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
        self.level         = self.generateLevel(1, 100)           
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
        self.level         = self.generateLevel(1, 100)           
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
        self.level         = self.generateLevel(1, 100)           
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
        self.level         = self.generateLevel(1, 100)           
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
        self.level         = self.generateLevel(1, 100)           
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
        self.level         = self.generateLevel(1, 21)           
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
        self.level         = self.generateLevel(22, 100)           
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
        self.level         = self.generateLevel(1, 20)           
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
        self.level         = self.generateLevel(22, 100)           
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
        self.level         = self.generateLevel(22, 100)           
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
        self.level         = self.generateLevel(1, 23)           
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
        self.level         = self.generateLevel(24, 100)           
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
        self.level         = self.generateLevel(1, 30)           
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
        self.level         = self.generateLevel(31, 100)           
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
        self.level         = self.generateLevel(1, 25)           
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
        self.level         = self.generateLevel(1, 25)           
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
        self.level         = self.generateLevel(26, 100)           
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
        self.level         = self.generateLevel(26, 100)           
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
        self.level         = self.generateLevel(1, 27)           
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
        self.level         = self.generateLevel(1, 100)           
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
        self.level         = self.generateLevel(1, 27)           
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
        self.level         = self.generateLevel(28, 100)           
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
        self.level         = self.generateLevel(1, 100)           
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
        self.level         = self.generateLevel(1, 32)           
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
        self.level         = self.generateLevel(33, 100)           
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
        self.level         = self.generateLevel(1, 27)           
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
        self.level         = self.generateLevel(28, 100)           
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
        self.level         = self.generateLevel(1, 100)           
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
        self.level         = self.generateLevel(1, 100)           
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
        self.level         = self.generateLevel(1, 24)           
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
        self.level         = self.generateLevel(25, 100)           
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
        self.level         = self.generateLevel(25, 100)           
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
        self.level         = self.generateLevel(1, 15)           
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
        self.level         = self.generateLevel(16, 100)           
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
        self.level         = self.generateLevel(16, 100)           
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
        self.level         = self.generateLevel(1, 27)           
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
        self.level         = self.generateLevel(28, 100)           
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
        self.level         = self.generateLevel(28, 100)           
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
        self.level         = self.generateLevel(1, 20)           
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
        self.level         = self.generateLevel(21, 100)           
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
        self.level         = self.generateLevel(21, 100)           
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
        self.level         = self.generateLevel(1, 29)           
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
        self.level         = self.generateLevel(30, 100)           
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
        self.level         = self.generateLevel(1, 24)           
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
        self.level         = self.generateLevel(1, 24)           
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
        self.level         = self.generateLevel(25, 100)           
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
        self.level         = self.generateLevel(25, 100)           
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
        self.level         = self.generateLevel(25, 100)           
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
        self.level         = self.generateLevel(25, 100)           
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
        self.level         = self.generateLevel(1, 39)           
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
        self.level         = self.generateLevel(1, 39)           
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
        self.level         = self.generateLevel(40, 100)           
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
        self.level         = self.generateLevel(40, 100)           
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
        self.level         = self.generateLevel(1, 36)           
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
        self.level         = self.generateLevel(37, 100)           
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
        self.level         = self.generateLevel(1, 29)           
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
        self.level         = self.generateLevel(1, 29)           
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
        self.level         = self.generateLevel(1, 100)           
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
        self.level         = self.generateLevel(1, 100)           
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
        self.level         = self.generateLevel(1, 30)           
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
        self.level         = self.generateLevel(31, 100)           
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
        self.level         = self.generateLevel(1, 33)
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
        self.level         = self.generateLevel(34, 100)
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
        self.level         = self.generateLevel(1, 37)
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
        self.level         = self.generateLevel(1, 37)
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
        self.level         = self.generateLevel(38, 100)
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
        self.pokedex       = 89.0
        self.species       = "Alolan Muk"
        self.nature        = self.generateNature()
        self.type          = ["Poison", "Dark"]
        self.level         = self.generateLevel(38, 100)
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
        self.level         = self.generateLevel(1, 100)
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
        self.level         = self.generateLevel(1, 100)
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
        self.level         = self.generateLevel(1, 24)
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
        self.level         = self.generateLevel(25, 100)
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
        self.level         = self.generateLevel(25, 100)
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
        self.level         = self.generateLevel(1, 100)
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
        self.level         = self.generateLevel(1, 25)
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
        self.level         = self.generateLevel(26, 100)
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
        self.level         = self.generateLevel(1, 27)
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
        self.level         = self.generateLevel(28, 100)
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
        
class rhydon(pokemon):
    def __init__(self):
        self.pokedex       = 112.0
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
       
class articuno(pokemon):
    def __init__(self):
        self.pokedex       = 144.0
        self.species       = "Articuno"
        self.nature        = self.generateNature()
        self.type          = ["Ice", "Flying"]
        self.level         = self.generateLevel(1, 100)
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
        self.level         = self.generateLevel(1, 100)
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
        self.level         = self.generateLevel(1, 100)
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

        
class mewtwo(pokemon):
    def __init__(self):
        self.pokedex       = 150
        self.species       = "Mewtwo"
        self.nature        = self.generateNature()
        self.type          = ["Psychic"]
        self.level         = self.generateLevel(1, 100)
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
        self.pokedex       = 151
        self.species       = "Mew"
        self.nature        = self.generateNature()
        self.type          = ["Psychic"]
        self.level         = self.generateLevel(1, 100)
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

class raikou(pokemon):
    def __init__(self):
        self.pokedex       = 243
        self.species       = "Raikou"
        self.nature        = self.generateNature()
        self.type          = ["Electric"]
        self.level         = self.generateLevel(1, 100)
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
        self.pokedex       = 244
        self.species       = "Entei"
        self.nature        = self.generateNature()
        self.type          = ["Fire"]
        self.level         = self.generateLevel(1, 100)
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
        self.pokedex       = 245
        self.species       = "Suicune"
        self.nature        = self.generateNature()
        self.type          = ["Water"]
        self.level         = self.generateLevel(1, 100)
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
        self.pokedex       = 249
        self.species       = "Lugia"
        self.nature        = self.generateNature()
        self.type          = ["Psychic", "Flying"]
        self.level         = self.generateLevel(1, 100)
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
        self.pokedex       = 250
        self.species       = "Ho-Oh"
        self.nature        = self.generateNature()
        self.type          = ["Fire", "Flying"]
        self.level         = self.generateLevel(1, 100)
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
        self.pokedex       = 251
        self.species       = "Celebi"
        self.nature        = self.generateNature()
        self.type          = ["Psychic", "Grass"]
        self.level         = self.generateLevel(1, 100)
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

class regirock(pokemon):
    def __init__(self):
        self.pokedex       = 377
        self.species       = "Regirock"
        self.nature        = self.generateNature()
        self.type          = ["Rock"]
        self.level         = self.generateLevel(1, 100)
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
        self.pokedex       = 378
        self.species       = "Regice"
        self.nature        = self.generateNature()
        self.type          = ["Ice"]
        self.level         = self.generateLevel(1, 100)
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
        self.pokedex       = 379
        self.species       = "Registeel"
        self.nature        = self.generateNature()
        self.type          = ["Steel"]
        self.level         = self.generateLevel(1, 100)
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
        self.pokedex       = 380
        self.species       = "Latias"
        self.nature        = self.generateNature()
        self.type          = ["Dragon", "Psychic"]
        self.level         = self.generateLevel(1, 100)
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
        self.pokedex       = 381
        self.species       = "Latios"
        self.nature        = self.generateNature()
        self.type          = ["Dragon", "Psychic"]
        self.level         = self.generateLevel(1, 100)
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
        self.pokedex       = 382
        self.species       = "Kyogre"
        self.nature        = self.generateNature()
        self.type          = ["Water"]
        self.level         = self.generateLevel(1, 100)
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
        self.pokedex       = 383
        self.species       = "Groudon"
        self.nature        = self.generateNature()
        self.type          = ["Ground"]
        self.level         = self.generateLevel(1, 100)
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
        self.pokedex       = 384
        self.species       = "Rayquaza"
        self.nature        = self.generateNature()
        self.type          = ["Dragon", "Flying"]
        self.level         = self.generateLevel(1, 100)
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
        self.pokedex       = 385
        self.species       = "Jirachi"
        self.nature        = self.generateNature()
        self.type          = ["Steel", "Psychic"]
        self.level         = self.generateLevel(1, 100)
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
        self.pokedex       = 386
        self.species       = "Deoxys"
        self.nature        = self.generateNature()
        self.type          = ["Psychic"]
        self.level         = self.generateLevel(1, 100)
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

class uxie(pokemon):
    def __init__(self):
        self.pokedex       = 480
        self.species       = "Uxie"
        self.nature        = self.generateNature()
        self.type          = ["Psychic"]
        self.level         = self.generateLevel(1, 100)
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
        self.pokedex       = 481
        self.species       = "Mesprit"
        self.nature        = self.generateNature()
        self.type          = ["Psychic"]
        self.level         = self.generateLevel(1, 100)
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
        self.pokedex       = 482
        self.species       = "Azelf"
        self.nature        = self.generateNature()
        self.type          = ["Psychic"]
        self.level         = self.generateLevel(1, 100)
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
        self.pokedex       = 483
        self.species       = "Dialga"
        self.nature        = self.generateNature()
        self.type          = ["Steel", "Dragon"]
        self.level         = self.generateLevel(1, 100)
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
        self.pokedex       = 484
        self.species       = "Palkia"
        self.nature        = self.generateNature()
        self.type          = ["Water", "Dragon"]
        self.level         = self.generateLevel(1, 100)
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
        self.pokedex       = 485
        self.species       = "Heatran"
        self.nature        = self.generateNature()
        self.type          = ["Fire", "Steel"]
        self.level         = self.generateLevel(1, 100)
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
        self.pokedex       = 486
        self.species       = "Regigigas"
        self.nature        = self.generateNature()
        self.type          = ["Normal"]
        self.level         = self.generateLevel(1, 100)
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
        self.pokedex       = 487
        self.species       = "Giratina"
        self.nature        = self.generateNature()
        self.type          = ["Ghost", "Dragon"]
        self.level         = self.generateLevel(1, 100)
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
        self.pokedex       = 488
        self.species       = "Cresselia"
        self.nature        = self.generateNature()
        self.type          = ["Psychic"]
        self.level         = self.generateLevel(1, 100)
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
        self.pokedex       = 489
        self.species       = "Phione"
        self.nature        = self.generateNature()
        self.type          = ["Water"]
        self.level         = self.generateLevel(1, 100)
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
        self.pokedex       = 490
        self.species       = "Manaphy"
        self.nature        = self.generateNature()
        self.type          = ["Water"]
        self.level         = self.generateLevel(1, 100)
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
        self.pokedex       = 491
        self.species       = "Darkrai"
        self.nature        = self.generateNature()
        self.type          = ["Dark"]
        self.level         = self.generateLevel(1, 100)
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
        self.pokedex       = 492
        self.species       = "Shaymin"
        self.nature        = self.generateNature()
        self.type          = ["Grass"]
        self.level         = self.generateLevel(1, 100)
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
        self.pokedex       = 493
        self.species       = "Arceus"
        self.nature        = self.generateNature()
        self.type          = ["Normal"]
        self.level         = self.generateLevel(1, 100)
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
        self.pokedex       = 494
        self.species       = "Victini"
        self.nature        = self.generateNature()
        self.type          = ["Psychic", "Fire"]
        self.level         = self.generateLevel(1, 100)
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

class chespin(pokemon):
    def __init__(self):
        self.pokedex       = 650.0
        self.species       = "Chespin"
        self.nature        = self.generateNature()
        self.type          = ["Grass"]
        self.level         = self.generateLevel(1, 15)
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
        self.level         = self.generateLevel(16, 35)
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
        self.level         = self.generateLevel(36, 100)
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
        self.level         = self.generateLevel(1, 15)
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
        self.level         = self.generateLevel(16,35)
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
        self.level         = self.generateLevel(36, 100)
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
        self.level         = self.generateLevel(1, 15)
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
        self.level         = self.generateLevel(16, 35)
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
        self.level         = self.generateLevel(1, 15)
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
        self.level         = self.generateLevel(1, 19)
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
        self.level         = self.generateLevel(20, 100)
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
        self.level         = self.generateLevel(1, 16)
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
        self.level         = self.generateLevel(17, 34)
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
        self.level         = self.generateLevel(35, 100)
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
        self.level         = self.generateLevel(1, 8)
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
        self.level         = self.generateLevel(9, 11)
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
        self.level         = self.generateLevel(12, 100)
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
        self.level         = self.generateLevel(1, 34)
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
        self.level         = self.generateLevel(35, 100)
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
        self.level         = self.generateLevel(1, 18)
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
        self.level         = self.generateLevel(19, 100)
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
        self.level         = self.generateLevel(1, 100)     # TODO: Test this is correct
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
        self.level         = self.generateLevel(1, 31)
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
        self.level         = self.generateLevel(32, 100)
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
        
class typenull(pokemon):
    def __init__(self):
        self.pokedex       = 772.0
        self.species       = "Type: Null"
        self.nature        = self.generateNature()
        self.type          = ["Normal"]
        self.level         = self.generateLevel(1, 100)
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
        self.level         = self.generateLevel(1, 100)
        self.hp            = 95
        self.attack        = 95
        self.defense       = 95
        self.spAtk         = 95
        self.spDef         = 95
        self.speed         = 95
        self.friend        = 70
        self.gender        = self.generateGender(0)              
        self.abilities     = [""]
        self.ability       = "RKS System"
        self.hiddenAbility = ""
        self.hidAbBool     = False 
        
class nihilego(pokemon):
    def __init__(self):
        self.pokedex       = 793.0
        self.species       = "Nihilego"
        self.nature        = self.generateNature()
        self.type          = ["Rock", "Poison"]
        self.level         = self.generateLevel(1, 100)
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
        self.level         = self.generateLevel(1, 100)
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
        self.level         = self.generateLevel(1, 100)
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
        self.level         = self.generateLevel(1, 100)
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
        self.level         = self.generateLevel(1, 100)
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
        self.level         = self.generateLevel(1, 100)
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
        self.level         = self.generateLevel(1, 100)
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

class poipole(pokemon):
    def __init__(self):
        self.pokedex       = 803.0
        self.species       = "Poipole"
        self.nature        = self.generateNature()
        self.type          = ["Poison"]
        self.level         = self.generateLevel(1, 100)
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
        self.level         = self.generateLevel(1, 100)
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
        self.level         = self.generateLevel(1, 100)
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
        self.level         = self.generateLevel(1, 100)
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


class cobalion(pokemon):
    def __init__(self):
        self.pokedex       = 638
        self.species       = "Coballion"
        self.nature        = self.generateNature()
        self.type          = ["Steel", "Fight"]
        self.level         = self.generateLevel(1, 100)
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
        self.pokedex       = 639
        self.species       = "Terrakion"
        self.nature        = self.generateNature()
        self.type          = ["Rock", "Fight"]
        self.level         = self.generateLevel(1, 100)
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
        self.pokedex       = 640
        self.species       = "Virizion"
        self.nature        = self.generateNature()
        self.type          = ["Grass", "Fight"]
        self.level         = self.generateLevel(1, 100)
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
        self.pokedex       = 641
        self.species       = "Tornadus"
        self.nature        = self.generateNature()
        self.type          = ["Flying"]
        self.level         = self.generateLevel(1, 100)
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
        self.pokedex       = 642
        self.species       = "Thundurus"
        self.nature        = self.generateNature()
        self.type          = ["Electric", "Flying"]
        self.level         = self.generateLevel(1, 100)
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
        self.pokedex       = 643
        self.species       = "Reshiram"
        self.nature        = self.generateNature()
        self.type          = ["Dragon", "Fire"]
        self.level         = self.generateLevel(1, 100)
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
        self.pokedex       = 644
        self.species       = "Zekrom"
        self.nature        = self.generateNature()
        self.type          = ["Dragon", "Electric"]
        self.level         = self.generateLevel(1, 100)
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
        self.pokedex       = 645
        self.species       = "Landorus"
        self.nature        = self.generateNature()
        self.type          = ["Electric", "Flying"]
        self.level         = self.generateLevel(1, 100)
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
        self.pokedex       = 646
        self.species       = "Kyurem"
        self.nature        = self.generateNature()
        self.type          = ["Dragon", "Ice"]
        self.level         = self.generateLevel(1, 100)
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
        self.pokedex       = 647
        self.species       = "Keldeo"
        self.nature        = self.generateNature()
        self.type          = ["Water", "Fight"]
        self.level         = self.generateLevel(1, 100)
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
        self.pokedex       = 648
        self.species       = "Meloetta"
        self.nature        = self.generateNature()
        self.type          = ["Normal", "Psychic"]
        self.level         = self.generateLevel(1, 100)
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
        self.pokedex       = 649
        self.species       = "Genesect"
        self.nature        = self.generateNature()
        self.type          = ["Bug", "Steel"]
        self.level         = self.generateLevel(1, 100)
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

class xerneas(pokemon):
    def __init__(self):
        self.pokedex       = 716
        self.species       = "Xerneas"
        self.nature        = self.generateNature()
        self.type          = ["Fairy"]
        self.level         = self.generateLevel(1, 100)
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
        self.pokedex       = 717
        self.species       = "Yveltal"
        self.nature        = self.generateNature()
        self.type          = ["Dark", "Flying"]
        self.level         = self.generateLevel(1, 100)
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
        self.pokedex       = 718
        self.species       = "Zygarde"
        self.nature        = self.generateNature()
        self.type          = ["Dragon", "Ground"]
        self.level         = self.generateLevel(1, 100)
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
        self.pokedex       = 719
        self.species       = "Diancie"
        self.nature        = self.generateNature()
        self.type          = ["Rock", "Fairy"]
        self.level         = self.generateLevel(1, 100)
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
        self.pokedex       = 720
        self.species       = "Hoopa"
        self.nature        = self.generateNature()
        self.type          = ["Psychic", "Ghost"]
        self.level         = self.generateLevel(1, 100)
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
        self.pokedex       = 721
        self.species       = "Volcanion"
        self.nature        = self.generateNature()
        self.type          = ["Fire", "Water"]
        self.level         = self.generateLevel(1, 100)
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

class cosmog(pokemon):
    def __init__(self):
        self.pokedex       = 789
        self.species       = "Cosmog"
        self.nature        = self.generateNature()
        self.type          = ["Psychic"]
        self.level         = self.generateLevel(1, 100)
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
        self.pokedex       = 790
        self.species       = "Cosmoem"
        self.nature        = self.generateNature()
        self.type          = ["Psychic"]
        self.level         = self.generateLevel(1, 100)
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
        self.pokedex       = 791
        self.species       = "Solgaleo"
        self.nature        = self.generateNature()
        self.type          = ["Psychic", "Steel"]
        self.level         = self.generateLevel(1, 100)
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
        self.pokedex       = 792
        self.species       = "Lunala"
        self.nature        = self.generateNature()
        self.type          = ["Psychic", "Ghost"]
        self.level         = self.generateLevel(1, 100)
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
        self.pokedex       = 793
        self.species       = "Nihilego"
        self.nature        = self.generateNature()
        self.type          = ["Rock", "Poison"]
        self.level         = self.generateLevel(1, 100)
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
        self.pokedex       = 794
        self.species       = "Buzzwole"
        self.nature        = self.generateNature()
        self.type          = ["Bug", "Fight"]
        self.level         = self.generateLevel(1, 100)
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
        self.pokedex       = 795
        self.species       = "Pheromosa"
        self.nature        = self.generateNature()
        self.type          = ["Bug", "Fight"]
        self.level         = self.generateLevel(1, 100)
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
        self.pokedex       = 796
        self.species       = "Xurkitree"
        self.nature        = self.generateNature()
        self.type          = ["Electric"]
        self.level         = self.generateLevel(1, 100)
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
        self.pokedex       = 797
        self.species       = "Celesteela"
        self.nature        = self.generateNature()
        self.type          = ["Steel", "Flying"]
        self.level         = self.generateLevel(1, 100)
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
        self.pokedex       = 798
        self.species       = "Kartana"
        self.nature        = self.generateNature()
        self.type          = ["Grass", "Steel"]
        self.level         = self.generateLevel(1, 100)
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
        self.pokedex       = 799
        self.species       = "Guzzlord"
        self.nature        = self.generateNature()
        self.type          = ["Dark", "Dragon"]
        self.level         = self.generateLevel(1, 100)
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
        self.pokedex       = 800
        self.species       = "Necrozma"
        self.nature        = self.generateNature()
        self.type          = ["Psychic"]
        self.level         = self.generateLevel(1, 100)
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
        self.pokedex       = 801
        self.species       = "Magearna"
        self.nature        = self.generateNature()
        self.type          = ["Steel", "Fairy"]
        self.level         = self.generateLevel(1, 100)
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
        self.pokedex       = 802
        self.species       = "Marshadow"
        self.nature        = self.generateNature()
        self.type          = ["Fight", "Ghost"]
        self.level         = self.generateLevel(1, 100)
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

class Poipole(pokemon):
    def __init__(self):
        self.pokedex       = 803
        self.species       = "Poipole"
        self.nature        = self.generateNature()
        self.type          = ["Poison"]
        self.level         = self.generateLevel(1, 100)
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

class Naganadel(pokemon):
    def __init__(self):
        self.pokedex       = 804
        self.species       = "Naganadel"
        self.nature        = self.generateNature()
        self.type          = ["Poison", "Dragon"]
        self.level         = self.generateLevel(1, 100)
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
        self.pokedex       = 805
        self.species       = "Stakataka"
        self.nature        = self.generateNature()
        self.type          = ["Rock", "Steel"]
        self.level         = self.generateLevel(1, 100)
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
        self.pokedex       = 806
        self.species       = "Blacephalon"
        self.nature        = self.generateNature()
        self.type          = ["Fire", "Ghost"]
        self.level         = self.generateLevel(1, 100)
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
        self.pokedex       = 807
        self.species       = "Zeraora"
        self.nature        = self.generateNature()
        self.type          = ["Electric"]
        self.level         = self.generateLevel(1, 100)
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
        self.pokedex       = 808
        self.species       = "Meltan"
        self.nature        = self.generateNature()
        self.type          = ["Steel"]
        self.level         = self.generateLevel(1, 100)
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
        self.pokedex       = 809
        self.species       = "Melmetal"
        self.nature        = self.generateNature()
        self.type          = ["Steel"]
        self.level         = self.generateLevel(1, 100)
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

class zacian(pokemon):
    def __init__(self):
        self.pokedex       = 888
        self.species       = "Zacian"
        self.nature        = self.generateNature()
        self.type          = ["Fairy"]
        self.level         = self.generateLevel(1, 100)
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
        self.pokedex       = 889
        self.species       = "Zamazenta"
        self.nature        = self.generateNature()
        self.type          = ["Fight"]
        self.level         = self.generateLevel(1, 100)
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
        self.pokedex       = 890
        self.species       = "Eternatus"
        self.nature        = self.generateNature()
        self.type          = ["Poison", "Dragon"]
        self.level         = self.generateLevel(1, 100)
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

        
#pokemon = flabebe()
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

# note: spelling it flavour for now because in Sassi's words: "fuck america"

# TODO:
#  Synchronize
#  Mega 'mon
