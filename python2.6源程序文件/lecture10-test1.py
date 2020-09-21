import lib601.dist as dist
'''
toss = dist.DDist({'head':0.5,'tail':0.5})
print toss
print toss.prob('head')
print toss.prob('tail')
print toss.prob('H')
'''

def TESTgivenAIDS(AIDS):
     if AIDS=='true':
          return dist.DDist({'positive':0.985946,'negative':0.014054})
     else:
          return dist.DDist({'positive':0.023000,'negative':0.977000})

#print TESTgivenAIDS('true')
#print TESTgivenAIDS('true').prob('negative')

AIDS=dist.DDist({'true':0.0037,'false':0.9963})
AIDSandTEST=dist.JDist(AIDS,TESTgivenAIDS)
print AIDSandTEST
