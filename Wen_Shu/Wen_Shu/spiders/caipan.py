# -*- coding: utf-8 -*-
import scrapy
import datetime
from urllib import parse
from scrapy.http import Request
from w3lib.html import remove_tags
from Wen_Shu.items import Wen_Shu_ArticleItem
class CaipanSpider(scrapy.Spider):
    name = 'caipan'
    allowed_domains = ["court.gov.cn"]
    start_urls = ['http://www.court.gov.cn/wenshu/gengduo-6.html'] #文书网首页url

    def parse(self, response):
        """
                1.获取文章列表页中的文章URL并交给scrapy下载后并进行解析
                2.获取下一页的URL并交给scrapy进行下载，下载完成后交给parse

                """
        post_nodes = response.css(".list .wslist .l .list_tit a")
        for post_node in post_nodes:
            post_url = post_node.css("::attr(href)").extract_first("")
            yield Request(url=parse.urljoin(response.url, post_url),callback=self.parse_detail)   # 域名连接作用
            #提取下一页并交给scrapy进行下载
        next_url = response.css(".next::attr(href)").extract_first("")
        if next_url:
            yield Request(url=parse.urljoin(response.url,next_url), callback=self.parse)
    def parse_detail(self,response):
        #填充到item创建的字段
        Wen_Article = Wen_Shu_ArticleItem()
        title = response.xpath('//*[@id="container"]/div/div/div[1]/text()').extract_first("")
        datetime1 = response.xpath('//*[@id="container"]/div/div/div[2]/ul/li[2]/text()').extract_first("")
        content = response.xpath('//*[@id="zoom"]').extract_first("").replace('\n', '').replace('\r', '').replace('//W3C//DTDHTML4.0Transitional//EN\\', '').replace('\t', '').replace('\xa0', '')
        content = remove_tags(content)
        print(content)
        Wen_Article["title"] = title
        Wen_Article["datetime1"] = datetime1
        Wen_Article["content"] = content
        yield Wen_Article #创建好字段 调用函数   注意在settings中的itempileline不能让他默认注释