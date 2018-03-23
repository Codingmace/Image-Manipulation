# Linkedlist class which links one noad to another.
from Node import *


class LinkedList(object):
    
    def __init__(self):
        self.head = None
        
    def isEmpty(self):
        return self.head == None
    
    # Adds node to the end
    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head(temp)

    # Returns Number of Nodes
    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()    
        return count
    
    # Searches for node with the value of Item
    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found

    # Removes node with the value of Item
    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
    
