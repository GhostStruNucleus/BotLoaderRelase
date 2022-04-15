from selenium import webdriver
import colorama
from colorama import Fore
from os import system, name
from time import time, strftime, gmtime, sleep
from selenium.webdriver.common.by import By
import threading, warnings
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import chromedriver_autoinstaller
from selenium.webdriver.chrome.service import Service
import os
import undetected_chromedriver as uc
from datetime import datetime


'''
Copyright (c) 2022 @GhostStru
NO Permission is hereby granted, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software, including limitation of the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to forbid persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NON INFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.'''

warnings.filterwarnings("ignore")


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

clear()
system('title Bot Loader @GhostStru')

def printBigText():
    bigText1 = f"""
{Fore.LIGHTMAGENTA_EX}
{" "*round(os.get_terminal_size().columns/2-32)}  ▄▄▄▄·     ▄▄▄▄▄▄▄    ▐▌·              ▐▌   ▪ ▐▌▀▄    .
{" "*round(os.get_terminal_size().columns/2-32)} ▐█ ▀█▪▪     •██  •    ▐▌              ▄▌ ▌    ▐▌  ▀▄.
{" "*round(os.get_terminal_size().columns/2-32)} ▐█▀▀█▄ ▄█▀▄  ▐█.▪     ▐▌ ▪▪   ▄█▀▄   ▄▌ ▪ ▌   ▐▌ ▪▪ ▌
{" "*round(os.get_terminal_size().columns/2-32)} ██▄▪▐█▐█▌.▐▌ ▐█▌·     ▐▌     ▐█▌.▐▌  ▌·▀▀▀.▌  ▐▌.   ▌
{" "*round(os.get_terminal_size().columns/2-32)} ·▀▀▀▀  ▀█▄▀▪ ▀▀▀     ·▀▀▀▀▀▀. ▀█▄▀▪  ▌ ▪▪   ▌ ▐▌▀█▄▀ ▪▪
"""
    bigText2 = bigText1.replace('▪', f'{Fore.GREEN}▪{Fore.LIGHTMAGENTA_EX}')
    bigText3 = bigText2.replace('•', f'{Fore.GREEN}•{Fore.LIGHTMAGENTA_EX}')
    bigText4 = bigText3.replace('·', f'{Fore.GREEN}·{Fore.LIGHTMAGENTA_EX}')
    bigText5 = bigText4.replace('.', f'{Fore.GREEN}.{Fore.LIGHTMAGENTA_EX}')
    print(bigText5)
def printOptions():
    info = f"""
{Fore.WHITE}
{" "*round(os.get_terminal_size().columns/2-42)}╔═══════════════════════════════════════════════════════════════════════════════════╗
{" "*round(os.get_terminal_size().columns/2-42)}║                                                                                   ║
{" "*round(os.get_terminal_size().columns/2-42)}║          {Fore.WHITE}[{Fore.LIGHTGREEN_EX}>{Fore.WHITE}] {Fore.LIGHTGREEN_EX}About: {Fore.LIGHTMAGENTA_EX}This Is A Advanced Tool That Uses Zefoy{Fore.WHITE}                       ║
{" "*round(os.get_terminal_size().columns/2-42)}║          {Fore.LIGHTMAGENTA_EX}To Bot TikTok Follows, Hearts, Views, & Shares.{Fore.WHITE}                          ║
{" "*round(os.get_terminal_size().columns/2-42)}║          {Fore.WHITE}[{Fore.LIGHTGREEN_EX}>{Fore.WHITE}] {Fore.LIGHTGREEN_EX}Updates: {Fore.LIGHTMAGENTA_EX}Minor Adjustments --4/10/2022{Fore.WHITE}                               ║
{" "*round(os.get_terminal_size().columns/2-42)}║          {Fore.WHITE}[{Fore.LIGHTGREEN_EX}>{Fore.WHITE}] {Fore.LIGHTGREEN_EX}Made By: {Fore.LIGHTMAGENTA_EX}GhostStru#0001{Fore.WHITE}                                              ║
{" "*round(os.get_terminal_size().columns/2-42)}║          {Fore.WHITE}[{Fore.LIGHTGREEN_EX}>{Fore.WHITE}] {Fore.LIGHTGREEN_EX}Download Chrome Driver: {Fore.LIGHTMAGENTA_EX}https://chromedriver.chromium.org/downloads{Fore.WHITE}  ║
{" "*round(os.get_terminal_size().columns/2-42)}║                                                                                   ║
{" "*round(os.get_terminal_size().columns/2-42)}╚═══════════════════════════════════════════════════════════════════════════════════╝
"""
    print(info)
vidUrl = input("TikTok video URL: ")

def clear():
    os.system("cls")

    printBigText()

    print(f'{" "*round(os.get_terminal_size().columns/2-14)}{Fore.WHITE}[{Fore.LIGHTGREEN_EX}>{Fore.WHITE}] {Fore.LIGHTGREEN_EX}Made By: {Fore.LIGHTMAGENTA_EX}GhostStru#0001 {Fore.WHITE}[{Fore.LIGHTGREEN_EX}<{Fore.WHITE}]\n{" "*round(os.get_terminal_size().columns/2-30)}{Fore.WHITE}[{Fore.LIGHTGREEN_EX}>{Fore.WHITE}] {Fore.LIGHTGREEN_EX}Github: {Fore.LIGHTMAGENTA_EX}https://github.com/GhostStruNucleus {Fore.WHITE}[{Fore.LIGHTGREEN_EX}<{Fore.WHITE}]')

    printOptions()
clear()
def timez():
    global current_time
    print(f"{Fore.WHITE}[{Fore.YELLOW}*{Fore.WHITE}] {Fore.YELLOW}Time Started")
    while True:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        sleep(0.5)


def main():
    global value
    global Views
    global Hearts
    global Shares
    global Comments
    global total_comments
    global comments_num
    global number
    global Username
    global current_time

    if vidUrl:
        clear()
        start = time()
        time_elapsed = strftime('%H:%M:%S', gmtime(time() - start))
        print(f"{Fore.WHITE}[{Fore.LIGHTGREEN_EX}>{Fore.WHITE}] {Fore.LIGHTGREEN_EX}Loading silent driver")
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--mute-audio")
        #chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
        #chromedriver_autoinstaller.install()  # installing auto chromedriver
        chrome_options.headless = True
        driver = uc.Chrome(use_subprocess=True, options=chrome_options)
        driver.get("https://zefoy.com/")
        print(f"{Fore.WHITE}[{Fore.LIGHTGREEN_EX}>{Fore.WHITE}] {Fore.LIGHTGREEN_EX}Page loaded")
        driver.add_cookie({"name": "PHPSESSID", "value": value})
        print(f"{Fore.WHITE}[{Fore.LIGHTGREEN_EX}>{Fore.WHITE}] {Fore.LIGHTGREEN_EX}Cookie injected")
        driver.refresh()
        wait = WebDriverWait(driver, 15)
        waits = WebDriverWait(driver, 3)
        #driver.set_window_size(1024, 480)
        try:
            waits.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main"]/div/div[1]/div')))
            print(f"{Fore.WHITE}[{Fore.LIGHTGREEN_EX}>{Fore.WHITE}] {Fore.LIGHTGREEN_EX}Page loaded")
        except:
            pass

        Views = 0
        Hearts = 0
        Shares = 0
        Comments = 0
        total_comments = 1
        comments_num = 0
        number = 0
        Username = "@Anonymous"


    def beautify(arg):
        return format(arg, ',d').replace(',', '.')


    def title():  # Update the title IF option 1 was picked.
        global Views
        global Hearts
        global Shares
        global Comments
        global Username
        global number
        global comments_num
        global Followers

        while True:
            time_elapsed = strftime('%H:%M:%S', gmtime(time() - start))
            system(f'title Bot Loader @GhostStru ^| Views: {beautify(Views)} ^| Hearts: {beautify(Hearts)} ^| Shares: {beautify(Shares)} ^| Elapsed Time: {time_elapsed}')

    #Followers
    def loop0():
        global current_time
        global Followers

        try:
            ck = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div[1]/div[3]/div/div[1]/div/p/small')))
            if ck.text == "soon will be update":
                print(f"{Fore.WHITE}[{Fore.RED}X {Fore.WHITE}| "+str(current_time)+"] Unavailable => Followers")
                loop1()  # if it's being updated, continue right away
            else:
                wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div[1]/div[3]/div/div[1]/div/button'))).click()

        except:
            print(f"{Fore.WHITE}[{Fore.BLUE}= {Fore.WHITE}| "+str(current_time)+"] The captcha is unsolved! 1")
            sleep(10)
            driver.refresh()
            loop1()

        try:
            methodFollowers()
            sleep(3)
            driver.refresh()
            loop1()

        except:
            try:
                lmt = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "h4")))
                timer_message = lmt.text
                print(f"{Fore.WHITE}[{Fore.BLUE}= {Fore.WHITE}| "+str(current_time)+"] Followers Timer: " + timer_message)

                message_split = timer_message.split()

                if timer_message == "Checking Timer..." or timer_message == "Next Submit: READY....!":
                    methodFollowers()
                elif message_split[4].isnumeric():
                    timer = int(message_split[2])
                    timer2 = int(message_split[4])

                    if (timer == 0) and (timer2 <= 10):
                        sleeping = timer2 + 1
                        print(f"{Fore.WHITE}[{Fore.BLUE}= {Fore.WHITE}| "+str(current_time)+"] Sleep: " + str(sleeping))
                        sleep(sleeping)
                        methodFollowers()
                    else:
                        print("\n[X | "+str(current_time)+"] Skipping Followers..")

                driver.refresh()
                loop1()

            except:
                try:
                    fn = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Not found video.']")))
                    print(f"{Fore.WHITE}[{Fore.RED}X {Fore.WHITE}| "+str(current_time)+"] Not found video..\n")
                    methodFollowers()
                    sleep(3)
                    driver.refresh()
                    loop1()
                except:
                    print(f"{Fore.WHITE}[{Fore.LIGHTMAGENTA_EX}- {Fore.WHITE}| "+str(current_time)+"] An error occurred. Skipping => Followers")
                    sleep(0.5)
                    driver.refresh()
                    loop1()


    #Views
    def loop1():
        global current_time
        global Views

        try:
            ck = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div[1]/div[3]/div/div[4]/div/p/small")))
            if ck.text == "soon will be update":
                print(f"{Fore.WHITE}[{Fore.RED}X {Fore.WHITE}| "+str(current_time)+"] Unavailable => Views")
                loop2()  #if it's being updated, continue right away
            else:
                wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div[1]/div[3]/div/div[4]/div/button"))).click()
        except:
            print(f"{Fore.WHITE}[{Fore.LIGHTMAGENTA_EX}- {Fore.WHITE}| "+str(current_time)+"] The captcha is unsolved! 2")
            sleep(10)
            driver.refresh()
            loop1()

        try:
            methodView()
            sleep(3)
            driver.refresh()
            loop2()

        except:
            try:
                lmt = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "h4")))
                timer_message = lmt.text
                print(f"{Fore.WHITE}[{Fore.BLUE}= {Fore.WHITE}| "+str(current_time)+"] Views Timer: " + timer_message)

                message_split = timer_message.split()

                if timer_message == "Checking Timer..." or timer_message == "Next Submit: READY....!":
                    methodView()
                elif message_split[4].isnumeric():
                    timer = int(message_split[2])
                    timer2 = int(message_split[4])

                    if (timer == 0) and (timer2 <= 10):
                        sleeping = timer2 + 1
                        print(f"{Fore.WHITE}[{Fore.BLUE}= {Fore.WHITE}| "+str(current_time)+"] Sleep: " + str(sleeping))
                        sleep(sleeping)
                        methodView()
                    else:
                        print(f"{Fore.WHITE}[{Fore.RED}X {Fore.WHITE}| "+str(current_time)+"] Skipping Views..")

                driver.refresh()
                loop2()

            except:
                try:
                    fn = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Not found video.']")))
                    print(f"{Fore.WHITE}[{Fore.RED}X {Fore.WHITE}| "+str(current_time)+"] Not found video..")
                    methodView()
                    sleep(3)
                    driver.refresh()
                    loop2()
                except:
                    print(f"{Fore.WHITE}[{Fore.LIGHTMAGENTA_EX}- {Fore.WHITE}| "+str(current_time)+"] An error occurred. Skipping => Views")
                    sleep(3)
                    driver.refresh()
                    loop2()


    #Hearts
    def loop2():
        global current_time
        global Hearts

        try:
            ck = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div[1]/div[3]/div/div[2]/div/p/small")))
            if ck.text == "soon will be update":
                print(f"{Fore.WHITE}[{Fore.RED}X {Fore.WHITE}| "+str(current_time)+"] Unavailable => Hearts")
                loop3()  #if it's being updated, continue right away
            else:
                wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div[1]/div[3]/div/div[2]/div/button"))).click()

        except:
            print(f"{Fore.WHITE}[{Fore.LIGHTMAGENTA_EX}- {Fore.WHITE}| "+str(current_time)+"] The captcha is unsolved! 3")
            sleep(10)
            driver.refresh()
            loop2()

        try:
            methodHearts()
            sleep(3)
            driver.refresh()
            loop3()

        except:
            try:
                lmt = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "h4")))
                timer_message = lmt.text
                print(f"{Fore.WHITE}[{Fore.BLUE}= {Fore.WHITE}| "+str(current_time)+"] Hearts Timer: " + timer_message)

                message_split = timer_message.split()

                if timer_message == "Checking Timer..." or timer_message == "Next Submit: READY....!":
                    methodHearts()
                elif message_split[4].isnumeric():
                    timer = int(message_split[2])
                    timer2 = int(message_split[4])

                    if (timer == 0) and (timer2 <= 10):
                        sleeping = timer2 + 1
                        print(f"{Fore.WHITE}[{Fore.BLUE}= {Fore.WHITE}| "+str(current_time)+"] Sleep: " + str(sleeping))
                        sleep(sleeping)
                        methodHearts()
                    else:
                        print(f"{Fore.WHITE}[{Fore.RED}X {Fore.WHITE}| "+str(current_time)+"] Hearts Unavailable")

                driver.refresh()
                loop3()

            except:
                try:
                    fn = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Not found video.']")))
                    print(f"{Fore.WHITE}[{Fore.RED}X {Fore.WHITE}| "+str(current_time)+"] Not found video..")
                    methodHearts()
                    sleep(3)
                    driver.refresh()
                    loop3()
                except:
                    print(f"{Fore.WHITE}[{Fore.LIGHTMAGENTA_EX}- {Fore.WHITE}| "+str(current_time)+"] An error occurred. Skipping => Hearts")
                    sleep(3)
                    driver.refresh()
                    loop3()


    #Shares
    def loop3():
        global current_time
        global Shares

        try:
            ck = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div[1]/div[3]/div/div[5]/div/p/small")))
            if ck.text == "soon will be update":
                print(f"{Fore.WHITE}[{Fore.RED}X {Fore.WHITE}| "+str(current_time)+"] Unavailable => Shares")
                loop4() #if it's being updated, continue right away
            else:
                wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div[1]/div[3]/div/div[5]/div/button"))).click()
        except:
            print(f"{Fore.WHITE}[{Fore.LIGHTMAGENTA_EX}- {Fore.WHITE}| "+str(current_time)+"] The captcha is unsolved! 4")
            sleep(10)
            driver.refresh()
            loop3()
        try:
            methodShare()
            sleep(3)
            driver.refresh()
            loop4()
        except:
            try:
                lmt = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "h4")))
                timer_message = lmt.text
                print(f"{Fore.WHITE}[{Fore.BLUE}= {Fore.WHITE}| "+str(current_time)+"] Shares Timer: " + timer_message)

                message_split = timer_message.split()

                if timer_message == "Checking Timer..." or timer_message == "Next Submit: READY....!":
                    methodShare()
                elif message_split[4].isnumeric():
                    timer = int(message_split[2])
                    timer2 = int(message_split[4])

                    if (timer == 0) and (timer2 <= 10):
                        sleeping = timer2 + 1
                        print(f"{Fore.WHITE}[{Fore.BLUE}= {Fore.WHITE}| "+str(current_time)+"] Sleep: " + str(sleeping))
                        sleep(sleeping)
                        methodShare()
                    else:
                        print(f"{Fore.WHITE}[{Fore.RED}X {Fore.WHITE}| "+str(current_time)+"] Skipping Shares")
                driver.refresh()
                loop4()
            except:
                try:
                    fn = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Not found video.']")))
                    print(f"\n{Fore.WHITE}[{Fore.RED}X {Fore.WHITE}| "+str(current_time)+"] Not found video..")
                    methodShare()
                    sleep(3)
                    driver.refresh()
                    loop4()
                except:
                    print(f"{Fore.WHITE}[{Fore.LIGHTMAGENTA_EX}- {Fore.WHITE}| "+str(current_time)+"] An error occurred. Skipping => Shares")
                    sleep(3)
                    driver.refresh()
                    loop4()


    #comment hearts
    def loop4():
        global current_time
        global Username
        global Comments
        global total_comments
        global comments_num
        global number

        if number == int(comments_num):
            number = 0
        try:
            ck = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div[1]/div[3]/div/div[3]/div/p/small")))
            if ck.text == "soon will be update":
                print(f"{Fore.WHITE}[{Fore.RED}X {Fore.WHITE}| "+str(current_time)+"] Unavailable => Comments Hearts")
                loop0()  #if it's being updated, continue right away
            else:
                wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div[1]/div[3]/div/div[3]/div/button"))).click()
        except:
            print(f"{Fore.WHITE}[{Fore.LIGHTMAGENTA_EX}- {Fore.WHITE}| "+str(current_time)+"] The captcha is unsolved! 5")
            sleep(10)
            driver.refresh()
            loop4()
        try:
            methodComments()
            sleep(3)
            driver.refresh()
            loop0()
        except:
            try:
                lmt = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "h4")))
                timer_message = lmt.text
                print(f"{Fore.WHITE}[{Fore.BLUE}= {Fore.WHITE}| "+str(current_time)+"] Comments Timer: " + timer_message)
                message_split = timer_message.split()
                if timer_message == "Checking Timer..." or timer_message == "Next Submit: READY....!":
                    methodComments()
                elif message_split[4].isnumeric():
                    timer = int(message_split[2])
                    timer2 = int(message_split[4])

                    if (timer == 0) and (timer2 <= 10):
                        sleeping = timer2 + 1
                        print(f"{Fore.WHITE}[{Fore.BLUE}= {Fore.WHITE}| "+str(current_time)+"] Sleep: " + str(sleeping))
                        sleep(sleeping)
                        methodComments()
                    else:
                        print(f"\n{Fore.WHITE}[{Fore.RED}X {Fore.WHITE}| "+str(current_time)+"] Skipping Comment-Hearts..")
                driver.refresh()
                loop0()
            except:
                try:
                    fn = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Not found video.']")))
                    print(f"{Fore.WHITE}[{Fore.RED}X {Fore.WHITE}| "+str(current_time)+"] Video Not Found..")
                    methodComments()
                    sleep(3)
                    driver.refresh()
                    loop0()
                except:
                    print(f"{Fore.WHITE}[{Fore.LIGHTMAGENTA_EX}- {Fore.WHITE}| "+str(current_time)+"] An error occurred. Skipping => Comments Hearts")
                    sleep(3)
                    driver.refresh()
                    loop0()

    def methodFollowers():
        global current_time
        global Followers

        print(f"{Fore.WHITE}[{Fore.LIGHTMAGENTA_EX}N {Fore.WHITE}| "+str(current_time)+"] Getting TikTok link")
        # sleep(1)
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="sid"]/div/form/div/input'))).clear()  # remove input
        wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"sid\"]/div/form/div/input"))).send_keys(vidUrl)  # input url
        wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"sid\"]/div/form/div/div/button"))).click()  # submit

        waits.until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"c2VuZF9mb2xsb3dlcnNfdGlrdG9r\"]/div[1]/div/form/button"))).click()

        Followers += 25
        print(f"{Fore.WHITE}[{Fore.GREEN}+ {Fore.WHITE}| "+str(current_time)+"] Followers Sent!")
        driver.refresh()


    def methodView():
        global current_time
        global Views
        print(f"{Fore.WHITE}[{Fore.LIGHTMAGENTA_EX}N {Fore.WHITE}| "+str(current_time)+"] Getting TikTok link")
        # sleep(1)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"sid4\"]/div/form/div/input"))).clear()  # remove input
        wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"sid4\"]/div/form/div/input"))).send_keys(vidUrl)  # input url
        wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"sid4\"]/div/form/div/div/button"))).click()  # submit
        sleep(2)
        tv = waits.until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"c2VuZC9mb2xsb3dlcnNfdGlrdG9V\"]/div[1]/div/form/button")))
        print(f"{Fore.WHITE}[{Fore.LIGHTMAGENTA_EX}- {Fore.WHITE}| "+str(current_time)+"] Total views: " + tv.text)
        Views = int(tv.text.replace(',', ''))

        waits.until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"c2VuZC9mb2xsb3dlcnNfdGlrdG9V\"]/div[1]/div/form/button"))).click()

        Views += 800
        print(f"{Fore.WHITE}[{Fore.GREEN}+ {Fore.WHITE}| "+str(current_time)+"] Views Sent!")


    def methodHearts():
        global current_time
        global Hearts

        print(f"{Fore.WHITE}[{Fore.LIGHTMAGENTA_EX}N {Fore.WHITE}| "+str(current_time)+"] Getting TikTok link")

        # sleep(1)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"sid2\"]/div/form/div/input"))).clear()  # remove input
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="sid2"]/div/form/div/input'))).send_keys(vidUrl)  # input url
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="sid2"]/div/form/div/div/button'))).click()  # submit
        sleep(2)
        th = waits.until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"c2VuZE9nb2xsb3dlcnNfdGlrdG9r\"]/div[1]/div/form/button")))
        print(f"{Fore.WHITE}[{Fore.LIGHTMAGENTA_EX}- {Fore.WHITE}| "+str(current_time)+"] Total hears: " + th.text)
        Hearts = int(th.text.replace(',', ''))
        waits.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="c2VuZE9nb2xsb3dlcnNfdGlrdG9r"]/div[1]/div/form/button'))).click()
        print(f"{Fore.WHITE}[{Fore.GREEN}+ {Fore.WHITE}| "+str(current_time)+"] Hearts Sent!")


    def methodShare():
        global current_time
        global Shares
        print(f"{Fore.WHITE}[{Fore.LIGHTMAGENTA_EX}N {Fore.WHITE}| "+str(current_time)+"] Getting TikTok link")
        # sleep(1)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"sid7\"]/div/form/div/input"))).clear()  # remove input
        wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"sid7\"]/div/form/div/input"))).send_keys(vidUrl)  # input url
        wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"sid7\"]/div/form/div/div/button"))).click()  # submit
        sleep(2)
        ts = waits.until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"c2VuZC9mb2xsb3dlcnNfdGlrdG9s\"]/div[1]/div/form/button")))
        print(f"{Fore.WHITE}[{Fore.LIGHTMAGENTA_EX}- {Fore.WHITE}| "+str(current_time)+"] Total share: " + ts.text)
        Shares = int(ts.text.replace(',', ''))
        waits.until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"c2VuZC9mb2xsb3dlcnNfdGlrdG9s\"]/div[1]/div/form/button"))).click()
        print(f"{Fore.WHITE}[{Fore.GREEN}+ {Fore.WHITE}| "+str(current_time)+"] Shares Sent!")


    def methodComments():
        global current_time
        global Username
        global Comments
        global total_comments
        global comments_num
        global number
        print(f"{Fore.WHITE}[{Fore.LIGHTMAGENTA_EX}N {Fore.WHITE}| "+str(current_time)+"] Getting TikTok link")
        # sleep(1)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"sid3\"]/div/form/div/input"))).clear()  # remove input
        wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"sid3\"]/div/form/div/input"))).send_keys(vidUrl)  # input url
        wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"sid3\"]/div/form/div/div/button"))).click()  # submit
        sleep(2)
        tm = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"c2VuZC9mb2xsb3dlcnNfdGlrdG9r\"]/div[1]/div/form/button")))
        comments_num = tm.text
        print(f"{Fore.WHITE}[{Fore.BLUE}= {Fore.WHITE}| "+str(current_time)+"] Get number of comments: " + comments_num)
        # sleep(1)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"c2VuZC9mb2xsb3dlcnNfdGlrdG9r\"]/div[1]/div/form/button"))).click()
        sleep(2)
        if total_comments == int(comments_num):
            usernamenya = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"c2VuZC9mb2xsb3dlcnNfdGlrdG9r\"]/form[" + str(total_comments) + "]/ul/li/div/span[1]")))
            komentarnya = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"c2VuZC9mb2xsb3dlcnNfdGlrdG9r\"]/form[" + str(total_comments) + "]/ul/li/div/span[2]")))
            counlovenya = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"c2VuZC9mb2xsb3dlcnNfdGlrdG9r\"]/form[" + str(total_comments) + "]/ul/li/div/div/span")))
            print("[? | "+str(current_time)+"] " + usernamenya.text + " : " + komentarnya.text + " [" + counlovenya.text + " hearts]")
            Comments = int(counlovenya.text.replace(',', ''))
            Username = str(usernamenya.text)
            wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"c2VuZC9mb2xsb3dlcnNfdGlrdG9r\"]/form[" + str(total_comments) + "]/ul/li/div/button"))).click()
            number = int(comments_num)
            total_comments = 1

        else:
            usernamenya = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"c2VuZC9mb2xsb3dlcnNfdGlrdG9r\"]/form[" + str(total_comments) + "]/ul/li/div/span[1]")))
            komentarnya = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"c2VuZC9mb2xsb3dlcnNfdGlrdG9r\"]/form[" + str(total_comments) + "]/ul/li/div/span[2]")))
            counlovenya = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"c2VuZC9mb2xsb3dlcnNfdGlrdG9r\"]/form[" + str(total_comments) + "]/ul/li/div/div/span")))
            print("[? | "+str(current_time)+"] " + usernamenya.text + " : " + komentarnya.text + " [" + counlovenya.text + " hearts]")
            Comments = int(counlovenya.text.replace(',', ''))
            Username = str(usernamenya.text)
            wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"c2VuZC9mb2xsb3dlcnNfdGlrdG9r\"]/form[" + str(total_comments) + "]/ul/li/div/button"))).click()
            number += 1
            total_comments += 1
        print(f"{Fore.WHITE}[{Fore.GREEN}+ {Fore.WHITE}| "+str(current_time)+"] Comments Hearts Sent!")

    clear()
    print("Log:")

    if int(len(vidUrl)) >= 20:
        driver.get("https://zefoy.com/")

        a = threading.Thread(target=title)
        b = threading.Thread(target=loop0)

        a.start()
        b.start()

    else:
        print(f"{vidUrl} {Fore.WHITE}=> {Fore.RED}URL is invalid!")


def sessid():
    global value
    global current_time
    t = threading.Thread(target=timez)
    t.start()
    if os.path.isfile('key.txt'):
        os.remove("key.txt")
        e = open("key.txt", "w+")
    else:
        e = open("key.txt", "w+")
    chromedriver_autoinstaller.install()
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    browser = webdriver.Chrome(r"chromedriver.exe", options=options)
    browser.set_window_size(900, 1080)
    browser.get("https://zefoy.com/")
    print(f"{Fore.WHITE}[{Fore.YELLOW}*{Fore.WHITE}] {Fore.YELLOW}Complete captcha")
    WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div[1]/div[3]/div/div[1]/div/button')))
    print(f"{Fore.WHITE}[{Fore.YELLOW}*{Fore.WHITE}] {Fore.YELLOW}Generating session ID...")
    browser.set_window_position(-10000, 0)
    id = browser.get_cookie('PHPSESSID')
    f = open('key.txt', 'a+')
    f.write(id['value'])
    print(f"{Fore.WHITE}[{Fore.YELLOW}*{Fore.WHITE}] {Fore.YELLOW}Session ID: {Fore.WHITE}" + id['value'])
    value = id['value']
    browser.quit()
    main()
sessid()