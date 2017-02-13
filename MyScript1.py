from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
html = urlopen('http://www.06274.com.ua/doska/full/51734')
bs0bj = BeautifulSoup(html, "html.parser")
# достаем данные пользователя (имя и телефон) и текст объявления
contact = bs0bj.findAll('div', {'class':'info'})
print(contact[1].get_text()) #телефон
print(contact[2].get_text()) #имя
text_block = bs0bj.findAll('div', {'class':'text-block'})
text = text_block[0].get_text()
print(re.sub(r'\s+', ' ', text)) # текст объявления
