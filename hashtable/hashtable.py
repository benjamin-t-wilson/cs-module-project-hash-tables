class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * (capacity)
        self.size = 0
        self.max_load_factor = 0.7
        self.min_load_factor = 0.2


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        return len(self.storage)


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        return self.size / self.capacity if self.size > 0 else 0


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        hash = 5381

        # loop through each character in key
        for char in key:
            # multiplies hash value by 33 and adds integer representation of character
            hash = (hash * 33) + ord(char)
        return hash


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        index = self.hash_index(key)
        self.size += 1
        # item does not exist
        if self.storage[index] is None:
            self.storage[index] = HashTableEntry(key, value)
        else:
            node = self.storage[index]
            while node:
                if node.key == key:
                    node.value = value
                    return
                elif node.next:
                    node = node.next
                else:
                    node.next = HashTableEntry(key, value)
                    return


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        index = self.hash_index(key)
        
        if self.storage[index]:

            self.size -= 1

            if self.storage[index].key == key:
                if self.storage[index].next is not None:
                    self.storage[index] = self.storage[index].next
                else:
                    self.storage[index] = None
            else:
                node = self.storage[index]
                while node.next:
                    if node.next.key == key:
                        node.next = None
                    else:
                        node = node.next
        else:
            print("item does not exist")


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        index = self.hash_index(key)

        if self.storage[index]:
            node = self.storage[index]
            while node:
                if node.key == key:
                    return node.value
                else:
                    node = node.next
        else:
            return self.storage[index]


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        if self.get_load_factor() > self.max_load_factor:
            old_storage = self.storage.copy()
            self.capacity = new_capacity or self.capacity * 2
            self.storage = [None] * self.capacity

            for item in old_storage:
                while item:
                    self.put(item.key, item.value)
                    item = item.next
            return
        elif self.get_load_factor() < self.min_load_factor and self.capacity > 8:
            old_storage = self.storage.copy()
            self.capacity = new_capacity or self.capacity / 2
            self.storage = [None] * self.capacity

            for item in old_storage:
                while item:
                    self.put(item.key, item.value)
                    item = item.next
            return
        else:
            return


if __name__ == "__main__":
    ht = HashTable(8)
    print("LARGE BOI ", ht.get_load_factor())
    ht.put("line_1", "'Twas brillig, and the slithy toves")
    print("LARGE BOI ", ht.get_load_factor())
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    print("LARGE BOI ", ht.get_load_factor())
    ht.put("line_3", "All mimsy were the borogoves,")
    print("LARGE BOI ", ht.get_load_factor())
    ht.put("line_4", "And the mome raths outgrabe.")
    print("LARGE BOI ", ht.get_load_factor())
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    print("LARGE BOI ", ht.get_load_factor())
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    print("LARGE BOI ", ht.get_load_factor())
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    print("LARGE BOI ", ht.get_load_factor())
    ht.put("line_8", 'The frumious Bandersnatch!"')
    print("LARGE BOI ", ht.get_load_factor())
    ht.put("line_9", "He took his vorpal sword in hand;")
    print("LARGE BOI ", ht.get_load_factor())
    ht.put("line_10", "Long time the manxome foe he sought--")
    print("LARGE BOI ", ht.get_load_factor())
    ht.put("line_11", "So rested he by the Tumtum tree")
    print("LARGE BOI ", ht.get_load_factor())
    ht.put("line_12", "And stood awhile in thought.")
    print("LARGE BOI ", ht.get_load_factor())

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
