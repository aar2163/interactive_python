import re
class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         try:
          return self.items.pop()
         except IndexError:
          print 'Ill-formatted expression'
          exit()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)

def infixToPostfix(infixexpr):
    prec = {}
    prec["^"] = 4
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    opStack = Stack()
    postfixList = []
    tokenList = list(infixexpr)

    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfixList.append(token)
        elif token == ' ':
         continue
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            while (not opStack.isEmpty()) and \
               (prec[opStack.peek()] >= prec[token]):
                  postfixList.append(opStack.pop())
            opStack.push(token)

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
    return " ".join(postfixList)

def do_operands(token,operands):
 operand2 = int(operands.pop())
 operand1 = int(operands.pop())
 #print token, operand1,operand2
 result = doMath(token,operand1,operand2)
 operands.push(result)

def direct(infixexpr):
    prec = {}
    prec["^"] = 4
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    operands = Stack()
    operators = Stack()
    postfixList = []
    tokenList = list(infixexpr)

    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            #postfixList.append(token)
            operands.push(token)
        elif token == ' ':
         continue
        elif token == '(':
            operators.push(token)
        elif token == ')':
            topToken = operators.pop()
            do_operands(topToken,operands)
            while topToken != '(':
                #postfixList.append(topToken)
                topToken = operators.pop()
                if topToken != '(':
                 do_operands(topToken,operands)
        else:
            while (not operators.isEmpty()) and \
               (prec[operators.peek()] >= prec[token]):
                  topToken = operators.pop()
                  do_operands(topToken,operands)
            operators.push(token)

    while not operators.isEmpty():
        topToken = operators.pop()
        do_operands(topToken,operands)

    return operands.peek()


def postfixEval(postfixExpr):
    operandStack = Stack()
    tokenList = postfixExpr.split()

    for token in tokenList:
        if token in "0123456789":
            operandStack.push(int(token))
        else:
            operand2 = operandStack.pop()
            operand1 = operandStack.pop()
            result = doMath(token,operand1,operand2)
            operandStack.push(result)
    return operandStack.pop()

def doMath(op, op1, op2):
    if op == "^":
        return pow(op1,op2)
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2

#print(infixToPostfix("A * B + C * D"))
#print(infixToPostfix("( A + B ) * C - ( D - E ) * ( F + G )"))

#print(postfixEval('7 8 + 3 2 + /'))
#pf = infixToPostfix("5 * 3 ^ (4 - 2)")

result = direct("5 * 3 ^ (4 - 2)")

print result

