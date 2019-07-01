from scrapy import cmdline

try:
    cmdline.execute("scrapy crawl love_spider".split()) #cmdline执行文件,跟spider文件中的name一样
    input("Congratulation! It' working ... Press enter to end !")
except Exception as e:
    input("Sorry,It' not working ... Press enter to click !")