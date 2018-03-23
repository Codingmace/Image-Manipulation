# Combining Node and LinkedList into 1 File
# Singly LinkedList
class Node :

    def __init__(self, data) :
        self.data = data
        self.next = None
        self.prev = None


class LinkedList :

    def __init__(self) :
        self.head = None        

    # Adds node with Data to the end
    def add(self, data) :
        node = Node(data)
        if self.head == None:    
            self.head = node
        else :
            node.next = self.head
            node.next.prev = node                        
            self.head = node 

    # Iterates using temp to find item
    def search(self, item) :
        temp = self.head
        if temp != None :
            while temp.next != None :
                if (temp.data == item) :
                    return temp                
                temp = temp.next
            if (temp.data == item) :
                return temp
        return None

    # Finds and Removes Node with value Item
    def remove(self, item) :
        tmp = item.prev
        item.prev.next = item.next
        item.prev = tmp        

    # Returns LinkedList as a String
    def __str__(self) :
        s = ""
        p = self.head
        if p != None:        
            while p.next != None :
                s += p.data + " "
                p = p.next
            s += p.data
        return s
    
