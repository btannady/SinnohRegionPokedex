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
    assert(findWithType("fire") == [["Chimchar", "Fire", "", "390"], ["Monferno", "Fire", "Fighting", "391"], ["Infernape", "Fire", "Fighting", "392"], ["Ponyta", "Fire", "", "77"], ["Rapidash", "Fire", "", "78"], ["Flareon", "Fire", "", "136"], ["Houndour", "Dark", "Fire", "228"], ["Houndoom", "Dark", "Fire", "229"], ["Magby", "Fire", "", "240"], ["Magmar", "Fire", "", "126"], ["Magmortar", "Fire", "", "467"]])
    assert(findWithType("FIRE") == [["Chimchar", "Fire", "", "390"], ["Monferno", "Fire", "Fighting", "391"], ["Infernape", "Fire", "Fighting", "392"], ["Ponyta", "Fire", "", "77"], ["Rapidash", "Fire", "", "78"], ["Flareon", "Fire", "", "136"], ["Houndour", "Dark", "Fire", "228"], ["Houndoom", "Dark", "Fire", "229"], ["Magby", "Fire", "", "240"], ["Magmar", "Fire", "", "126"], ["Magmortar", "Fire", "", "467"]])
    assert(findWithType("fire") == [["Chimchar", "Fire", "", "390"], ["Monferno", "Fire", "Fighting", "391"], ["Infernape", "Fire", "Fighting", "392"], ["Ponyta", "Fire", "", "77"], ["Rapidash", "Fire", "", "78"], ["Flareon", "Fire", "", "136"], ["Houndour", "Dark", "Fire", "228"], ["Houndoom", "Dark", "Fire", "229"], ["Magby", "Fire", "", "240"], ["Magmar", "Fire", "", "126"], ["Magmortar", "Fire", "", "467"]])
    
    # test invalid pokemon inputs
    
    

# test the findWithNdex function
def test_findWithNdex():
    
    assert(findWithNdex("94") == ["Gengar", "Ghost", "Poison", "94"])        # test for positive integer, string
    assert(findWithNdex("483") == ["Dialga", "Steel", "Dragon", "483"])      # test for positive integer, string
    assert(findWithNdex("282") == ["Gardevoir", "Psychic", "", "282"])       # test for positive integer, string
    
    assert(findWithNdex(448) == ["Lucario", "Fighting", "Steel", "448"])     # test for positive integer, int
    assert(findWithNdex(143) == ["Snorlax", "Normal", "", "143"])            # test for positive integer, int
    assert(findWithNdex(428) == ["Lopunny", "Normal", "", "428"])            # test for positive integer, int
    
    # test for negative integer values; which are invalid pokemon ndexs
    assert(findWithNdex("-428") == ["invalid data type"]) # string
    assert(findWithNdex(-428) == ["not found"]) # int 
    
    # test for float values; which are invalid pokemon ndexs
    assert(findWithNdex("282.5") == ["invalid data type"]) # type string 
    assert(findWithNdex(282.5) == ["invalid data type"]) # type float 
    
    # test for string values; which are invalid pokemon ndexs
    assert(findWithNdex("pikachu") == ["invalid data type"]) 
    assert(findWithNdex("oBAma") == ["invalid data type"]) 
    
    