from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time
import random


str=input("Enter your request")
browser=webdriver.Chrome()
browser.get('https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0')
assert "Википедия" in browser.title
time.sleep(5)

search_box=browser.find_element(By.ID,"searchInput")
search_box.send_keys(str)
time.sleep(5)
search_box.send_keys(Keys.ENTER)
time.sleep(5)
while True:
    choice=input("1-I want to see paragraphs, 2-I want to see something on the subject,3-I want nothing")
    if choice=="1":
        paragraphs=browser.find_elements(By.TAG_NAME,"p")
        for paragraph in paragraphs:
            print(paragraph.text)
            str2=input("1-I want to see paragraphs, 2-I want to see something")
            if str2=="2":
                break
    elif choice=="2":
        hatnotes = []
        for element in browser.find_elements(By.TAG_NAME, "div"):
            cl = element.get_attribute("class")
            if cl == "hatnote navigation-not-searchable":
                hatnotes.append(element)

        hatnote = random.choice(hatnotes)

        link = hatnote.find_element(By.TAG_NAME, "a").get_attribute("href")
        browser.get(link)
        time.sleep(5)
    else:
        print("Ok, I will stop the browser.")
        break
browser.quit()
