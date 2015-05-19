class LogicGate:
 
 def __init__(self,n):
  self.name = n
  self.output = None
 
 def getOutput(self):
  self.output = self.PerformGateLogic()
  return self.output

class BinaryGate(LogicGate):
 
 def __init__(self,n):
  LogicGate.__init__(self,n)
  self.pinA = None
  self.pinB = None

 def getPinA(self):
  if self.pinA == None:
   return int(input("enter pin a:"))
  else:
   return self.pinA.getFrom().getOutput()

 def getPinB(self):
  if self.pinB == None:
   return int(input("enter pin b:"))
  else:
   return self.pinB.getFrom().getOutput()

 def setNextPin(self, source):
  if self.pinA == None:
   self.pinA = source
  elif self.pinB == None:
   self.pinB = source
  else:
   print("no empty pins")

class AndGate(BinaryGate):
 
 def __init__(self,n):
  BinaryGate.__init__(self,n)

 def PerformGateLogic(self):
  a = self.getPinA()
  b = self.getPinB()

  if(a == 1 and b == 1):
   return True
  else:
   return False

class NAndGate(AndGate):
 def __init__(self,n):
  AndGate.__init__(self,n)

 def PerformGateLogic(self):
  r = AndGate.PerformGateLogic(self)
  return False if r else True

class OrGate(BinaryGate):
 
 def __init__(self,n):
  BinaryGate.__init__(self,n)

 def PerformGateLogic(self):
  a = self.getPinA()
  b = self.getPinB()

  if(a == 1 or b == 1):
   return True
  else:
   return False

class NOrGate(OrGate):
 def __init__(self,n):
  OrGate.__init__(self,n)

 def PerformGateLogic(self):
  r = OrGate.PerformGateLogic(self)

  return False if r else True

class UnaryGate(LogicGate):

 def __init__(self,n):
  LogicGate.__init__(self, n)
  self.pin = None

 def getPin(self):
  if self.pin == None:
   return int(input("enter pin:"))
  else:
   return self.pin.getFrom().getOutput()

 def setNextPin(self, source):
  if self.pin == None:
   self.pin = source
  else:
   print("no empty pins")

class NotGate(UnaryGate):
 
 def __init__(self,n):
  UnaryGate.__init__(self,n)

 def PerformGateLogic(self):
  if self.getPin():
   return 0
  else:
   return 1

class Connector:

 def __init__(self, fgate, tgate):
  self.fromgate = fgate
  self.togate = tgate

  tgate.setNextPin(self)

 def getFrom(self):
  return self.fromgate

 def getTo(self):
  return self.togate

g1 = AndGate("G1")
g2 = AndGate("G2")
g3 = NOrGate("G3")
c1 = Connector(g1,g3)
c2 = Connector(g2,g3)
print(g3.getOutput())

g4 = NAndGate("G4")
g5 = NAndGate("G5")
g6 = AndGate("G6")
c3 = Connector(g4,g6)
c4 = Connector(g5,g6)
print(g6.getOutput())





