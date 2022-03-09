class node:
    def __init__(self,data,next):
        self.data = data
        self.next = next
    
class Linked_List:
    def __init__(self):
        self.head = None
    
    def insert_node_begin(self,data):
        self.head = node(data,self.head)
    
    def print(self):
        temp = self.head
        x = ""
        while temp:
            x += str(temp.data)+"->"
            temp = temp.next
        print(x)

if __name__ == '__main__':
    sike = Linked_List()
    sike.insert_node_begin(5)
    sike.insert_node_begin(7)
    sike.print()
