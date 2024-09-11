from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


chrome = webdriver.Chrome()
chrome.get("http://the-internet.herokuapp.com/add_remove_elements/")
for add in range(5):
    button = chrome.find_element(By.XPATH, '//button[text()="Add Element"]').click()
    sleep(2)
    delete_button = chrome.find_elements(By.XPATH, '//button[text()="Delete"]')
print(f"Список кнопок делит, {len(delete_button)}")

    