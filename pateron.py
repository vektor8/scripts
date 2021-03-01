# This script downloads all pdfs from Guitar Nick's patreon page
# Of course you need an account and to support Guitar Nick
# TO DO: don't download duplicates
# Sorry Guitar Nick :(

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.patreon.com/login?ru=%2Feurope")
f = open("patreoncred.txt")
email_input = driver.find_element_by_id("email")
email_input.send_keys(f.readline())
password_input = driver.find_element_by_id("password")
password_input.send_keys(f.readline(), Keys.ENTER)

time.sleep(2)
driver.get("https://www.patreon.com/guitarnick/posts?filters[tag]=PDF")
time.sleep(5)
count = 0
condition = True
while condition:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    try:
        download_links = driver.find_elements_by_tag_name("a")
        for i in download_links:
            if ".pdf" in i.text:
                driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't')
                driver.get(i.get_attribute("href"))
                driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 'w')
                count += 1
        load_button = driver.find_element_by_xpath(
            "/html/body/div/div/div[3]/div[3]/div[1]/div[3]/div/div/div/div[4]/div/div/div[5]/button")
        load_button.click()
        time.sleep(15)
    except:
        condition = False

driver.quit()
print(count)
