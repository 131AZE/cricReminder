from Tkinter import *
import tkMessageBox
import requests
import time
import sys
from bs4 import BeautifulSoup
def hello():
    page = requests.get("http://cricbuzz.com")
    soup = BeautifulSoup(page.content, 'html.parser')
    for i in  soup.find_all('div',class_ = "cb-col cb-col-25 cb-mtch-blk"): #Section for feautured games on cricbuzz
        nextUrl = "http://cricbuzz.com"+i.find('a')["href"]
        sub_page = requests.get(nextUrl)                     #Open each individual match's link
        soup1 = BeautifulSoup(sub_page.content, 'html.parser')
        navBar =  soup1.find('nav',class_ = "cb-nav-bar") #Navbar in individual page
        for j in navBar.find_all('a'):
            if j.get_text() == "Scorecard":
                scoreURL = "http://cricbuzz.com"+j["href"]
                score_page = requests.get(scoreURL)
                soup2 = BeautifulSoup(score_page.content, 'html.parser')
                for k in soup2.find_all('div',class_ = "cb-col cb-col-100 cb-scrd-itms"):
                    batsman =  k.find('div',class_ = "cb-col-27")
                    try:
                        name = batsman.find('a').get_text()
                    except:
                        pass
                    if "Dhoni" in name:
                                statusDiv = k.find('div',class_ = "cb-col-33")  #If the name matches check the status of batsman
                                try: 
                                    status = statusDiv.find('span').get_text()
                                except: 
                                    pass
                                if status == "not out":         #Check if Dhoni is on strike
                                    tkMessageBox.showinfo("Notification","Dhoni on Strike")
                                    sys.exit()           
top = Tk() 
top.withdraw()
while True: 
    time.sleep(1000)
    hello()
   
