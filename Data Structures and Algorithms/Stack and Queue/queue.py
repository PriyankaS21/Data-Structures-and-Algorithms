# Bad way
myListbad = []
myListbad.append("superman")
myListbad.append("batman")
myListbad.append("flash")
myListbad
myListbad.pop(0)
myListbad

# Better way
from collections import deque

mylist = deque()
mylist.append("superman")
mylist.append("superman")
mylist.append("batman")
mylist
mylist.popleft()
mylist
mylist.popleft()
mylist
mylist.popleft()
mylist
mylist.popleft()
mylist


# 3rd good way
from queue import Queue

mylist = Queue()
mylist.put("superman")
mylist.put("aquaman")
mylist.put("flash")
mylist
mylist.get()
mylist.get()
mylist.get()
mylist.get()

mylist.get_nowait() # tells list i sempty or not, not a good way


