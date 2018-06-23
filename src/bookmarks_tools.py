
# fileio

def appendText(fileName, txt):
    try:
        f = open(fileName, 'a+')
    except:
        print("Error: opening File '%s'", fileName)
        sys.exit()

    f.write(txt)
    f.close()

def writeFile(fileName, txt):

    try:
        f = open(fileName, 'w')
    except:
        print("Error: opening File '%s'", fileName)
        sys.exit()
    f.write(txt)
    f.close()

