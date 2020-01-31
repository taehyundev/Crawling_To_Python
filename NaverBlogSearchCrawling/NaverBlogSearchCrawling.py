import urllib.request
from bs4 import BeautifulSoup

url = 'https://search.naver.com/search.naver?where=post&sm=tab_jum&query=python'
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

title = soup.find_all(class_='sh_blog_title')


for i in title:
    print(i.attrs['title'])
    print(i.attrs['href']+'\n') 
