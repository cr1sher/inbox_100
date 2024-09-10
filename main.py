from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pickle


login = ""
passw = ""

new_pass = ""
new_name = ['Никита', 'Шарапов']

options = webdriver.ChromeOptions()
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                     "Chrome/126.0.0.0 YaBrowser/24.7.0.0 Safari/537.36")

driver = webdriver.Chrome(options=options)

### логинимся ###

driver.get('https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Fwww.google.com%2F&ec=GAZAmgQ&hl=ru&ifkv=Ab5oB3oIyqEvBnsFUtFHSP99WBjQDosG7wxakIizIkKnKG7qXyvPKeDV0wKG1BddUNEGTitentgt4Q&passive=true&flowName=GlifWebSignIn&flowEntry=ServiceLogin&dsh=S-1643219810%3A1725975226658157&ddm=0')

time.sleep(1)
email_input = driver.find_element(by=By.ID, value="identifierId")
email_input.clear()
email_input.send_keys(login)

login_button = driver.find_element(by=By.CSS_SELECTOR, value="#identifierNext > div > button").click()
time.sleep(5)
passw_input = driver.find_element(by=By.CSS_SELECTOR, value="input[name='Passwd']")
passw_input.clear()
passw_input.send_keys(passw)
passw_button = driver.find_element(by=By.CSS_SELECTOR, value="#passwordNext > div > button").click()

### save cookies ###

pickle.dump(driver.get_cookies(), open(f"{login}_cookies", "wb"))

### save date of birth, reserve email
time.sleep(5)
driver.get("https://myaccount.google.com/u/2/personal-info")
time.sleep(5)
date = driver.find_element(by=By.CSS_SELECTOR, value="#i12")
reserve = driver.find_element(by=By.CSS_SELECTOR, value="#i14")
reserve_email = reserve.text.split()[-1]
date_of_birth = date.text.split()[-1] + " " + date.text.split()[-2] + " " + date.text.split()[-3]


### change password ###

time.sleep(5)

driver.get("https://myaccount.google.com/signinoptions/password")

new_passw = driver.find_element(by=By.CSS_SELECTOR, value="#i6")
conf_passw = driver.find_element(by=By.CSS_SELECTOR, value="#i12")
new_passw.clear()
new_passw.send_keys(new_pass)
time.sleep(3)
conf_passw.send_keys(new_pass)
time.sleep(3)
click_change = driver.find_element(by=By.CSS_SELECTOR, value="button[type='submit']").click()

time.sleep(5)

### change name ###

driver.get("https://myaccount.google.com/u/2/profile/name/edit?continue=https://myaccount.google.com/")

name1_input = driver.find_element(by=By.CSS_SELECTOR, value="#i7")
name1_input.clear()
name2_input = driver.find_element(by=By.CSS_SELECTOR, value="#i12")
name2_input.clear()

name1_input.send_keys(new_name[0])
name2_input.send_keys(new_name[1])

try:
    driver.find_element(By.XPATH, '//span[text()="Сохранить"]').click()
except:
    driver.find_element(By.XPATH, '//span[text()="Save"]').click()


### save to CSV
file = open("save.csv", "w")
file.write(rf"{login}, {new_pass}, {date_of_birth}, {reserve_email}")
file.close()


time.sleep(1000)
