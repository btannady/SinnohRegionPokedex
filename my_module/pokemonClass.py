# CLASS DEFINITIONS

#----------------------------------------------------------------------------------------------------
# class responsible of holding each individual Pokemon's data by species
class Pokemon:
    
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
        print("[" + self.pokeName + "'s TYPE has been successfully changed!]")
        
    def setPokeNdex(self, newPokeNdex):
        self.pokeNdex = newPokeNdex
        print("[" + self.pokeName + "'s NATIONAL INDEX has been successfully changed!]")
        
    #---------------------------------------------
                