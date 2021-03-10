class Node:
    def __init__(self, dataValue=None):
        self.dataValue = dataValue
        self.nextNode = None

class SLinkedList:
    def __init__(self):
        self.headNode = None

    def getIndex(self,data):
        currentIndex=0
        currentNode=self.headNode
        
        while currentNode != None:

            if currentNode.dataValue ==data: 
                return "The index of {} is {}.".format(data,currentIndex)
            
            currentIndex +=1
            currentNode=currentNode.nextNode
            
        return "No such data value"

    def traverse(self):
        currentNode = self.headNode
        while currentNode is not None:
            print (currentNode.dataValue)
            currentNode = currentNode.nextNode
        
    def insert (self, index, data):
        if index == 1:
            newNode = Node(data)
            newNode.nextNode = self.headNode
            self.headNode = newNode
            
        else: 
            i = 1
            currentNode = self.headNode
        
            while i < index-1 and currentNode is not None:
                currentNode = currentNode.nextNode
                i = i+1

            if currentNode is None:
                print("Index out of bound.")
            else: 
                newNode = Node(data)
                newNode.nextNode = currentNode.nextNode
                currentNode.nextNode = newNode
                
    def append(self, data):

        newNode = Node(data)

        if self.headNode is None:
            self.headNode = newNode
            return

        currentNode = self.headNode

        while currentNode.nextNode != None:
            currentNode = currentNode.nextNode

        currentNode.nextNode = newNode

    def remove(self, data):
        if self.headNode is None:
            print("The list is empty")
            return
        
        if self.headNode.dataValue == data:
            self.headNode = self.headNode.nextNode
            return 
        
        currentNode = self.headNode

        while currentNode.nextNode != None:
            if currentNode.nextNode.dataValue == data:
                break
            currentNode = currentNode.nextNode

        if currentNode is None:
            print("No such item to remove")
            return     

        currentNode.nextNode = currentNode.nextNode.nextNode

newFruitList = SLinkedList()
newFruitList.append("Apple")
newFruitList.append("Durian")
newFruitList.append("Orange")
newFruitList.append("Orange")
newFruitList.append("Watermelon")
newFruitList.append("WTF")
newFruitList.remove("Orange")
newFruitList.remove("Orange")
newFruitList.traverse()
