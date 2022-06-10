from abc import ABC

class Abs(ABC):
    address = ''

    def __init__(self, address):
        self.address = address

    def calculateFreqs(self):
        pass

class ListCount(Abs):
    def __init__(self, address):
        Abs.__init__(self, address)

    def calculateFreqs(self, address):
        myFile = open(address)
        x = myFile.readline().split()
        myList = []

        for i in x:

            if i not in myList:
                myList.append(i)

        for i in range(0, len(myList)):
            print(myList)

class DictCount(Abs):
  def __init__(self,addr):
   super().__init__(addr)

  def calculateFreqs(self):
   file = open(self.address, "r")
   myDictionary={}
   for line in file:
    for word in line.split():
     myDictionary[word] = myDictionary.get(word,0)+1
    print(myDictionary)

listObj = ListCount("C:\\Users\\melo\\Desktop\\strange.txt")
listObj.calculateFreqs()

print()

dictObj = DictCount("C:\\Users\\melo\\Desktop\\strange.txt")
dictObj.calculateFreqs()