import requests
from bs4 import BeautifulSoup
from Pill_Scrapper import Pill_Scapper
def main():
        url = "https://vitanetonline.com/manufacture/Solaray/"
        Pill_db_Scrapper = Pill_Scapper(url)
        Pill_db_Scrapper.gather_all_other_info()
        #Pill_db_Scrapper.add_to_Database("mssql+pyodbc://server/database") Windows Auth
        #Pill_db_Scrapper.add_to_Database("mssql+pyodbc://user:password@server/database") SQL Auth
        return None
def run_test():
    from Pill_Product import Pill_Product
    request  = requests.get("https://vitanetonline.com/description/36784/vitamins/Food-Source-B-Complex/")
    soup = BeautifulSoup(request.content,"html.parser")
    product = Pill_Product()
    product.set_name( soup.find("h1",{"itemprop":"name"}).text )
    print(product.get_name())

    product.set_retail_price(soup.find("span",{"class":"retail"}).text[1:] )
    print(product.get_retail_price())
    
    product.set_sale_price(soup.find("span",{"class":"sale"}).text[1:] )
    print(product.get_sale_price())

    product.set_UPC(soup.find("em",{"itemprop":"productID"}).text)
    print(product.get_UPC())

    product.set_SKU_vitanetonline(soup.find("em",{"itemprop":"sku"}).text)
    print(product.get_SKU_vitanetonline())

    holder = soup.find("dl",{"class":"info-list"})
    holder = holder.find_all('dt')
    holder = holder[3].find('b')
    #print(holder.text[2:holder.text.find("e")])
    product.set_special_price(holder.text[2:holder.text.find("e")])
    print(product.get_special_pricing())
main()
#run_test()