__author__ = "pengliang"
from scrapy.cmdline import execute
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
execute(["scrapy","crawl","caipan"])#调用这个函数 来执行spider 命令