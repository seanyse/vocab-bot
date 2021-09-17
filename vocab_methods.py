from logging import exception
from seleniumwire import webdriver
import time
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import requests

class seleniumMethods:

    def __init__(self, username, password, url):

        self.user = username
        self.pswrd = password
        self.url = url
    
    def init_browser(self):
        
        # initiate browser setting
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"
        options = webdriver.ChromeOptions()
        options.add_argument(f'user-agent={user_agent}')
                
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--allow-running-insecure-content')
        options.add_argument("--disable-extensions")
        options.add_argument("--window-size=900,700")
        options.add_argument("--window-position=600,150")
        options.add_argument("--proxy-server='direct://'")
        options.add_argument("--proxy-bypass-list=*")
        options.add_argument("--start-minimized")
        options.add_argument('--disable-gpu')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--no-sandbox')
        options.add_argument('ignore-certificate-errors')
        options.add_experimental_option("excludeSwitches", ['enable-automation'])
        options.add_argument("disable-infobars")
        # options.add_argument("--mute-audio")

        # initiate browser
        global driver
        driver = webdriver.Chrome(executable_path="chromedriver.exe", options=options)

        

    def login(self):

        # login
        driver.get("https://vocab.com/login")

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'value')))

        username = driver.find_element_by_name('username') 
        password = driver.find_element_by_name('password')

        username.send_keys(self.user)
        password.send_keys(self.pswrd)

        driver.find_element_by_xpath('//*[@id="loginform"]/div[6]/button').submit()

        # check if login valid
        for request in driver.requests:  
            if request.response:  
                response = request.response.status_code,  

        response = str(response)

        print(response)
        if response == "(200,)":
            return True
        else:
            return False

    def changeURL(self, url):

        driver.get(url)

    def checkValue(self):

        # button position changes every question based on which question it is, scrapes question to build xpath for next question button
        driver.get(self.url)

        # html = driver.page_source
        # fileToWrite = open("page_source.txt", "w")
        # fileToWrite.write(html)
        # fileToWrite.close()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "body-wrapper")))
        soup = BeautifulSoup(driver.page_source, "html.parser")

        
        for span_tag in soup('li', {'class':'enabled selected'}):
            field = span_tag.find('span', {'class':''}).text
        
            

        return field

        # place = soup.find('li', {"class":"enabled selected"}).get('value')
        # print(place)
    
    def getType(self):
        print('working')


    def getQuestion(self):
        
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "page")))

        soup = BeautifulSoup(driver.page_source, "html.parser")

        for strong in soup('div', {'class':'instructions'}):
            question = strong.find('strong', {'class':''}).text

        return question

        
    def mcqSubmit(question_num):

        driver.find_element_by_xpath('//*[@id="challenge"]/div/div[1]/div[' + question_num + ']/div/div/section[1]/div[1]/div[4]/a[1]').click()



class requestMethods():

    def __init__(self):
        pass
        
    def init_req(self):


        global headers
        global request

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
            'Accept': 'text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0. 8' ,
            'Accept-Language': 'en-US, en;q=0.5',
            'DNT': '1',
            'Connection':'keep-alive',
            'Upgrade-Insecure-Requests':'1',
            'Accept-Encoding':'identity',
        }

        request = requests.Session()



    def getAnswer(definition):
        
        url = "https://www.vocabulary.com/dictionary" + definition

        r = request.get(url, headers=headers)

        soup = BeautifulSoup(r.text, "html.parser")


class logic():

    def __init__(self):
        pass

    def getPercentage(self):

        print("working")




