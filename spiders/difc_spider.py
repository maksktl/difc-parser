from scrapy.exceptions import CloseSpider
from scrapy.spiders import SitemapSpider

from config import FIELDS_XPATH, KEY_XPATH, VALUE_XPATH, TITLES, INFORMATION_XPATH, COMPANY_OVERVIEW_XPATH, \
    CONVERT_TO_NULL, TOTAL
from items import CompanyItem
from utils.content_getter import ContentGetter


class CompaniesSpider(SitemapSpider):
    name = 'companies'
    sitemap_urls = ['https://www.difc.ae/public_register_1.xml']
    sitemap_rules = [
        ('/public-register/', 'parse_company')
    ]
    content_getter = ContentGetter(FIELDS_XPATH, KEY_XPATH, VALUE_XPATH, TITLES, CONVERT_TO_NULL)
    companies_parsed = 0

    def parse_company(self, response):
        # Проверяем количество спарсеных компание, если число больше нужного, то заканчиваем работу
        if self.companies_parsed >= TOTAL:
            raise CloseSpider(f"{self.companies_parsed} companies was parsed!")
        self.companies_parsed += 1

        item = CompanyItem()
        try:
            # Get containers where stored necessary data
            company_overview_container = response.xpath(COMPANY_OVERVIEW_XPATH)
            information_containers = response.xpath(INFORMATION_XPATH)
        except ValueError:
            self.logger.error('XPath error, please check site if there are some changes')
            return {}

        # Collecting company overview block data
        values = {}
        for fields in company_overview_container:
            info = self.content_getter.get_information(fields)
            for key, value in info.items():
                values[key] = value
        item['company_overview'] = values

        # Collecting other data
        for container in information_containers:
            key = self.content_getter.get_title(container)
            value = self.content_getter.get_information(container)
            try:
                item[key] = value
            except KeyError:
                self.logger.warning(f'Unexpected key: {key}. Probably there are new data!')

        # Set id
        item['_id'] = item['company_overview']['registered_number']
        yield item
