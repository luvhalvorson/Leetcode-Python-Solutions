class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.mymap = []

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        mymap = self.mymap
        isexist = 0
        for pair in mymap:
            if key == pair[0]:
                pair[1] = value
                isexist = 1
                break
        if not isexist:
            mymap.append([key, value])

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        mymap = self.mymap
        
        for pair in mymap:
            if key == pair[0]:
                return pair[1]
        return -1
        

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        mymap = self.mymap
        
        for pair in mymap:
            if key == pair[0]:
                mymap.remove(pair)
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)