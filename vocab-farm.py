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

    num_right, num_wrong, num_total = 0, 0, 0
    while True:
        print(f"Questions Right, {num_right}: Questions Wrong {num_wrong}: Questions Total {num_total}")
        questionData = ""

        q_num = browser.checkValue()
        print(q_num)
        type = browser.getType()
        
        print("Type is " + type)
        if type == "MCQ":
            questionData = browser.mcqGetQuestionData(q_num)

            questionData = str(questionData)
            # answerData = request.getAnswerData(questionData)
            
            answer_num = logic.getAnswer(questionData)

            browser.mcqSubmit(q_num, answer_num)
            time.sleep(2)
            next = browser.nextQuestion()

            print("next is")
            print(next)
            questionData = questionData.split(",")
            if next == True:
                
                print("-----------------------------")
                print(questionData)
                data.write(questionData[0], questionData[answer_num])
                num_right += 1
            else:
                index_found = False
                browser.mcqSubmit(q_num, 1)
                time.sleep(1)
                foo = browser.nextQuestion()
                if foo == True and index_found == False:
                    print("-----------------------------")
                    print(questionData)
                    data.write(questionData[0], questionData[1])
                    index_found = True
                    
                browser.mcqSubmit(q_num, 2)
                time.sleep(1)
                foo = browser.nextQuestion()
                if foo == True and index_found == False:
                    print("-----------------------------")
                    print(questionData)
                    data.write(questionData[0], questionData[2])
                    index_found = True
                    
                browser.mcqSubmit(q_num, 3)
                time.sleep(1)
                foo = browser.nextQuestion()
                if foo == True and index_found == False:
                    print("-----------------------------")
                    print(questionData)
                    data.write(questionData[0], questionData[3])
                    index_found = True

                browser.mcqSubmit(q_num, 4)
                time.sleep(1)
                foo = browser.nextQuestion()   
                if foo == True and index_found == False:
                    print("-----------------------------")
                    print(questionData)
                    data.write(questionData[0], questionData[4])
                
                num_wrong += 1
            num_total += 1
                              

                
            
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

        elif type == "PICTURE":
            
            browser.pictureSubmit(q_num)

        
   
if __name__=="__main__":
    main()