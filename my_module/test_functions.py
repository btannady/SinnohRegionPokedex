from my_module.functions import * # for functions, classes, and objects


# tests the findWithName function
def test_findWithName():
    
    # test valid pokemon names
    assert(findWithName("pikachu") == ["Pikachu", "Electric", "25"])        # test for all lowercase input
    assert(findWithName("GARCHOMP") == ["Garchomp", "Dragon", "Ground", "445"]) # test for all uppercase input
    assert(findWithName("mAgIKArP") == ["Magikarp", "Water", "129"])        # test for mixed-casing input
    
    # test invalid pokemon names
    assert(findWithName("mrPoopyHead321") == ["not found"])
    assert(findWithName("Harambe") == ["not found"]) 
    assert(findWithName("Jake Paul") == ["not found"])
    assert(findWithName(9232) == ["not found"])
    assert(findWithName(124.32) == ["not found"])


# ----------------------------------------------------------------------

# tests the findWithType function
def test_findWithType():
    
    # test valid pokemon with one string input
    assert(findWithType("fire") == [["Chimchar", "Fire", "390"], ["Monferno", "Fire", "Fighting", "391"], ["Infernape", "Fire", "Fighting", "392"], ["Ponyta", "Fire", "77"], ["Rapidash", "Fire", "78"], ["Bowsette", "Fire", "Dragon", "???"], ["Flareon", "Fire", "136"], ["Houndour", "Dark", "Fire", "228"], ["Houndoom", "Dark", "Fire", "229"], ["Magby", "Fire", "240"], ["Magmar", "Fire", "126"], ["Magmortar", "Fire", "467"]])
    assert(findWithType("FIRE") == [["Chimchar", "Fire", "390"], ["Monferno", "Fire", "Fighting", "391"], ["Infernape", "Fire", "Fighting", "392"], ["Ponyta", "Fire", "77"], ["Rapidash", "Fire", "78"], ["Bowsette", "Fire", "Dragon", "???"], ["Flareon", "Fire", "136"], ["Houndour", "Dark", "Fire", "228"], ["Houndoom", "Dark", "Fire", "229"], ["Magby", "Fire", "240"], ["Magmar", "Fire", "126"], ["Magmortar", "Fire", "467"]])
    assert(findWithType("FiRe") == [["Chimchar", "Fire", "390"], ["Monferno", "Fire", "Fighting", "391"], ["Infernape", "Fire", "Fighting", "392"], ["Ponyta", "Fire", "77"], ["Rapidash", "Fire", "78"], ["Bowsette", "Fire", "Dragon", "???"],["Flareon", "Fire", "136"], ["Houndour", "Dark", "Fire", "228"], ["Houndoom", "Dark", "Fire", "229"], ["Magby", "Fire", "240"], ["Magmar", "Fire", "126"], ["Magmortar", "Fire", "467"]])
    
    # test valid pokemon with two string inputs
    assert(findWithType("ground", "dragon") == [["Gible", "Dragon", "Ground", "443"], ["Gabite", "Dragon", "Ground", "444"], ["Garchomp", "Dragon", "Ground", "445"]])
    assert(findWithType("Ghost", "Poison") == [["Gastly", "Ghost", "Poison", "92"], ["Haunter", "Ghost", "Poison", "93"], ["Gengar", "Ghost", "Poison", "94"]])
    
    # test invalid pokemon inputs
    assert(findWithType("swamp") == [["not found"]])
    assert(findWithType("booger") == [["not found"]])
    assert(findWithType("stinky") == [["not found"]])
    

# ----------------------------------------------------------------------

# tests the findWithNdex function
def test_findWithNdex():
    
    # test for valid pokemon; string of integer input
    assert(findWithNdex("94") == ["Gengar", "Ghost", "Poison", "94"])        # test for positive integer, string
    assert(findWithNdex("483") == ["Dialga", "Steel", "Dragon", "483"])      # test for positive integer, string
    assert(findWithNdex("282") == ["Gardevoir", "Psychic", "282"])       # test for positive integer, string
    
    # test for valid pokemon; integer input
    assert(findWithNdex(448) == ["Lucario", "Fighting", "Steel", "448"])     # test for positive integer, int
    assert(findWithNdex(143) == ["Snorlax", "Normal", "143"])            # test for positive integer, int
    assert(findWithNdex(428) == ["Lopunny", "Normal", "428"])            # test for positive integer, int
    
    # test for valid pokemon; float input
    assert(findWithNdex(282.5) == ["Gardevoir", "Psychic", "282"]) # type float 
    
    # test string of negative integer values; which are invalid pokemon ndexs
    assert(findWithNdex("-428") == ["not found"]) # string
    
    # test negative integer values; which are invalid pokemon ndexs
    assert(findWithNdex(-428) == ["not found"]) # int 
    
    # test for float values; which are invalid pokemon ndexs
    assert(findWithNdex("282.5") == ["invalid data type"]) # type string 
   
    # test for string values; which are invalid pokemon ndexs
    assert(findWithNdex("pikachu") == ["invalid data type"]) 
    assert(findWithNdex("oBAma") == ["invalid data type"]) 
    
    