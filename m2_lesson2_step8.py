from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import os


try:
  link = "http://suninjuly.github.io/file_input.html"
  browser = webdriver.Chrome()
  browser.get(link)

  input1 = browser.find_element(By.CSS_SELECTOR, "input[name='firstname']")
  input1.send_keys("Ivan")

  input2 = browser.find_element(By.CSS_SELECTOR, "input[name='lastname']")
  input2.send_keys("Ivanov")
  input3 = browser.find_element(By.CSS_SELECTOR, "input[name='email']")
  input3.send_keys("ivanov@test.com")
  element = browser.find_element(By.CSS_SELECTOR,"input[id='file']")
  current_dir = os.path.abspath(os.path.dirname(__file__))
  file_path = os.path.join(current_dir, 'file.txt')
  element.send_keys(file_path)

  button = browser.find_element(By.XPATH, "//button[@type='submit']")
  button.click()

finally:
    time.sleep(5)
    browser.quit()