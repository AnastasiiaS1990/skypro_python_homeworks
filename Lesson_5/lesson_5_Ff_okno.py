from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


firefox = webdriver.Firefox()
firefox.get("http://the-internet.herokuapp.com/entry_ad")
sleep(2)
close_button = firefox.find_element(By.CSS_SELECTOR, ".modal-footer").click()
firefox.quit()

