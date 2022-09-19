from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

PATH = "C:\Program Files (x86)\chromedriver.exe"
LINK = "https://developer.automationanywhere.com/challenges/AutomationAnywhereLabs-ShoppingList.html#"
EXCEL = "ShoppingList.csv"

df = pd.read_csv(EXCEL)

driver = webdriver.Chrome(PATH)
driver.get(LINK)
driver.maximize_window()

input_box = driver.find_element(By.XPATH, '//*[@id="myInput"]')
add_item_button = driver.find_element(By.XPATH, '//*[@id="myDIV"]/div[2]/button')
submit_button = driver.find_element(By.XPATH, '/html/body/div[2]/div/form/div[3]/button')

for i in range(len(df)):
    input_box.send_keys(df["Favorite Food"][i])
    add_item_button.click()

driver.find_element(By.XPATH, '//*[@id="agreeToTermsYes"]').click()
submit_button.click()