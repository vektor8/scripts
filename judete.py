# I heard there is a county/city in Romania which is an anagram for "masturbare" and went ahead and tried to find
# that place. Unfortunately didn't find it, maybe it is a village and not a city nor a county

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import unidecode

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
# counties 42
# /html/body/div[3]/div[3]/div[5]/div[1]/table[3]/tbody/tr[1]/td[1]/a
# /html/body/div[3]/div[3]/div[5]/div[1]/table[3]/tbody/tr[2]/td[1]/a
# /html/body/div[3]/div[3]/div[5]/div[1]/table[3]/tbody/tr[42]/td[1]/a
# /html/body/div[3]/div[3]/div[5]/div[1]/table[3]/tbody/tr[9]/td[1]/a
result = []
driver.get("https://ro.wikipedia.org/wiki/Jude%C8%9Bele_Rom%C3%A2niei")
j = 0
for i in range(1, 43):
    if i != 10:
        county = driver.find_element_by_xpath(
            "/html/body/div[3]/div[3]/div[5]/div[1]/table[3]/tbody/tr[" + str(i) + "]/td[1]/a").get_attribute("text")
        print(unidecode.unidecode(county))
        if sorted(unidecode.unidecode(county)) == sorted("masturbare"):
            result.append(county)
            j += 1

print(str(j))

# cities 318
# /html/body/div[3]/div[3]/div[5]/div[1]/table[3]/tbody/tr[1]/td[1]/b/a
# /html/body/div[3]/div[3]/div[5]/div[1]/table[3]/tbody/tr[2]/td[1]/b/a
# /html/body/div[3]/div[3]/div[5]/div[1]/table[3]/tbody/tr[36]/td[1]/a
# /html/body/div[3]/div[3]/div[5]/div[1]/table[3]/tbody/tr[317]/td[1]/a
driver.get("https://ro.wikipedia.org/wiki/Lista_ora%C8%99elor_din_Rom%C3%A2nia")

for i in range(1, 318):
    try:
        city = driver.find_element_by_xpath(
            "/html/body/div[3]/div[3]/div[5]/div[1]/table[3]/tbody/tr[" + str(i) + "]/td[1]/b/a").get_attribute("text")
    except NoSuchElementException:
        city = driver.find_element_by_xpath(
            "/html/body/div[3]/div[3]/div[5]/div[1]/table[3]/tbody/tr[" + str(i) + "]/td[1]/a").get_attribute("text")
    print(unidecode.unidecode(city))
    if sorted(unidecode.unidecode(city)) == sorted("masturbare"):
        result.append(city)
        j += 1

driver.quit()
if j == 0:
    print("Nothing found :(")
else:
    for i in result:
        print(i)

print(str(j))
