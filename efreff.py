import datetime
import random
import time
from datetime import datetime
import ThreadPoolExecutorPlus
from selenium import webdriver
from selenium.webdriver.common.by import By


def auth():
    # Открытие браузера
    global inquiry_numbers_list
    browser = webdriver.Chrome()
    start_datatime = datetime.now().time()
    print("Начало теста в " + str(start_datatime))
    browser.get("http://10.11.3.145:7981/Login/Login")
    time.sleep(2)
    browser.implicitly_wait(2)
    login = browser.find_element(By.NAME, "login")
    password = browser.find_element(By.NAME, "pwd")
    # Ввод логина и пароля
    login.send_keys("regionAdmin")
    password.send_keys("123456")
    time.sleep(2)
    browser.implicitly_wait(2)
    browser.find_element(By.CLASS_NAME, "pull-right").click()
    browser.implicitly_wait(3)

    # Смена области видимости
    browser.find_element(By.ID, "scopeLink").click()
    browser.implicitly_wait(4)
    time.sleep(2)
    region = browser.find_element(By.CSS_SELECTOR, "input[type='checkbox']")
    browser.implicitly_wait(4)
    time.sleep(2)
    region.click()

    # Выбор муниципалитета
    municipallity = browser.find_element(By.ID, "s2id_autogen1")
    browser.implicitly_wait(2)
    time.sleep(2)
    municipallity.click()

    # Список муниципалитетов для ввода
    municipality_list = ["Фрунзенский район", "Приморский район", "Московский район", "Красносельский район",
                         "Центральный район", "Пушкинский район"]
    browser.implicitly_wait(2)
    time.sleep(2)
    municipallity_l = browser.find_element(By.CSS_SELECTOR, ".select2-focused")
    browser.implicitly_wait(2)
    time.sleep(2)

    # Рандомный выбор муниципалитета из списка
    i = random.randint(0, len(municipality_list) - 1)
    choice_municipallity_random = municipality_list[i]
    municipallity_l.send_keys(choice_municipallity_random + "\n")
    print("Муниципалитет выбран")
    time.sleep(1)
    browser.find_element(By.CSS_SELECTOR, ".btn-primary").click()
    browser.implicitly_wait(4)
    time.sleep(2)
    browser.find_element(By.CSS_SELECTOR, ".btn:nth-child(3) > .head-menu-a").click()
    browser.implicitly_wait(3)
    time.sleep(2)
    # Клик на меню Реестры
    browser.find_element(By.CSS_SELECTOR, "#sidebar_ul > .ng-scope:nth-child(13) > a").click()
    browser.implicitly_wait(3)
    time.sleep(2)


browser.find_element(By.CSS_SELECTOR,.ui-iggrid-pagedropdowncontainer > .ui-igedit-field