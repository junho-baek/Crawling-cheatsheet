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




#과제

#프로그램을 실행하면 검색어를 입력받게해서 해당 검색어로 크롤링 되게 만들어보자
#내가 원하는 페이지까지 크롤링해보자

