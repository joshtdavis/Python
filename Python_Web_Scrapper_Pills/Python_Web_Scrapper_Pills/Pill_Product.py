class Pill_Product(object):
    """description of class"""
    __name = ""
    __retail_price = 0
    __sale_price = 0
    __special_pricing = 0
    __UPC = ""
    __SKU_vitanetonline = ""
    __url = ""

    def __init__(self):
        return None

    def set_name(self,name):
        self.__name = name
        return None
    def get_name(self):
        return self.__name

    def set_retail_price(self,price):
        self.__retail_price = price
        return None
    def get_retail_price(self):
        return self.__retail_price

    def set_sale_price(self,price):
        self.__sale_price = price
        return None
    def get_sale_price(self):
        return self.__sale_price

    def set_UPC(self,UPC):
        self.__UPC = UPC
        return None
    def get_UPC(self):
        return self.__UPC

    def set_URL(self,URL):
        self.__url = URL
        return None
    def get_URL(self):
        return self.__url

    def set_SKU_vitanetonline(self,SKU):
        self.__SKU_vitanetonline = SKU
        return None
    def get_SKU_vitanetonline(self):
        return self.__SKU_vitanetonline

    def set_special_price(self,special_price):
        self.__special_pricing = special_price
        return None
    def get_special_pricing(self):
        return self.__special_pricing
    def to_String(self):
        return "Name: " + self.get_name() + "\nSpecial Price: " + self.get_special_pricing() + ": \nUPC Code: " + self.get_UPC() + "\nSKU Vitanet: " + self.get_SKU_vitanetonline()