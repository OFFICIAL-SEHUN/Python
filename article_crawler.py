from tkinter.messagebox import QUESTION
import requests
from bs4 import BeautifulSoup
import re

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36'}

keyword = input("검색어 입력:")

#for page in range(n,m): #페이지 개수만큼
url="https://www.google.com/search?q={keyword}" #검색 키워드
#-------------------------------------#
res = requests.get(url,headers=headers)
res.raise_for_status() #프로세스중 오류 발생하면 html객체 반환 #200반환하면 정상
soup=BeautifulSoup(res.text, "lxml") #파서 지정 #파서종류: html.parser, lxml , xml ,html5lib
article=soup.find_all("a",attrs={"class":"WlydOe"})
#article=soup.find_all("a",attrs={"class":re.compile("WlydOe")}) #

for i in article():
    print(article['href'])
'''for item in items:
        #광고 상품 제외
        ad_bedge = item.find("span",attrs={"class":"ad-badge-text"})
        if ad_bedge:
            print("<광고 상품 제외>")
            print("-"*60)
            continue

        name=item.find("div",attrs={"class":"name"}).get_text() #제품명
        link=item.find("a",attrs={"class":"search-product-link"})["href"] #링크
        
        s_price=item.find("strong",attrs={"class":"price-value"}).get_text() #가격
        i_price=int(s_price.replace(',',"")) #가격 ','문자 제거 / 문자형 > 정수형

        if not "그래픽카드" in name: #그래픽카드 아니면 제외
            continue
        if not 1500000>=i_price>500000: #원하는 가격 옵션   
            continue
        if not ("3060" or "3060ti" or "3070" or "3070ti" or "6600" or "6700") in name: #3060,3060ti,3070,3070ti,6600,6700 아니면 제외
            continue
        
        print(name,"→",s_price)#제품명 및 가격 출력
        print("바로가기:{}".format("https://www.coupang.com" + link))#바로가기 링크 출력
        print("-"*100) #줄긋기
        '''