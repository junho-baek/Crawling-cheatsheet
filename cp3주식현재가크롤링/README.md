# cp3 네이버 주식 현재가 크롤링

## 여러 종목 현재가를 크롤링하고, 엑셀에 저장해보자

> - 주식 현재가를 감싸고 있는 html 태그의 id 값으로 파싱
> - 여러 종목을 크롤링할 땐 for 문
> - f 스트링 조작법, replace 등 문자열 조작 익숙해지기
> - 

~~~shell
pip install openpyxl
~~~
> 다음은 openpyxl 을 이용해서 엑셀을 만드는 예시이다.
~~~python
import openpyxl

# 1) 엑셀 만들기
wb = openpyxl.Workbook()

# 2) 엑셀 워크시트 만들기

ws = wb.create_sheet('학생 정보')

# 3) 데이터 추가하기

ws['A1'] = '학번'
ws['B1'] = '이름'

ws['A2'] = 2020123456
ws['B2'] = '백준호'

# 4) 엑셀 저장하기

wb.save(r'학생정보.xlsx')
~~~

> 다음은 엑셀을 수정하는 코드이다. 파이썬으로 엑셀을 더 잘 다루고 싶다면 openpyxl 공식문서를 참고하자


~~~python
import openpyxl

fpath = '학생정보.xlsx'

# 1) 엑셀 불러오기
wb = openpyxl.load_workbook(fpath)


# 2) 엑셀 시트 선택
ws = wb['학생 정보']

# 3) 데이터 수정하기
ws['A3'] = 2020122222
ws['B3'] ='junho-baek'

# 4) 엑셀 저장하기

wb.save(fpath)
~~~


>종목 코드를 미리 리스트에 저장하고, for 문을 이용해서 주식 현재가를 크롤링했다.   

~~~python
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
  

~~~

> ### 과제
> 주식 현재가 크롤링 데이터를 엑셀에 저장해보자

> 과제 스스로 풀어본 것
~~~python
import requests
from bs4 import BeautifulSoup
import openpyxl

# 엑셀 준비
wb = openpyxl.Workbook()
ws = wb.create_sheet('주식현재가')

ws['A1'] = '종목'
ws['B1'] = '현재가'

ws['A2'] = '삼성전자'
ws['A3'] = 'sk하이닉스'
ws['A4'] = '카카오'

#종목 코드 리스트
codes = [
  '005930',
  '000660',
  '035720'
]
prices = []
for i in codes:
  url = f"https://finance.naver.com/item/sise.naver?code={i}"
  
  response = requests.get(url)
  
  html = response.text
  
  soup = BeautifulSoup(html, 'html.parser')
  
  #현재가 텍스트만 변수에 저장
  price = soup.select_one("#_nowVal").text
  
  #변수의 타입 변경 용이하게 하기 위해 ','를''로 바꿔줌 
  price = price.replace(',','')
  
  prices.append(price)
  
ws['B2'] = prices[0]
ws['B3'] = prices[1]
ws['B4'] = prices[2]

wb.save(r'주식현재가.xlsx')
~~~

>
> 과제 해설.
~~~python
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

~~~