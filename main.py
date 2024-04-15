class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtBegin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node



    def insertAtIndex(self,data,index):
        new_node=Node(data)
        current_node = self.head
        position=0
        if (position == index):
            self.insertAtBegin(data)
        else:
            while (current_node != None and position+1!=index):
                position+=1
                current_node=current_node.next
            if current_node != None:
                new_node.next =current_node.next
                current_node.next=new_node
            else:
                print('index not found')



    def insertAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head

            while ( current_node.next != None):
                current_node= current_node.next
            current_node.next= new_node




    def updateNode (self, data , index):
        current_node =self.head
        position =0
        if position == index:
            current_node.data= data
        else:
            while (current_node != None and position+1 != index):
                position+=1
                current_node=current_node.next
            if current_node != None:
                current_node.data = data
            else:
                print('index not found')


    def del_first_node(self):
        if self.head == None:
            print('list is empty')

        else:
            current_node=self.head
            self.head=current_node.next


    def del_index(self,index):
        position=0
        current_node =self.head
        if position== index:
            self.del_first_node()
        else :
            while (current_node != None and position+1!=index):
                position+=1
                current_node=current_node.next
            if (current_node!=None):
                current_node.next =current_node.next,next
            else:
                print('node does not exist')



    def del_end (self):
        if self.head == None:
            print('no element in the list')
        else :
            current_node = self.head
            while current_node.next.next:
                current_node=current_node.next
            current_node.next = None

    def del_node(self, data):
        current_node = self.head

        if current_node.data == data:
            self.del_first_node()
            return

        while (current_node != None and current_node.next.data != data):
            current_node = current_node.next

        if current_node == None:
            return
        else:
            current_node.next = current_node.next.next

    def sizeOfLL(self):
        size = 0
        if (self.head):
            current_node = self.head
            while (current_node):
                size = size + 1
                current_node = current_node.next
            return size
        else:
            return 0






    def printLL(self):
        current_node = self.head
        while (current_node):
            print(current_node.data)
            current_node = current_node.next



def main():
    llist = LinkedList()

    while True:
        print('Press 0 for : printing the araay')
        print('Press 1 for : insert value at the starting')
        print('Press 2 for : insert value at the end')
        print('Press 3 for : insert value at an index')
        print('Press 4 for : update the node with index')
        print('Press 5 for : remove first node ')
        print('Press 6 for : remove last node')
        print('Press 7 for : remove node at an index')
        print('Press 8 for : remove a node for data ')
        print('Press 9 for : get the size of list ')

        choice = int(input('Enter your choice '))

        if choice == 0:
            llist.printLL()
        elif choice == 1:
            data = input('enter data here')
            llist.insertAtBegin(data)
            print('opreation complete ')
        elif choice == 2:
            data = input('enter data here')
            llist.insertAtEnd(data)
            print('opreation complete ')
        elif choice == 3:
            data = input('enter data here')
            index = int(input('insert index here'))
            llist.insertAtIndex(data,index)
            print('opreation complete ')
        elif choice == 4:
            data = input('enter data here')
            index = int(input('insert index here'))
            llist.updateNode(data,index)
            print('opreation complete ')
        elif choice == 5:
            llist.del_first_node()
            print('opreation complete ')
        elif choice == 6:
            llist.del_end()
            print('opreation complete ')
        elif choice == 7:
            index=int(input('enter index here'))
            llist.del_index(index)
            print('opreation complete ')
        elif choice == 8:
            data = input('enter data here')

            llist.del_node(data)
            print('opreation complete ')
        elif choice == 9:
            print(llist.sizeOfLL())





if __name__ == '__main__':
    main()
