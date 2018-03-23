# Combining Node and LinkedList into 1 File
# Doubly LinkedList
class Node :

    def __init__(self, data, per) :
        self.per = per
        self.data = data
        self.next = None
        self.prev = None


class LinkedList :

    def __init__(self) :
        self.head = None        

    def add(self, data, per) :
        node = Node(data, per)
        if self.head == None:    
            self.head = node
        else :
            node.next = self.head
            node.next.prev = node                        
            self.head = node 

    def search(self, k) :
        p = self.head
        if p != None :
            while p.next != None :
                if (p.data == k) :
                    return p                
                p = p.next
            if (p.data == k) :
                return p
        return None

    def remove(self, p) :
        tmp = p.prev
        p.prev.next = p.next
        p.prev = tmp        

    def size(self):
        p = self.head            
        con = 0
        if p != None:
            while p.next != None:
                p = p.next
                con += 1
        return con
                
    def __str__(self) :
        s = ""
        p = self.head
        if p != None:
            while p.next != None :
                s += p.data + " " + str(p.per) + " "
                p = p.next
            s += p.data
        return s
    
