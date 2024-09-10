from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pickle


options = webdriver.ChromeOptions()

driver = webdriver.Chrome()
driver.get("http://x.com")

for cookie in pickle.load(open("cookies", "rb")):
    driver.add_cookie(cookie)
driver.refresh()

password = ''


time.sleep(3)

### постим случайную новость
news_input = driver.find_element(By.CSS_SELECTOR, 'br[data-text="true"]')
news_input.send_keys('hello world')
driver.find_element(By.XPATH, '//span[text()="Post"]').click()
print('попытка опубликовать случайный твит')
time.sleep(3)

## смена Email

new_email = input(f"Введите новый Email\n")
driver.get("https://x.com/i/flow/add_email")
time.sleep(5)
passw = driver.find_element(by=By.CSS_SELECTOR, value='input[name="password"]')
passw.send_keys(password)
time.sleep(5)
driver.find_element(By.XPATH, '//span[text()="Next"]').click()
time.sleep(5)
email = driver.find_element(by=By.CSS_SELECTOR, value='input[name="email"]')
email.send_keys(new_email)
time.sleep(5)
driver.find_element(By.XPATH, '//span[text()="Next"]').click()
email_code = input("Email отправлен, введите полученный код\n")
email_code_input = driver.find_element(by=By.CSS_SELECTOR, value='input[name="verfication_code"]')
email_code_input.send_keys(email_code)
time.sleep(3)
driver.find_element(By.XPATH, '//span[text()="Verify"]').click()
print('Email изменен')
pickle.dump(driver.get_cookies(), open("cookies", "wb"))


### смена пароля
time.sleep(2)
driver.get("https://x.com/settings/password")
time.sleep(2)
passw_old = driver.find_element(by=By.CSS_SELECTOR, value='input[name="current_password"]')
passw_old.send_keys(password)
time.sleep(2)
pass_new = input('введите новый пароль\n')
passw_new = driver.find_element(by=By.CSS_SELECTOR, value='input[name="new_password"]')
passw_conf = driver.find_element(by=By.CSS_SELECTOR, value='input[name="password_confirmation"]')
passw_new.send_keys(pass_new)
time.sleep(1)
passw_conf.send_keys(pass_new)
time.sleep(3)
driver.find_element(By.XPATH, '//span[text()="Save"]').click()
print(f'Пароль изменен на {pass_new}')
pickle.dump(driver.get_cookies(), open("cookies", "wb"))

time.sleep(2)
