'''
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.

'''
from collections import deque

class LRUCache:

    def __init__(self, capacity: int):
        self.c=capacity
        self.m=dict()
        self.deq=deque()

    def get(self, key: int) -> int:
        if key in self.m: #  if key is in the dictionary
            value=self.m[key]
            self.deq.remove(key) #remove the key
            self.deq.append(key) #add the key to the first in deq
            return value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.m: # if key is not in the dictionary
            if len(self.deq)==self.c: # check if the deq has reached its capacity
                oldest=self.deq.popleft() #remove the least recently used item to make room for the new element
                del self.m[oldest]
                # if not reach its full capcity, we can just append the new key in line 40
        else:# if key already exist in the dictionary
            self.deq.remove(key)#remove the existing key to prepare for its updated value. So it won't have duplicated keys when we append to the map with new value

        self.m[key]=value # update the value in the key no matter if the key is in the dictionary or not
        self.deq.append(key)# append new key to the front of the queue
                
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)