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
  
  
