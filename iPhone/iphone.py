#!/home/harin/Desktop/Inventory/env/bin/python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import smtplib

baseLink = 'https://www.apple.com/ca/shop/buy-iphone/iphone-14-pro/6.1-inch-display-128gb-gold'


options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")
options.add_argument("--no-sandbox")
options.add_argument("user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36")
browser = webdriver.Chrome(executable_path="./chromedriver", options=options)
browser.get(baseLink)
time.sleep(3)
# browser.get_screenshot_as_file("screenshot.png")
browser.find_element(By.XPATH, "//input[@id='noTradeIn']").click()
time.sleep(3)
# browser.get_screenshot_as_file("screenshot1.png")
browser.find_element(By.XPATH, "//input[@id='applecareplus_58_noapplecare']").click()
time.sleep(10)
# browser.get_screenshot_as_file("screenshot2.png")
browser.find_element(By.XPATH, "//span[contains(text(), 'Check availability')]/ancestor::button").click()
time.sleep(3)
# browser.get_screenshot_as_file("screenshot3.png")
browser.find_element(By.XPATH, "//input[@name='search']").send_keys("V6B 0E4")
time.sleep(3)
# browser.get_screenshot_as_file("screenshot4.png")
browser.find_element(By.XPATH, "//input[@name='search']").send_keys(Keys.ENTER)
time.sleep(3)
# browser.get_screenshot_as_file("screenshot5.png")
today = browser.find_elements(By.XPATH, "//div[contains(@class, 'rf-productlocator-main')]//span[contains(text(), 'Available Today')]")
tmr = browser.find_elements(By.XPATH, "//div[contains(@class, 'rf-productlocator-main')]//span[contains(text(), 'Available Tomorrow')]")
suggestToday = browser.find_elements(By.XPATH, "//div[contains(@class, 'rf-productlocator-suggestions')]//span[contains(text(), 'Available Today')]")
suggestTmr = browser.find_elements(By.XPATH, "//div[contains(@class, 'rf-productlocator-suggestions')]//span[contains(text(), 'Available Tomorrow')]")
browser.close()

print(len(today) > 0)
print(len(tmr) > 0)
print(len(suggestToday) > 0)
print(len(suggestTmr) > 0)

phoneNumber = 'PHONE'
email = 'EMAIL'
password = 'PASSWORD'

text = '\nNo iPhone :('
if len(today) > 0 or len(tmr) > 0 or len(suggestToday) > 0 or len(suggestTmr) > 0:
    if len(today) > 0 or len(tmr) > 0:
        text = '\niPhone Available!'
    else:
        text = '\nSuggestion Available!'

print(text)

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(email, password)
    server.sendmail(email, phoneNumber + '@txt.freedommobile.ca', text)
    server.close()
    print("Successfully sent email")
except SMTPException:
    print("Error: unable to send email")