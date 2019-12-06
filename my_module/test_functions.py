from my_module.functions import *


# test the findWithName function
def test_findWithName():
    
    assert(findWithName("pikachu") == ["Pikachu", "Electric", "", "25"])        # test for all lowercase input
    assert(findWithName("GARCHOMP") == ["Garchomp", "Dragon", "Ground", "445"]) # test for all uppercase input
    assert(findWithName("mAgIKArP") == ["Magikarp", "Water", "", "129"])        # test for mixed-casing input
    
    # test invalid pokemon names
    assert(findWithName("mrPoopyHead321") == "The Pokémon name [myPoopyHead321] was not found in the Pokédex database...")
    assert(findWithName("Harambe") == "The Pokémon name [Harambe] was not found in the Pokédex database...") 
    assert(findWithName("Jake Paul") == "The Pokémon name [Jake Paul] was not found in the Pokédex database...")
 
    
# test the findWithType function
def test_findWithType():
    
    # test valid pokemon string inputs
    assert(findWithType("fire") == ["ChimcharFire390", "MonfernoFireFighting391", "InfernapeFireFighting392", "PonytaFire77", "RapidashFire78", "FlareonFire136", "HoundourDarkFire228", "HoundoomDarkFire229", "MagbyFire240", "MagmarFire126", "MagmortarFire467"])
    assert(findWithType("FIRE") == ["ChimcharFire390", "MonfernoFireFighting391", "InfernapeFireFighting392", "PonytaFire77", "RapidashFire78", "FlareonFire136", "HoundourDarkFire228", "HoundoomDarkFire229", "MagbyFire240", "MagmarFire126", "MagmortarFire467"])
    assert(findWithType("fire") == ["ChimcharFire390", "MonfernoFireFighting391", "InfernapeFireFighting392", "PonytaFire77", "RapidashFire78", "FlareonFire136", "HoundourDarkFire228", "HoundoomDarkFire229", "MagbyFire240", "MagmarFire126", "MagmortarFire467"])
    
    # test invalid pokemon inputs
    
    

# test the findWithNdex function
def test_findWithNdex():
    
    assert(findWithNdex("94") == "GengarGhostPoison94")        # test for positive integer, string
    assert(findWithNdex("483") == "DialgaSteelDragon483")      # test for positive integer, string
    assert(findWithNdex("282") == "GardevoirPsychic282")       # test for positive integer, string
    
    assert(findWithNdex(448) == "LucarioFightingSteel448")     # test for positive integer, int
    assert(findWithNdex(143) == "SnorlaxNormal143")            # test for positive integer, int
    assert(findWithNdex(428) == "LopunnyNormal428")            # test for positive integer, int
    
    # test for negative integer values; which are invalid pokemon ndexs
    assert(findWithNdex("-428") == "The Pokémon National Index [-428] was not found in the Pokédex database...") # string
    assert(findWithNdex(-428) == "The Pokémon National Index [-428] was not found in the Pokédex database...") # int 
    
    # test for float values; which are invalid pokemon ndexs
    assert(findWithNdex("282.5") == "The Pokémon National Index [-282.5] was not found in the Pokédex database...") # type string 
    assert(findWithNdex(282.5) == "The Pokémon National Index [-282.5] was not found in the Pokédex database...") # type float 
    
    # test for string values; which are invalid pokemon ndexs
    assert(findWithNdex("pikachu") == "The Pokémon National Index [pikachu] was not found in the Pokédex database...") 
    assert(findWithNdex("oBAma") == "The Pokémon National Index [oBAma] was not found in the Pokédex database...") 
    
    