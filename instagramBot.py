from selenium import webdriver
import time

import os.path

url = "https://www.instagram.com/"

browser = webdriver.Firefox()
browser.get(url)
time.sleep(3)

jscommand = """
followers = document.querySelector(".isgrP");
followers.scrollTo(0,followers.scrollHeight);
var lenOfpage = followers.scrollHeight;
return lenOfpage;
"""
listt = []
Followers_Count = 0 
My_Followers_Count = 0


def logout():
    browser.get(url)
    logoutbutton = browser.find_element_by_xpath(
        '//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[5]/span')
    logoutbutton.click()
    logoutbutton1 = browser.find_element_by_xpath(
        '/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/div[2]/div/div[2]/div[2]/div')
    logoutbutton1.click()


def scroll():
    lenofpage = browser.execute_script(jscommand)
    Scroll(lenofpage, jscommand)


def Scroll(lenofpage, jscommand):
    match = False
    while(match == False):
        lastcount = lenofpage
        time.sleep(1)
        lenofpage = browser.execute_script(jscommand)
        if lastcount == lenofpage:
            match = True


def Get_Followers(File_name = "own"):


    File = str(File_name) + ".txt"
    if not os.path.isfile(File):
        if File_name == "own":
            go_to_Profile()
            
        else:
            Go_To_ProfileOf(File_name)

        GetFollowers = browser.find_elements_by_css_selector(
             '.FPmhX.notranslate._0imsa ')
        
        time.sleep(2)
        with open(File, "w", encoding="utf-8") as fi:
            for f in GetFollowers:
                listt.append(f.text)
                fi.write(f.text)
                fi.write("\n")
                print(f.text)  
            
    else:
        with open(File, "r", encoding="utf-8") as fi:
            GetFollowers = fi.read()
        print(GetFollowers)


def login(Type = "Instagram"):
    info=Get_info()
    
    if Type == "Instagram":
        
        setusername = browser.find_element_by_xpath(
        "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input")
        setusername.send_keys(info[0])
        setpassword = browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input")
        setpassword.send_keys(info[1])
        loginbutton =browser.find_element_by_xpath(
        "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button")
        loginbutton.click()
        time.sleep(5)
    else:
        loginWithFacebook = browser.find_element_by_xpath(
        '/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[5]/button/span[2]')
        loginWithFacebook.click()
        setusername = browser.find_element_by_xpath('//*[@id="email"]')
        setusername.send_keys(info[0])
        setpassword = browser.find_element_by_xpath('//*[@id="pass"]')
        setpassword.send_keys(info[1])
        loginbutton = browser.find_element_by_xpath('//*[@id="loginbutton"]')
        loginbutton.click()
    print("Wait 10 sec")
    time.sleep(5)
    try:
        notnow = browser.find_element_by_xpath(
            '/html/body/div[4]/div/div/div/div[3]/button[2]')
        notnow.click()
    except:
        pass
    print("wait 5 sec")
    time.sleep(5)
    try:
        s =  browser.find_element_by_css_selector(
            '.js.logged-in.client-root.js-focus-visible.sDN5V')
    except:
            print("Your 'username' or 'password' is wrong ")
            browser.get(url)
            Type_()
  
    time.sleep(2)


def go_to_Profile():
    logoutbutton = browser.find_element_by_xpath(
        '//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[5]/span')
    logoutbutton.click()
    gotoProfile = browser.find_element_by_xpath(
        '//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[5]/div[2]/div/div[2]/div[2]/a[1]')
    gotoProfile.click()
    time.sleep(2)
    count_of_Followers = browser.find_element_by_xpath(
        '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a/span')
    count = int(count_of_Followers.text)
    print(count)
    
    time.sleep(2)
    buttons = browser.find_elements_by_css_selector(".Y8-fY ")[1].click()
    time.sleep(3)
    scroll()


def Go_To_ProfileOf(profile):
           
    browser.get(url+str(profile))
    count_of_Followers = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a/span')
    count = int(count_of_Followers.text)
    print(count,"Followers of",profile)
    if count >1000:
        print(
            "The count of Followers is big you may have a problem with getting Followers if you want to get press yes if you dont press no")
        yes_no = str(input())
        if yes_no == 'no':
            Go_To_ProfileOf(input(
        "please write the name of profile you want to get followers \n"))
            return     
    time.sleep(2)
    buttons = browser.find_elements_by_css_selector(".Y8-fY ")[1].click()
    scroll()
    
def Get_info():
    print("please be sure or you have to restart the program")
    username=input(str("Enter username: "))
    password=input(str("Enter pasword: "))
    print("")
    return (username,password)



def Type_():
    print("Enter 1 to sign with Instgram account Enter 2 to sign with Facebook account ")
    sign_ = int(input())
    if sign_ == 1:
        login()
    elif sign_ == 2:
        login("Facebook")
    else:
        print("Enter vaild number please")
        Type_()

def main1():
    print("browser launching..... ")
    Type_()
    Get_Followers()
    time.sleep(3)
    while True:
        Get_Followers(input(
        "please write the name of profile you want to get followers \n"))
        Continue = input("If you want to take one more of Followers press 1 to logout press 2: ")
        if int(Continue) != 1:
            break
    print("Borwser closing .........")
    logout()
    time.sleep(3)
    browser.close()

if __name__ =="__main__":
    main1() 
