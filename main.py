class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LInkedList:
    def __init__(self):
        self.head=None
    def listLength(self):
        currentNode=self.head
        length=0
        while currentNode is not None:
            length =+1
            currentNode=currentNode.next
        return length
    def insertHead(self,newNode):
        tempoNode=self.head
        self.head=newNode
        self.head.next=tempoNode
        del tempoNode
    def insertAtIndex(self,newNode,position):
        if position < 0 or position > self.listLength():
            print("Invalid Position")
            return
        if position ==0:
            self.insertHead(newNode)
            return
        currentNode=self.head
        currentPosition=0
        while True:
            if currentPosition == position:
                previousNode.next=newNode
                newNode.next=currentNode
                break
            previousNode=currentNode
            currentNode=currentNode.next
            currentPosition +=1
    def insertEnd(self,newNode):
        if self.head is None:
            self.head=newNode
        else:
            lastNode=self.head
            while True:
                if lastNode.next is None:
                    break
                lastNode=lastNode.next
            lastNode.next=newNode
    def printLL(self):
        if self.head is None:
            print("the list is empty")
            return
        currentNode=self.head
        while True:
            if currentNode is None:
                break
            print(currentNode.data)
            currentNode=currentNode.next
    def deleteEnd(self):
        lastNode=self.head
        while lastNode.next is not None:
            previousNode=lastNode
            lastNode=lastNode.next
        previousNode.next=None
    def deletAtIndex(self,position):
        currentNode=self.head
        currentPosition=0
        while True:
            if currentPosition ==position:
                previousNode.next=currentNode.next
                currentNode.next=None
                break
            previousNode=currentNode
            currentNode=currentNode.next
            currentPosition +=1




firstNode=Node("Mengistu")
linkedList=LInkedList()
linkedList.insertEnd(firstNode)

secondNode=Node("Araya")
linkedList.insertEnd(secondNode)

thirdNode=Node("Kalayu")
linkedList.insertEnd(thirdNode)

newFirstNode=Node("Menge")
linkedList.insertHead(newFirstNode)

atAnyNode=Node("Meresa")
linkedList.insertAtIndex(atAnyNode,2)

atZeroIndex=Node("Maregye")
linkedList.insertAtIndex(atZeroIndex,0)

atInvalidIndex=Node("Kalau")
linkedList.insertAtIndex(atInvalidIndex,12)
linkedList.deleteEnd()
linkedList.deletAtIndex(2)


linkedList.printLL()
