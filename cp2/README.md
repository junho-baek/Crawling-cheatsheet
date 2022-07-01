# 뉴스 기사 제목과 url 크롤링

## 삼성전자를 검색했을 때 뜨는 뉴스를 크롤링해보자

- 뉴스를 검색한 후 f12를 눌러서 링크가 걸린 태그의 클래스명을 봄
- 해당 클래스로 크롤링을 진행할 것임
- html 태그의 속성을 불러오고 싶을 때는 attrs['']


~~~python
import requests
from bs4 import BeautifulSoup

response = requests.get('https://search.naver.com/search.naver?where=news&sm=tab_jum&query=삼성전자')

html = response.text

#html 문서를 다루기 쉽게 만들어 줌

soup = BeautifulSoup(html, 'html.parser')

#select 전체 다 가져옴/ select_one 하나만 가져옴
links = soup.select(".news_tit")

for i in links:
  #태그 안의 택스트 요소를 가져온다.
  title = i.text
  #태그의 속성 값은 attrs[''] 로 가져올 수 있다.
  url = i.attrs['href']
  print(title,url)


#과제

#프로그램을 실행하면 검색어를 입력받게해서 해당 검색어로 크롤링 되게 만들어보자
#내가 원하는 페이지까지 크롤링해보자
~~~

## 과제 1
### 프로그램을 실행하면 검색어를 입력받게해서 해당 검색어로 크롤링 되게 만들어보자

~~~python

import requests
from bs4 import BeautifulSoup
import pyautogui

# search = input('검색하고 싶은 뉴스?: ')
search = pyautogui('검색하고 싶은 뉴스?: ')

response = requests.get(f'https://search.naver.com/search.naver?where=news&sm=tab_jum&query={search}')

html = response.text

#html 문서를 다루기 쉽게 만들어 줌

soup = BeautifulSoup(html, 'html.parser')

#select 전체 다 가져옴/ select_one 하나만 가져옴
links = soup.select(".news_tit")

for i in links:
  #태그 안의 택스트 요소를 가져온다.
  title = i.text
  #태그의 속성 값은 attrs[''] 로 가져올 수 있다.
  url = i.attrs['href']
  print(title,url)


#과제

#프로그램을 실행하면 검색어를 입력받게해서 해당 검색어로 크롤링 되게 만들어보자
#내가 원하는 페이지까지 크롤링해보자

# url 인터넷 주소 형식
#프로토콜//도메인/페스/파라미터 형식
#파라미터는 키와 벨류를 가짐

#pyautogui
#pyautogui.prompt("")

~~~