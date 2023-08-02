import openpyxl
DB_FOLDER = "data/DB_bending.xlsx"
class Item:

    def __init__(
            self,
            db_path: str = None,
            type_holder: str = None,
            type_item: str = None,
            code_item: str = None,
            length_item: str = None,
            length_item_mm: list = None,
            weight: float = 0.0,
            price_item: float = 0.0,
            discount_item: float = 0.0,
            cross_section_param: dict = None,
            image_path: str = None,
            en_name_item: str = None,
            ua_name_item: str = None,
            amount_item: int = 0
    ) -> None:
        self.db = openpyxl.load_workbook(DB_FOLDER)
        self.db_path: str = db_path
        self.type_holder: str = type_holder
        self.type_item: str = type_item
        self.code_item: str = code_item
        self.length_item: str = length_item
        self.length_item_mm: list = length_item_mm
        self.weight: float = weight
        self.price_item: float = price_item
        self.discount_item: float = discount_item
        self.cross_section_param: dict = cross_section_param
        self.image_path: str = image_path
        self.en_name_item: str = en_name_item
        self.ua_name_item: str = ua_name_item
        self.amount_item: str = amount_item


    def set_db_path(self, new_path: str) -> None:
        self.db_path = new_path

    def get_db_path(self) -> str:
        return self.db_path
    def set_type_holder(self, new_type_holder: str) -> None:
        self.type_holder = new_type_holder

    def get_type_holder(self) -> str:
        return self.type_holder

    def set_type_item(self, new_type_item: str) -> None:
        self.type_item = new_type_item

    def get_type_item(self) -> str:
        return self.type_item

    def set_code_item(self, new_code_item: str) -> None:
        self.code_item = new_code_item

    def get_code_item(self) -> str:
        return self.code_item

    def set_length_item(self, new_lenght_item: str) -> None:
        self.length_item = new_lenght_item

    def get_length_item(self) -> str:
        return self.length_item

    def set_length_item_mm(self, new_length_item_mm: list) -> None:
        self.length_item_mm = new_length_item_mm

    def get_length_item_mm(self) -> list:
        return self.length_item_mm

    def set_weight_item(self, new_weight: float) -> None:
        self.weight = new_weight

    def get_weight_item(self) -> float:
        return self.weight

    def set_price_item(self, new_price_item: float) -> None:
        self.price_item = new_price_item

    def get_price_item(self) -> float:
        return self.price_item

    def set_discount_item(self, percent: float) -> None:
        self.discount_item = percent

    def get_discount_item(self) -> float:
        return self.discount_item

    def set_cross_section_param(self, new_dict: dict) -> None:
        self.cross_section_param = new_dict

    def get_cross_section_param(self) -> dict:
        return self.cross_section_param

    def set_image_path(self, new_img_path: str) -> None:
        self.image_path = new_img_path

    def get_image_path(self) -> str:
        return self.image_path

    def set_en_name_item(self, new_en_name: str) -> None:
        self.en_name_item = new_en_name

    def get_en_name_item(self) -> str:
        return self.en_name_item

    def set_ua_name_item(self, new_ua_name: str) -> None:
        self.ua_name_item = new_ua_name


    def get_amount_item(self) -> int:
        return self.amount_item

class Invoice:

    def __init__(
            self,
            rate: float = 0.0,
            list_item: list = None,
            packing_price: float = 0.0,
            delivery_price: float = 0.0,
            commission_percentage: float = 0.0,
            tecnostamp_discount: float = 0.0,
    ) -> None:
        self.rate = rate
        self.list_item = list_item
        self.packing_price = packing_price
        self.delivery_price = delivery_price
        self.commission_percentage = commission_percentage
        self.tecnostamp_discount = tecnostamp_discount

    def set_rate(self, new_rate: float) -> None:
        self.rate = new_rate

    def get_rate(self) -> float:
        return self.rate

    def set_list_item(self, new_list_item: list[Item]) -> None:
        self.list_item = new_list_item

    def get_list_item(self) -> list[Item]:
        return self.list_item

    def set_packing_price(self, new_packing_price: float) -> None:
        self.packing_price = new_packing_price

    def get_packing_price(self) -> float:
        return self.packing_price

    def set_delivery_price(self, new_delivery_price: float) -> None:
        self.delivery_price = new_delivery_price

    def get_delivery_price(self) -> float:
        return self.delivery_price

    def set_tecnostamp_discount(self, new_tecnostamp_discount: str) -> None:
        self.tecnostamp_discount = new_tecnostamp_discount

    def get_tecnostamp_discount(self) -> float:
        return self.tecnostamp_discount
