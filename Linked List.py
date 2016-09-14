class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next  = next

    def __str__(self):
        return str(self.value)


#Create nodes
n0= Node("Mango")
n1= Node("Banana")
n2= Node("Apple")
n3= Node("Watermelon")
n4= Node("Orange")
n5=Node("Someting")
n6=Node("Pineapple")
n4_3 = Node("Grape")

#link them
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5



def iteration(n):
    while(n!=None):
        print (n.value)
        n=n.next

def Finding_cell(n, target):
    while(n!=None):
        if(n.value==target):
            return "True"
        n=n.next
    return "Not in the list"

def AddAtBeggining (top, new):
    new.next=top.next
    top.next=new

def AddAtEnd(top, new):
    while(top.next!=None):
        top=top.next
    top.next=new
    new.next=None
def insertcell(afterthis, new):
    new.next=afterthis.next
    afterthis.next=new

def delete(afterMe):
    
    afterMe.next=afterMe.next.next

iteration(n1) 
print ()    
insertcell(n4, n4_3)
print ()
iteration(n1) 
print ()
AddAtBeggining(n1, n0)
print ()
iteration(n1) 
print ()
AddAtEnd(n1, n6)
print ()
iteration(n1) 
print ()
print (Finding_cell(n1, "Apple"))
print ()
iteration(n1) 
print ()
delete(n3)
print ()
