from vocab_methods import dataMethods, requestMethods, seleniumMethods, logicMethods
import json
import time

f = open('data.json',)
data = json.load(f)
for i in data["data"]:
    username = i["username"]
    password = i["password"]
    url = i["url"]

def main():

    browser = seleniumMethods(username, password, url)
    request = requestMethods()
    logic = logicMethods()
    data = dataMethods()

    browser.init_browser()
    request.init_req()

    status = browser.login()

    while True:
        if status == True:
            print("Login Success")
            break
        else:
            print("Login Failed, Retrying")
            status = browser.login()

    browser.changeURL(url)

    while True:
        
        q_num = browser.checkValue()
        print(q_num)
        type = browser.getType()
        
        print("Type is " + type)
        if type == "MCQ":
            questionData = browser.mcqGetQuestionData(q_num)

            questionData = str(questionData)
            answerData = request.getAnswerData(questionData)
            
            answer_num = logic.getAnswer(questionData, answerData)

            browser.mcqSubmit(q_num, answer_num)
            time.sleep(2)
            next = browser.nextQuestion()

            if next:
                answerData = answerData.split(",")
                data.write(questionData, answerData[answer_num-1])
                pass
            else:
                
                browser.mcqSubmit(q_num, 1)
                if browser.nextQuestion():
                    answerData = answerData.split(",")
                    data.write(questionData, answerData[0])

                time.sleep(1)
                browser.mcqSubmit(q_num, 2)
                if browser.nextQuestion():
                    answerData = answerData.split(",")
                    data.write(questionData, answerData[1])

                time.sleep(1)
                browser.mcqSubmit(q_num, 3)
                if browser.nextQuestion():
                    answerData = answerData.split(",")
                    data.write(questionData, answerData[2])

                time.sleep(1)
                browser.mcqSubmit(q_num, 4)
                if browser.nextQuestion():
                    answerData = answerData.split(",")
                    data.write(questionData, answerData[3])

                time.sleep(1)
                browser.nextQuestion()


                
            
        elif type == "PARAGRAPH":
            questionData = browser.mcqGetParagraphData(q_num)

            questionData = str(questionData)
            answerData = request.getAnswerData(questionData)
        
            logic.getAnswer(questionData, answerData)
            
        elif type == "SENTANCEMCQ":
            print("not solvable")
             
        elif type == "AUDIO":
            answer = browser.audioGetAnswer()
            browser.audioSubmit(q_num, answer)

            next = browser.nextQuestion()

            if next:
                pass
            else:
                print("jere")
                browser.audioGiveUp()
                browser.nextQuestion()

        elif type == "IDK":
            browser.changeURL(url)
            time.sleep(5)
            print("not solvable")

        
   
if __name__=="__main__":
    main()