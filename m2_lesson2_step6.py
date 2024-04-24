from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
  link = "https://suninjuly.github.io/execute_script.html"
  browser = webdriver.Chrome()
  browser.get(link)

  x_element = browser.find_element(By.ID,"input_value")
  x = x_element.text
  print(x)
  y = calc(x)

  input1 = browser.find_element(By.ID, "answer")
  input1.send_keys(y)
  checkbox1 = browser.find_element(By.ID, "robotCheckbox").click()
  radiobutton1 = browser.find_element(By.ID, "robotsRule")
  browser.execute_script("return arguments[0].scrollIntoView(true);",radiobutton1)
  radiobutton1.click()

  button = browser.find_element(By.XPATH, "//button[@type='submit']")
  browser.execute_script("return arguments[0].scrollIntoView(true);",button)
  button.click()

finally:
    time.sleep(5)
    browser.quit()