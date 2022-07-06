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
search = pyautogui.prompt('검색하고 싶은 뉴스?: ')

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

## 과제 2
### #내가 원하는 페이지까지 크롤링해보자

> 내가 만든 것.. 페이지 버튼에 나와있는 링크를 바탕으로   
> 페이지 버튼 내에 모든 자료 크롤링!
> 
~~~python
import requests
from bs4 import BeautifulSoup

search = input('검색하고 싶은 뉴스?: ')

response = requests.get(f'https://search.naver.com/search.naver?where=news&sm=tab_jum&query={search}')

html = response.text

#html 문서를 다루기 쉽게 만들어 줌

soup = BeautifulSoup(html, 'html.parser')

#select 전체 다 가져옴/ select_one 하나만 가져옴

btns = soup.select(".btn")
for i in btns:
  
  title = i.text
  
  url = i.attrs['href']
  print(title,'페이지 기사 결과입니다.')
  response = requests.get(f'https://search.naver.com/search.naver{url}')
  html = response.text
  soup = BeautifulSoup(html, 'html.parser')
  links = soup.select(".news_tit")
  for i in links:
    #태그 안의 택스트 요소를 가져온다.
    title = i.text
    #태그의 속성 값은 attrs[''] 로 가져올 수 있다.
    url = i.attrs['href']
    print(title,url)




~~~

> 쌤이 하신거   
> 파라미터 쿼리를 관찰하고 페이지별로 규칙적인 증가패턴을 발견한 뒤 그걸 변수화 해서 사용자가 원하는 페이지 크롤링이 가능하게 했음
>
~~~python
import requests
from bs4 import BeautifulSoup
# import pyautogui

search = input('검색하고 싶은 뉴스?: ')
lastPage = int(input('마지막 페이지 번호를 입력해주세요: '))
# url 을 잘봐서 페이지 별로 달라지는 쿼리 파라미터를 관찰해서 찾으심
pageNum = 1
for i in range(1, lastPage* 10 , 10):

  print(f"{pageNum} 페이지 입니다============================")
  response = requests.get(f'https://search.naver.com/search.naver?where=news&sm=tab_jum&query={search}&start={i}')
  
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
  pageNum += 1
  
  

~~~