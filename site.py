#pip install requests
# pip install beautifulsoup4
# pip install lxml
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}
URL = 'https://realt.by/belarus/sale/shops/?objectType=15'
response = requests.get(URL,headers=headers)
soup = BeautifulSoup(response.text,'lxml')
a_tags = soup.find_all('a',class_='z-1 absolute top-0 left-0 w-full h-full cursor-pointer')
#print(len(soup))
#for i in soup:
 #   print('https://realt.by'+ i['href'])
pages = soup.find_all('a',class_='focus:outline-none sm:focus:shadow-10bottom cursor-pointer select-none inline-flex font-normal text-body min-h-[2.5rem] min-w-[2.5rem] py-0 items-center !px-1.25 justify-center mx-1 hover:bg-basic-200 rounded-md disabled:text-basic-500')
print(pages)
last_page = [i.text for i in pages][-1]
urls = [f'https://realt.by/belarus/sale/shops/?objectType=15&page={str(i)}'for i in range(1,int(last_page) +1)]
#print(*urls,sep='\n')
counter = []
for i in tqdm(urls):
    resp = requests.get(i,headers=headers).text
    data = BeautifulSoup(resp,'lxml')
    a_tags = data.find_all('a', class_='z-1 absolute top-0 left-0 w-full h-full cursor-pointer')
    for g in a_tags:
        url = 'https://realt.by'+g['href']
        counter.append(url)
with open('urls.txt','w') as f:
    for i in counter:
        f.write(i+'\n')

