# CLASS DEFINITIONS; This file contains our Pokemon class

#----------------------------------------------------------------------------------------------------
class Pokemon:
    
    """ class responsible of holding each individual Pokemon's data by species
    
    Getter methods
    --------------
    getPokeName : string
        Returns the string of what the name of the pokemon is
    getPokeType : string
        Returns the string of what type the pokemon is
    getPokeNdex : integer
        Returns the integer of what the national index number of the pokemon is
    
    Setter methods
     --------------
    setPokeType : void
        Sets the pokemon's type to a different value
    setPokeNdex : void
        Sets the pokemon's nation index number to a different value
    
    """
    
    def __init__(self, pokeName, pokeType, pokeNdex):
        self.pokeName = pokeName # pokemon's name; expects a string
        self.pokeType = pokeType # pokemon's nature types; expects a List
        self.pokeNdex = pokeNdex # pokemon's official national index; expects int or string
        
    #---------------------------------------------
    #getter methods
    def getPokeName(self):
        return self.pokeName
    
    def getPokeType(self):
        return self.pokeType
    
    def getPokeNdex(self):
        return self.pokeNdex
    
    #---------------------------------------------
    #setter methods
    def setPokeType(self, newPokeType):
        self.pokeType = newPokeType
        
    def setPokeNdex(self, newPokeNdex):
        self.pokeNdex = newPokeNdex
        
    #---------------------------------------------
                