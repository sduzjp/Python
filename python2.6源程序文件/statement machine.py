class SM:
     def start(self):
          self.state=self.startState
     def step(self,inp):
          (s,o)=self.getNextValues(self.state,inp)
          self.state=s
          return o
     def transduce(self,inputs):
          self.start()
          return [self.step(inp) for inp in inputs]

class Turnstile(SM):
     startState='locked'

     def getNextValues(self,state,inp):
          if inp=='coin':
               return ('unlocked','enter')
          elif inp=='turn':
               return ('locked','pay')
          elif state=='locked':
               return ('locked','pay')
          else:
               return ('unlocked','enter')
testInput=[None,'coin',None,'turn','turn','coin','coin']
ts=Turnstile()
print ts.transduce(testInput)
