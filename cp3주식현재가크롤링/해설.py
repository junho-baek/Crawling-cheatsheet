import requests
from bs4 import BeautifulSoup
import openpyxl

fpath = r'주식현재가'
wb =openpyxl.load_workbook(fpath)
ws = wb.active #현재 활성화된 시트 선택

#종목 코드 리스트
codes = [
  '005930',
  '000660',
  '035720'
]

row = 2
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
  ws[f'B{row}'] = int(price)
  row += 1
  
wb.save(fpath)
