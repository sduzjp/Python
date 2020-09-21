# @description:通过占位符来构造通用URL爬取多个网页实例--爬取名言,处理爬取网页顺序问题
# @Author: 周健平
# @company: 山东大学
# @Time: 2020/7/16 22:28
import time

import scrapy

start_time = time.time( )


# 清空原来文件所有内容并返回
def read_account( filename ):
    with open( filename , 'r+' , encoding='utf-8' ) as f:
        res = f.readlines( )
        print( res )
        f.seek( 0 )
        f.truncate( )


read_account( 'mingYan2_txt.txt' )


class MingYan1( scrapy.Spider ):
    name = 'MingYan2'
    # 通过占位符来构造通用url，这里会存在爬取网页的时候不是顺序爬取的，这是由于多线程的原因
    # scrapy框架是异步爬虫框架，并不是等待你一个url访问完了再去访问下一个，这样很占用系统资源
    # 而是在访问一个url的空隙（等待相应的空闲时间）再同时去访问别的url，不至于闲置系统资源。
    # 所以输出的时候就是线程中哪个先完成哪个就先输出了
    start_urls = ["http://lab.scrapyd.cn/page/{}/".format( i ) for i in range( 1 , 2 )]
    index = 1

    def parse( self , response ):
        # 爬取出每页的名言正文内容
        f = open( 'mingYan2_txt.txt' , 'a' , encoding='utf-8' )
        contents = response.xpath( '//div[@class="quote post"]' ).xpath( 'string(.)' ).extract( )
        for i in range( len( contents ) ):
            f.write( contents[i] )
            # 把每页的五条名言依次写入文本中
        f.write( "-----------------------------" )
        f.close( )
        # 利用回调函数依次爬取多个网页，可以解决顺序问题
        if self.index != 6:
            next_url = ["http://lab.scrapyd.cn/page/{}/".format( page ) for page in
                        range( self.index + 1 , self.index + 2 )]
            self.index += 1
            yield scrapy.Request( next_url[0] , callback=self.parse )
        else:
            end_time = time.time( )
            spend_time = end_time - start_time
            print( "程序运行了%.2f秒" % spend_time )
