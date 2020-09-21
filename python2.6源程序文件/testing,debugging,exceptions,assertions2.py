try:
     a=int(input("tell me one number:"))
     b=int(input("tell me another number:"))
     print("a/b=",a/b)
     print("a+b=",a+b)
except ValueError:
     print("Could not convert to a number.")
except ZeroDivisionError:
     print("Can't divide by zero")
except:
     print("something went very wrong")
