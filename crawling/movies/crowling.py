

import requests as req
import urllib.request
from bs4 import BeautifulSoup as bs
from openpyxl import Workbook
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep


# 엑셀파일 생성
workbook = Workbook()
sheet = workbook.active

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

path = 'C:/Users/java2/Desktop/Workspace/BGV/crawling/'

url = 'http://www.cgv.co.kr/movies/' 
driver.get(url)

# HTML 요청
#url = 'http://www.cgv.co.kr/movies/' 
#html = req.get(url, headers={'User-Agent':'Mozilla/5.0'}).text      

#print(html)

# 문서 객체 생성
#dom = bs(html, 'html.parser')

# 데이터 파싱
btnMore = driver.find_element(By.CSS_SELECTOR, '#contents > div.wrap-movie-chart > div.sect-movie-chart > button')
btnMore.click()

sleep(3)

images = driver.find_elements(By.CSS_SELECTOR ,'ol > li > div.box-image > a > span > img')
contents = driver.find_elements(By.CSS_SELECTOR, 'ol > li > div.box-contents > a > strong')
pers = driver.find_elements(By.CSS_SELECTOR, 'ol > li > div.box-contents > div > strong > span')
eggs = driver.find_elements(By.CSS_SELECTOR, 'ol > li > div.box-contents > div > div > span.percent')
whens = driver.find_elements(By.CSS_SELECTOR, 'ol > li > div.box-contents > span.txt-info > strong')
#print('images size : ', len(images))


#lis = dom.select('#contents > div.wrap-movie-chart > div.sect-movie-chart > ol > li > div.box-image > a > span > img')
#per = dom.select('#contents > div.wrap-movie-chart > div.sect-movie-chart > ol > li > div.box-contents > div > strong > span')
#list = dom.select('#movie_more_container > li > div.box-image > a > span > img')

"""
for img in images:
    src = img.get_attribute('src')
    print('src :', src);
    
    filename = src.split('/')[-1]
    saveUrl = path+filename
    r = urllib.request.Request(src, headers={'User-Agent':'Mozilla/5.0'})
    imgUrl = urllib.request.urlopen(r).read()
    with open(saveUrl, "wb") as f:
        f.write(imgUrl)
"""
for img,content,per,egg,when in zip(images, contents, pers, eggs, whens):
    src = img.get_attribute('src')
    filename = src.split('/')[-1]

    title = content.text
    percent = per.text
    eggper = egg.text
    day = when.text

    sheet.append([filename.strip(), title.strip(), percent.strip(), eggper.strip(), day.strip()])


    
    
    


"""
for lit in list:
    src = lit.get('src')

    filename = src.split('/')[-1]
    saveUrl = path+filename
    r = urllib.request.Request(src, headers={'User-Agent':'Mozilla/5.0'})
    imgUrl = urllib.request.urlopen(r).read()
    with open(saveUrl, "wb") as f:
        f.write(imgUrl)     

""" 
        
print('종료...')        

# 엑셀 파일 저장/종료
workbook.save('C:/Users/java2/Desktop/CGV.xlsx')
workbook.close()
