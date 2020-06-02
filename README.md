# Pokecord2

## What is Pokecord2?
Pokecord2 is a recreation of the Pokecord discord bot which allowed users to play pokemon in a discord server. Pokecord2 is currently a work in progress, so we appreciate any support we can get.

## pokedex.py
Pokedex.py is the module of the bot which handles pokemon. There is a main pokemon class containing the subroutines that are needed for all pokemon, and then there are individual classes inheriting pokemon for each of the individual pokemon.
You can help us by adding more pokemon. There are 980 pokemon, not including different versions of the same, so we need help adding each one. You can add pokemon by copying an exisiting class and changing the names and the values to one we don't already have.

## spawn.py
This script is the actual bot. This handles messages and pokemon spawning. Every 5-30 minutes background_loop() picks a random pokemon, sends it's pokedex number to a channel, and then the user can use the 'catch' command to catch the pokemon by typing it's name
