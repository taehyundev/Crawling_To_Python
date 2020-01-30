from bs4 import BeautifulSoup
from urllib.request import urlopen
i=1
j=0
top = 51 # op.gg에 51명 정보가 최대값이였음
jul = 40 #이하동문
mid = 53
bot = 24
sup = 36
sett = [top,jul,mid,bot,sup]
data ="<top rank>\n"
print("<top rank>");
with urlopen('https://www.op.gg/champion/statistics') as response:
    soup = BeautifulSoup(response, 'html.parser')
    f = open(r"~Rank.txt",'w')
    for anchor in soup.select('div.champion-index-table__name'):
        print(str(i)+"등 : "+anchor.get_text())
        data += str(i)+"등 : "+anchor.get_text()+ "\n"
        if(i==sett[j]):
            i=0
            j+=1
            if(j==1):
                data += "\n\n<jul rank>\n"
                print("\n\n" +"<jul rank>")
            if(j==2):
                data += "\n\n<mid rank>\n"
                print("\n\n" +"<mid rank>")
            if(j==3):
                data += "\n\n<bot rank>\n"
                print("\n\n" +"<bot rank>")
            if(j==4):
                data += "\n\n<sup rank>\n"
                print("\n\n" +"<sup rank>")
        i +=1

f.write(data)
f.close()
