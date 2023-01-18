# Importing the necessary libraries
import pywhatkit
import sys

# Assigning a class function for singly linked lists
class Node(object):
    # Singly linked node
    def __init__(self, value=None, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

# Assigning a class function for doubly linked lists
class doubly_linked_list(object):
    # Doubly linked list
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

   # Append an item 
    def append_video(self, value):
        new_item = Node(value, None, None)
        if self.head is None:
            self.head = new_item
            self.tail = self.head
        else:
            new_item.prev = self.tail
            self.tail.next = new_item
            self.tail = new_item
        self.count += 1

    # Delete a specific item          
    def delete_video(self, value):
        current = self.head
        node_deleted = False
        if current is None:
            node_deleted = False

        elif current.value == value:
            self.head = current.next
            self.head.prev = None
            node_deleted = True

        elif self.tail.value == value:
            self.tail = self.tail.prev
            self.tail.next = None
            node_deleted = True

        else:
            while current:
                if current.value == value:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                    node_deleted = True
                current = current.next

        if node_deleted:
            self.count -= 1
            
    def iter(self):
        # Iterate the list for appending the value in the list
        current = self.head
        while current:
            item_val = current.value
            current = current.next
            yield item_val
 
    # appending the values to the files
    def add_to_list(self):
        fileadd = open("C:/Users/New/Downloads/Final Projects/Movie_Recommended_System_using_LinkedList/movielist.txt","w")
        for node in self.iter():
            fileadd.write(node) 
            fileadd.write("\n") 
        fileadd.close()
        
    # defing the function for displaying the list
    def displist(self):
        a_file = open("C:/Users/New/Downloads/Final Projects/Movie_Recommended_System_using_LinkedList/movielist.txt","r")
        lines = a_file.readlines()
        for line in lines:
            print(line)
        a_file.close()
          
items = doubly_linked_list()

items.append_video('Varisu')

# Defining the function to ADD,DELETE,DISPLAY AND PLAY the movie
def main():
    print("\n ***************PLEASE ENTER ANY ONE OF THE FOLLOWING OPTIONS***************")
    print("\n1. ADD Movie\n")
    print("2. DELETE Movie\n")
    print("3. DISPLAY Movie\n")
    print("4. PLAY Movie\n")
    print("5. EXIT")
    ch = int(input("\nEnter Your Choice: "))
    if ch == 1:
            Data = input ("Enter Movie Name:")
            items.append_video(Data)
            print("\nThe movie will be added to the list shortly")
            movie = open("C:/Users/New/Downloads/Final Projects/Movie_Recommended_System_using_LinkedList/movielist.txt","a")
            movie.write("\n")
            movie.write(Data)
            movie.close()
                  
    elif ch == 2:
            movi = input ("Enter Movie Name to be deleted: ")
            items.delete_video(movi)  
            print("\n The list will be deleted after 30 days that is it will be reflected in the website after one month")
            
    elif ch == 3:
            print("********Available Movie********")
            items.displist()
            print("********End of List********")
            
    elif ch == 4:
        movie_name = input("Enter Movie name: ")
        pywhatkit.playonyt(movie_name)

    elif ch == 5:
            print("****************Thank you for using Self Movie Recommended system****************")
            sys.exit()
    else:
            print("\nPlease enter the options from 1 to 5")

while True:
    main()
