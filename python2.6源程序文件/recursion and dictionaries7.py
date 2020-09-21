
# -*- coding: cp936 -*-
def most_common_words(freqs):
     values=freqs.values()
     best=max(values)
     words=[]
     for k in freqs:
          if freqs[k]==best:
               words.append(k)
     return (words,best)
'''
创建一个字典
通过value确定key并且返回元组（key，value）
'''
def words_often(freqs,minTimes):
     result=[]
     done=False
     while not done:
          temp=most_common_words(freqs)
          if temp[1]>=minTimes:
               result.append(temp)
               for w in temp[0]:
                    del(freqs[w])
          else:
               done=True
     return result
#beatles={key1:value1,key2:value2,,,,,}
#print(words_often(beatles,5))
          
