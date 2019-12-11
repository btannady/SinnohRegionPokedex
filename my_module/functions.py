from my_module.pokemonObjects import *


# FUNCTION DEFINITIONS

#----------------------------------------------------------------------------------------------------
def findWithName(userSearch):
    
    """ Spits out pokemon data corresponding to the inputted Pokemon name
    
    Parameters
    ----------
    userSearch : string
        String to determine what pokemon to search for in data set
    
    Returns
    -------
    pokeDataOutput : List of strings
        List of string containing information of pokemon data to later display to user
    
    """
    
    # prepares the output list to return
    pokeDataOutput = []
    
    # appends the pokemon that fit the search criteria into our output list
    for monster in pokedex:
        if monster.getPokeName() == userSearch.lower():
            
            # sets the first element of the list to string of pokemon name
            pokeDataOutput.append(monster.getPokeName().capitalize())
            
            # sets the second and third element of the list to string(s) of the pokemon type(s)
            for item in monster.getPokeType():
                pokeDataOutput.append(item.capitalize())
                
            # sets the last element of the list to string of pokemon Ndex  
            pokeDataOutput.append(str(monster.getPokeNdex()))
            
            return pokeDataOutput
            
    # if we reached here, then that means the userSearch input was not found in pokedex database
    pokeDataOutput = ["not found"]
    return pokeDataOutput
    
    
#----------------------------------------------------------------------------------------------------
def findWithType(userSearch1 = "", userSearch2 = ""):
    
    """ Spits out pokemon data corresponding to the inputted Pokemon type(s)
    
    Parameters
    ----------
    userSearch1 : string
        String to determine what pokemon to search for in data set
    userSearch2 : string
        String to determine what pokemon to search for in data set
    
    Returns
    -------
    pokeDataOutput : List of lists of strings
        List of lists containing string information of pokemon data to later display to user
    
    """

    pokeDataOutput = [] # prepares the final output list to return
    
    # uses to tell whether or not we found the Pokemon
    pokeFound = False
    
    # if we get in here, it means user is searching for Pokemon with 2 types
    if userSearch2 != "":
        
        tempList1 = [] # use this list to hold Pokemon that have at least userSearch1 type
        for monster in pokedex: # for each pokemon in database
            for monsterType in monster.getPokeType(): # for each type of the current pokemon
                if monsterType == userSearch1.lower(): # if the current pokemon has a type that matches userSearch1
                    tempList1.append(monster) # add the pokemon onto our list of pokemon with at least userSearch1, tempList1
                    
        # now search thru the list of userSearch1 type pokemon, tempList1, for pokemon that are also userSearch2
        for monster in tempList1: # for each pokemon in list of userSearch1 type pokemon, tempList1
            for monsterType in monster.getPokeType():  # for each type of the current pokemon
                if monsterType == userSearch2.lower(): # if the current pokemon has a type that matches userSearch2
                    
                # if we reach here, it means we found a pokemon that completely meets the search criteria
                # we can now append this current pokemon set into our final filtered list, pokeDataOutput
                
                    # prepares a temporary list to hold the current pokemon's data, to append to pokeDataOutput
                    somePokemonSet = []
                
                    # sets the first element of the somePokemonSet list to string of current pokemon's name
                    somePokemonSet.append(monster.getPokeName().capitalize())
            
                    # sets the second and third elements of the somePokemonSet list to strings of the current pokemon's types
                    for item in monster.getPokeType():
                        somePokemonSet.append(item.capitalize())
                    
                    # sets the fourth element of the somePokemonSet list to string of the current pokemon's Ndex  
                    somePokemonSet.append(str(monster.getPokeNdex()))
            
                    # append the current somePokemonSet list into our final filtered list
                    pokeDataOutput.append(somePokemonSet) 

                    pokeFound = True # use this variable to later verify that we found at least one pokemon
                    
        # verifies whether we found the user's Pokemon
        if pokeFound:
            return pokeDataOutput
        else:
            # if we reached here, then that means the userSearch input was not found in pokedex database
            return [["not found"]] 
    
#---------------------------------------  

    # if we get inside here, it means user is searching for Pokemon with only 1 type
    else:
    
        # search thru the list for userSearch1 type pokemon
        for monster in pokedex: # for each pokemon in database
            for monsterType in monster.getPokeType(): # for each type of the current pokemon
                if monsterType == userSearch1.lower(): # if the current pokemon has a type that matches userSearch1
                    
                # if we reach here, it means we found a pokemon that completely meets the search criteria
                # we can now append this current pokemon set into our final filtered list, pokeDataOutput
                
                    # prepares a temporary list to hold the current pokemon's data, to append to pokeDataOutput
                    somePokemonSet = []
                    
                    # sets the first element of the somePokemonSet list to string of current pokemon's name
                    somePokemonSet.append(monster.getPokeName().capitalize())
            
                    # sets the second element of the somePokemonSet list to string of the current pokemon's type
                    for item in monster.getPokeType():
                        somePokemonSet.append(item.capitalize())
                    
                    # sets the third element of the somePokemonSet list to string of the current pokemon's Ndex   
                    somePokemonSet.append(str(monster.getPokeNdex()))
            
                    # append the current somePokemonSet list into our final filtered list
                    pokeDataOutput.append(somePokemonSet) 

                    pokeFound = True
        
        # verifies whether we found the user's Pokemon
        if pokeFound:
            return pokeDataOutput
        else:
            # if we reached here, then that means the userSearch input was not found in pokedex database
            return [["not found"]]
        

#----------------------------------------------------------------------------------------------------
def findWithNdex(userSearch):
    
    """ Spits out pokemon data paired to the inputted Pokemon Ndex (national index number)
    
    Parameters
    ----------
    userSearch : integer
        String to determine what pokemon to search for in data set
    
    Returns
    -------
    pokeDataOutput : List of strings
        List of string containing information of pokemon data to later display to user
    
    """
    
    # prepares the output list to return
    pokeDataOutput = []
    
    
    # check that user input a valid integer value
    try:
        intTester = int(userSearch)
    except ValueError:
        pokeDataOutput.append("invalid data type")
        return pokeDataOutput
  
    
    # appends the pokemon that fit the search criteria into our output list
    for monster in pokedex:
        if monster.getPokeNdex() == int(userSearch):
            
            # sets the first element of the list to string of pokemon name
            pokeDataOutput.append(monster.getPokeName().capitalize())
            
            # sets the second and third element of the list to string(s) of the pokemon type(s)
            for item in monster.getPokeType():
                pokeDataOutput.append(item.capitalize())
                
            # sets the last element of the list to string of pokemon Ndex  
            pokeDataOutput.append(str(monster.getPokeNdex()))
            
            return pokeDataOutput
            
    # if we reached here, then that means the userSearch input was not found in pokedex database
    pokeDataOutput = ["not found"]
    return pokeDataOutput


