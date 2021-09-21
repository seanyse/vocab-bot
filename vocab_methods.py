from logging import exception, fatal
from selenium.common.exceptions import NoSuchAttributeException
from selenium import webdriver
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
        options.add_argument("--window-size=1100,900")
        options.add_argument("--window-position=500,50")
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

        # add check login valid
        return True

      

    def changeURL(self, url):

        driver.get(url)

    def checkValue(self):
        
        while True:
            try:
                # button position changes every question based on which question it is, scrapes question to build xpath for next question button
                
                print("checkvalue")

                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "body-wrapper")))
                soup = BeautifulSoup(driver.page_source, "html.parser")

                field = ""
                for span_tag in soup('li', {'class':'enabled selected'}):
                    field = span_tag.find('span', {'class':''}).text
                
                if field == "":
                    # time.sleep(2)
                    pass
                    

                else:
                    return field
            except Exception as e:
                print(e)
                # time.sleep(1.5)
                pass
                

            # place = soup.find('li', {"class":"enabled selected"}).get('value')
            # print(place)
    
    def getType(self):
        
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "page")))

        soup = BeautifulSoup(driver.page_source, "html.parser")

        # finds mcq question
        try:
            for strong in soup('div', {'class':'instructions'}):
                while True:
                    try:
                        strong.find('strong', {'class':''})
                        return "MCQ"
                    except:
                        try:
                            soup.find('div', {'class':"sentence"})
                            return "SENTANCEMCQ"

                        except :
                            try:
                                soup.find('div', {'class': "sentence blanked"})
                                return "PARAGRAPH"
                            except:
                                try:
                                    soup.find('div', {'class': "spelltheword"})
                                    return "AUDIO"
                                except:
                                    try:
                                        
                                        return "IDK"
                                    except:
                                        return "Error Returning"

        except Exception as e:
            print(e)
        

            


    def mcqGetQuestionData(self, question_num):
        
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "choices")))
        time.sleep(3)

        soup = BeautifulSoup(driver.page_source, "html.parser")
        
        try:
            for strong in soup('div', {'class':'instructions'}):
                question = strong.find('strong', {'class':''}).text
                print("question is" + question + "1")

            
        except:
            print("error getting question data, retrying")
            
            soup = BeautifulSoup(driver.page_source, "html.parser")
            question = soup.find('div', {'class': "sentence"}).text
            print("question is" + question + "2")
            
                
        # gets answer choices
        x = 1
        choices = ''
        while x <= 4:
            x_str = str(x)
            q_num_str = str(question_num)

            choice = driver.find_element_by_xpath('//*[@id="challenge"]/div/div[1]/div[' + q_num_str + ']/div/div/section[1]/div[1]/div[4]/a[' + x_str + ']').text
            choice = str(choice)
            choices = choices + "," + choice
            x+=1
        
        print(question + choices)
        return question + choices


    def mcqSubmit(self, question_num, answer_num):

        question_num = str(question_num)
        answer_num = str(answer_num)

        try:
            driver.find_element_by_xpath('//*[@id="challenge"]/div/div[1]/div[' + question_num + ']/div/div/section[1]/div[1]/div[4]/a[' + answer_num + ']').click()
        except:
            return False
        
    def getParagraphData():

        print("working on it")

        return "working on it"
    
    def nextQuestion(self):
        try:
            driver.find_element_by_xpath('//*[@id="challenge"]/div/div[2]/button').click()
            return True
        except:
            return False

    def changeURL(self, url):
        driver.get(url)

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



    def getAnswerData(self, definition):
        
        question_data = definition.split(",")
        url = "https://www.vocabulary.com/dictionary/" + question_data[0]
        url_2 = "https://www.merriam-webster.com/thesaurus/" + question_data[0]
        print(url)
        print(url_2)

        r = request.get(url, headers=headers)

        # get answer
        try:
            soup = BeautifulSoup(r.text, "html.parser")
            short_def = soup.find('p', {'class': "short"}).text
            long_def = soup.find('p', {'class': "long"}).text
        except:
            print("failed finding def")
            short_def = ""
            long_def = ""
        print(short_def)
        print(long_def)

        r = request.get(url_2, headers=headers)

        soup = BeautifulSoup(r.text, "html.parser")

        synonyms = ""
        for ultag in soup.find_all('ul', {'class':'mw-list'}):
            for litag in ultag.find_all('li'):
                synonyms = synonyms + (litag.text)


        
        synonyms = synonyms.strip()
        synonyms = synonyms.replace(" ", "").replace("\n", " ")
        print(synonyms)
        return short_def + ":" + long_def + ":" + synonyms


class logicMethods():

    def __init__(self):
        pass

   

    def getAnswer(self, questionData, answerData):

        # calc percentage, highest % gets answer
        print("Def start start")
        

        # removes all unncessary words
        # answerData = ' '.join(answerData)

        answerData = answerData.replace(" and ", "").replace(" or ", "").replace(" is ", "").replace(" was ", "").replace(" has ", "").replace(" a ", "").replace(" from ", "")

        print(questionData)
        print(answerData)

        questionData = questionData.split(",")

        question_1 = questionData[1].split(" ")
        question_2 = questionData[2].split(" ")
        question_3 = questionData[3].split(" ")
        question_4 = questionData[4].split(" ")

        num_1 = 0
        num_2 = 0
        num_3 = 0
        num_4 = 0

        for x in range(0, len(question_1)):
            if question_1[x] in answerData: 
                num_1+=1
                
        for x in range(0, len(question_2)):
            if question_2[x] in answerData: 
                num_2+=1

        for x in range(0, len(question_3)):
            if question_3[x] in answerData: 
                num_3+=1

        for x in range(0, len(question_4)):
            if question_4[x] in answerData: 
                num_4+=1


        print(num_1)
        print(num_2)
        print(num_3)
        print(num_4)

        num_1 = str(num_1)
        num_2 = str(num_2)
        num_3 = str(num_3)
        num_4 = str(num_4)

        num_total = num_1 + "," + num_2 + "," + num_3 + "," + num_4

        num_total = num_total.split(",")
        try:
            max_value = max(num_total)
            max_index = num_total.index(max_value)
        except:
            max_index = 1

        max_index+=1
        print("Index_mx is")
        print(max_index)

        return max_index
        


    def count_occurrences(self, word, sentence):
        return sentence.lower().split().count(word)


    

        
        

        




