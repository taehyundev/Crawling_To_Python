import urllib.request
import re
from bs4 import BeautifulSoup
try:
    i=0
    name =  ['강태현', '이한주','이수진']
    score = [0,0,0]
    s = ''
    r=0
    rank = [0,0,0]
    url = ['https://github.com/taehyundev',  'https://github.com/lee-hanju','https://github.com/leeejin']
    for x in range(0, 3):
        html = urllib.request.urlopen(url[x]).read()
        soup = BeautifulSoup(html, 'html.parser')
        for contri in soup.find_all(class_='f4 text-normal mb-2'):
            if(re.findall("\d", contri.get_text(" ", strip=True))):
               score[i]= re.findall("\d", contri.get_text(" ", strip=True))
               for j in range(0, len(score[i])):
                   s+=score[i][j]
               i +=1
               print(name[x]+"님의 총 커밋 : "+s + " contibutions")
               rank[r] = int(s)
               s =''
               r +=1
    print("\n\n<Rank>")
    max = [0,0,0]
    max[0] = rank[0]
    c =0
    for z in range(1, 3):
        if(max[c] < rank[z]):
            c = z
            max[c] = rank[z]

    print(name[c] +"님이 현재 1등입니다.")
    max[c] =0
    rank[c] =0
    for z in range(1, 3):
        if(max[c] < rank[z]):
            c = z
            max[c] = rank[z]

    print(name[c] +"님이 현재 2등입니다.")
    max[c] =0
    rank[c] =0
    for z in range(1, 3):
        if(max[c] < rank[z]):
            c = z
            max[c] = rank[z]

    print(name[c] +"님이 현재 3등입니다.")
            
except:
    print("인터넷을 연결해 주세요");

