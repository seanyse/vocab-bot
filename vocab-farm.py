from vocab_methods import seleniumMethods
import json

f = open('data.json',)
data = json.load(f)
for i in data:
    
    username = i["username"]
    password = i["password"]
    url = i["url"]

def main():

    browser = seleniumMethods(username, password, url)
    browser.init_browser()
    status = browser.login()

    while True:
        if status == True:
            print("Login Success")
            break
        else:
            print("Login Failed, Retrying")
            status = browser.login()

    browser.checkValue()

# driver.get(url)
# time.sleep(.5)

# change = 0
# while True:
#     if change == 10:
#         change = 0

#     change += 1
#     refresh = 0
    
#     while True:
#         try:

#             driver.execute_script("window.scrollTo(0, window.scrollY + 50)")
#             time.sleep(.5)
#             change_str = str(change)
#             driver.find_element_by_xpath('//*[@id="challenge"]/div/div[1]/div[' + change_str + ']/div/div/section[1]/div[1]/div[5]/span[2]/a[1]').click()
            
# # //*[@id="challenge"]/div/div[1]/div[2]/div/div/section[1]/div[1]/div[5]/span[2]/a[1]
#             break
#         except Exception as e:
#             time.sleep(2)
#             print(f"retrying 3 {e}")
#             refresh += 1
#             if refresh == 5:
#                 driver.refresh()
#                 refresh = 0 
#                 break
            
#     x = 1
#     while True:
#         time.sleep(.5)
        
#         try:
#             str_x = str(x)

#             print("Submitting Answer")
#             driver.execute_script("window.scrollTo(0, window.scrollY - 50)")
#             time.sleep(1)

#             driver.find_element_by_xpath('//*[@id="challenge"]/div/div[1]/div[' + change_str + ']/div/div/section[1]/div[1]/div[4]/a[1]').click()
            

#             driver.find_element_by_xpath('//*[@id="challenge"]/div/div[1]/div[' + change_str + ']/div/div/section[1]/div[1]/div[4]/a[' + str_x + ']').click()
#             x += 1

#             # //*[@id="challenge"]/div/div[1]/div[2]/div/div/section[1]/div[1]/div[4]/a[1]
#             if x == 5:
#                 break

#         except Exception as e:
#             print(e)
#             x += 1
#             refresh += 1
#             if refresh == 10:
#                 driver.refresh()
#                 refresh = 0 
#                 x = 1
#             try:
#                 driver.find_element_by_xpath('//*[@id="challenge"]/div/div[2]/button').click()
#             except:
#                 pass
                
                
#     while True:
        
#         try:
#             driver.find_element_by_xpath('//*[@id="challenge"]/div/div[2]/button').click()
#             time.sleep(1)
#             driver.find_element_by_xpath('//*[@id="challenge"]/div/div[2]/button').click()
#             break

#         except:
            
#             print("error fatal")
#             time.sleep(5)
#             refresh += 1
#             if refresh == 10:
#                 driver.refresh()
#                 refresh = 0 
   
if __name__=="__main__":
    main()