from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


chrome = webdriver.Chrome()
chrome.get("http://uitestingplayground.com/dynamicid")
button = chrome.find_element(By.XPATH, '//button[text()="Button with Dynamic ID"]').click

sleep(2)
