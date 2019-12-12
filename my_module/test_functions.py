from my_module.functions import *


# test the findWithName function
def test_findWithName():
    
    # test valid pokemon names
    assert(findWithName("pikachu") == ["Pikachu", "Electric", "", "25"])        # test for all lowercase input
    assert(findWithName("GARCHOMP") == ["Garchomp", "Dragon", "Ground", "445"]) # test for all uppercase input
    assert(findWithName("mAgIKArP") == ["Magikarp", "Water", "", "129"])        # test for mixed-casing input
    
    # test invalid pokemon names
    assert(findWithName("mrPoopyHead321") == ["not found"])
    assert(findWithName("Harambe") == ["not found"]) 
    assert(findWithName("Jake Paul") == ["not found"])
    assert(findWithName(9232) == ["not found"])
    assert(findWithName(124.32) == ["not found"])
    
test_findWithName()

# ----------------------------------------------------------------------

# test the findWithType function
def test_findWithType():
    
    # test valid pokemon with one string input
    assert(findWithType("fire") == [["Chimchar", "Fire", "", "390"], ["Monferno", "Fire", "Fighting", "391"], ["Infernape", "Fire", "Fighting", "392"], ["Ponyta", "Fire", "", "77"], ["Rapidash", "Fire", "", "78"], ["Flareon", "Fire", "", "136"], ["Houndour", "Dark", "Fire", "228"], ["Houndoom", "Dark", "Fire", "229"], ["Magby", "Fire", "", "240"], ["Magmar", "Fire", "", "126"], ["Magmortar", "Fire", "", "467"]])
    assert(findWithType("FIRE") == [["Chimchar", "Fire", "", "390"], ["Monferno", "Fire", "Fighting", "391"], ["Infernape", "Fire", "Fighting", "392"], ["Ponyta", "Fire", "", "77"], ["Rapidash", "Fire", "", "78"], ["Flareon", "Fire", "", "136"], ["Houndour", "Dark", "Fire", "228"], ["Houndoom", "Dark", "Fire", "229"], ["Magby", "Fire", "", "240"], ["Magmar", "Fire", "", "126"], ["Magmortar", "Fire", "", "467"]])
    assert(findWithType("FiRe") == [["Chimchar", "Fire", "", "390"], ["Monferno", "Fire", "Fighting", "391"], ["Infernape", "Fire", "Fighting", "392"], ["Ponyta", "Fire", "", "77"], ["Rapidash", "Fire", "", "78"], ["Flareon", "Fire", "", "136"], ["Houndour", "Dark", "Fire", "228"], ["Houndoom", "Dark", "Fire", "229"], ["Magby", "Fire", "", "240"], ["Magmar", "Fire", "", "126"], ["Magmortar", "Fire", "", "467"]])
    
    # test valid pokemon with two string inputs
    assert(findWithType("ground", "dragon") == [["gible", "dragon", "ground", "443"], ["gabite", "dragon", "ground", "444"], ["garchomp", "dragon", "ground", "445"]])
    assert(findWithType("ghost", "poison") == [["gastly", "ghost", "poison", "92"], ["haunter", "ghost", "poison", "93"], ["gengar", "ghost", "poison", "94"]])
    
    # test invalid pokemon inputs
    assert(findWithType("swamp") == [["not found"]])
    assert(findWithType("booger") == [["not found"]])
    assert(findWithType("stinky") == [["not found"]])
    
test_findWithType()

# ----------------------------------------------------------------------

# test the findWithNdex function
def test_findWithNdex():
    
    assert(findWithNdex("94") == ["Gengar", "Ghost", "Poison", "94"])        # test for positive integer, string
    assert(findWithNdex("483") == ["Dialga", "Steel", "Dragon", "483"])      # test for positive integer, string
    assert(findWithNdex("282") == ["Gardevoir", "Psychic", "", "282"])       # test for positive integer, string
    
    assert(findWithNdex(448) == ["Lucario", "Fighting", "Steel", "448"])     # test for positive integer, int
    assert(findWithNdex(143) == ["Snorlax", "Normal", "", "143"])            # test for positive integer, int
    assert(findWithNdex(428) == ["Lopunny", "Normal", "", "428"])            # test for positive integer, int
    
    # test for negative integer values; which are invalid pokemon ndexs
    assert(findWithNdex("-428") == ["not found"]) # string
    assert(findWithNdex(-428) == ["not found"]) # int 
    
    # test for float values; which are invalid pokemon ndexs
    assert(findWithNdex("282.5") == ["invalid data type"]) # type string 
    assert(findWithNdex(282.5) == ["invalid data type"]) # type float 
    
    # test for string values; which are invalid pokemon ndexs
    assert(findWithNdex("pikachu") == ["invalid data type"]) 
    assert(findWithNdex("oBAma") == ["invalid data type"]) 
    
test_findWithNdex()
    