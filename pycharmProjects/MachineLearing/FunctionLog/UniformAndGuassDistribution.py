# @description:均匀分布和高斯分布
# @Author: 周健平
# @company: 山东大学
# @Time: 2020/4/19 10:00
import matplotlib.pyplot as plt
import numpy

if __name__ == "__main__":
    u = numpy.random.uniform( 0.0 , 1.0 , 10000 )
    plt.hist( u , 80 , facecolor='g' , alpha=0.75 )
    plt.grid( True )
    plt.show( )

    times = 10000
    for time in range( times ):
        u += numpy.random.uniform( 0.0 , 1.0 , 10000 )
    print( len( u ) )
    u /= times
    print( len( u ) )
    plt.hist( u , 80 , facecolor='g' , alpha=0.75 )
    plt.grid( True )
    plt.show( )
