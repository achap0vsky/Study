from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
  link = "https://suninjuly.github.io/math.html"
  browser = webdriver.Chrome()
  browser.get(link)

  x_element = browser.find_element(By.ID, "input_value")
  x = x_element.text
  y = calc(x)

  input1 = browser.find_element(By.ID, "answer")
  input1.send_keys(y)

  checkbox1 = browser.find_element(By.ID,"robotCheckbox")
  checkbox1.click()
  radiobutton1 = browser.find_element(By.ID,"robotsRule")
  radiobutton1.click()
  button = browser.find_element(By.XPATH, "//button[@type='submit']")
  button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()