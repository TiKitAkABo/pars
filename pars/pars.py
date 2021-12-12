from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time
import csv


opt = Options()

opt.add_argument('user-agent= Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0')
driver=webdriver.Chrome(options=opt)
driver.get("https://www.nseindia.com/market-data/pre-open-market-cm-and-emerge-market")
time.sleep(5)

data=[]
pris=[]
driver.find_elements(By.CLASS_NAME, 'common_table')
n=driver.find_elements(By.TAG_NAME, 'tbody')
price=driver.find_elements(By.TAG_NAME, 'tr')
fin=driver.find_elements(By.XPATH, '//td[7]')
cin=driver.find_elements(By.XPATH, '//td[2]/a')

for name in fin:
 data.append(name.text)

for named in cin:
 pris.append(named.text)

driver.close()

opt.add_argument("--start-maximized")
opt.add_argument('user-agent= Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0')
opt.add_experimental_option("prefs", {"profile.default_content_setting_values.cookies": 2})
driver=webdriver.Chrome(options=opt)
driver.maximize_window
wait = WebDriverWait(driver, 30)
action = ActionChains(driver)
driver.get("https://nseindia.com/")

driver.execute_script("window.scrollTo(0, 300)") 
time.sleep(2)
driver.execute_script("window.scrollTo(0, 500)") 
time.sleep(2)
driver.execute_script("window.scrollTo(0, 700)") 
time.sleep(1)
driver.execute_script("window.scrollTo(0, 1000)") 
time.sleep(5)
Vie_Btn = driver.find_element(By.XPATH, '//*[@id="gainers_loosers"]/div[3]/a')
Vie_Btn.click()
time.sleep(5)
but1=driver.find_element(By.XPATH, '//*[@id="liveMrktStockSel"]')
but1.click()
time.sleep(6)
but=driver.find_element(By.XPATH, '//*[@id="equitieStockSelect"]/optgroup[4]/option[7]')
but.click()
but1.click()
driver.execute_script("window.scrollTo(0, 900)") 
time.sleep(6)



with open('some.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(zip(pris,data))