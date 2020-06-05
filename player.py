class player:
    def __init__(self, playerID, starter):
        self.ID      = playerID
        self.starter = starter

        self.pokemon = [starter]

    def addPokemon(self, toAdd):
        self.pokemon.append(toAdd)
