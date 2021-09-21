from vocab_methods import requestMethods, seleniumMethods, logicMethods
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

            time.sleep(4)

            next = browser.nextQuestion()

            if next:
                pass
            else:
                browser.mcqSubmit(1, answer_num)
                next_1 = browser.nextQuestion()

                if next_1:
                    break
                else:
                    browser.mcqSubmit(2, answer_num)
                    next_2 = browser.nextQuestion()

                    if next_2:
                        break
                    else:
                        browser.mcqSubmit(3, answer_num)
                        next_3 = browser.nextQuestion()

                        if next_3:
                            break
                            
                        else:
                            browser.mcqSubmit(4, answer_num)
                            next_4 = browser.nextQuestion()

                            if next_4:
                                break
                            else:
                                break

            

            
            
        elif type == "PARAGRAPH":
            questionData = browser.mcqGetParagraphData(q_num)

            questionData = str(questionData)
            answerData = request.getAnswerData(questionData)
        
            logic.getAnswer(questionData, answerData)
            
        elif type == "SENTANCEMCQ":
            print("not solvable")
            
        elif type == "AUDIO":
            print("not solvable")
        elif type == "IDK":
            print("not solvable")

        
   
if __name__=="__main__":
    main()