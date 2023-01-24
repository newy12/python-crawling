### for MacOS
import csv
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from time import sleep

# chromedriver 위치에서 코드작업 필수 

chrome_options = Options()
driver = webdriver.Chrome(service=Service('경로입력/chromedriver'), options=chrome_options)

URL = 'http://miraes.net/'
def crawl():

    column_list = ["제품코드","제품명","판매가","회원가"]
    with open('미래과학도매2.csv','w',-1,newline='') as f:
        w=csv.writer(f)
        w.writerow(column_list)

        driver.get(URL)
        #팝업없애기
        #driver.find_element(By.XPATH,'//*[@id="layout_config_full"]/div[1]/div[2]/div[1]/label/input').click()
        #driver.find_element(By.XPATH,'//*[@id="layout_config_full"]/div[1]/div[2]/div[2]').click()
        sleep(1)
        #로그인

        driver.find_element(By.XPATH,'//*[@id="tnb_inner"]/ul/li[1]/a').click()
        sleep(1)
        driver.find_element(By.XPATH,'//*[@id="login_id"]').send_keys('cray5404')
        driver.find_element(By.XPATH,'//*[@id="login_pw"]').send_keys('rladudgus12#')
        driver.find_element(By.XPATH,'//*[@id="login_fld"]/dl/dd[4]/button').click()
        sleep(1)
        #추천물건
        driver.find_element(By.XPATH,'//*[@id="header"]/div[4]/div[2]/ul/li[1]/a').click()
      
        #주문양식
        #https://www.i-screammall.co.kr/mypage/order_catalog?page=1&regist_date%5B0%5D=2022-01-01&regist_date%5B1%5D=2023-01-14&popup=&iframe=

        sleep(1)

        # 조회 화면 이동
        for page in range(1, 5, 1):
            AURL = 'http://miraes.net/shop/list.php?ca_id=013&page_rows=&sort=index_no&sortodr=desc&page='+str(page)
            driver.get(AURL)
            sleep(1)

            element = driver.find_element(By.XPATH,'//*[@id="container"]/div[4]/div[2]/ul')
            li = element.find_elements(By.XPATH,'//*[@id="container"]/div[4]/div[2]/ul/li')
            

            for i in li :
                #사진 = i.find_element(By.XPATH,'//*[@id="container"]/div[4]/div[2]/ul/li/a/dl/dt/img').text
                제품코드 = i.find_element(By.CSS_SELECTOR,'.tal.mart10').text
                제품명 = i.find_element(By.CSS_SELECTOR,'.pname').text
                상품가 = i.find_element(By.CSS_SELECTOR,'.price > span:first-child').text
                회원가전체 = i.find_element(By.CSS_SELECTOR,'.price > span:last-child').text
                회원가 = 회원가전체.replace('회원가','')
                w.writerow([제품코드,제품명,상품가,회원가])
def main():
    crawl()

if __name__ == '__main__':
    main()
