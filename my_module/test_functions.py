from my_module.functions import *


# test the findWithName function
def test_findWithName():
    
    assert(findWithName("pikachu") == "PikachuElectric25")        # test for all lowercase input
    assert(findWithName("GARCHOMP") == "GarchompDragonGround445") # test for all uppercase input
    assert(findWithName("mAgIKArP") == "MagikarpWater129")        # test for mixed-casing input
    
    # test invalid pokemon names
    assert()findWithName("mrPoopyHead321") == ["The Pokémon name [myPoopyHead321] was not found in the Pokédex database..."] 
    assert()findWithName("Harambe") == ["The Pokémon name [Harambe] was not found in the Pokédex database..."] 
    assert()findWithName("Jake Paul") == ["The Pokémon name [Jake Paul] was not found in the Pokédex database..."] 
 
    
# test the findWithType function
def test_findWithType():
    



# test the findWithNdex function
def test_findWithNdex():
    
    # test with positive int value
    # test with negative int value
    # test with random character
    # test with string value
    # test with all capitals string
    # test with all lowercase string
    # test with both capital&lowercase string