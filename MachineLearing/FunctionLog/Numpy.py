# @description:numpy库的学习
# @Author: 周健平
# @company: 山东大学
# @Time: 2020/4/29 15:01

# print( help( np ) )
# print( help( np.array( [] ) ) )
# numbers = np.array( [1 , 2 , 3 , 4] )
# print( numbers )
# print( numbers.dtype )

# 设置文件的绝对路径，分隔符，分隔后数据的类型，分隔跳过文件第一行
# helloworld = np.genfromtxt( "E:\\Python_language\\pycharmProjects\\project2\\FunctionLog\\helloworld.txt" ,
#                             delimiter=',' ,
#                             dtype=str ,
#                             skip_header=1 )
# print( helloworld )

# 一种查询数组中元素的方式
# vector = np.array( [5 , 10 , 15 , 20] )
# equal_to_ten = (vector == 10)
# print( equal_to_ten )
# print( vector[equal_to_ten] )
#
# # 一种矩阵的查询行或者列的方式
# matrix = np.array( [[5 , 10 , 15] , [20 , 25 , 30] , [35 , 40 , 45]] )
# second_column_25 = (matrix[: , 1] == 25)
# print( second_column_25 )
# print( matrix[second_column_25] )

#
