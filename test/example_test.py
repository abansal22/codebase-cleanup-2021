


# this is the app/example.py file

# import some code from the app dir
# inoke that code with certain inputs 
#.. to ensure that it produces the expected outputs


#def test_():
#    pass


from app.example import enlarge

def test_enlarge():
    #assert True
    #assert False
    #assert 2 == 2
    assert enlarge(9) == 900

# EXPECT THAT THE ENLARGE FUNCTION RETURNS A LARGER NUMBER

# EXPECT THAT WE GET A ROUNDED STRING BACK WITH DOLLAR SIGN

#