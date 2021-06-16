import requests
from bs4 import BeautifulSoup
import selenium

URL = 'https://movie.daum.net/moviedb/grade?movieId=129982'
driver = webdriver.Chrome("./chromedriver") # chrome창에 열기
driver.get(url=URL) # 실행할 웹페이지 불러오기
soup = BeautifulSoup(driver.page_source, 'html.parser')

# 원하는곳 접근
body = soup.find_all('div', {'class':'cmt_info'}) # 모든 .cmt_info를 불러온다
body2 = soup.find_all('p', {'class':'desc_txt'}) # 모든 평가글 가져옴
body3 = soup.find_all('div', {'class':'ratings'}) # 모든 별점 가져옴

stars = []
contents = []
for mtext, rating in zip(body2, body3):
    print(rating.text, mtext.text)
    stars.append(rating.text)
    contents.append(mtext.text)

import pandas as pd
df = pd.DataFrame({'score':stars
                  , 'contents':contents})

print(df)
