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
    (doesn't return anything, void function; simply prints data corresponding to pokemon to the user)
    
    """
    
    print("\n**********************************")
    
    # uses to tell whether or not we found the Pokemon
    pokeFound = False
    
    # if we get in here, it means user is searching for Pokemon with 2 types
    if userSearch2 != "":
        tempList1 = [] # carries Pokemon that have at least userSearch1 type
        for monster in pokedex:
            for monsterType in monster.getPokeType(): 
                if monsterType == userSearch1.lower():
                    tempList1.append(monster)
        for monster in tempList1:
            for monsterType in monster.getPokeType(): 
                if monsterType == userSearch2.lower():
                # this is our final filtered list, now we can display for the user
                    # display the pokemon name
                    print("Pokémon: ", end = '')
                    print(monster.getPokeName().capitalize())
            
                    # display the pokemon type(s)
                    print("Type: ", end = '')
                    for item in monster.getPokeType():
                        print(item.capitalize() + " ", end = '')
                    print("")
                
                    # display the pokemon Ndex    
                    print("National Index: #", end = '')
                    print(monster.getPokeNdex())
                
                    print("\n**********************************")
                    pokeFound = True
                    
        # verifies whether we found the user's Pokemon
        if pokeFound:
            return
        
        # if we reached here, then that means the userSearch input was not found in pokedex database
        print("The Pokémon with type [" + userSearch1 + "] and [" + userSearch2 + "] were not found in the Pokédex database...")
    
        print("\n**********************************")
    
#---------------------------------------  

    # if we get inside here, it means user is searching for Pokemon with only 1 type
    else:
    
        #displays the pokemon data
        for monster in pokedex:
            for monsterType in monster.getPokeType():
                if monsterType == userSearch1.lower():
            
                    # display the pokemon name
                    print("Pokémon: ", end = '')
                    print(monster.getPokeName().capitalize())
            
                    # display the pokemon type(s)
                    print("Type: ", end = '')
                    commaCounter = len(monster.getPokeType())
                    for item in monster.getPokeType():
                        print(item.capitalize() + " ", end = '')
                    print("")
                
                    # display the pokemon Ndex    
                    print("National Index: #", end = '')
                    print(monster.getPokeNdex())
                    
                    print("\n**********************************")
                    pokeFound = True
        
        # verifies whether we found the user's Pokemon
        if pokeFound:
            return
        
        # if we reached here, then that means the userSearch input was not found in pokedex database
        print("The Pokémon with type [" + userSearch1 + "] was not found in the Pokédex database...")
    
        print("\n**********************************")
        

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


