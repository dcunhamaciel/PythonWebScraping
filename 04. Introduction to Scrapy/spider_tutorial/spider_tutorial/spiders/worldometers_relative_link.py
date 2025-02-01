import scrapy

class WorldometersSpider(scrapy.Spider):
    name = "worldometers_relative_link"
    allowed_domains = ["www.worldometers.info"]
    start_urls = ["https://www.worldometers.info/world-population/population-by-country"]

    def parse(self, response):
        countries = response.xpath('//td/a')

        for country in countries:
            country_name = country.xpath('.//text()').get()
            link = country.xpath('.//@href').get()

            #absolute_url = f'https://www.worldometers.info/{link}'
            #absolute_url = response.urljoin(link)
            #yield scrapy.Request(absolute_url)

            yield response.follow(link)
