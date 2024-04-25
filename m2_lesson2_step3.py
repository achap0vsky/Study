from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select

try:
  link = "https://suninjuly.github.io/selects1.html"
  browser = webdriver.Chrome()
  browser.get(link)

  x_element = browser.find_element(By.XPATH,"//span[@id='num1']")
  x = x_element.text
  y_element = browser.find_element(By.XPATH,"//span[@id='num2']")
  y = y_element.text
  answer = int(x)+int(y)
  print(answer)

  select = Select(browser.find_element(By.TAG_NAME, "select"))
  select.select_by_value(str(answer))

  button = browser.find_element(By.XPATH, "//button[@type='submit']")
  button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()