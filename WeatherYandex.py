from bs4 import BeautifulSoup as bs
import requests

url = 'https://yandex.ru/pogoda/novosibirsk/details/10-day-weather?via=mf'
page = requests.get(url)
soup = bs(page.text, 'lxml')
#print(soup.prettify())
'''
for i in soup.find_all('a'):
	print(i.get('href'))
print()
'''

list1= []
link = soup.find_all('span', 'temp__value')
for i in range(2, len(link), 3):
	list1.append(link[i].text)

print(f'\nСегодня днем: {list1[1]}')
print()

list2 = []	
link=soup.find_all('div', 'weather-table__daypart')
for i in link:
	list2.append(i.text)

lst3 = []
new = soup.find_all('span', 'a11y-hidden')
for i in new:
	lst3.append(i.text)


for i in range(0, 13, 3):
	print(lst3[i])
print()
	
for i in range(17, 32, 3):
	print(lst3[i])
print()

for i in range(34, 49, 3):
	print(lst3[i])
print()

for i in range(51, 64, 3):
	print(lst3[i])
print()





