#!/usr/bin/env python3
# Anchor extraction from HTML document
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import matplotlib.pyplot as plt

name = input("What's your name? ");
url = 'https://www.acmicpc.net/user/'+ name;
user_info = [];
with urlopen(url) as response:
    soup = BeautifulSoup(response, 'html.parser')
    i=0
    for list_info in soup.find_all('tr'):
        if(i==5 or i==0 or i==1 or i==2):
            user_info.append(list_info.get_text());
            
        i= i+1
set_gragh = [];
num = re.findall("\d+",user_info[0]);
print("랭킹 : "+str(num[0]));

num = re.findall("\d+",user_info[2]);
print("제출 : "+str(num[0]));

num = re.findall("\d+",user_info[1]);
print("맞은 문제수 : "+str(num[0]));
set_gragh.append( num[0]);

num = re.findall("\d+",user_info[3]);
print("틀린 횟수 : "+str(num[0]));
set_gragh.append( num[0]);
group_name = ["Pass", "Fail"]
plt.pie(set_gragh,
        labels=group_name,
        colors=['b','r'],
        startangle =90,
        explode = (0.1,0),
        autopct='%1.1f%%')
plt.title('BaekJoon Chart');
plt.show();
