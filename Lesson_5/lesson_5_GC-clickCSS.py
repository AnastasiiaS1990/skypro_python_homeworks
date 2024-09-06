from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


chrome = webdriver.Chrome()
chrome.get("http://uitestingplayground.com/classattr")
button = chrome.find_element(By.XPATH, "//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')]").click()
sleep(5)
chrome.switch_to.alert.accept()
