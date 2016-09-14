class Node:
    def __init__(self, value=None, next=None, prev=None):
        self.value = value
        self.next  = next
        self.prev = prev 
    def __str__(self):
        return str(self.value)


#Create nodes
mynode1= Node("Banana")
mynode2= Node("Apple")
mynode3= Node("Orange")

#link them
mynode1.next = mynode2
mynode2.next = mynode3
mynode3.prev = mynode2
mynode2.prev = mynode1



def printEndToStart(lastnode):
    while(lastnode!=0):
        print (lastnode.value)
        lastnode=lastnode.prev


printEndToStart(mynode3)
        
