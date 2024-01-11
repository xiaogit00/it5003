M = 997 # M = table size is a prime number, rather small, for illustration purpose only,
# generally make load factor alpha = N/M < 7 (just a small number) where N is the maximum number of keys that you will likely need for your application

class hash_table: # this is an attempt to emulate Python dict()
    # the 'easiest' and most robust Hash Table is actually the one with Separate Chaining collision resolution technique
    def __init__(self):
        # interesting (new) technique, we can create a list of lists of pair of (string, int)
        self.underlying_table = [[] for _ in range(M)]

    # from https://visualgo.net/en/hashtable?slide=4-7
    def hash_function(self, v): # assumption 1: v uses ['A'..'Z'] only (be careful if this assumption is not true); assumption 2: v is a short string
        sum = 0
        for c in v: # for each character c in v
            sum = ((sum*26)%M + (ord(c)-ord('A')+1))%M # M is table size
        return sum

    def search(self, key): # to emulate mapper[key]
        for k, v in self.underlying_table[self.hash_function(key)]: # O(alpha), alpha is the length of this list, but with careful setup, alpha can be O(1)
            if k == key: # if there is an existing key
                return v # return this satellite data
        # if there is no previous key before (return v above is never executed)
        return None # we return a special symbol to say such key does not exist

    def remove(self, key): # to emulate del mapper[key]
        row = self.underlying_table[self.hash_function(key)] # get the reference of the row
        for i in range(len(row)): # O(alpha), alpha is the length of this chain
            if row[i][0] == key: # if there is an existing key
                row[i], row[-1] = row[-1], row[i] # swap the [key, value] to be deleted with the last [key, value] pair from the list, O(1)
                row.pop() # then erase it, O(1)
                break # do not do anything else
        # we do nothing if key is not actually found

    def insert(self, key, value): # to emulate mapper[key] = value
        if self.search(key):
            self.remove(key)
        self.underlying_table[self.hash_function(key)].append((key, value)) # just append at the back, O(1)

    def is_empty(self):
        total = 0
        for i in range(M):
            total += len(self.underlying_table[i])
        return total == 0



print("Our own Hash Table with Separate Chaining collision resolution technique")
ht = hash_table()
print(ht.is_empty()) # should be True

ht.insert("STEVEN", 77)
print(ht.is_empty()) # should be False

ht.insert("STEVEN", 39) # will update instead of creating a new one
ht.insert("GRACE", 38)
ht.insert("JANE", 10)
ht.insert("JOSHUA", 7)
ht.insert("JEMIMAH", 5)
print(ht.search("STEVEN")) # should be 39 (not 77, it has been overwritten)
print(ht.search("GRACE")) # should be 38
print(ht.search("STRANGER")) # should be None (does not exist)

ht.remove("STEVEN")
print(ht.search("STEVEN")) # should be None now (has just been deleted)
print(ht.search("GRACE")) # should remain 38
print(ht.search("JANE")) # should be 10

ht.remove("JANE")
print(ht.search("JANE")) # should be None now (has just been deleted)



print("Python dict version")
mapper = dict()
print(mapper == {}) # should be True

mapper["STEVEN"] = 77
# print(mapper == {}) # should be False

mapper["STEVEN"] = 39 # will update instead of creating a new one
mapper["GRACE"] = 38
mapper["JANE"] = 10
mapper["JOSHUA"] = 7
mapper["JEMIMAH"] = 5
print(mapper["STEVEN"]) # should be 39 (not 77, it has been overwritten)
print(mapper["GRACE"]) # should be 38
print(1 if "STRANGER" in mapper else -1) # should be -1 ("STRANGER" does not exist)

del mapper["STEVEN"]
# print(1 if "STEVEN" in mapper else -1) # should be -1 (has just been deleted)
# print(mapper["GRACE"]) # should remain 38
# print(mapper["JANE"]) # should be 10

# del mapper["JANE"]
# print(1 if "JANE" in mapper else -1) # should be -1 now (has just been deleted)