from selenium import webdriver
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import Select
import pandas as pd

PATH = "C:\Program Files (x86)\chromedriver.exe"
LINK = "https://developer.automationanywhere.com/challenges/automationanywherelabs-customeronboarding.html"
EXCEL = "MissingCustomers.csv"

df = pd.read_csv(EXCEL)

driver = webdriver.Chrome(PATH)
driver.get(LINK)
driver.maximize_window()

customer_name = driver.find_element(By.XPATH, '//*[@id="customerName"]')
customer_id = driver.find_element(By.XPATH, '//*[@id="customerID"]')
primary_contact = driver.find_element(By.XPATH, '//*[@id="primaryContact"]')
street_address = driver.find_element(By.XPATH, '//*[@id="street"]')
city = driver.find_element(By.XPATH, '//*[@id="city"]')
state = driver.find_element(By.XPATH, '//*[@id="state"]')
zip_code = driver.find_element(By.XPATH, '//*[@id="zip"]')
email = driver.find_element(By.XPATH, '//*[@id="email"]')
discount_offer_yes = driver.find_element(By.XPATH, '//*[@id="activeDiscountYes"]')
discount_offer_no = driver.find_element(By.XPATH, '//*[@id="activeDiscountNo"]')
nd_aggrement = driver.find_element(By.XPATH, '//*[@id="NDA"]')
register = driver.find_element(By.XPATH, '//*[@id="submit_button"]')

for i in range(df.shape[0]):
    customer_name.send_keys(df["Company Name"][i])
    customer_id.send_keys(df["Customer ID"][i])
    primary_contact.send_keys(df["Primary Contact"][i])
    street_address.send_keys(df["Street Address"][i])
    city.send_keys(df["City"][i])
    state.send_keys(df["State"][i])
    zip_code.send_keys(df["Zip"].astype('str')[i])
    email.send_keys(df["Email Address"][i])
    if df["Offers Discounts"][i] == "YES":
        discount_offer_yes.click()
    else:
        discount_offer_no.click()
    if df["Non-Disclosure On File"][i] == "YES":
        nd_aggrement.click()
    register.click()