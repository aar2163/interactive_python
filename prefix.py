operandsList = list("0123456789")
operatorsList = list("+-/*()")
parenthesisList = list("()")

prec = {}
prec['*'] = 3
prec['/'] = 3
prec['+'] = 2
prec['-'] = 2
prec['('] = 1
prec[')'] = 1
maxprec = 3

class Stack:
 def __init__(self):
  self.items = []
 def push(self,n):
  self.items.append(n)
 def pop(self):
  return self.items.pop()
 def peek(self):
  a = self.items
  return a[len(a)-1]
 def isEmpty(self):
  return len(self.items) == 0
 def __str__(self):
  return str(self.items) 
 def size(self):
  return len(self.items)

class Operation:
 def __init__(self):
  self.operator = None
  self.operand1 = None
  self.operand2 = None
  self.break_loop = False

 def do_op(self,operators,operands):
  print operators,operands
  self.operator = operators.pop()[0]
  print self.operator

  self.break_loop = True if self.operator == '(' else False

  if(self.operator in parenthesisList):
   return

  self.operand2 = operands.pop()
  self.operand1 = operands.pop()
  r = do_math(self)
  operands.push(r)

def do_math(operation):
 op = operation.operator
 op1 = int(operation.operand1)
 op2 = int(operation.operand2)

 if (op == '+'):
  return op1+op2 
 if (op == '-'):
  return op1-op2 
 if (op == '*'):
  return op1*op2 
 if (op == '/'):
  return op1/op2 

def get_prec(token,parenthesis):
 return prec[token] + maxprec*(parenthesis.size()+1)


def direct(string):
 operands = Stack()
 operators = Stack()
 parenthesis = Stack()
 operation = Operation()

 tokenList = list(string)

 for token in tokenList:
  if(token == ' '):
   continue
  elif(token in operandsList):
   operands.push(token)
  elif(token in operatorsList):
   if token == '(':
    parenthesis.push(token)

   tokenPrec = get_prec(token,parenthesis)
   print 'token', token, tokenPrec

   while not operators.isEmpty() and tokenPrec <= operators.peek()[1]:
    operation.do_op(operators,operands)
    if(operation.break_loop):
     break

   if token not in parenthesisList:
    operators.push((token,tokenPrec))
   elif token == ')':
    parenthesis.pop()
 while not operators.isEmpty():
  operation.do_op(operators,operands)
  
 print operands,operators


print direct("(4+2)*3 + (4-1) * (4 + 2)/ 2")

