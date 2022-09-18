from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import math

s = Service('C:/Users/eve/Downloads/chromedriver/chromedriver.exe')
driver = webdriver.Chrome(service=s)

driver.get("http://suninjuly.github.io/explicit_wait2.html")

WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
driver.find_element(By.ID, "book").click()

x = driver.find_element(By.ID, "input_value").text
z = str(math.log(abs(12 * math.sin(int(x)))))

print("value of x_element: ", z)

driver.find_element(By.ID, "answer").send_keys(z)

driver.find_element(By.ID, "solve").click()
