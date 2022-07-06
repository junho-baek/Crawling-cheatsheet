# 상품 정보 데이터 수집하기   
## 셀레니움 기초 사용법 정리

### 네이버 쇼핑 사이트에서 상품정보를 크롤링해서 엑셀에 저장   

> requests 한계: 셀레니움 라이브러리를 사용하는 이유
> - 로그인이 필요한 사이트에 적용이 어려움   
> - 동적으로(필요한 특정 부분을 나중에 렌더링하는 웹 기술) HTML을 만드는 경우 적용이 어려움
> - 동적인 웹의 예
> > 스크롤하거나 클릭하면 데이터가 생성됨   
  > URL주소가 변경되지 않았는데 데이터가 변함   
  > 표, 테이블 형태의 데이터
  
#### 셀레니움 기초 사용법  
- 셀레니움이란?
> - 웹 어플리케이션 테스트를 위한 도구
> - 브라우저를 실제로 띄워서 사람처럼 동작하도록 만들 수 있다.
- 사용법?
> - 크롬 드라이버 다운로드
> - 라이브러리 설치
> ~~~shell
> pip install selenium
> ~~~
~~~python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.chrome.options import Options
import warnings
import csv
import time


chrome_options = Options()
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"]) # 셀레니움 로그 무시
warnings.filterwarnings("ignore", category=DeprecationWarning) # Deprecated warning 무시 

# 크롬 브라우저가 저장된 디렉토리를 잘 적어주자
browser = webdriver.Chrome("/Users/baekjunho/Documents/chromedriver", options=chrome_options)

#웹 사이트 열기
browser.get('https://www.naver.com')
#로딩이 끝날 때까지 10초까지는 기다려줌
browser.implicitly_wait(10)


# 쇼핑 메뉴 클릭하기
browser.find_element_by_css_selector('a.nav.shop').click()
#쇼핑 창 렌더링되는 시간 2초 기다려줌
time.sleep(2)

#검색창 클릭
search = browser.find_element_by_css_selector('input._searchInput_search_input_QXUFf')
search.click()

# 검색어 입력

search.send_keys('아이폰 13')
search.send_keys(Keys.ENTER)

# 무한 스크롤

#스크롤 전 높이
#.execute_script는 자바스크립트 명령어를 사용할 수 있게 해준다.
before_h = browser.execute_script("return window.scrollY")

while True:
    # 맨 아래로 스크롤을 내린다.(END 버튼을 누름)
    browser.find_element_by_css_selector("body").send_keys(Keys.END)

    # 동적으로 렌더링 될 때까지 로딩 시간
    time.sleep(1)

    # 스크롤 후 높이
    after_h = browser.execute_script("return window.scrollY")

    if after_h == before_h:
        break
    before_h = after_h

# 파일 생성

f = open(r'/Users/baekjunho/Desktop/무제 폴더/data.csv', 'w', encoding='UTF-8', newline='')
csvWriter = csv.writer(f)

# 상품 정보 div

items = browser.find_elements_by_css_selector(".basicList_info_area__17Xyo")

for i in items:
    name = i.find_element_by_css_selector(".basicList_title__3P9Q7").text
    try:
        price = i.find_element_by_css_selector(".price_num__2WUXn").text
    except:
        price = "판매중단"
    #태그의 속성 가져오는 법
    link = i.find_element_by_css_selector(".basicList_title__3P9Q7 > a").get_attribute('href')
    print(name, price, link)
    #데이터쓰기
    csvWriter.writerow([name, price, link])

#파일 닫기
f.close
~~~

# (추가)웹 사이트 자동화
- 웹 사이트 자동화 종류
  - 크롤링
  - 로그인
  - 업로드
  - 다운로드
  - 좋아요
  - 매수 매도
- 셀레니움 4
>  <학습 목표>
> 1. 최신 업데이트된 방식? 
> 2. 크롬 드라이버 자동 업데이트 코드
> 3. 브라우저 꺼짐 방지 코드
> 4. 불필요한 에러 메시지 제거
> ~~~
> pip install --upgrage pip
> pip install --upgrade selenium
> pip install webdriver_manager
> ~~~
>
> ~~~python
> 
> ~~~


## 실습