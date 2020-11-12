import scrapy


class CompanyItem(scrapy.Item):
    _id = scrapy.Field()
    company_overview = scrapy.Field()
    company_information = scrapy.Field()
    data_protection = scrapy.Field()
    former_properties = scrapy.Field()
