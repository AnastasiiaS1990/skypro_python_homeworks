from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
#from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

geckodriver_path = './Users/nasta/Desktop/Python/skypro_python_homeworks/geckodriver2' 

driver_chrome = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver_firefox = webdriver.Firefox(executable_path=geckodriver_path)
