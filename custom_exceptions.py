class DogNameError(Exception):

    def __init__(self,*args,**kwargs):
        Exception.__init__(self,*args,**kwargs)

try:
    dogName = input('What is ur dog name?')
    if any(char.isdigit() for char in dogName):
        raise DogNameError

except DogNameError:
    print('ur dog cant contain a numebr')
