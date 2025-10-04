import sys
from time import sleep
import os
import django
import requests
from bs4 import BeautifulSoup


sys.path.append("C:\\Users\\Vin Disel\\Desktop\\Work\\site_scrap")
os.environ["DJANGO_SETTINGS_MODULE"] = "site_scrap.settings"
django.setup()
from parser.models import Phone

url = 'https://brain.com.ua/ukr/Mobilniy_telefon_Apple_iPhone_16_Pro_Max_256GB_Black_Titanium-p1145443.html'

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
name = soup.find('h1', {'data-pid': '1145443'}).text.replace('\n', '')
color = soup.find('div', {'class': 'series-colors-column'})
colors = color.find_all('div', {'class': 'slice'})
all_color = []
for c in colors:
    col = c.get('style').replace('background: ', '')
    all_color.append(col)
mem = soup.find('div', {'class': 'series-items series-characteristics-container'})
mem_all = mem.find_all('a')
memory_list = []
for m in mem_all:
    memory_list.append(m.text.replace('\n', '').replace(' ', ''))

price = soup.find('div', {'class': 'br-pr-np', 'data-pid': '1145443'}).find('div').find('span').text.replace('\n',
                                                                                                             '').replace(
    ' ', '') + ' грн'
# sleep(10)
div_img = soup.find("div", class_="slick-track")
print('div_img: ', div_img)

#img_all = div_img.find_all("img") if div_img else []

#img = [i.get("src") for i in img_all]

#print("img: ", img)

code = soup.find('span', {'class': "br-pr-code-val"}).text
comments = soup.find('div', {'class': 'br-pt-rt-top main-comments-block price-comments-block'}).find('a').find(
    'span').text + 'відгуків'

char = dict()
ch = soup.find('div', {'class': 'br-pr-chr'}).find_all('div', {'class': 'br-pr-chr-item'})
for c in ch:
    charact = c.find_all('div')
    charact = charact[1:]
    for c1 in charact:
        item = c1.find_all('span')
        char.update({item[0].text.replace('\n',''): item[1].text.replace('\n','').replace(' ','')})
phone = Phone.objects.create(
    name= name,
    color= all_color,
    memory=memory_list,
    price=price,
    photo=None,
    code=code,
    fb=comments,
    characteristics=char,
    )


