from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


firefox = webdriver.Firefox()
firefox.get("http://the-internet.herokuapp.com/login")
input_name = firefox.find_element(By.ID, "username")
input_name.send_keys("tomsmith")
sleep(2)
input_pas = firefox.find_element(By.ID, "password")
input_pas.send_keys("SuperSecretPassword!")
sleep(2)
button = firefox.find_element(By.TAG_NAME, "button").click()
sleep(2)

firefox.quit()