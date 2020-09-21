def get_data(aTuple):
     nums=()
     words=()
     for t in aTuple:
          nums=nums+(t[0],)
          if t[1] not in words:
               words=words+(t[1],)
     min_n=min(nums)
     max_n=max(nums)
     unique_words=len(words)
     return (min_n,max_n,unique_words)
a=get_data(((0,1),(2,3),(4,5)))
print(a)
