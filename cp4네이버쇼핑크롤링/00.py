from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.chrome.options import Options
import warnings

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