class Queue:
 def __init__(self):
  self.items = []
 def enqueue(self,name):
  self.items.append(name)
 def dequeue(self):
  return self.items.pop(0)
 def size(self):
  return len(self.items)

def hotPotato(namelist, num):
    simqueue = Queue()
    for name in namelist:
        simqueue.enqueue(name)

    while simqueue.size() > 1:
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())

        simqueue.dequeue()

    return simqueue.dequeue()

print(hotPotato(["Bill","David","Susan","Jane","Kent","Brad"],7))
