class Node:
    def __init__(self, dataValue):
        self.dataValue = dataValue
        self.nextNode = None

class Stack:
    def __init__(self):
        self.size = 0
        self.removedNode = None
        self.headNode = Node("Invisible Node")
    
    def getSize(self):
        return self.size
    
    def isEmpty(self):
        return self.size == 0
    
    # look down
    def peek(self):
        if self.isEmpty():
            print("Peeking from am empty stack")
            return
        return self.headNode.nextNode.dataValue
    
    def push(self, data):
        newNode = Node(data)
        newNode.nextNode = self.headNode.nextNode
        self.headNode.nextNode = newNode
        self.size += 1
        self.removedNode = None

    # undo
    def pop(self):
        if self.isEmpty():
            print("Popping from am empty stack")
            return
        self.removedNode = self.headNode.nextNode
        self.headNode.nextNode = self.headNode.nextNode.nextNode
        self.size -= 1
        return self.removedNode.dataValue

    def redo(self):
        if self.removedNode is None:
            print("Nothing to redo")
            return
        justRemovedNode = self.removedNode
        justRemovedNode.nextNode = self.headNode.nextNode
        self.headNode.nextNode = justRemovedNode
        self.size += 1
        self.removedNode = None

    def traverse(self):
        currentNode = self.headNode.nextNode
        if currentNode == None:
            print("Stack is empty")

        while currentNode != None:
            print(currentNode.dataValue)
            currentNode = currentNode.nextNode

    
class truck:
    def __init__(self):
        self.options = [{
            "ID" : 1,
            "Type" : "Truck",
            "Size" : "Small",
            "MaxBoxes" : 3,
            },
            {
            "ID" : 2,
            "Type" : "Truck",
            "Size" : "Big",
            "MaxBoxes" : 5,
            }]

