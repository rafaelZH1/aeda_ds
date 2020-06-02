from .tad_dictionary import Dictionary
from ..exceptions import NoSuchElementException, DuplicatedKeyException
from ..lists.singly_linked_list import SinglyLinkedList
from .item import Item
import ctypes 

class HashTable(Dictionary):
    def __init__(self, size=101):
        self.size_array = size
        self.num_elements = 0
        self.table = (self.size_array * ctypes.py_object)()

        for i in range(self.size_array):
            self.table[i] = SinglyLinkedList()

    def size(self):
        return self.num_elements

    def is_full(self):
        return False

    def get(self, k):
        if self.is_empty():
            raise NoSuchElementException()
        idx = self.hash_function(k)
        colision = self.table[idx]
        itera = colision.iterador()
        while itera.has_next():
            item = itera.next()
            if item.get_key() == k:
                return item.get_value()
            

    def insert(self, k, v):
        if self.has_key(k):
            raise DuplicatedKeyException()
        idx = self.hash_function(k)
        item = Item(k,v)
        self.table[idx].insert_first(item)
        self.num_elements += 1

    def update(self, k, v):
        if not self.has_key(k):
            raise NoSuchElementException()
        idx = self.hash_function(k)
        colision = self.table[idx]
        itera = colision.iterador()
        while itera.has_next():
            current_item = itera.next()
            if current_item.get_key() == k:
                return self.current_item.set_value(v)

    def remove(self, k):
        if self.num_elements == 0:
            raise NoSuchElementException()
        idx = self.hash_function(k)
        colision = self.table[idx]
        itera = colision.iterador()
        a = 0
        while itera.has_next():
            current_item = itera.next()
            if current_item.get_key() == k:
                self.table[idx].remove(a)

    def keys(self):
        if self.num_elements == 0:
            raise NoSuchElementException()
        for idx in range(self.size_array):
            colision = self.table[idx]
            itera = colision.iterador()
            while itera.has_next():
                current_item = itera.next()
                if current_item.get_key():
                    return self.current_item.get_keys()

    def values(self):
        if self.num_elements == 0:
            raise NoSuchElementException()
        for idx in range (self.size_array):
            colision = self.table[idx]
            itera = colision.iterador()
            while itera.has_next():
                item = itera.next()
                if item.get_key():
                    return self.item.get_value()

    def items(self):
        item_list = SinglyLinkedList
        for i in range (self.size_array):
            colision = self.table[i]
            itera = colision.iterador()
            while itera.has_next():
                current_item = itera.next()
                item_list.insert_last(current_item)
            return item_list

    def hash_function(self, k):
        return sum([ord(c) for c in k]) % self.size_array