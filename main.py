from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import tkinter as tk
from time import sleep
def GetInfo():
    tkWindow = tk.Tk()  
    tkWindow.geometry('250x70')  
    tkWindow.title('Login')
    tk.Label(tkWindow, text="User Name").grid(row=0, column=0)
    username = tk.StringVar()
    tk.Entry(tkWindow, textvariable=username).grid(row=0, column=1,ipadx=20)  
    tk.Label(tkWindow,text="Password").grid(row=1, column=0)  
    password = tk.StringVar()
    tk.Entry(tkWindow, textvariable=password).grid(row=1, column=1,ipadx=20)  
    tk.Button(tkWindow, text="Login",activebackground="gray",width=35, command=lambda:LoginTwitter(username.get(),password.get(),tkWindow)).grid(row=2,column=0,columnspan=2)  
    tkWindow.mainloop()

def WriteTXT(elements,counter):
    file = open("temp.txt","a")
    tweets=[]
    for element in elements:
        tweets.append(element.text)
    for tweet in tweets:
        file.write(str(counter)+".\n"+tweet+"\n"+"*********************************************"+"\n")
        counter+=1
    file.close()
    return counter


def LoginTwitter(username,password,tkWindow):
    tkWindow.destroy()
    browser = webdriver.Firefox()
    browser.get("https://twitter.com/login")
    browser.implicitly_wait(2)
    #username="taha.mucasiroglu@gmail.com"
    #password="*Basket*67"
    browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input').send_keys(username)
    browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input').send_keys(password)
    sleep(0.5)
    browser.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div/div/span/span").click()
    sleep(3)
    search=browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div[2]/input')
    search.send_keys("request for startup",Keys.ENTER)
    sleep(3)
    lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    match=False
    while(match==False):
        lastCount = lenOfPage
        sleep(3)
        lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
        if lastCount == lenOfPage:
            match=True
    sleep(3)
    elements=browser.find_elements_by_css_selector(".css-1dbjc4n.r-1iusvr4.r-16y2uox.r-1777fci.r-1mi0q7o")
    counter=1
    counter=WriteTXT(elements,counter)
    browser.close()


    





GetInfo()










