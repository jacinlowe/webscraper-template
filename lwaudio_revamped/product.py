from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Dict, List, Union


@dataclass(order=True, frozen=True)
class BaseDictKey:
    """Great little class.
    this will allow any param to not be needed for initiation
    essentially it will set any non initiated attribute to None.
    Makes it very easy to only implement the params you need to.

    """

    def __init_subclass__(cls, *args, **kwargs) -> None:
        for field, value in cls.__annotations__.items():
            cls.__annotations__[field] = Union[value, None]
            if not hasattr(cls, field):
                setattr(cls, field, None)
        super().__init_subclass__(*args, **kwargs)


class Product(ABC):
    @abstractmethod
    def to_dict(self):
        """will transform the product into a dictionary for export or what have you"""
        pass

    @abstractmethod
    def from_dict(self, dictionary: Dict):
        """Will load product from a dictionary"""
        pass


@dataclass
class AAMPProduct(BaseDictKey, Product):
    """Text goes here i think lol"""

    sku: str
    ean: str
    product_name: str
    name: str
    description_text: str
    description: str
    price_ssp: str
    discount_price: str
    net_price: str
    stock_handling: str
    stock_amount: str
    can_run_empty_product: bool
    main_picture: str
    all_pictures: List[str]
    is_new_product: bool
    category_name: str
    sub_cat_1: str
    sub_cat_2: str
    sub_cat_3: str
    sub_cat_4: str
    is_old_product: bool
    brand: str
    can_hide_product: bool
    stock_message: str

    def to_dict(self):
        return {
            "Artikelnummer": self.sku,
            "EAN-kod": self.ean,
            "SKU-kod": self.product_name,
            "Namn (SV)": self.name,
            "Inledande text (SV)": self.description_text,
            "Beskrivning (SV)": self.description,
            "Pris (SEK)": self.price_ssp,
            "Extrapris (SEK)": self.discount_price,
            "Inköpspris (SEK)": self.net_price,
            "Lagerhantering (1/0)": self.stock_handling,
            "Lagersaldo": self.stock_amount,
            "Tillåt beställningar även om lagret är slut och visa lagermeddelande (1/0)": self.can_run_empty_product,
            "Huvudbild": self.main_picture,
            "Alla bilder": self.all_pictures,
            "Nyhet (1/0)": self.is_new_product,
            "Produktgruppens namn": self.category_name,
            "Undergrupp nivå 1": self.sub_cat_1,
            "Undergrupp nivå 2": self.sub_cat_2,
            "Undergrupp nivå 3": self.sub_cat_3,
            "Undergrupp nivå 4": self.sub_cat_4,
            "Skick": self.is_old_product,
            "Varumärke": self.brand,
            "Dölj produkten om lagret är slut (1/0)": self.can_hide_product,
            "Visa Lagersaldo eller lagermedelanade": self.stock_message,
        }

    def from_dict(self, dictionary: Dict):
        for key, value in dictionary.items():
            if key == "Artikelnummer":
                self.sku = value
            elif key == "EAN-kod":
                self.ean = value
            elif key == "SKU-kod":
                self.product_name = value
            elif key == "Namn (SV)":
                self.name = value
            elif key == "Inledande text (SV)":
                self.description_text = value
            elif key == "Beskrivning (SV)":
                self.description = value
            elif key == "Pris (SEK)":
                self.price_ssp = value
            elif key == "Extrapris (SEK)":
                self.discount_price = value
            elif key == "Inköpspris (SEK)":
                self.net_price = value
            elif key == "Lagerhantering (1/0)":
                self.stock_handling = value
            elif key == "Lagersaldo":
                self.stock_amount = value
            elif (
                key
                == "Tillåt beställningar även om lagret är slut och visa lagermeddelande (1/0)"
            ):
                self.can_run_empty_product = value
            elif key == "Huvudbild":
                self.main_picture = value
            elif key == "Alla bilder":
                self.all_pictures = value
            elif key == "Nyhet (1/0)":
                self.is_new_product = value
            elif key == "Produktgruppens namn":
                self.category_name = value
            elif key == "Undergrupp nivå 1":
                self.sub_cat_1 = value
            elif key == "Undergrupp nivå 2":
                self.sub_cat_2 = value
            elif key == "Undergrupp nivå 3":
                self.sub_cat_3 = value
            elif key == "Undergrupp nivå 4":
                self.sub_cat_4 = value
            elif key == "Skick":
                self.is_old_product = value
            elif key == "Varumärke":
                self.brand = value
            elif key == "Dölj produkten om lagret är slut (1/0)":
                self.can_hide_product = value
            elif key == "Visa Lagersaldo eller lagermedelanade":
                self.stock_message = value
