import os


def write_encryption(userInput):
    with open('text files\\save', 'w+') as progFile:
        progFile.write(userInput)


def getfilepath():
    with open('text files\\save', 'w') as progFile:
        filePath = os.path.realpath(progFile.name)
        return filePath
