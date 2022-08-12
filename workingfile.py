from bs4 import BeautifulSoup 
import requests
from csv import writer

url = 'https://www.newegg.com/todays-deals?cm_sp=Head_Navigation-_-Under_Search_Bar-_-Today%27s+Best+Deals&icid=677316'
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
lists = soup.find_all('div', class_= 'item-cell')


with open('deals.csv', 'w', encoding = 'utf8', newline= '') as f:
    thewriter = writer(f)
    header = ['Product', 'Old Price', 'New Price', 'Percent saved', 'Shipping']
    thewriter.writerow(header)
    limit = 0
    for list in lists:
        limit= limit+1
        if limit >20:
            break
        title = list.find('a', class_='item-title')
        if title is not None:
            title = title.text
        oldprice = list.find('span', class_='price-was-data')
        if oldprice is not None:
            oldprice = oldprice.text
        newprice = list.find('li', class_='price-current')
        if newprice is not None:
            newprice = newprice.text
            newprice = newprice.replace('\xa0–', '')
        percentsave = list.find('span', class_='price-save-percent')
        if percentsave is not None:
            percentsave = percentsave.text
        shippingprice= list.find('li', class_='price-ship')
        if shippingprice is not None:
            shippingprice = shippingprice.text

        info = [title, oldprice, newprice, percentsave, shippingprice]
        thewriter.writerow(info)
    


    