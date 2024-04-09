# T can be implemented as an array of keys, T has the size of the universe of keys
def direct_access_insert(T, key):
    T[key] = True

def direct_access_delete(T, key):
    T[key] = False

def direct_access_search(T,key):
    return T[key]

# the typical size of the set is way smaller than the size of the universe |S|<<|U|
# complexity is constant O(1)