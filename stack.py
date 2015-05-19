
class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def search(self,item):
      return item in self.items

     def pop(self):
         try:
          return self.items.pop()
         except IndexError:
          print 'Ill-formatted expression'
          exit()

     def peek(self):
         try:
          return self.items[len(self.items)-1]
         except:
          return False

     def size(self):
         return len(self.items)
