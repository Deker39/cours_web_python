from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up the WebDriver
driver = webdriver.Chrome()

# Open the website
driver.get("https://xn--80apegdhdcbsio.in.ua/")

# Wait for the element with ID "aw0" to be clickable
wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.ID, "aswift_1")))
driver.switch_to.frame(element)

link = wait.until(EC.element_to_be_clickable((By.TAG_NAME, "a")))

print(link.get_attribute('href'))

# driver.get(link.get_attribute('href'))

# Click the element
link.click()


# Close the WebDriver
# driver.quit()
