import lib601.dist as dist

def PTgD(diseaseValue):
     if diseaseValue=='disease':
          return dist.DDist({'posTest':0.98,'negTest':0.02})
     else:
          return dist.DDist({'posTest':0.05,'negTest':0.95})

print PTgD('disease').prob('posTest')
print PTgD('noDisease').prob('posTest')
