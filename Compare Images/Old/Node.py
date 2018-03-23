# Object used to store values for LinkedList

class Node:

    def __init__(self, initdata):
        self.data = initdata
        self.next = None
    
    # Return Node Value
    def getData(self):
        return self.data

    # Returns Node linked to
    def getNext(self):
        return self.next

    # Sets Node Data
    def setData(self, newdata):
        self.data = newdata

    # Sets Linked Node
    def setNext(self, newnext):
        self.next = newnext
        
