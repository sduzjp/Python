def sum_list(alist):
    sum_temp=0
    for i in alist:
        sum_temp+=i
    return sum_temp
print(sum_list)
my_list=[23,45,67,89,108]
my_sum=sum_list(my_list)
print("sum of my_list:%d"%(my_sum))
