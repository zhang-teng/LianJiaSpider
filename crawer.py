import re
from bs4 import BeautifulSoup
import urllib.request
import sys

class house_item(object):
    def __init__(self, bs4_item):
        self.item = bs4_item
        self.dic = dict()
    def parse(self):
        z = self.item
        try:
            self.temp_id = z.find('div',class_='title').find(href=True)['href']
            self.title = z.find('div',class_='title').text
            self.address = z.find('div',class_='address').find('a').text
            self.house_info = z.find('div',class_='houseInfo').contents[-1]
            self.floor = list(z.find('div',class_='flood').strings)[0]
            self.nearby = z.find('div',class_='flood').a.text
            self.follow_info = z.find('div',class_='followInfo').text
            self.tags = '|'.join(z.find('div',class_='tag').strings)
            self.total_price = z.find('div',class_='totalPrice').text
            self.unit_price = z.find('div',class_='unitPrice').span.text
        except:
            print(self.item,file=sys.stderr)
    def Dump(self):
        pass
    def paralise(self):
        pass

def parse_lianjia_ershou(response_text):
    soup = BeautifulSoup(response_text)
    all_item = soup.body.find('li',class_='clear')
    all_house = list(map(lambda x:house_item(x),all_item))
    return all_house
