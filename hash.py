# While Hash Tables tradition use key value pairs
# For this assignment you may assume the value may be hashed directly. 
# In practice, the only changes to support key/value pairs would be in __getKey()

# Be sure to implement rehashing

# Be sure to use some other data structure internally

class HashTable:

	# While Hash Tables tradition use key value pairs
# For this assignment you may assume the value may be hashed directly. 
# In practice, the only changes to support key/value pairs would be in __getKey()

# Be sure to implement rehashing

# Be sure to use some other data structure internally


###############sorry forgot to work on until late Sunday because I was getting caught up in other classes
class HashTable:

    # set up the hash table, with no values in it
    def __init__(self):
        self.__tableSize = 4
        self.size = 0
        
    # given some input, figure out its hash values
    # * You may use python hash() in this method
    def __getKey(self, x):
        return x % len(self)
        
    # rehash the table if it is not of appropriate size
    # * Rehashing is required for this assignment, though this is private
    # * I reserve the write to change the parameters of random list generation in autograder to force rehashing
    def __rehash(self, m):
        pass
        
    # insert x into the hash table
    # * Use some data structure to deal with collisions, such as:
    #   - Python List
    #   - Linked List
    #   - BST
    #   - Python Set
    #   - Python Dictionary
    #   - Stack
    #   - Queue
    def insert(self, x):
        pass
        
    # remove x from the hash table
    def remove(self, x):
        loc = self.getHash(x.__getKey())
    while(self.table[loc] != None and self.table[loc] != x):
        loc = (loc + 1) % self.max
    if self.table[loc] == None:
        return
    self.size = self.size - 1
    if self.size < self.max / 4:
        self.rehash()
        return
    self.table[loc] = None
    fix = self.next(loc)
    while self.table[fix] != None:
        if self.getHash(self.table[fix]) > loc: #write a proof
            fix = self.next(fix)
        else:
            self.table[loc] = self.table[fix]
            loc = fix
            self.table[loc] = None
            fix = self.next(fix)
    return
                
    # check if x is in the hash table
    def contains(self, x):
        pass
