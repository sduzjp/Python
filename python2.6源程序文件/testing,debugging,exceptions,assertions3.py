def get_ratios(L1,L2):
     '''Assumes:L1 and L2 are lists of equal length of numbers
     returns:a list containing L1[i]/L2[i]
     '''
     ratios=[]
     for index in range(len(L1)):
          try:
               ratios.append(L1[index]/float(L2[index]))
          except ZeroDivisionError:
               ratios.append(float('nan'))
          except:
               raise ValueError("get_ratios called with bad arg")
     return ratios
L1=[0,1,2,3,4,5]
L2=[1,2,3,0,4,5]
t=get_ratios(L1,L2)
print t
