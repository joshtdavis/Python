import requests
from bs4 import BeautifulSoup
from Pill_Product import Pill_Product
import sqlalchemy as sqla
class Pill_Scapper(object):
    """description of class"""
    __Front_url = ""
    __request = ""
    __soup = ""
    __urls = []
    __products = []
    def __init__(self):
        return None

    def __init__(self,url):
        self.__Front_url = url
        self.__request = requests.get(self.__Front_url)
        self.__soup = BeautifulSoup(self.__request.content,"html.parser")
        self.__urls = self.__gather_all_urls()

    def get_requests(self,url):
        self.__request = requests.get(url)
        return self.__request

    def gather_all_other_info(self):
        for url in self.__urls:
            self.__request  = requests.get(url)
            self.__soup = BeautifulSoup(self.__request.content,"html.parser")
            product = Pill_Product()
            #self.__g_data = self.__soup.find("h1",{"itemprop":"name"})
            try:
                product.set_name( self.__soup.find("h1",{"itemprop":"name"}).text )
                product.set_retail_price(self.__soup.find("span",{"class":"retail"}).text[1:] )    
                product.set_sale_price(self.__soup.find("span",{"class":"sale"}).text[1:] )
                product.set_UPC(self.__soup.find("em",{"itemprop":"productID"}).text)
                product.set_SKU_vitanetonline(self.__soup.find("em",{"itemprop":"sku"}).text)
                holder = self.__soup.find("dl",{"class":"info-list"})
                holder = holder.find_all('dt')
                holder = holder[3].find('b')
                product.set_special_price(holder.text[2:holder.text.find("e")])
                product.set_URL(url)
                self.__products.append(product)
                print("Product added\n" + product.to_String())
            except Exception as e:
                print(url)
                print(e)
    def add_to_Database(self,databaseString):
        sucess = False
        try:
            engine = sqla.create_engine(databaseString)
            connection = engine.connect()
            # need to do more reasearch regarding how to add to database
            # attempting to use sqlachemy core with metadata
            trans = connection.begin()
            metadata = sqla.MetaData()
            #metadata.reflect(bind=engine)
            productTable = sqla.Table('Product',metadata,autoload=True,autoload_with=engine)
            productlocations = sqla.Table('ProductLocations',metadata,autoload=True,autoload_with=engine)
            for product in self.__products:
                insertProducts = productTable.insert().values(upcCode=product.get_UPC,SKU=product().get_SKU_vitanetonline(),name=product.get_name(),manufacturer='Solaray')
                insertProductLocations = productlocations.insert().values(url=product.get_URL(),productID=product.get_UPC(),retailPrice=product.get_retail_price(),salePrice=product.get_sale_price(),specialGroupPrice=product.get_special_pricing())
                engine.execute(insertProducts)
                engine.execute(insertProductLocations)
            '''statement = "Insert into Product(upcCode,SKU,name,manufacturer) Values "
            for product in self.__products:
                staement += "( '" + product.get_UPC() + "','" + product.get_SKU_vitanetonline() + "','" + product.get_name() + "','" + "Solaray' ),"
            statement = statement[:-1] + ";"
            result = connection.execute(statement)'''
            trans.commit()
            connection.close()
            sucess = True
        except Exception as e:
            trans.rollback()
            connection.close()
            print(e)
            sucess = False
        return sucess
    def get_all_urls(self):
        return __urls

    def __gather_all_urls(self):
        __urlss = []
        self.__g_data = self.__soup.find("div",{"class":"heading-block"})
        #print(self.__g_data)
        self.__g_data = self.__g_data.find_all('table')
        self.__g_data = self.__g_data[0].find_all('a')
        self.__g_data = self.__g_data[:-1]
        for link in self.__g_data:
            #print(link.get("href"))
            if("/des" in str(link.get("href"))):
                print("https://vitanetonline.com"+link.get("href"))
                __urlss.append("https://vitanetonline.com"+link.get("href"))
        return __urlss