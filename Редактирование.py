import ThreadPoolExecutorPlus
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


#Зайти в систему
def auth():
    browser = webdriver.Chrome()
    browser.get("http://10.11.3.145:7381/Login/Login")
    time.sleep(2)
    login = browser.find_element(By.NAME, "login")
    password = browser.find_element(By.NAME, "pwd")
    login.send_keys("regionAdmin")
    password.send_keys("123456")
    time.sleep(2)
    browser.find_element(By.CLASS_NAME, "pull-right").click()
    time.sleep(5)

#Область видимости
    browser.find_element(By.ID, "scopeLink").click()
    time.sleep(4)
    region = browser.find_element(By.CSS_SELECTOR,"input[type='checkbox']")
    time.sleep(10)
    region.click()

#Выбрать муниципалитет
    municipallity = browser.find_element(By.ID, "s2id_autogen1")
    time.sleep(2)
    municipallity.click()
    time.sleep(2)
    municipallity_l = browser.find_element(By.CSS_SELECTOR,".select2-focused")
    time.sleep(10)
    municipallity_l.send_keys("Мо")


municipality_list = ['Фрунзенский район', 'Приморский район', 'Московский район', 'Красносельский район']

executors_list = []
executor = ThreadPoolExecutorPlus
with ThreadPoolExecutorPlus.ThreadPoolExecutor(max_workers=5) as executor:
    executors_list.append(executor.submit(auth))
    executors_list.append(executor.submit(auth))
    executors_list.append(executor.submit(auth))