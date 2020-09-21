def isPalindrome(s):
     def tochars(s):
          s=s.lower()
          ans=''
          for c in s:
               if c in 'abcdefghijklmnopqrstuvwxyz':
                    ans+=c
          return ans
     def isPal(s):
          if len(s)<=1:
               return True
          else:
               return s[0]==s[-1] and isPal(s[1:-1])
     return isPal(tochars(s))
print(isPalindrome('Able was I,ere I saw EIba'))
print(isPalindrome('i love you'))
print(isPalindrome('Able was I ere I saw Elba'))
