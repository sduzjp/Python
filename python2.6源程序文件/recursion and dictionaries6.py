# -*- coding: cp936 -*-
def lyrics_to_frequencies(lyrics):
     myDict={}
     for word in lyrics:
          if word in myDict:
               myDict[word]+=1
          else:
               myDict[word]=1
     return myDict
'''
创建一个字典
利用value来记录key出现的次数
'''
