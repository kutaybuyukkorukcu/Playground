from selenium import webdriver
import time

browser = webdriver.Chrome()

browser.get("https://www.instagram.com")

time.sleep(10)

giris_yap = browser.find_element_by_xpath("//*[@id='react-root']/section/matin/article/div[2]/div[2]/p/a")

giris_yap.click()

time.sleep(2)

username = browser.find_element_by_name("username")
password = browser.find_element_by_name("password")

username.send_keys("@username")
password.send_keys("@password")

time.sleep(5)

login = browser.find_element_by_xpath("//*[@id='react-root']/section/matin/article/div[2]/div[1]/div/form/span/button")
login.click()

time.sleep(10)

browser.close()