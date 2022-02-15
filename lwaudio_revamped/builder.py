from .website_strategy import Website
from .product import Product


class ProductBuilder:
    def __init__(self, website_scraper: Website, product: Product) -> None:
        self.product = product
        self.scraper = website_scraper

    def build_product(self):
        self.product.from_dict(self.scraper.get_all_data())
