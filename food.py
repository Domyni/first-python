class Node:
    def __init__(self, dataValue = None):
       self.dataValue = dataValue 
       self.nextNode = None

class SLinkedList:
    def __init__(self):
        self.headNode = None
    
    def append(self, data):
        newNode = Node(data)

        if self.headNode is None:
            self.headNode = newNode
            return

        currentNode = self.headNode

        while currentNode.nextNode != None:
            currentNode = currentNode.nextNode

        currentNode.nextNode = newNode

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

        while currentNode != None:
            print(currentNode.dataValue)
            currentNode = currentNode.nextNode

    def delete(self, data):
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

class Food():
    def __init__(self):
        self.menuList = [
            { "id": 1, 
              "name": "Chicken Burger",
              "price": 10
            },
            { "id": 2 ,
              "name": "Beef Burger",
              "price": 12
            },
            { "id": 3,
              "name": "Fries",
              "price": 3
            },
            { "id": 4,
              "name": "Soda",
              "price": 2
            },
        ]

        self.taxRate = 0.06
        self.total = 0

    def addFood(self, id, quantity):
        self.total += (self.menuList[id - 1].get("price") * quantity)

    def removeFood(self, id, quantity):
        self.total -= (self.menuList[id - 1].get("price") * quantity)

    def totalPriceWithTax(self):
        return self.total + (self.total * self.taxRate)
  
    def averagePerPax(self, p):
        return self.totalPriceWithTax() / p
