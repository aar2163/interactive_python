from stack import Stack

class poles:
 def __init__(self):
  self.current = None
  self.pcurrent = None
  self.size = None
  self.max = None
  self.p1 = Stack()
  self.p2 = Stack()
  self.p3 = Stack()
  self.goto1 = [self.p2,self.p3]
  self.goto2 = [self.p3,self.p1]
  self.goto3 = [self.p1,self.p2]
  self.next_move = [(self.p1,self.goto1),(self.p2,self.goto2),(self.p3,self.goto3)]

def make_initial(n):
 p = poles()
 p.current = 1
 p.pcurrent = p.p1
 p.size = n
 p.max = 1

 for i in range(n):
  p.p1.push(n-i)

 return p

def do_move(p1,p2):
 i = p1.pop()
 p2.push(i)
 return 1

def can_move(source,p,g):
 bReturn = (False,False)
 if p.size() > 0:
  for h,k in enumerate(g):

   if (p == source and k.size() == 0) or p.peek() < k.peek():
     bReturn = (k,h)
     break
     

 return bReturn

def move_tower(poles):
 nsteps = 0
 p1 = poles.p1
 p2 = poles.p2
 p3 = poles.p3
 g1 = poles.goto1
 g2 = poles.goto2
 g3 = poles.goto3

 for hk,k in enumerate(poles.next_move):
  pl = k[0]
  gl = k[1]
  m,h = can_move(p1,pl,gl)
  if m:
   nsteps += do_move(pl,m)
   delta = (h+hk+2) % 3
   poles.next_move = poles.next_move[delta:] + poles.next_move[:delta]
   break

 if p1.size() == 0:
  return nsteps
 else:
  return nsteps + move_tower(poles)
  
  

 

poles = make_initial(6)

nsteps = move_tower(poles)
print nsteps


