from my_module.functions import *

"""
Keep in mind, all the functions used are void.
"""

# tests if functions return an error
def iserror(func, *args, **kw):
    try:
        func(*args, **kw)
        return False
    except Exception:
        return True
    

# test the findWithName function
def test_findWithName():
    
    # check function doesn't throw an error
    assert(iserror(float, 'as1f') == False)
 
    
# test the findWithType function
def test_findWithType():
    
    # test with positive int value
    # test with negative int value
    # test with random character
    # test with string value
    # test with all capitals string
    # test with all lowercase string
    # test with both capital&lowercase string


# test the findWithNdex function
def test_findWithNdex():
    
    # test with positive int value
    # test with negative int value
    # test with random character
    # test with string value
    # test with all capitals string
    # test with all lowercase string
    # test with both capital&lowercase string