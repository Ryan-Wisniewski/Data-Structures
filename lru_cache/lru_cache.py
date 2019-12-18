from doubly_linked_list import DoublyLinkedList

## Add to head if most recently used item. 

## Subtract from tail IF the amount of data exeeds 
# the one of the cache

## IF the key itself is already in cache. Need to move 
# that entry to the head of the list.

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.limit = limit
        self.size = 0
        self.order = DoublyLinkedList()
        self.storage = dict()

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    #Needs to lookup the key and see if its in the cache.
    #Add to head if most recently used item.
    def get(self, key):
        if key in self.storage:
            node = self.storage[key]
            self.order.move_to_front(node)
            return node.value[1]
        else:
            return None

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    #Needs to lookup the key to see if its in hte table. 
    # If in table move the entry to the head of the DLL
    # If > limit needs to remove from the tail of the DLL
    def set(self, key, value):

        # if key in cache
        if key in self.storage:
            node = self.storage[key]
            node.value = (key, value)
            self.order.move_to_front(node)
            return


        # if in cache move to front & update
        if self.size == self.limit:
            del self.storage[self.order.tail.value[0]]
            self.order.remove_from_tail()
            self.size -= 1

        # Defining head as most recent and tail is oldest
        self.order.add_to_head((key, value))
        self.storage[key] = self.order.head
        self.size += 1

