import urllib.request
from bs4 import BeautifulSoup
try:
    while True:
        date = input("날짜 입력(2020-01-31형식) : ");
        name =  ['강태현','이수진', '이한주']
        url = ['https://github.com/taehyundev', 'https://github.com/leeejin', 'https://github.com/lee-hanju']
        for i in range(0, 3):
            html = urllib.request.urlopen(url[i]).read()
            soup = BeautifulSoup(html, 'html.parser')
            title = soup.find_all(class_='day')
            for j in title:
                if (j["data-date"] == date):
                    if(int(j["data-count"]) == 0 ):
                        print(name[i]+" : 커밋X")
                    else:
                        print(name[i]+" : "+ j["data-count"])
        c = input("더하시겠습니까?(y/n)\n");
        if(c == 'n'):
            break;
except:
    print("인터넷 연결이 안되어있음")
