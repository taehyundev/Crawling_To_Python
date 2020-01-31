import urllib.request
from bs4 import BeautifulSoup

date = input("날짜 입력(2020-01-31형식) : ");
name =  ['강태현','이수진']
url = ['https://github.com/taehyundev', 'https://github.com/leeejin']
for i in range(0, 2):
    html = urllib.request.urlopen(url[i]).read()
    soup = BeautifulSoup(html, 'html.parser')
    title = soup.find_all(class_='day')
    for j in title:
        if (j["data-date"] == date):
            if(int(j["data-count"]) == 0 ):
                print(name[i]+" : 커밋X")
            else:
                print(name[i]+" : "+ j["data-count"])
    
