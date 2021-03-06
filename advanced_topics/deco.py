import os

def Exists(oldFunc):
    def inside(filename):
        if (os.path.exists(filename)):
            oldFunc(filename)
        else:
            print('The file does not exist')
    return inside
    
@Exists
def outputLine(inFile):
    with open(inFile) as f:
        print(f.readlines())

func = Exists(outputLine)

outputLine("deco.py")
outputLine("test.py")
