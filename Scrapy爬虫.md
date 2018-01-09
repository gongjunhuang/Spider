Scrapy常见命令

     bench         Run quick benchmark test                                                                                  **fetch **        Fetch a URL using the Scrapy downloader                                                                   genspider     Generate new spider using pre-defined templates                                                           runspider     Run a self-contained spider (without creating a project)                                                  settings      Get settings values                                                                                       **shell**         Interactive scraping console        进入shell界面                                                                      startproject  Create new project                                                                                        version       Print Scrapy version                                                                                      **view **         Open URL in browser, as seen by Scrapy  
     
** scrapy fetch 'url' **
 
     from scrapy.spiders import Spider
    
    class FirstSpider(Spider):
        name = 'first'
        allowed_domains = ['bing.com']
        start_urls = ['http://www.bing.com',]
        def parse(self, response):
            pass
            

爬取命令
** scrapy runspider first.py**

**scrapy genspider -l **     创建爬虫项目

看生成爬虫列表    **basic   crawl     csvfeed   xmlfeed**

**scrapy genspider -t basic**  爬虫命   域名

**scrapy crawl 爬虫名**运行哪个爬虫


**Xpath表达式**

**/从顶端开始寻找       //寻找所有的标签**

定位某个标签**[@属性=？]**        **//li[@class='xpath']/a/@href**

/html/head

text()

href=''     属性

    item = ReadFreeItem()
            item['content'] = response.xpath('').extract()
            yield item

scrapy startproject name
scrapy genspider -t basic name 域名

parse_item:通过Xpath来处理链接

通过浏览器爬取：from scrapy.http import Request，在start_requests中设置User-Agent，并在settings中设置User-Agent

爬取完毕之后在pipelines中处理爬取的item

