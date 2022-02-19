from logging import exception, fatal
from selenium.common.exceptions import NoSuchAttributeException
from selenium import webdriver
import time
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import requests
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import re


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
        options.add_argument("--mute-audio")
        options.add_argument("--headless")

        # initiate browser
        global driver
        driver = webdriver.Chrome(executable_path="chromedriver.exe", options=options)

        

    def login(self):

        # login
        driver.get("https://vocabulary.com/login")

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
    def mastery(self, t):
        if t == "T":
            mastery = True

    def kill(self):
        driver.close()

    def checkValue(self):
        
        while True:
            try:
                # button position changes every question based on which question it is, scrapes question to build xpath for next question button
                
                self.nextQuestion()
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "body-wrapper")))
                soup = BeautifulSoup(driver.page_source, "html.parser")

                field = ""
                for span_tag in soup('li', {'class':'enabled selected'}):
                    field = span_tag.find('span', {'class':''}).text
                
                if field == "":
                    # time.sleep(2)
                    pass
                    

                else:
                    if self.mastery == True:
                        print("mastery detected adding 1")
                        return str(int(field) + 1)
                    if int(field) >= 10:
                        self.mastery = False

                    return str(field)
            except Exception as e:
                print(e)
                # time.sleep(1.5)
                pass
                

            # place = soup.find('li', {"class":"enabled selected"}).get('value')
            # print(place)
    
    def getType(self):
        
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "page")))

        soup = BeautifulSoup(driver.page_source, "html.parser")
        
        self.nextQuestion()

        q_num = self.checkValue()
        q_num = str(q_num)
     
        try:
            driver.find_element_by_xpath('//*[@id="challenge"]/div/div[1]/div[' + q_num + ']/div/div/section[1]/div[1]/div[2]/div[2]/input')
            return "AUDIO"
        except:
            try:
                driver.find_element_by_xpath('//*[@id="challenge"]/div/div[1]/div[' + q_num + ']/div/div/section[1]/div[1]/div[4]/a[1]')
                return "MCQ"
                
            except:
                try:
                    driver.find_element_by_xpath('//*[@id="challenge"]/div/div[1]/div[' + q_num + ']/div/div/section[1]/div[1]/div[2]/a[1]')
                    return "PICTURE"
                except:
                    return "MASTERY"

            


    def mcqGetQuestionData(self, question_num):
        
        
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "choices")))
        time.sleep(1.5)

        soup = BeautifulSoup(driver.page_source, "html.parser")
        
        try:
            questions = soup.findAll('div', {'class': 'instructions'})
            result = soup.findAll("strong")
            result.reverse()
            print(result)

            result_2 = str(result)
            pattern = "<strong>(.*?)</strong>"

            substring = re.search(pattern, result_2).group(1)
            
            question = substring

            # for strong in soup('div', {'class':'instructions'}):
            #     question = strong.find('strong', {'':''}).text
                




        except:
            print(e)

            for strong in soup('div', {'class':'sentence'}):
                try:
                    question = strong.find('strong', {'':''}).text
                    
                except Exception as e:
                    print(e)
            
               
        # gets answer choices
        x = 1
        choices = ''
        while x <= 4:
            x_str = str(x)
            q_num_str = str(question_num)
            try:
                choice = driver.find_element_by_xpath('//*[@id="challenge"]/div/div[1]/div[' + q_num_str + ']/div/div/section[1]/div[1]/div[4]/a[' + x_str + ']').text
            except:
                choice = ""
                pass
            choice = str(choice)
            choices = choices + "," + choice
            x+=1
        
        return question + choices


    def mcqSubmit(self, question_num, answer_num):

        question_num = str(question_num)
        answer_num = str(answer_num)

        try:
            driver.find_element_by_xpath('//*[@id="challenge"]/div/div[1]/div[' + question_num + ']/div/div/section[1]/div[1]/div[4]/a[' + answer_num + ']').click()
        except:
            return False
        
    def paragraphGetData():

        return "working on it"
    
    def nextQuestion(self):
        try:
            driver.find_element_by_xpath('//*[@id="challenge"]/div/div[2]/button').click()
            return True
        except:
            return False

    def changeURL(self, url):
        driver.get(url)

    
    def pictureSubmit(self, q_num):
        
        while True:
            try:
                driver.find_element_by_xpath('//*[@id="challenge"]/div/div[1]/div[' + q_num + ']/div/div/section[1]/div[1]/div[2]/a[1]').click()
                time.sleep(1)
                driver.find_element_by_xpath('//*[@id="challenge"]/div/div[1]/div[' + q_num + ']/div/div/section[1]/div[1]/div[2]/a[2]').click()
                time.sleep(1)
                driver.find_element_by_xpath('//*[@id="challenge"]/div/div[1]/div[' + q_num + ']/div/div/section[1]/div[1]/div[2]/a[3]').click()
                time.sleep(1)
                driver.find_element_by_xpath('//*[@id="challenge"]/div/div[1]/div[' + q_num + ']/div/div/section[1]/div[1]/div[2]/a[4]').click()
                return
            except:
                time.sleep(1)


    def audioGetAnswer(self):
        
        soup = BeautifulSoup(driver.page_source, "html.parser")
        # //*[@id="challenge"]/div/div[1]/div[6]/div/div/section[1]/div[1]/div[1]/div[1]

        # //*[@id="challenge"]/div/div[1]/div[1]/div/div/section[1]/div[1]/div[1]/div[1]

        # this is experimental
        question_num = self.checkValue()
        question_num = int(question_num)
        answers = soup.findAll('div', {'class':'sentence complete'})
        
        # print("experimental audio finder is ")
        # print(answers)

        result = soup.findAll("strong")
        result.reverse()
        
        print("experemental audio parsed is")
        print(result)
        result = str(result)
        pattern = "<strong>(.*?)</strong>"
        
        substring = re.search(pattern, result).group(1)
        
        return substring


        

        # this actually works
        
        # for strong in soup('div', {'class':'sentence complete'}):
        #     try:
        #         answer = strong.find('strong', {'':''}).text
        #         return answer
        #     except Exception as e:
        #         print(e)

    def audioSubmit(self, q_num, answer):
        q_num = str(q_num)
        # find answer input box
        try:
            blank = driver.find_element_by_xpath('//*[@id="challenge"]/div/div[1]/div[' + q_num + ']/div/div/section[1]/div[1]/div[2]/div[2]/input')
            blank.send_keys(answer)
            time.sleep(1)
            driver.find_element_by_xpath('//*[@id="challenge"]/div/div[1]/div[' + q_num + ']/div/div/section[1]/div[1]/div[2]/div[3]/button[1]').click()
        except:
            pass
        # //*[@id="challenge"]/div/div[1]/div/div/div/section[1]/div[1]/div[2]/div[2]/input
        # //*[@id="challenge"]/div/div[1]/div[2]/div/div/section[1]/div[1]/div[2]/div[2]/input
    def audioGiveUp(self):
        num = self.checkValue()
        num = str(num)
    
        try:
            # driver.find_element_by_xpath('//*[@id="challenge"]/div/div[1]/div[' + num + ']/div/div/section[1]/div[1]/div[2]/div[3]/button[2]').click()
            # driver.find_element_by_xpath('//*[@id="challenge"]/div/div[1]/div[2]/div/div/section[1]/div[1]/div[2]/div[3]/button[2]').click()
            driver.find_element_by_xpath('//*[@id="challenge"]/div/div[1]/div[' + num + ']/div/div/section[1]/div[1]/div[2]/div[3]/button[2]').click()

        except Exception as e:
            print(e)
            self.nextQuestion()
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

        r = request.get(url, headers=headers)

        # get answer
        soup = BeautifulSoup(r.text, "html.parser")
        try:
            
            short_def = soup.find('p', {'class': "short"}).text
        except:
            print("failed finding def short")
            short_def = ""

        try:
            long_def = soup.find('p', {'class': "long"}).text
        except:
            print("failed finding def long")
            long_def = ""


        r = request.get(url_2, headers=headers)

        soup = BeautifulSoup(r.text, "html.parser")

        synonyms = ""
        for ultag in soup.find_all('ul', {'class':'mw-list'}):
            for litag in ultag.find_all('li'):
                synonyms = synonyms + (litag.text)


        synonyms = synonyms.strip()
        synonyms = synonyms.replace(" ", "").replace("\n", " ")
        return short_def + ":" + long_def + ":" + synonyms


class logicMethods():

    def __init__(self):
        pass

    def removeStopWords(self, definition):
        stop_words = set(stopwords.words('english'))
        word_tokens = word_tokenize(definition)
        filtered_sentence = [w for w in word_tokens if not w in stop_words]
        filtered_sentence = []
        for w in word_tokens:
            if w not in stop_words:
                filtered_sentence.append(w)
        return ' '.join(filtered_sentence)

    def getAnswer(self, questionData):

        
        

        # questionData = questionData.replace(" and", "").replace(" that ", "").replace(" is ", "").replace(" was ", "").replace(" has ", "").replace(" a ", "").replace(" from ", "")
        # questionData = questionData.replace(" for ", "").replace(" at ", "").replace(" the ", "").replace(" a ", "").replace(" is ", "").replace(" in ", "").replace(" an ", " ").replace("an ", "")
        # questionData = questionData.replace(" to ", "").replace(" or ", "").replace(" of ", "").replace(" as ", "").replace(" a", "").replace("a ", "")
        
        questionData = questionData.split(",")
        
        # word is the question you need to answer, question_1 - 4 are the questions you can answer
        questionData[0] = self.removeStopWords(questionData[0])
        questionData[1] = self.removeStopWords(questionData[1])
        questionData[2] = self.removeStopWords(questionData[2])
        questionData[3] = self.removeStopWords(questionData[3])
        questionData[4] = self.removeStopWords(questionData[4])

        print(questionData)
        data = pd.read_csv("data.csv")

        print(questionData[0])
        if questionData[0] == "________":
            

            print("___________ detected")
            for index in data.index:
                if data.loc[index, 'Word'] == questionData[1]:
                    return 1
                if data.loc[index, 'Word'] == questionData[2]:
                    return 2
                if data.loc[index, 'Word'] == questionData[3]:
                    return 3
                if data.loc[index, 'Word'] == questionData[4]:
                    return 4

        for index in data.index:
            if data.loc[index, 'Word'] in questionData:
                answerData = data.loc[index, 'Definition']

        try:
            foo = answerData.split(":")
        except:
            answerData = "answerData"
        try:
            
            print(answerData)
        except:
            print("failed finding answer")
            answerData = "answerdata"
        

        question_1 = questionData[1].split(" ")
        question_2 = questionData[2].split(" ")
        question_3 = questionData[3].split(" ")
        question_4 = questionData[4].split(" ")

        num_1, num_2, num_3, num_4 = 0, 0, 0, 0

        for x in range(0, len(question_1)):
            if question_1[x] in answerData: 
                print(question_1[x])
                num_1+=1
                
        for x in range(0, len(question_2)):
            if question_2[x] in answerData: 
                print(question_2[x])
                num_2+=1

        for x in range(0, len(question_3)):
            if question_3[x] in answerData: 
                print(question_3[x])
                num_3+=1

        for x in range(0, len(question_4)):
            if question_4[x] in answerData: 
                print(question_4[x])
                num_4+=1

        num_1, num_2, num_3, num_4 = str(num_1), str(num_2), str(num_3), str(num_4)
        
        num_total = num_1 + "," + num_2 + "," + num_3 + "," + num_4
        print(num_total)

        num_total = num_total.split(",")
        try:
            max_value = max(num_total)
            max_index = num_total.index(max_value)
        except:
            max_index = 1

        max_index+=1
        print("max index is")
        print(max_index)
        return max_index

    def count_occurrences(self, word, sentence):
        return sentence.lower().split().count(word)




class dataMethods():

    def __init__(self):

        try:
            data = pd.read_csv("data.csv")
        except:
            print("Failed Finding Dataset")

    def write(self, vocab, answer):
        instance = pd.read_csv("data.csv")

        vocab, answer = str(vocab), str(answer)
        print(f"writing {answer} to {vocab}")

        try:
            for index in instance.index:
                if instance.loc[index,'Word']==vocab:
                    current = instance.loc[index, 'Definition']
                    instance.loc[index, 'Definition'] = answer + "," + str(current)

            instance.to_csv("data.csv", index=False)
            print("Written")
        except Exception as e:
            print("Failed Writing")
            print(e)