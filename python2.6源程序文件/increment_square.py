
def increment(n):
     return n+1
def square(n):
     return n**2
def findSequence(initial,goal):
     candidates=[(str(initial),initial)]
     for i in range(1,goal-initial+1):
          newsCandidates=[]
          for (action,result) in candidates:
               for (a,r) in [('increment',increment),
                             ('square',square)]:
                    newsCandidates.append((action+' '+a,r(result)))
                    print i,':',newsCandidates[-1]
                    if newsCandidates[-1][1]==goal:
                         return newsCandidates[-1]
          candidates=newsCandidates

          
def apply(opList,arg):
     if len(opList)==0:
          return arg
     else:
          return apply(opList[1:],opList[0](arg))

def addLevel(opList,fctList):
     return [x+[y] for y in fctList for x in opList]

def findSequence1(initial,goal):
     opList=[[]]
     for i in range(1,goal-initial+1):
          opList=addLevel(opList,[increment,square])
          for seq in opList:
               if apply(seq,initial)==goal:
                    return seq

class Node:
     def __init__(self,parent,action,answer):
          self.parent=parent
          self.action=action
          self.answer=answer
     def path(self):
          if self.parent==None:
               return [(self.action,self.answer)]
          else:
               return self.parent.path()+[(self.action,self.answer)]

def findSequence2(initial,goal):
     q=[Node(None,None,1)]
     while q:
          parent=q.pop(0)
          for (a,r) in [('increment',increment),('square',square)]:
               newNode=Node(parent,a,r(parent.answer))
               if newNode.answer==goal:
                    return newNode.path()
               else:
                    q.append(newNode)
     return None
answer=findSequence2(1,100)
print 'answer=',answer
