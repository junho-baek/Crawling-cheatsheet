import requests
from bs4 import BeautifulSoup
#종목 코드 리스트
codes = [
  '005930',
  '000660',
  '035720'
]
for i in codes:
  url = f"https://finance.naver.com/item/sise.naver?code={i}"
  
  response = requests.get(url)
  
  html = response.text
  
  soup = BeautifulSoup(html, 'html.parser')
  
  #현재가 텍스트만 변수에 저장
  price = soup.select_one("#_nowVal").text
  
  #변수의 타입 변경 용이하게 하기 위해 ','를''로 바꿔줌 
  price = price.replace(',','')
  
  print(price)
  
