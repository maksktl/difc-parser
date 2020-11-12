from scrapy.crawler import CrawlerProcess

from spiders.difc_spider import CompaniesSpider

if __name__ == '__main__':
    process = CrawlerProcess(settings={
        "ITEM_PIPELINES": {
            'pipelines.DifcScraperPipeline': 300,
        }
    })
    process.crawl(CompaniesSpider)
    process.start()
