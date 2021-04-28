class Atbash:
    def __init__(self):
        self.alphabetOriginal = [
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
                                 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        self.alphabetReverse = sorted(self.alphabetOriginal, reverse=True)
        self.inputList = []
        self.encryptedList = []

    def atbashencrypt(self, userInput):
        for progIteration in range(0, len(userInput)):
            self.inputList.append(userInput[progIteration].lower())

        for indexInput in range(0, len(self.inputList)):
            for indexOriginal in range(0, 26):

                if self.inputList[indexInput] == self.alphabetOriginal[indexOriginal]:
                    self. encryptedList.append(self.alphabetReverse[indexOriginal])
                    break

                elif self.inputList[indexInput] not in self.alphabetOriginal:
                    self.encryptedList.append(self.inputList[indexInput])
                    break

        returnValue = ''

        for append in self.encryptedList:
            returnValue += append

        return returnValue


if __name__ == '__main__':
    print(Atbash().atbashencrypt('hello'))
