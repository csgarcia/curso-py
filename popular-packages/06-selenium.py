# dont name this file selenium.py
# otherwise it will conflict with the actual selenium package
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv

load_dotenv()  # Loads variables from .env into environment

# options = webdriver.ChromeOptions()
# options.add_experimental_option("detach", True)
# browser = webdriver.Chrome(options=options)
browser = webdriver.Chrome()
browser.implicitly_wait(10)
browser.get(os.environ.get("SELENIUM_TEST_URL"))
btn = browser.find_element(By.CSS_SELECTOR, "button.button-auth")
btn.click()

user_input = browser.find_element(By.NAME, "username")
password_input = browser.find_element(By.NAME, "password")

user_input.send_keys(os.environ.get("SELENIUM_TEST_USERNAME"))
password_input.send_keys(os.environ.get("SELENIUM_TEST_PASSWORD"))
password_input.send_keys(Keys.ENTER)

# if you want the full class chain include the escaped colon:
# selector = "h1.text-blackGrayScale.text-3xl.lg\\:text-3xl.font-semibold.text-left.tracking-wide.mb-10"
h1 = WebDriverWait(browser, 10).until(EC.presence_of_element_located(
    (By.CSS_SELECTOR, "h1.text-blackGrayScale")))
text = h1.text                  # e.g. "Hola, Carlos"
name = text.split(",")[-1].strip()

assert name == "Carlos"
print("Name extracted:", name)

browser.quit()
