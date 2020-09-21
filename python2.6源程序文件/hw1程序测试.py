# -*- coding: cp936 -*-
import pdb
import lib601.sm as sm
import string
import operator

class BinaryOp:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        return self.opStr + '(' + \
               str(self.left) + ', ' +\
               str(self.right) + ')'
    __repr__ = __str__
    
class Sum(BinaryOp):
    opStr = 'Sum'
    op=operator.add
    def eval(self,adict):
         l=self.left
         r=self.right
         t=self.op(l.eval(adict),r.eval(adict))
         return float(t)
     
class Prod(BinaryOp):
    opStr = 'Prod'
    op=operator.mul
    def eval(self,adict):
         l=self.left
         r=self.right
         t=self.op(l.eval(adict),r.eval(adict))
         return float(t)
     
class Quot(BinaryOp):
    opStr = 'Quot'
    op=operator.truediv
    def eval(self,adict):
         l=self.left
         r=self.right
         t=self.op(l.eval(adict),r.eval(adict))
         return float(t)
     
class Diff(BinaryOp):
    opStr = 'Diff'
    op=operator.sub
    def eval(self,adict):
         l=self.left
         r=self.right
         t=self.op(l.eval(adict),r.eval(adict))
         return float(t)
     
class Assign(BinaryOp):
    opStr = 'Assign'
    def eval(self,adict):
         l=self.left
         r=self.right
         adict[l.name]=r.eval(adict)
         
class Number:
    def __init__(self, val):
        self.value = val
    def __str__(self):
        return 'Num('+str(self.value)+')'
    def eval(self,adict):
         return self.value
    __repr__ = __str__

class Variable:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'Var('+self.name+')'
    def eval(self,adict):
         return adict[self.name]
    __repr__ = __str__


def numberTok(token):
    for char in token:
        if not char in string.digits: return False
    return True

# token is a string
# returns True its first character is a letter
def variableTok(token):
    for char in token:
        if char in string.letters: return True
    return False

seps = ['(', ')', '+', '-', '*', '/', '=']

def tokenize(string):
    # <your code here>
    strlist=list(string)
    def strjoin(alist):                     #将列表中的字符连成字符串
        str_=''
        for i in range(len(alist)):
            str_+=alist[i]
        return str_
    def strsplit(alist):
        list1=[]
        list2=[]
        for char in alist[::-1]:            #循环删除列表中的空格！
            if char==' ':
                alist.remove(char)
        i=0
        while i<=len(alist)-1:              #将列表中属于seps里的字符直接放到list1中
            if alist[i] in seps:
                list1.append(alist[i])
                i+=1
            elif alist[i].isdigit()==True:  #将列表中数字字符整体放到list1中
                j=i
                while j<=len(alist)-1:            
                    if alist[j].isdigit()==True:
                        list2.append(alist[j]) #判断数字字符是单个字符还是一连串数字字符
                        j+=1
                    else:
                        break
                list1.append(strjoin(list2))
                i=j
                list2=[]
            elif alist[i].isalpha()==True:  #将列表中字母字符整体放到list1中
                j=i
                while j<=len(alist)-1:
                    if alist[j].isalpha()==True:#判断字母字符是单个字符还是一连串字母字符
                        list2.append(alist[j])
                        j+=1
                    else:
                        break
                list1.append(strjoin(list2))
                i=j
                list2=[]
        return list1
    return strsplit(strlist)

#测试程序序列
#print tokenize('(1+(2*3))')
#print tokenize('(fred+george)')
#print tokenize('((fred + george) / (voldemort + 666))')
#print tokenize('(1+((2*3)+(a/b)))')



# tokens is a list of tokens
# returns a syntax tree:  an instance of {\tt Number}, {\tt Variable},
# or one of the subclasses of {\tt BinaryOp} 
def parse(tokens):
    def parseExp(index): #找到每一个括号内的运算符，然后通过运算符划分为前者运算对象和后者运算对象，并将对象进行Number和Variable处理
        # <your code here>                
        if numberTok(tokens[index])==True:#判断运算对象是否为数字，若是，将其转化为float型
            t=Number(float(tokens[index]))
            index+=1
            return (t,index)
        elif variableTok(tokens[index])==True:#判断运算对象是否为字母
            t=Variable(tokens[index])
            index+=1
            return (t,index)
        else:
            index+=1
            (left,index) = parseExp(index)           #运算对象前者，并进行递归调用 
                    
            char = tokens[index]                        
            
            index+=1                                
            (right,index) = parseExp(index)          #运算对象后者，并进行递归调用
             #判断运算符号是哪种，并对应不同的类   
            if char=='+':                           
                op=Sum(left,right)
                index+=1
                return (op,index)
            elif char=='-':
                op=Diff(left,right)
                index+=1
                return (op,index)
            elif char=='*':
                op=Prod(left,right)
                index+=1
                return (op,index)
            elif char=='/':
                op=Quot(left,right)
                index+=1
                return (op,index)
            elif char=='=':
                op=Assign(left,right)
                index+=1
                return (op,index)
            
    (parsedExp, nextIndex) = parseExp(0)
    return parsedExp
'''
alist1=['888']
alist2=['you']
alist3=['(','3','+','4',')']
alist4=['(','(','a','*','b',')','/','(','cee','-','doh',')',')']
alist5=tokenize('((a*b)/(cee-doh))')
print parse(alist1)
print parse(alist2)
print parse(alist3)
print parse(alist4)
print parse(alist5)
'''

# thing is any Python entity
# returns True if it is a number
def isNum(thing):
    return type(thing) == int or type(thing) == float




# Run calculator interactively
def calc():
    env = {}
    while True:
        e = raw_input('%')            # prints %, returns user input
        print '%',                    # your expression here
        print '   env =', env

# exprs is a list of strings
# runs calculator on those strings, in sequence, using the same environment
def calcTest(exprs):
    env = {}
    for e in exprs:
        print '%', e                    # e is the experession
        tokens=tokenize(e)
        parsedExp=parse(tokens)
        print parsedExp.eval(env)
        print '   env =', env

def testEval():
    env = {}
    Assign(Variable('a'), Number(5.0)).eval(env)
    print Variable('a').eval(env)
    env['b'] = 2.0
    print Variable('b').eval(env)
    env['c'] = 4.0
    print Variable('c').eval(env)
    print Sum(Variable('a'), Variable('b')).eval(env)
    print Sum(Diff(Variable('a'), Variable('c')), Variable('b')).eval(env)
    Assign(Variable('a'),Sum(Variable('a'), Variable('b'))).eval(env)
    print Variable('a').eval(env)
    print env

#testEval()


'''
env={}
print Number(6.0).eval(env)
env['a']=5.0
print Variable('a').eval(env)
print Assign(Variable('c'),Number(10.0)).eval(env)
print Variable('c').eval(env)
print Sum(5,Number(10)).eval(env)
print Prod(Number(5),Number(10)).eval(env)
print Diff(Number(5),Number(10)).eval(env)
print Quot(Number(5),Number(10)).eval(env)
t=Quot(Variable('a'), Variable('c')).eval(env)
print Sum(t,Number(10)).eval(env)
print Prod(Variable('a'),Variable('c')).eval(env)
print Diff(Variable('a'),Variable('c')).eval(env)
print Quot(Variable('a'),Variable('c')).eval(env)
print env
'''
testExprs = ['(2 + 5)',
             '(z = 6)',
             'z',
             '(w = (z + 1))',
             'w'
             ]
calcTest(testExprs)


