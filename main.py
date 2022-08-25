import string
import requests
import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from random import choice, randint
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys


password = ''.join(choice(string.ascii_letters + string.digits) for _ in range(10))


class D:

    def register(self, email, username):

        url = "https://discord.com/register"

        # driver = webdriver.Chrome("/home/av/chromedriver_linux64/chromedriver")
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

        driver.get(url)

        driver.maximize_window()

        driver.find_element(By.NAME, "email").send_keys(email)
        driver.find_element(By.NAME, "username").send_keys(username)
        driver.find_element(By.NAME, "password").send_keys(password)

        driver.find_element(By.CLASS_NAME, "month-1Z2bRu").click()

        html_source = driver.page_source
        soup = BeautifulSoup(html_source, 'html.parser')
        months = soup.find(class_='css-1rel15f').get_text(',')
        month_list = months.split(",")

        driver.find_element(By.ID, "react-select-2-input").send_keys(choice(month_list), Keys.RETURN)
        driver.find_element(By.ID, "react-select-3-input").send_keys(randint(1, 31), Keys.ENTER)
        driver.find_element(By.ID, "react-select-4-input").send_keys(randint(1940, 2000), Keys.ENTER)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "contents-3ca1mk"))).click()


        sleep(20)



    def login(self, email, password):

        url = "https://discord.com/login"
        driver = webdriver.Chrome("/home/av/chromedriver_linux64/chromedriver")

        driver.get(url)

        driver.maximize_window()

        sleep(2)

        driver.find_element(By.NAME, "email").send_keys(email)
        driver.find_element(By.NAME, "password").send_keys(password)

        sleep(3)

        driver.find_element(By.XPATH, "//*[@id=\"app-mount\"]/div[2]/div/div[1]/div/div/div/div/form/div/div/div[1]/div[2]/button[2]").click()

        sleep(15)

        s = requests.Session()
        payload = {
            'login': email,
            'password': password
        }

        res = s.post('https://discord.com/api/v9/auth/login', json=payload)
        s.headers.update({'authorization': res.json()['token']})
        print(json.loads(res.content.decode())["token"])
        return s


email = input("Email: ")
username = input("Username: ")

a = D()

a.register(email, username)
a.login(email, password)