from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


firefox = webdriver.Firefox()
firefox.get("http://the-internet.herokuapp.com/inputs")
input = firefox.find_element(By.TAG_NAME, "input")
input.send_keys("1000")
sleep(2)
input.clear()
sleep(2)
input.send_keys("999")
sleep(2)

firefox.quit()