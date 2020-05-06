from nodes import SingleListNode
from list import List
from exceptions import EmptyListException, InvalidPositionException, NoSuchElementException


class single_linked_list(List):

    def __init__(self, head):
        self.head = None
        self.tail = None
        self.num_elements = 0


    # Returns true iff the list contains no elements.
    def is_empty(self):
        return self.head == 0

    # Returns the number of elements in the list.

    def size(self):
        return self.num_elements

    # Returns the first element of the list.
    # Throws EmptyListException.

    def get_first(self):
        if self.is_empty():
            raise EmptyListException()
        return self.head.get_element()

    # Returns the last element of the list.
    # Throws EmptyListException.

    def get_last(self):
        if self.is_empty():
            raise EmptyListException()
        return self.tail.get_element()

    # Returns the element at the specified position in the list.
    # Range of valid positions: 0, ..., size()-1.

    def get(self, position):
        if self.is_empty():
            raise EmptyListException()
        node = self.head
        current_position = 0
        while current_position < position:
            node = node.get_next()
            current_position += 1
        return node.get_element()

    # Returns the position in the list of the
    # first occurrence of the specified element,
    # or -1 if the specified element does not
    # occur in the list.

    def find(self, element):
        node = self.head
        position = 0
        while node is not None:
            if node.get_element() == element:
                return position
            node = node.get_next()
            position += 1
        return -1

    # Inserts the specified element at the first position in the list.

    def insert_first(self, element):
        node = SingleListNode(element, self.head)
        self.head = node
        self.num_elements +=1
        if self.tail is None:
            self.head = self.tail
        self.num_elements += 1

    # Inserts the specified element at the last position in the list.

    def insert_last(self, element):
        node = SingleListNode(element, None)
        if self.tail is not None:
            self.tail.set_next(node)
        self.tail = node
        if self.head is None:
            self.head = self.tail
        self.num_elements += 1


    # Inserts the specified element at the specified position in the list.
    # Range of valid positions: 0, ..., size().
    # If the specified position is 0, insert corresponds to insertFirst.
    # If the specified position is size(), insert corresponds to insertLast.
    # Throws InvalidPositionException.

    def insert(self, element, position):
        while position < self.size():
            if position == 0:
                self.insert_first(element)
            if position == self.num_elements:
                self.insert_last(element)
            if position > 0 and position < self.size():
                current = self.head
                for i in range(position):
                    if i == position:
                        new = SingleListNode(element, current.get_next())
                        current.set_next(new)
                self.num_elements += 1
        else:
            position > 0 and position > self.size()
            raise InvalidPositionException()



    # Removes and returns the element at the first position in the list.
    # Throws EmptyListException.

    def remove_first(self):
        if self.is_empty():
            raise EmptyListException()
        else:
            self.head = self.get_next

    # Removes and returns the element at the last position in the list.
    # Throws EmptyListException.

    def remove_last(self):
        if self.is_empty():
            raise EmptyListException()
        current_position = 0
        node = self.head
        while current_position < self.size():
            if node.next_node == self.tail:
                node.next_node = None
                self.tail = node
                break
            node = node.get_next()
            current_position += 1
            self.num_elements -= 1

    
    # Removes and returns the element at the specified position in the list.
    # Range of valid positions: 0, ..., size()-1.
    # Throws InvalidPositionException.

    def remove(self, position):
        if position > 0 and position > self.size()-1:
            raise InvalidPositionException()
        while position < (self.size()-1):
            if position == 0:
                self.remove_first()
            if position == (self.size()-1):
                self.remove_last()
            if position > 0 and position < (self.size()-1):
                for i in range(position):
                    if i == position-1:
                        current.set_next(current.get_next().get_next())
                    current = current.get_next()
                self.tail = None
                self.num_elements = 0

                

    # Removes all elements from the list.

    def make_empty(self):
        self.head = None
        self.tail = None
        self.num_elements = 0

    # Returns an iterator of the elements in the list (in proper sequence).
    
    def iterator(self): pass